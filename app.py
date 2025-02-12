import os
import streamlit as st
from google import genai

st.set_page_config("SUTD AI WORKSHOP")
st.title("Hello world")

client = genai.Client(api_key="YOUR-API-KEY") 
 
response = client.models.generate_content( 
    model='gemini-2.0-flash',  
    contents='Tell me what is AI in one paragraph' 
) 
 
st.write(response.text)


qns = st.text_input(label = "Ask Gemini Question")

if st.button("Submit"):
    response2 = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = qns
    )
    
    st.write(response2.text)