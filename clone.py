from git import Repo
from pathlib import Path
from urllib.parse import urlparse
import re

def parse_github_url(url: str):
    pattern = r"^(?:https?:\/\/|git@)github\.com[:\/](?P<username>[^\/]+)\/(?P<repo>[^\/\s.]+?)(?:\.git)?\/?$"
    match = re.search(pattern, url.strip())
    
    if match:
        username = match.group("username")
        repo_name = match.group("repo")
        return username, repo_name
    else:
        raise ValueError("Invalid GitHub repository URL")

def clone_repo():
    github_url = input("Enter github url: ")
    # Get repository name
    repo_name = Path(urlparse(github_url).path).name
    # Local destination
    local_path = Path("repos") / repo_name
    # Create repos folder if it doesn't exist
    local_path.parent.mkdir(parents=True, exist_ok=True)
    # Clone repository (added depth=1 for faster shallow cloning)
    Repo.clone_from(github_url, local_path, depth=1)
    print("Repository cloned successfully!")
    print("Location:", local_path)
    return (str(local_path),parse_github_url(github_url))