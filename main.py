from flask import Flask, request
import requests
import os
from utils.openai_client import ask_gpt

app = Flask(__name__)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not set!")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print("=== Incoming JSON from Telegram ===")
    print(data)

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if not text:
        return "ok"

    response = ask_gpt(text)
    send_message(chat_id, response)
    return "ok"

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

