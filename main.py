import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
st.title("Langchain First UI Project")
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
   api_key=api_key,
)
input = st.text_input("Search Your Query")
bt = st.button("Search")
if input is not None:
    if bt:
        response = llm.invoke(input)
        st.write(response.content)


