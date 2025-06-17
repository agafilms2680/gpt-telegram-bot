import openai
import os

# Получаем API-ключ из переменной окружения
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Основная функция — отправляет запрос к GPT и возвращает ответ
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Ты — умный и дружелюбный Telegram-ассистент."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"].strip()

