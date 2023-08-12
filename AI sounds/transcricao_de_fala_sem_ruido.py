#pip install SpeechRecognition
#pip install PyAudio
import speech_recognition as sr
import librosa
import soundfile as sf
from IPython.display import Audio, Javascript
from io import BytesIO
from base64 import b64decode
import numpy as np

print("versão speech_recognition: ", sr.__version__)

r = sr.Recognizer()

audio_source = "arquivo.wav"
data,sample_rate = librosa.load(audio_source,sr=None)
Audio(data,rate=sample_rate)
audio = sr.AudioFile(audio_source)
with audio as source:
    r.adjust_for_ambient_noise(source,duration=0.7)
    texto = r.record(source,duration=10)
    
print(r.recognize_google(texto,language="pt-BR",show_all=True))