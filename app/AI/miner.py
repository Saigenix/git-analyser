from app.AI.model import generate_review
def get_code(repo: str, pr_number: int):
    # fetch the from repo
    # analyze code
    # return analysis results
    review = generate_review("print('hello world')")
    return {
        "res": review,
    }