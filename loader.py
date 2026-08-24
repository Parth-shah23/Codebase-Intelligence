from langchain_core import document_loaders
from pathlib import Path
def clean_files(repo):
    repo = Path(repo)
    # 1. Names of folders/files to skip completely
    not_allowed_names = {".git", ".gitignore"}
    # 2. File extensions to skip (always include the dot)
    not_allowed_exts = {".json"}
    clean_files = [
        f for f in repo.rglob("*")
        if f.is_file()  # Ensures directories aren't included
        and f.name not in not_allowed_names  # Filters full names (e.g. .gitignore)
        and f.suffix.lower() not in not_allowed_exts  # Filters extensions (e.g. .json)
        and not any(part in not_allowed_names for part in f.parts)  # Prevents searching inside .git folder
    ]
    return clean_files