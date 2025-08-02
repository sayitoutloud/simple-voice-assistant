import requests

class LMStudioClient:
    def __init__(self, url="http://YOUR_IP/lmstudio-api/v1/chat/completions", model="llama3:8b", token="lm-studio"):
        self.url = url
        self.model = model
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def question(self, msg: str, temperature=0.7) -> str:
        daten = {
            "model": self.model,
            "messages": [{"role": "user", "content": msg}],
            "temperature": temperature
        }

        try:
            answer = requests.post(self.url, headers=self.headers, json=daten)
            answer.raise_for_status()
            ergebnis = answer.json()
            return ergebnis['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"? Error in LM Studio request: {e}"
