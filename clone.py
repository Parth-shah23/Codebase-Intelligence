from git import Repo
from pathlib import Path
from urllib.parse import urlparse

def clone_repo():
    github_url = input("Enter github url: ")
    # Get repository name
    repo_name = Path(urlparse(github_url).path).name
    # Local destination
    local_path = Path("repos") / repo_name
    # Create repos folder if it doesn't exist
    local_path.parent.mkdir(parents=True, exist_ok=True)
    # Clone repository
    repo = Repo.clone_from(github_url, local_path)
    print("Repository cloned successfully!")
    print("Location:", local_path)
    return repo