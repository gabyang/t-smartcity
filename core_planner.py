from openai import OpenAI
from dotenv import load_dotenv
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    ChatMessage,
    FunctionMessage,
    HumanMessage,
)
from langchain.tools.render import format_tool_to_openai_function
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph
from langgraph.prebuilt.tool_executor import ToolExecutor, ToolInvocation

import operator
from typing import Annotated, List, Sequence, Tuple, TypedDict
from langchain.agents import create_openai_functions_agent
from langchain.tools.render import format_tool_to_openai_function
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL
import os
import json
import re
import functools

# Load environment variables
load_dotenv()
os.environ['TAVILY_API_KEY'] = ""
client = OpenAI(api_key=os.getenv(""))

# Tools for the agents
@tool
def process_json_arrays(file1: str, file2: str):
    """
    Extract and process data from two JSON files containing arrays of objects.

    Parameters:
    - file1: Path to the first JSON file.
    - file2: Path to the second JSON file.

    Returns:
    - A combined or comparative result based on the JSON arrays.
    """
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

        if not isinstance(data1, list) or not isinstance(data2, list):
            return "Both files must contain an array of JSON objects."

        combined = data1 + data2
        keys1 = {key for obj in data1 for key in obj.keys()}
        keys2 = {key for obj in data2 for key in obj.keys()}
        common_keys = keys1.intersection(keys2)

        summary = {
            "File1_Count": len(data1),
            "File2_Count": len(data2),
            "Combined_Count": len(combined),
            "Common_Keys": list(common_keys),
            "First_File_Example": data1[0] if data1 else None,
            "Second_File_Example": data2[0] if data2 else None,
        }
        return summary
    except Exception as e:
        return f"Error processing JSON arrays: {repr(e)}"

@tool
def analyze_json_array(extracted_data: Annotated[str, "The extracted JSON data to analyze for insights."]):
    """
    Analyze the extracted JSON data and provide insights.

    Parameters:
    - extracted_data: A stringified JSON object containing the processed data.

    Returns:
    - Insights derived from the data.
    """
    try:
        data = json.loads(extracted_data)
        insights = {
            "File1_Count": data.get("File1_Count", 0),
            "File2_Count": data.get("File2_Count", 0),
            "Common_Keys": data.get("Common_Keys", []),
            "Summary": f"File 1 contains {data.get('File1_Count', 0)} items, "
                       f"File 2 contains {data.get('File2_Count', 0)} items, "
                       f"and they share {len(data.get('Common_Keys', []))} common keys."
        }
        return insights
    except Exception as e:
        return f"Failed to analyze data: {repr(e)}"

# Python REPL tool
repl = PythonREPL()

# Tool list
tools = [process_json_arrays, analyze_json_array]

# Agent state definition
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str

# Tool executor
tool_executor = ToolExecutor(tools)

# Node function for tool execution
def tool_node(state):
    messages = state["messages"]
    last_message = messages[-1]
    tool_input = json.loads(last_message.additional_kwargs["function_call"]["arguments"])
    if len(tool_input) == 1 and "__arg1" in tool_input:
        tool_input = next(iter(tool_input.values()))
    tool_name = last_message.additional_kwargs["function_call"]["name"]
    action = ToolInvocation(
        tool=tool_name,
        tool_input=tool_input,
    )
    response = tool_executor.invoke(action)
    function_message = FunctionMessage(
        content=f"{tool_name} response: {str(response)}", name=action.tool
    )
    return {"messages": [function_message]}

# Name sanitizer
def sanitize_name(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

# Routing function
def router(state):
    messages = state["messages"]
    last_message = messages[-1]
    if "function_call" in last_message.additional_kwargs:
        return "call_tool"
    if "FINAL ANSWER" in last_message.content:
        return "end"
    return "continue"

# Agent creator
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_agent(llm, tools, system_message: str):
    functions = [convert_to_openai_function(t) for t in tools]
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant, collaborating with other assistants."
                " Use the provided tools to progress towards answering the question."
                " If you or any of the other assistants have the final answer or deliverable,"
                " prefix your response with FINAL ANSWER so the team knows to stop."
                " You have access to the following tools: {tool_names}.\\\\n{system_message}",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    prompt = prompt.partial(system_message=system_message)
    prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
    return prompt | llm.bind_functions(functions)

# Agents
data_extractor_agent = create_agent(
    llm,
    [process_json_arrays],
    system_message="You should extract data from the two files for the Data Analyst agent to use."
)

data_analyst_agent = create_agent(
    llm,
    [analyze_json_array],
    system_message="You should analyze the extracted data and draw insights to be shown to the user."
)

# Nodes
extractor_node = functools.partial(agent_node, agent=data_extractor_agent, name="Data Extractor")
analyst_node = functools.partial(agent_node, agent=data_analyst_agent, name="Data Analyst")

# Workflow
workflow = StateGraph(AgentState)

workflow.add_node("Data Extractor", extractor_node)
workflow.add_node("Data Analyst", analyst_node)
workflow.add_node("call_tool", tool_node)

workflow.add_conditional_edges(
    "Data Extractor",
    router,
    {"continue": "Data Analyst", "call_tool": "call_tool", "end": END},
)
workflow.add_conditional_edges(
    "Data Analyst",
    router,
    {"continue": "Data Extractor", "call_tool": "call_tool", "end": END},
)
workflow.add_conditional_edges(
    "call_tool",
    lambda x: x["sender"],
    {
        "Data Extractor": "Data Extractor",
        "Data Analyst": "Data Analyst",
    },
)

workflow.set_entry_point("Data Extractor")
graph = workflow.compile()

# Execution
for s in graph.stream(
    {
        "messages": [
            HumanMessage(
                content="Give me some data insights from the two JSON files."
            )
        ],
    },
    {"recursion_limit": 150},
):
    print(s)
    print("----")