from langchain.prompts import PromptTemplate

template = """
    You are a code review agent. Analyze the following patch for xyz:

    Patch:
    xyz

    Identify:
    - Style issues
    - Potential bugs
    - Best practices
    - Performance concerns

    Provide a structured JSON response with your findings.

    Thought:{agent_scratchpad}
"""

review_prompt = PromptTemplate.from_template(template)
