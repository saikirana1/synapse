import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


def openai_client():
    api_key = os.getenv("open_ai_api_key")
    return OpenAI(api_key=api_key)
