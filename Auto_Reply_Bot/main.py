import streamlit as st
from auto_bot import start_bot
from watermark import add_watermark

st.set_page_config(page_title="Auto Chat Replier by Sonu Kumar Sharma", layout="centered")
st.title("🤖 Auto Chat Replier - Naruto Style")

add_watermark()

api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
chat_history = st.text_area("Paste WhatsApp Chat Here", height=300)

if st.button("Generate Reply"):
    if not api_key or not chat_history:
        st.warning("Please provide both chat and API key.")
    else:
        try:
            response = start_bot(chat_history, api_key)
            st.success("✅ Reply Generated:")
            st.markdown(f"**💬 Naruto's Reply:**\n\n{response}")
        except Exception as e:
            st.error(f"Error: {e}")
