import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
api_key = os.getenv("API_KEY")


async def generate_review(code):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("give review for this code", code)
    print("review",response.text)
    return response.text
