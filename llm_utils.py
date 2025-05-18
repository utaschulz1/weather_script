from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_llm_response(prompt):
    """Get a response from the LLM."""
    try:
        response = client.responses.create(
            model="gpt-4",
            instructions="You are a helpful but terse AI assistant.",
            input=prompt,
        )
        return response.output_text
    except Exception as e:
        print(f"Error getting LLM response: {e}")
        return None

def print_llm_response(prompt):
    """Print the LLM response."""
    response = get_llm_response(prompt)
    if response:
        print(response)