import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
import asyncio

words_by_level = {
    "fácil": ["gato", "cachorro", "maçã", "leite", "sol"],
    "médio": ["casa", "escola", "amigo", "janela", "amarelo"],
    "difícil": ["tecnologia", "universidade", "informação", "pronúncia", "imaginação"]
}

dificuldade = input("qual dificuldade você quer?(fácil, médio, difícil)")

palavra_escolhida = random.choice(words_by_level[dificuldade])

print(palavra_escolhida, "fale esse palavra em englês")




duration = 5  # segundos de gravação
sample_rate = 44100
print("Fale agora...")
recording = sd.rec(
  int(duration * sample_rate), # o número de amostras a serem registradas
  samplerate=sample_rate,      # taxa de amostras
  channels=1,                  # 1 significa gravação mono
  dtype="int16")               # tipo de dados para as amostras registradas
sd.wait()  # aguardando o término da gravação

wav.write("output.wav", sample_rate, recording)
print("Gravação concluída, estou reconhecendo...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio, language="en")
    
    translator = Translator()
    translated = asyncio.run(
    translator.translate(text, src="en", dest="pt")) # O 'en' aqui é um código para inglês
    
except sr.UnknownValueError:             # - se o Google não conseguiu entender a fala devido a ruídos ou silêncio
    print("A fala não pôde ser reconhecida.")
except sr.RequestError as e:             # - se não houver conexão com a Internet ou a API estiver indisponível
    print(f"Service error: {e}")

if translated.text.lower() == palavra_escolhida:


    print("boa quase flunte")
    print(''' 888888888888888888888888888888888
    88888___88888888888888888___88888
    8888_____888888888888888_____8888
    8888_____888888888888888_____8888
    8888_____888888888888888_____8888
    8888_____888888888888888_____8888
    8888_____888888888888888_____8888
    8888_____888888888888888_____8888
    8888_____88____888____88_____8888
    8888_____8______8______8_____8888
    8888_____8______8______8_____8888
    8888_____8______8______8_____8888
    8888_____8______8______8_____8888
    8888_____8____8888888888888888888
    8888_____8___88_____________88888
    8888_____8__88_______________8888
    8888______888_________________888
    8888________88_________________88
    8888__________88_______________88
    8888____________88_____________88
    8888_____________88___________888
    8888______________8___________888
    8888_______________8__________888
    8888_______________8_________8888
    88888_______________________88888
    888888_____________________888888
    888888888888888888888888888888888
    ''')

else:
    print("a pratica leva a perfeição")
    print('''______________________¶¶¶
___________________¶¶¶¶¶
__________________¶¶¶¶¶¶
________________¶¶¶¶¶¶¶
_______________¶¶¶¶¶¶¶¶
_______________¶¶¶¶¶¶¶¶
______________¶¶¶¶¶¶¶¶¶¶
______________¶¶¶¶¶¶¶¶¶¶
______________¶¶¶¶¶¶¶¶¶¶¶______________¶¶¶
______________¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶¶
_______¶______¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶¶¶
_______¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶
_______¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
_______¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶
_______¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_______¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶______¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________¶____¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶¶¶¶
____¶¶¶¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶_____________________¶¶¶¶¶¶
_________¶¶¶¶¶¶___________________¶¶¶¶
_____________¶¶¶¶¶______________¶
''')

print(translated.text)







