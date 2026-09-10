from clone import clone_repo
from clean import clean_files_pathspec
from splitter import split_into_chunks
from embeddings import create_embeddings_store_in_vectorDB
from query import generate_answer




repo, username, repo_name = clone_repo()
cleaned_files = clean_files_pathspec(repo)
chunks = split_into_chunks(cleaned_files, username, repo_name)
vector_db = create_embeddings_store_in_vectorDB(chunks)

print("\nVector store ready. Enter your queries below (Ctrl+C to exit).\n")
while True:
    try:
        answer = generate_answer(vector_db)
        print("\nAnswer:\n", answer, "\n")
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
        break
