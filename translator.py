from deep_translator import GoogleTranslator
from gtts import gTTS
import os

print("🌍 Simple Translator")

text = input("Enter text: ")
lang = input("Enter language (hi, kn, ta, te, fr, es): ")

# Translate
translated = GoogleTranslator(source='auto', target=lang).translate(text)
print("Translated:", translated)

# Speak audio
file = "output.mp3"
gTTS(translated, lang=lang).save(file)
os.startfile(file)