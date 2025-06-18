# main.py
import streamlit as st
from auto_bot import start_bot

st.set_page_config(page_title="Auto Chat Replier by Sonu Kumar Sharma")
st.title("🤖 Auto Chat Replier - Naruto Style")

st.markdown("This bot replies on WhatsApp like Naruto. Paste your API key and it starts auto-replying.")

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    if st.button("Start Bot"):
        start_bot(api_key)
else:
    st.warning("Please enter your OpenAI API key to proceed.")
