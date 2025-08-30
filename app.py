from dotenv import load_dotenv
load_dotenv() ##load all the environment variables from .env file

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro Model and get responses
model=genai.GenerativeModel("gemini-2.5-flash")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


##intializing the streamlit app
st.set_page_config(page_title="Q&A Demo", page_icon=":robot_face:")    
st.header("Ask me anything :robot_face:")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

##when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("Response: ")
    st.write(response)
