from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


embedding_model=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
persistance_diarectory="backend/chroma"


def pdfEmbeddings(chunks):
    embeddings=embedding_model
    text=[chunk.page_content for chunk in chunks]
    documents=embeddings.embed_documents(text)
    return documents

def vectorestore(chunks):
    vectore_db=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persistance_diarectory
    )
    return vectore_db
