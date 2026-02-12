import requests
import traceback
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
        ],
        "temperature": 0.7
    }

    try:
        print("Calling DeepSeek API...", flush=True)

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60   # 🔥 Important
        )

        print(f"API Status Code: {response.status_code}", flush=True)

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("DeepSeek API ERROR:", flush=True)
        traceback.print_exc()
        raise e



