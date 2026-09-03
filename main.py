from clone import clone_repo
from loader import clean_files_pathspec
repo = clone_repo()
cleaned_files = clean_files_pathspec(repo)
print(cleaned_files)
