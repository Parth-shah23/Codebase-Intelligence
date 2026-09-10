import os
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langchain_huggingface import HuggingFaceEmbeddings
# pyrefly: ignore [missing-import]
from langchain_qdrant import QdrantVectorStore

load_dotenv()

def embedding_model():
    # Wrap SentenceTransformer in LangChain's HuggingFaceEmbeddings class
    embeddings = HuggingFaceEmbeddings(
        model_name="nomic-ai/nomic-embed-text-v1.5",
        model_kwargs={
            "trust_remote_code": True,
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        },
        query_encode_kwargs={
            "prompt_name": "query",
            "normalize_embeddings": True
        }
    )
    return embeddings



def create_embeddings_store_in_vectorDB(chunks):
    embeddings = embedding_model()
    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name="codebase_intelligence"
    )
    return vector_store




