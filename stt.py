import speech_recognition as sr
from lm_studio import LMStudioClient
from tts import SprachAusgabe

# Speech To Text
class STT:
    def __init__(self, sprache="de-DE"):
        self.recognizer = sr.Recognizer()
        self.sprache = sprache
        self.assistent = LMStudioClient()
        self.tts = SprachAusgabe("de")

    def start(self):
        with sr.Microphone() as quelle:
            print("??? Sprachueberwachung gestartet. Sprich jederzeit...")
            self.recognizer.adjust_for_ambient_noise(quelle)

            while True:
                try:
                    print("?? ...warte auf Spracheingabe...")
                    audio = self.recognizer.listen(quelle)

                    print("?? Verarbeite Sprache...")
                    text = self.recognizer.recognize_google(audio, language=self.sprache)

                    print("?? Erkannt:", text)

                    # ?? An LM Studio schicken
                    antwort = self.assistent.frage(text)
                    self.tts.sprechen(antwort)
                    print("?? Antwort von LM Studio:", antwort)
                    print("-" * 50)

                except sr.UnknownValueError:
                    print("?? Sprache konnte nicht verstanden werden.")
                except sr.RequestError as e:
                    print("? Google-Fehler:", e)
                except KeyboardInterrupt:
                    print("\n?? Programm durch Benutzer beendet.")
                    break
