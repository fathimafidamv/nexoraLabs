from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI

from backend.model import ChatRequest
from backend.rag.load import pdfLoader
from backend.rag.splitter import pdfSplitter
from backend.rag.embedding import pdfEmbeddings , vectorestore
from backend.query import chat


app = FastAPI()


pdf_paths=[
    "backend/data/Nexora_Company_Profile.pdf",
    "backend/data/Nexora_Product_Catalogue.pdf",
    "backend/data/Nexora_FAQ.pdf"
]

documents=pdfLoader(pdf_paths)

chunks=pdfSplitter(documents)

embeddings=pdfEmbeddings(chunks)

vectore_db = vectorestore(documents)


@app.get("/")
def home():
    return{
        "Nexora backend running succsesfully"
    }

@app.post("/chat")
def ask_query(request:ChatRequest):
    answer = chat(
        request.query,
        vectore_db
    )

    return{
        "answer":answer
    }