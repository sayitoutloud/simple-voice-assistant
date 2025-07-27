import requests

class LMStudioClient:
    def __init__(self, url="http://YOUR_IP/lmstudio-api/v1/chat/completions", model="llama3:8b", token="lm-studio"):
        self.url = url
        self.model = model
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def frage(self, nachricht: str, temperature=0.7) -> str:
        daten = {
            "model": self.model,
            "messages": [{"role": "user", "content": nachricht}],
            "temperature": temperature
        }

        try:
            antwort = requests.post(self.url, headers=self.headers, json=daten)
            antwort.raise_for_status()
            ergebnis = antwort.json()
            return ergebnis['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"? Fehler bei LM Studio Anfrage: {e}"
