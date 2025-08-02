from gtts import gTTS
import pygame
import tempfile

class SpeechOutput:
    def __init__(self, lan="en"):
        self.lan = lan
        pygame.mixer.init()

    def speak(self, text):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                tts = gTTS(text=text, lang=self.lan)
                tts.save(tmpfile.name)

                pygame.mixer.music.load(tmpfile.name)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
        except Exception as e:
            print("? Error in speech output:", e)
