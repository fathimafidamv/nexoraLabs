from langchain_community.document_loaders import PyPDFLoader

def pdfLoader(pdf_paths):
    all_documents=[]
    for pdf_path in pdf_paths:
        loader=PyPDFLoader(pdf_path)
        documents= loader.load()
        all_documents.extend(documents)
    return all_documents