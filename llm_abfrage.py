import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

#load environment variables from the .env file
load_dotenv('.env', override=True)

#Initilize the OpenAI Client
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def print_llm_response(prompt):
    """This function takes a prompt and prints the response from OpenAI's GPT-4o model."""
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a helpful but terse AI assistant.",
            input=prompt,
        )
        print(response.output_text)
    except Exception as e:
        print("Error:", str(e))

def get_llm_response(prompt):
    """This function takes a prompt and returns the response from OpenAI's GPT-4o model."""
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a helpful but terse AI assistant.",
            input=prompt,
        )
        return response.output_text
    except Exception as e:
        print("Error:", str(e))
        return None
    


