import openai
import re
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def parse_query(user_query: str):
    """
    Expected format: 'generate synthetic data for <city_or_country> with <type_of_data> to <do_something>'

    Returns:
        location (str): The city or country from the query
        data_type (str): The type of data requested (e.g. 'demographic data', 'financial data')
        purpose (str): The reason or purpose for generating data
    """

    pattern = r"Generate synthetic data for (.+?) with (.+?) to (.+)"
    match = re.search(pattern, user_query, re.IGNORECASE)

    if not match:
        raise ValueError(
            "Query not in expected format: 'Generate synthetic data for <city/country> with <type_of_data> to <action>'"
        )

    location = match.group(1).strip()
    data_type = match.group(2).strip()
    purpose = match.group(3).strip()

    return location, data_type, purpose


def get_locale_for_location(location: str) -> str:
    """
    A small dictionary that maps city/country names to a Faker locale.
    Fallback to 'en_US' if unknown.
    """

    locale_map = {
        "Germany": "de_DE",
        "Berlin": "de_DE",
        "France": "fr_FR",
        "Paris": "fr_FR",
        "United States": "en_US",
        "USA": "en_US",
        "Singapore": "en_SG",
        "India": "en_IN",
        "Japan": "ja_JP",
        "China": "zh_CN",
    }

    # Do a simple case-insensitive match
    normalized = location.lower()
    for key in locale_map:
        if key.lower() == normalized:
            return locale_map[key]

    # Default fallback
    return "en_US"


def suggest_columns_for_data_type(data_type: str):
    """
    Return a list of column specs for the requested data type.
    Each spec can be a dict with keys: name, type, description.
    """

    data_type_lower = data_type.lower()

    if "demographic" in data_type_lower:
        # Basic demographic columns
        return [
            {"name": "Id", "type": "string", "description": "UUID"},
            {"name": "Name", "type": "string", "description": "Local Names"},
            {"name": "Age", "type": "int", "description": "18 to 80"},
            {"name": "Gender", "type": "string", "description": "Inclusive"},
            {"name": "Location", "type": "string", "description": "City/Region"},
        ]
    elif "financial" in data_type_lower:
        # Sample financial columns
        return [
            {"name": "TransactionId", "type": "string", "description": "UUID"},
            {"name": "AccountHolder", "type": "string", "description": "Name"},
            {
                "name": "TransactionDate",
                "type": "datetime",
                "description": "Random date/time",
            },
            {"name": "Amount", "type": "float", "description": "Transaction amount"},
            {
                "name": "Currency",
                "type": "string",
                "description": "Local currency code",
            },
        ]
    else:
        # Fallback / default set of columns
        return [
            {"name": "Id", "type": "string", "description": "UUID"},
            {
                "name": "Field1",
                "type": "string",
                "description": "Faker-generated string",
            },
            {"name": "Field2", "type": "int", "description": "Random integer"},
        ]


def build_code_generation_prompt(location: str, locale: str, columns: list):
    """
    Build the text prompt that instructs GPT to produce Python code.
    """
    # Format each column as required lines:
    column_lines = []
    for col in columns:
        column_lines.append(
            f"  Column name: {col['name']}, type: {col['type']}, Description: {col.get('description','')}"
        )

    column_instructions = "\n".join(column_lines)

    # Construct the final prompt:
    prompt = f"""
        Write python code to generate a pandas dataframe based on the requirements:
        {column_instructions}

        Note:
            - Return the code only, no additional texts or comments
            - Use faker library
            - Use the Faker locale: {locale}
            - Generate 100 rows
            - Final result must be saved as a CSV file named 'synthetic_data.csv'
        """
    return prompt.strip()


def generate_synthetic_data_code(user_query: str) -> str:
    location, data_type, purpose = parse_query(user_query)
    locale = get_locale_for_location(location)
    columns = suggest_columns_for_data_type(data_type)
    prompt_for_code = build_code_generation_prompt(location, locale, columns)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Python code."},
            {"role": "user", "content": prompt_for_code}
        ],
        max_tokens=700,
        temperature=0.2,
    )

    code_output = response.choices[0].message.content.strip()
    return code_output