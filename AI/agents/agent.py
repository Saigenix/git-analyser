from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_google_genai import GoogleGenerativeAI
from prompts import review_prompt
from utils.github_service import fetch_files, fetch_file_diff
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")


def create_code_review_agent():
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

    tools = [
        StructuredTool.from_function(
            name="FetchFiles",
            func=fetch_files,
            description="Fetches the diff or patch for a specific file in a GitHub pull request.",
        ),
        StructuredTool.from_function(
            name="AnalyzeFileDiff",
            func=fetch_file_diff,
            description="Analyzes the content of a file for issues like style, bugs, or performance.",
        ),
    ]

    # Create the agent
    agent = create_tool_calling_agent(tools=tools, llm=llm, prompt=review_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor


