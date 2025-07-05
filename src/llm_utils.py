import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def get_gemini_model():
    api_key = os.getenv("GOOGLE_API_KEY")
    model_name = os.getenv("GOOGLE_MODEL_NAME")

    if not api_key or not model_name:
        raise ValueError("GOOGLE_API_KEY and GOOGLE_MODEL_NAME environment variables must be set.")

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)
