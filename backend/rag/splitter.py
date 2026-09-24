from langchain_text_splitters import RecursiveCharacterTextSplitter

def pdfSplitter(doc:str):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=400 , 
        chunk_overlap=150
    )
    chunks=splitter.split_documents(doc)
    return chunks