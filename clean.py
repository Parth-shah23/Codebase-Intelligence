import os
from pathlib import Path
import pathspec

def clean_files_pathspec(repo):
    repo = Path(repo).resolve()
    gitignore_path = repo / ".gitignore"
    
    patterns = [".git/"]  # Always exclude .git
    
    # Read .gitignore patterns if the file exists
    if gitignore_path.is_file():
        with open(gitignore_path, "r", encoding="utf-8") as f:
            patterns.extend(f.readlines())
            
    # Build GitIgnoreSpec matcher
    spec = pathspec.GitIgnoreSpec.from_lines(patterns)

    # 1. Non-text assets & binaries to exclude for RAG
    not_allowed_exts = {
        ".json", ".png", ".jpg", ".jpeg", ".gif", 
        ".svg", ".ico", ".webp", ".pdf", ".zip", ".pyc"
    }

    # 2. File names to exclude (config noise/lockfiles)
    not_allowed_names = {
        ".gitignore", ".env", "package-lock.json", 
        "yarn.lock", "pnpm-lock.yaml", "poetry.lock"
    }

    clean_files = []

    for root, dirnames, filenames in os.walk(repo):
        rel_root = Path(root).relative_to(repo)

        # Prune ignored directories using pathspec
        dirnames[:] = [
            d for d in dirnames 
            if not spec.match_file(str(rel_root / d) + "/")
        ]

        for filename in filenames:
            rel_file_path = rel_root / filename
            abs_file_path = Path(root) / filename

            # Skip if matched by .gitignore rules
            if spec.match_file(str(rel_file_path)):
                continue

            # Skip explicitly blacklisted file names (e.g. .gitignore)
            if filename in not_allowed_names:
                continue

            # Skip binary, asset, and image extensions
            if abs_file_path.suffix.lower() in not_allowed_exts:
                continue

            clean_files.append(abs_file_path)

    return clean_files



