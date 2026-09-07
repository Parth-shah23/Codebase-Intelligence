from clone import clone_repo
from clean import clean_files_pathspec
from splitter import split_into_chunks
from embeddings import create_embeddings_store_in_vectorDB

repo,username,repo_name = clone_repo()
cleaned_files = clean_files_pathspec(repo)
chunks = split_into_chunks(cleaned_files,username,repo_name)
vector_db = create_embeddings_store_in_vectorDB(chunks)
