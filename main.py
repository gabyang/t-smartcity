import os 
from getpass4 import getpass
from langchain_ibm import WatsonxLLM

watsonx_api_key = getpass("input your watsonx api key: ")
os.environ["WATSONX_APIKEY"] = watsonx_api_key

#NEED TO ADJUST AGAIN LATER
parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 100,
    "min_new_tokens": 1,
    "temperature": 1,
    "top_k": 50,
    "top_p": 1,
}

#MODEL INITIALIZATION
#CURRENTLY USING US SOUTH REGION
watsonx_llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    url="https://us-south.ml.cloud.ibm.com",
    project_id="b34cd5a2-d419-4360-b4f0-83308e7bacd5",
    params=parameters,
)

# Calling a single prompt

watsonx_llm.invoke("Who is man's best friend?")

for chunk in watsonx_llm.stream(
    "Describe your favorite breed of dog and why it is your favorite."
):
    print(chunk, end="")




