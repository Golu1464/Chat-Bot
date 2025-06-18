import streamlit as st
from openai import OpenAI

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    messages = chat_log.strip().split("/2024] ")
    return any(sender_name in msg for msg in messages[-2:])

def start_bot(chat_history, api_key):
    client = OpenAI(api_key=api_key)

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Naruto, a bilingual coder from India. Respond humorously and roast the other person."},
                {"role": "system", "content": "Don't start like this: [21:02, 12/6/2024] Rohan Das:"},
                {"role": "user", "content": chat_history}
            ]
        )
        return completion.choices[0].message.content.strip()
    else:
        return "No new message from Rohan Das to reply to."
