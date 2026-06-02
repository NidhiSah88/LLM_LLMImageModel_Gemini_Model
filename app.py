from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables from .env file

import streamlit as st 
import os 
import google.generativeai as genai 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) ## configuring the google generative ai with the api key from environment variable

##  function to load Gemini Pro model and responses 
# model=genai.GenerativeModel("gemini-pro") ## loading the Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text 

# Streamlit UI
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

user_input = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

if submit:
    with st.spinner("Generating response..."):
        response = get_gemini_response(user_input)
        st.write("Response:")
        st.write(response)













    















