from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

def ask_openai(message: str):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=message
    )

    return response.output_text