from celery import Celery
from AI.agents.agent import create_code_review_agent
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Celery
celery_app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_RESULT_BACKEND"),
)


@celery_app.task(bind=True)
def analyze_pr_task(self, repo: str, pr_number: int):
    print("async task is running...")
    agent = create_code_review_agent()
    result = agent.invoke(input={"repo": repo, "pr_number": pr_number, "github_token": ""})

    return result
