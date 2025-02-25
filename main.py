import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant, please respond to the user's questions"),
        ("user", "question:{question}")
    ]
)

groq_api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)
output = StrOutputParser()


st.title("Mindful AI Chatbot")
st.write("This is a simple chatbot that can answer your questions.")
input_text = st.text_input("Ask me anything")

chain = prompt|llm|output

if input_text:
    st.subheader("Answer:")
    st.write(chain.invoke({"question": input_text}))