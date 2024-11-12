import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

PROMPT = """
You are a code reviewer for pull requests of github. Your job is to provide a detailed analysis of the code changes in a pull request. Please provide a comprehensive review that includes:
- Code structure and organization
- Functionality and purpose of the code
- Readability and clarity of the code
- Potential bugs and errors
- Suggestions for improvements
- Any other relevant information that can help improve the code
Please provide a detailed analysis that is easy to understand and follows a consistent style.
"""

def generate_review(code):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{PROMPT}: {code}")
    # print("review", response.text)
    return response.text
