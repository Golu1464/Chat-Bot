# main.py
import streamlit as st
from auto_bot import start_bot

st.set_page_config(page_title="Auto Chat Replier")

st.title("🤖 Naruto Chat Replier")
st.markdown("Simulates how Naruto would roast someone based on your pasted chat.")

api_key = st.text_input("Enter OpenAI API Key", type="password")
chat_text = st.text_area("Paste WhatsApp Chat Text")

if st.button("Generate Reply"):
    if not api_key or not chat_text:
        st.warning("API key and chat are required.")
    else:
        try:
            reply = start_bot(chat_text, api_key)
            st.success("✅ Reply generated successfully:")
            st.markdown(f"**💬 Naruto's Reply:**\n\n{reply}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
