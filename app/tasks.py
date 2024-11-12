from celery import Celery
from app.AI.miner import get_code
# Configure Celery
celery_app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/1"
)


@celery_app.task(bind=True)
def analyze_pr_task(self, repo: str, pr_number: int):
    print("async task is running...")
    get_code_review = get_code(repo, pr_number)
    return {
        "repo": repo,
        "pr_number": pr_number,
        "review": get_code_review,
    }
