import streamlit as st 
import requests

from dotenv import load_dotenv
load_dotenv()

st.title(":blue[NexoraDocs AI]")
st.markdown("An AI-powered document assistant")


if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)



query = st.chat_input("Ask about nexora...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append(
        {
            "role":"user",
            "content":query
        }
    )


    with st.chat_message("assistant"):
        with st.spinner("searching..."):
            BACKEND_URL="https://nexoralabs-itv0.onrender.com"
            try:
                response=requests.post(
                f"{BACKEND_URL}/chat",
                json={"query":query},
                timeout=20
                )
            except Exception as e:
                print(f"Error because {e}")

            answer=response.json()["answer"]
        st.markdown(answer)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )







