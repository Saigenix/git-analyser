from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult
from pydantic import BaseModel

# from app.tasks import analyze_pr_task
import uuid


app = FastAPI()


class AnalyzeRequest(BaseModel):
    repo_url: str
    pr_number: int
    github_token: str


# Endpoint to submit a new PR for analysis
@app.post("/analyze-pr")
async def analyze_pr(request: AnalyzeRequest):
    # print(request.repo, request.pr_number)
    task_id = str(uuid.uuid4())
    # task = analyze_pr_task.apply_async(
    #     args=[request.repo, request.pr_number], task_id=task_id
    # )
    return {"task_id": task_id, "status": "submitted"}


# Endpoint to check the status of an analysis task
@app.get("/status/{task_id}")
async def get_status(task_id: str):
    return {"task_id": task_id, "status": "in-progress"}


# Endpoint to retrieve the analysis results
@app.get("/results/{task_id}")
async def get_results(task_id: str):

    return {"task_id": task_id, "status": "completed"}


@app.get("/")
async def get_results():
    return {
        "message": "Welcome to the application",
    }
