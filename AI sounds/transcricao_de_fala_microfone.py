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
print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.1)
    audio = r.listen(source)
    try:
        print(r.recognize_google(audio,language="pt-BR",show_all=True))
    except sr.UnknownValueError:
        print("não foi possível fazer a transcrição!")


