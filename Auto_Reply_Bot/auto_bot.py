# auto_bot.py (Cloud-safe version without GUI)
from openai import OpenAI

def start_bot(chat_text, api_key):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Naruto, a bilingual coder from India. Respond humorously and roast the other person."},
            {"role": "user", "content": chat_text}
        ]
    )
    return completion.choices[0].message.content
