import streamlit as st
from auto_bot import start_bot
from watermark import add_watermark

st.set_page_config(page_title="Auto Chat Replier by Sonu Kumar Sharma")

st.title("🤖 Auto Chat Replier")
add_watermark()

api_key = st.text_input("Enter your OpenAI API Key", type="password")

if api_key:
    st.success("API key added successfully. Starting bot...")
    start_bot(api_key)
else:
    st.warning("Please enter your OpenAI API key to start.")