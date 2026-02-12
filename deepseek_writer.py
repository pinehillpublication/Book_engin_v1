import requests
from config import DEEPSEEK_API_KEY

def write_text(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()["choices"][0]["message"]["content"]

