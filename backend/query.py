from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")


def chat(query, vector_db):

    retrieved_docs = vector_db.similarity_search(query, k=4)

    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    prompt = f"""
You are NexoraDocs AI, an AI assistant for  Nexora Labs.
Our Company name is Nexora LAbs.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:
"I couldn't find this information in the provided Nexora Labs documents."

Do not make up information.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content