import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

PROMPT = """
You are a code reviewer for pull requests of github. Your job is to provide a detailed analysis of the code changes in a pull request. Please provide a comprehensive review that includes:
- Code style and formatting issues
- Potential bugs or errors
- Performance improvements
- Best practices
Please provide a detailed analysis that is easy to understand and follows a consistent style.PLEASE provide
output in JSON Format similar to this:
 "files": [
            {
                "name": "main.py",
                "issues": [
                    {
                        "type": "style",
                        "line": 15,
                        "description": "Line too long",
                        "suggestion": "Break line into multiple lines"
                    },
                    {
                        "type": "bug",
                        "line": 23,
                        "description": "Potential null pointer",
                        "suggestion": "Add null check"
                    }
                ]
            }
        ],
        "summary": {
            "total_files": 1,
            "total_issues": 2,
            "critical_issues": 1
        }
"""


def generate_review(code):
    print("code: \n\n\n", code)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{PROMPT}: {code}")
    # print("review", response.text)
    return code
