import requests


def extract_owner_repo(url: str):
    parts = url.split("/")

    if len(parts) >= 5 and parts[2] == "github.com":
        owner = parts[3]
        repo = parts[4]
        return owner, repo
    else:
        raise ValueError("Invalid GitHub URL format")


def fetch_files(repo: str, pr_number: int, github_token: str) -> dict:
    repo_owner, repo_name = extract_owner_repo(repo)
    # if github_token != "":
    #     headers = {"Authorization": f"Bearer {github_token}"}
    print("fetching files...")
    files_content = {}
    github_api_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/files"
    )
    try:
        response = requests.get(github_api_url)
        print("json", response.json())
        if response.status_code == 200:
            pr_files = response.json()

            for file in pr_files:
                file_url = file["raw_url"]
                file_response = requests.get(file_url)
                if file_response.status_code == 200:
                    files_content[file["filename"]] = file_response.text
                else:
                    print(f"Failed to fetch file content: {file['filename']}")
        else:
            print(f"Failed to fetch PR files: {response.status_code}")
            return {"error": f"Failed to fetch PR files: {response.status_code}"}
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}

    return files_content


def fetch_file_diff(repo: str, pr_number: int, github_token: str) -> dict:
    repo_owner, repo_name = extract_owner_repo(repo)
    # if github_token != "":
    #     headers = {"Authorization": f"Bearer {github_token}"}
    print("fetching files diff...")
    files_diff = {}
    github_api_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/files"
    )

    try:
        response = requests.get(github_api_url)

        if response.status_code == 200:
            pr_files = response.json()

            for file in pr_files:
                file_diff = file["patch"]
                files_diff[file["filename"]] = file_diff
        else:
            print(f"Failed to fetch PR files: {response.status_code}")
            return {"error": f"Failed to fetch PR files: {response.status_code}"}
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {"error": str(e)}

    return files_diff
