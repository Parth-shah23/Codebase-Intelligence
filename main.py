from clone import clone_repo
from clean import clean_files_pathspec
from splitter import split_into_chunks

repo = clone_repo()
cleaned_files = clean_files_pathspec(repo)
chunks = split_into_chunks(cleaned_files)
