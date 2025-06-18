from openai import OpenAI

def start_bot(chat_history, api_key):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Naruto, a bilingual coder from India. Respond humorously and roast the other person."},
            {"role": "system", "content": "Don't start like this: [21:02, 12/6/2024] Rohan Das:"},
            {"role": "user", "content": chat_history}
        ]
    )
    return response.choices[0].message.content
