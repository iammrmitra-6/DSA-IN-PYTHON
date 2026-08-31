import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv

#LOAD ENVIRONMENT VARIABLE
load_dotenv()

#configure gemini API
genai.configure(api_key=os.getenv("AIzaSyCUt98Dbwa-dUvezOkxIkeooWEU4IIC7z0"))

#LOAD MODEL
model=genai.GenerativeModel("gemini-2.5-flash")

#streamlit UI
st.title("DAC-Disaster Awarness Channel")
st.title("your one and only space for updates related to disaster and its prepardness....")

#user input
user_input = st.text_input("Ask anything")

#button of generate response

if st.button("Get your updates..."):
    if user_input.strip()=="":
        st.warning("feel free to ask about latest disaster related queries or get to know about effective disaster prepardness.... ")
    else:
        prompt=f"""
        You are a helpful AI assignment.
        Answer the user's question clearly about disater management and do not answer any other topic rather than disater mangement.

        User: {user_input}
        AI:
        """

        response = model.generate_content(prompt)
        st.success(response.text)
