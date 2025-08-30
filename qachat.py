from dotenv import load_dotenv
load_dotenv() ##load all the environment variables from .env file

import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load Gemini flash Model and get responses
model=genai.GenerativeModel("gemini-2.5-flash")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response


##intializing the streamlit app
st.set_page_config(page_title="Q&A Demo", page_icon=":robot_face:")    
st.header("Gemini LLM Application :robot_face:")

## Intialize session state to store chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

##when submit is clicked

if submit and input:
    response=get_gemini_response(input)
    ## Add user query and response to sesstion chat history
    st.session_state['chat_history'].append(("You ",input))
    st.subheader("The Response is: ")

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot ",chunk.text))  

st.subheader("The Chat History is: ")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")    
    