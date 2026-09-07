import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

def create_embeddings_store_in_vectorDB(chunks):
    # Wrap SentenceTransformer in LangChain's HuggingFaceEmbeddings class
    embeddings = HuggingFaceEmbeddings(
        model_name="nomic-ai/nomic-embed-code",
        model_kwargs={
            "trust_remote_code": True,
            "device": "cpu"  # Use "cuda" if running on a local GPU machine
        },
        encode_kwargs={
            "normalize_embeddings": True
        },
        query_encode_kwargs={
            "prompt_name": "query",  # Applies query prompt instruction automatically
            "normalize_embeddings": True
        }
    )

    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="codebase_intelligence"
    )
    
    return vector_store




