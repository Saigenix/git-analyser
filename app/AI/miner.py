import requests
from app.AI.model import generate_review


def extract_owner_repo(url: str):
    parts = url.split("/")

    if len(parts) >= 5 and parts[2] == "github.com":
        owner = parts[3]
        repo = parts[4]
        return owner, repo
    else:
        raise ValueError("Invalid GitHub URL format")


def get_code(repo: str, pr_number: int, github_token: str):
    repo_owner, repo_name = extract_owner_repo(repo)
    # if github_token != "":
    #     headers = {"Authorization": f"Bearer {github_token}"}
    github_api_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/files"
    )

    code_content = ""

    try:
        response = requests.get(github_api_url)

        if response.status_code == 200:
            pr_files = response.json()

            for file in pr_files:
                file_url = file["raw_url"]
                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    code_content += "\n" + file_response.text
                else:
                    print(f"Failed to fetch file content: {file['filename']}")
        else:
            print(f"Failed to fetch PR files: {response.status_code}")
            return {"error": f"Failed to fetch PR files: {response.status_code}"}
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}

    # Analyze code content
    review = generate_review(code_content)

    # Return the analysis results
    return {
        "res": review,
    }
