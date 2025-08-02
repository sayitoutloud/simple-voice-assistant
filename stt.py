import speech_recognition as sr
from lm_studio import LMStudioClient
from tts import SpeechOutput

# Speech To Text
class STT:
    def __init__(self, lan="en-EN"):
        self.recognizer = sr.Recognizer()
        self.language = lan
        self.assistent = LMStudioClient()
        self.tts = SpeechOutput("en")

    def start(self):
        with sr.Microphone() as quelle:
            print("??? Voice monitoring started. You can speak any time...")
            self.recognizer.adjust_for_ambient_noise(quelle)

            while True:
                try:
                    print("?? ...Waiting for voice input...")
                    audio = self.recognizer.listen(quelle)

                    print("?? Processing the language...")
                    text = self.recognizer.recognize_google(audio, language=self.language)

                    print("?? Recognized:", text)

                    # ?? Send to LM Studio
                    answer = self.assistent.question(text)
                    self.tts.speak(answer)
                    print("?? Answer of LM Studio:", antwort)
                    print("-" * 50)

                except sr.UnknownValueError:
                    print("?? Speech could not be understood.")
                except sr.RequestError as e:
                    print("? Google-Error:", e)
                except KeyboardInterrupt:
                    print("\n?? Program terminated by user.")
                    break
