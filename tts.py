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
            print("? Fehler bei SprachAusgabe:", e)
