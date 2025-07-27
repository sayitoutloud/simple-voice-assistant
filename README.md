# simple-voice-assistant

## Requirements
- Install LM Studio on your System (Windows) and activate the localhost API
- Raspberry Pi (4)
- Reverse Proxy Service: apache, nginx (I use xampp)

## Reverse Proxy Config
For xampp:
xampp\apache\conf\httpd.conf   
activate these two lines
```
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
```

xampp/apache/conf/extra/httpd-vhosts.conf   
add
```
<VirtualHost *:80>
    ServerName localhost
    DocumentRoot "C:/xampp/htdocs"

    ProxyRequests Off
    ProxyPreserveHost On

    <Proxy *>
        Require all granted
    </Proxy>

    ProxyPass /lmstudio-api/ http://localhost:1234/
    ProxyPassReverse /lmstudio-api/ http://localhost:1234/
</VirtualHost>
```

## Request Script (Python)
```
import requests

url = "http://10.0.0.45/lmstudio-api/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer lm-studio"
}

data = {
    "model": "llama3:8b",
    "messages": [{"role": "user", "content": "Hallo!"}],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

```

## Voice recognation & change it to text
```
pip install SpeechRecognition
pip install PyAudio
```

Google akzeptiert Audio nur in bestimmten Formaten (z. B. FLAC oder WAV)
Die speech_recognition-Bibliothek wandelt dein aufgenommenes Audio automatisch ins FLAC-Format um
Dafür wird das externe Tool flac verwendet (nicht in Python enthalten)
Ist es nicht vorhanden, bekommst du genau den Fehler, den du jetzt siehst
```
sudo apt update
sudo apt install flac
```

Script
```
import speech_recognition as sr

# Erkenner erstellen
recognizer = sr.Recognizer()

# Mikrofon verwenden
with sr.Microphone() as quelle:
    print("??? Bitte sprich jetzt...")
    recognizer.adjust_for_ambient_noise(quelle)  
    audio = recognizer.listen(quelle)           

    print("?? Verarbeite Sprache...")

    try:
        
        text = recognizer.recognize_google(audio, language="de-DE")
        print("?? Erkannt: " + text)
    except sr.UnknownValueError:
        print("?? Sprache konnte nicht erkannt werden.")
    except sr.RequestError as e:
        print(f"? Fehler bei der Verbindung zu Google: {e}")
```

## TTS Part (make sure! you have already SpeechRecognition installed)
```
pip install gtts playsound pygame
sudo apt install python3-gi gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
```

script
```
# tts.py

from gtts import gTTS
import pygame
import tempfile

class SprachAusgabe:
    def __init__(self, sprache="de"):
        self.sprache = sprache
        pygame.mixer.init()

    def sprechen(self, text):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                tts = gTTS(text=text, lang=self.sprache)
                tts.save(tmpfile.name)

                pygame.mixer.music.load(tmpfile.name)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
        except Exception as e:
            print("❌ Fehler bei SprachAusgabe:", e)

```
