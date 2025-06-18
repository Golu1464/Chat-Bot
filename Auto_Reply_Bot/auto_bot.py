# auto_bot.py
import pyautogui
import pyperclip
import time
from openai import OpenAI

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name in messages

def start_bot(api_key):
    client = OpenAI(api_key=api_key)
    st = __import__('streamlit')  # Lazy import to use Streamlit messages

    st.info("Bot is now running. Switch to WhatsApp Web and wait for messages...")
    pyautogui.click(1639, 1412)
    time.sleep(1)

    while True:
        time.sleep(5)
        pyautogui.moveTo(972, 202)
        pyautogui.dragTo(2213, 1278, duration=2.0, button='left')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        pyautogui.click(1994, 281)

        chat_history = pyperclip.paste()
        if is_last_message_from_sender(chat_history):
            try:
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are Naruto, a bilingual coder from India. Respond humorously and roast the other person."},
                        {"role": "system", "content": "Don't start like this: [21:02, 12/6/2024] Rohan Das:"},
                        {"role": "user", "content": chat_history}
                    ]
                )
                response = completion.choices[0].message.content
                pyperclip.copy(response)
                pyautogui.click(1808, 1328)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
                pyautogui.press('enter')
            except Exception as e:
                st.error(f"Bot Error: {e}")
                break
