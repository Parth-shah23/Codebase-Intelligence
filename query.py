from embeddings import embedding_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_query(vector_store):
    query = input("Enter your query: ")
    embeddings = embedding_model()
    return vector_store.similarity_search_with_score(query, k=5), query
      

def generate_answer(vector_store):
    query_results, query = get_query(vector_store)
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an expert AI codebase assistant. Answer the user's question accurately "
            "using ONLY the provided code snippets as context. "
            "Refer to specific file names when explaining. "
            "If the context is insufficient, state that clearly.\n\n"
            "Code Context:\n{context}"
        )),
        ("human", "{question}")
    ])
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.2,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    chain = prompt | llm | StrOutputParser()

    context_str = "\n\n".join(
        f"[Score: {score:.3f}] File: {doc.metadata.get('file_name', '?')}\n{doc.page_content}"
        for doc, score in query_results
    )

    return chain.invoke({"context": context_str, "question": query})