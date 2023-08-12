#pip install SpeechRecognition
#pip install PyAudio
import speech_recognition as sr
import librosa
import soundfile as sf
from IPython.display import Audio, Javascript
from io import BytesIO
from base64 import b64decode
import numpy as np

"""
Cada instância Recognizer tem sete métodos para reconhecer a fala de uma fonte de áudio usando várias APIs. Estes são:

    recognize_bing(): Microsoft Bing Speech
    recognize_google(): Google Web Speech API
    recognize_google_cloud(): Google Cloud Speech - requer a instalação do pacote google-cloud-speech
    recognize_houndify(): Houndify por SoundHound
    recognize_ibm(): IBM Speech to Text
    recognize_sphinx(): CMU Sphinx - requer a instalação do PocketSphinx
    recognize_wit(): Wit.ai
    Dos sete, só recognize_sphinx() funciona offline com o motor CMU Sphinx. Os outros seis exigem uma conexão com a internet.

o o SpeechRecognition é fornecido com uma chave de API padrão para a Google Web Speech API. As outras seis APIs exigem autenticação com uma chave de API ou uma combinação de nome de usuário/senha.
"""

print("versão speech_recognition: ", sr.__version__)

r = sr.Recognizer()

audio_source = "y2meta.net_320kbps-dark-souls-lore-historia-artorias-o-abysswalker.mp3"
data,sample_rate = librosa.load(audio_source,sr=None)
Audio(data,rate=sample_rate)

sf.write("arquivo.wav",data, sample_rate)
data,sample_rate = librosa.load(audio_source,sr=None)
Audio(data,rate=sample_rate)

audio_source = "arquivo.wav"
audio = sr.AudioFile(audio_source)
with audio as source:
    global texto
    texto = r.record(source,duration=40)

print(r.recognize_google(texto,language="pt-BR"))
print(r.recognize_google(texto,language="pt-BR",show_all=True))