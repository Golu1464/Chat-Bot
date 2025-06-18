import streamlit as st
from auto_bot import generate_reply

st.set_page_config(page_title="AI Auto Chat Bot", layout="centered")
st.title("🤖 AI Auto Chat Bot")

st.markdown("This bot replies like **Naruto** – fun, funny, and full of roast!")

api_key = st.text_input("🔐 Enter your OpenAI API Key", type="password")
user_message = st.text_area("💬 Enter your message to Naruto", height=200)

if st.button("Get Naruto's Reply"):
    if not api_key or not user_message:
        st.warning("Please provide both the API key and a message.")
    else:
        try:
            reply = generate_reply(user_message, api_key)
            st.success("Reply Generated:")
            st.markdown(f"**💬 Naruto's Reply:**\n\n{reply}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
