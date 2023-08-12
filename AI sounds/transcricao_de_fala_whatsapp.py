#pip install pydub
import speech_recognition as sr
from pydub import AudioSegment
import librosa
import soundfile as sf
from IPython.display import Audio, Javascript
from io import BytesIO
from base64 import b64decode
import numpy as np
import sys
import os

oggs = []
path = os.path.dirname("mini_speech_recognition")
abspath = os.path.abspath(path)
dirs = os.listdir(abspath)

for file in dirs:
    if file.endswith("ogg"):
        oggs.append(file)
print(oggs)

def ogg_to_wav(name):
    song = AudioSegment.from_ogg(abspath+"/"+name)
    export_name = os.path.splitext(name)[0]
    print(song)
    print(export_name)
    new_audio = song.export(export_name+".wav",format="wav")
    return new_audio

r = sr.Recognizer()
for ogg in oggs():
    new_audio = ogg_to_wav(ogg)
    audio = sr.AudioFile(new_audio)
    with audio as source:
        texto = r.record(source)
    print(r.recognize_google(texto,language="pt-BR"))