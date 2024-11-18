from fastapi import FastAPI, HTTPException
from celery.result import AsyncResult
from pydantic import BaseModel
from workers.tasks import analyze_pr_task
from utils.json_parser import parse_json
import uuid
from celery.result import AsyncResult

app = FastAPI()


class AnalyzeRequest(BaseModel):
    repo_url: str
    pr_number: int
    github_token: str


# Endpoint to submit a new PR for analysis
@app.post("/analyze-pr")
async def analyze_pr(request: AnalyzeRequest):
    print(request.repo_url, request.pr_number)
    task_id = str(uuid.uuid4())
    task = analyze_pr_task.apply_async(
        args=[request.repo_url, request.pr_number], task_id=task_id
    )
    return {"task_id": task.id, "status": "submitted"}


# Endpoint to check the status of an analysis task
@app.get("/status/{task_id}")
async def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": "pending"}
    elif task_result.state == "STARTED":
        return {"task_id": task_id, "status": "processing"}
    elif task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": "completed"}
    elif task_result.state == "FAILURE":
        return {"task_id": task_id, "status": "failed", "error": str(task_result.info)}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


# Endpoint to retrieve the analysis results
@app.get("/results/{task_id}")
async def get_results(task_id: str):
    task_result = AsyncResult(task_id)
    if task_result.state != "SUCCESS":
        raise HTTPException(status_code=404, detail="Results not available")
    task_result.result.output = parse_json(task_result.result.output)
    return {"task_id": task_id, "results": task_result.result}


@app.get("/")
async def get_results():
    return {
        "message": "Welcome to the application",
    }
