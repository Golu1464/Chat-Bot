from openai import OpenAI

def generate_reply(message, api_key):
    client = OpenAI(api_key=api_key)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Naruto, a bilingual coder from India. Respond humorously and roast the user like a friend."},
            {"role": "user", "content": message}
        ]
    )
    
    return completion.choices[0].message.content
