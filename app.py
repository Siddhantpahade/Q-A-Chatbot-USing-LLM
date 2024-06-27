# Q&A Chatbot

# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()   # Take environment variables from .env

import streamlit as st
import os

## Function to load OpenAI Model and get response
def get_openai_response(question):
    if not question:
        return "Input cannot be empty. Please ask a question."
    
    chat_model = ChatOpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model="gpt-3.5-turbo")
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=str(question))  # Ensure the question is a string
    ]
    response = chat_model(messages)
    return response.content  # Accessing the content directly

## Initialize our Streamlit App
st.set_page_config(page_title="Q&A Demo")

st.header("LangChain Application")

input_text = st.text_input("Input : ", key="input")

submit = st.button("Generate")

## If Ask button is clicked
if submit:
    response = get_openai_response(input_text)
    st.subheader("The Response is")
    st.write(response)
