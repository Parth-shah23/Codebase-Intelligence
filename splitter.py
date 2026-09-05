from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)
from pathlib import Path

# The RecursiveCharacterTextSplitter attempts to keep larger units (e.g., paragraphs) intact.
# If a unit exceeds the chunk size, it moves to the next level (e.g., sentences).
# This process continues down to the word level if necessary.


list = [e.value for e in Language] #List of lang supported by langchain for codes


from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

def split_into_chunks(clean_files):
    # 1. Pre-instantiate language splitters outside the loop for maximum speed
    language_splitters = {
        ".js": RecursiveCharacterTextSplitter.from_language(
            Language.JS, chunk_size=1000, chunk_overlap=150
        ),
        ".jsx": RecursiveCharacterTextSplitter.from_language(
            Language.JS, chunk_size=1000, chunk_overlap=150
        ),
        ".html": RecursiveCharacterTextSplitter.from_language(
            Language.HTML, chunk_size=1000, chunk_overlap=150
        ),
        ".ejs": RecursiveCharacterTextSplitter.from_language(
            Language.HTML, chunk_size=1000, chunk_overlap=150
        ),
        ".md": RecursiveCharacterTextSplitter.from_language(
            Language.MARKDOWN, chunk_size=1000, chunk_overlap=150
        ),
    }

    css_splitter = RecursiveCharacterTextSplitter(
        separators=["\n}\n", "}\n", "\n/*", "\n\n", "\n", " "],
        chunk_size=1000,
        chunk_overlap=150,
    )

    default_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )

    chunks = []

    for file_path in clean_files:
        path_obj = Path(file_path)
        suffix = path_obj.suffix.lower()

        try:
            with open(path_obj, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception as e:
            print(f"Skipping file {path_obj.name}: {e}")
            continue

        # Skip completely empty whitespace files
        if not content.strip():
            continue

        metadata = {
            "source": str(path_obj),
            "file_name": path_obj.name,
            "extension": suffix,
        }

        # 2. Select pre-built splitter instance
        if suffix == ".css":
            splitter = css_splitter
        elif suffix in language_splitters:
            splitter = language_splitters[suffix]
        else:
            splitter = default_splitter

        # Generate documents and flatten into chunks list
        docs = splitter.create_documents([content], [metadata])
        chunks.extend(docs)

    return chunks