import os
import json
import openai

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def load_json(file_path):
    """
    Load JSON data from the specified file path.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    print(f"Loading JSON file: {file_path}")  # Debug print
    with open(file_path, 'r') as f:
        data = json.load(f)
    print(f"Successfully loaded JSON data from {file_path}")  # Debug print
    return data

def generate_insight_report(user_input):
    """
    Generate an insight report based on user input and loaded JSON data.
    """
    try:
        print("Step 1: Loading data from specified files...")  # Debug print
        json_data = []
        
        file_paths = [
            "data/combined_park_area_per_subzone_square_meters.json",
            "data/combined_park_CIB_counts_per_subzone.json"
        ]
        
        for file in file_paths:
            json_data.append(load_json(file))
        
        # Combine all JSONs into a single string for the AI
        print("Step 2: Combining JSON data into a single string...")  # Debug print
        combined_data = "\n\n".join([json.dumps(data, indent=2) for data in json_data])

        # Step 3: Send data and user input to OpenAI
        print("Step 3: Sending data and query to OpenAI for analysis...")  # Debug print
        system_prompt = (
            "You are an AI trained to analyze data. A user will provide data in JSON format "
            "along with a query. Your job is to analyze the data and generate a clear, concise insight report. "
            "If you need to calculate averages, identify trends, or find extremes, do so based on the data provided."
            "Use your knowledge of Singapore geography in the analysis"
            "The data might be insufficient to generate an insight report."
            "If you think so, propose what data would be helpful for the urban planner to collect, and say that you are unable to answer the question"
            "You should use your contextual knowledge to provide qualitative insights in addition to data analysis."
        )
        user_message = (
            f"User query: {user_input}\n\n"
            f"JSON data:\n{combined_data}\n\n"
            "Generate an insight report based on the query and data."
        )

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.5,
            max_tokens=2000
        )

        print("Insight report successfully generated.")  # Debug print
        # Return the AI-generated insight report
        return response.choices[0].message.content.strip()

    except ValueError as e:
        print(f"An error occurred: {e}")  # Debug print
        return str(e)

#user_input = "Give me insights into the distribution of green space in Singapore."
#print("Starting the insight generation process...")  # Debug print
#insight_report = generate_insight_report(user_input, file_paths)
#print("\nInsight Report:\n", insight_report)

#output_file = "insight_report.txt"
#print(f"Writing the insight report to {output_file}...")  # Debug print
#with open(output_file, 'w') as f:
#    f.write(insight_report)
#print(f"Insight report successfully written to {output_file}.")  # Debug print