import numpy as np
import time
from datetime import datetime
import math
import matplotlib.pyplot as plt 
from IPython.display import Audio,HTML
import librosa 
import librosa.display as ld
import seaborn as sn

filename = librosa.util.example("trumpet")
y,sr = librosa.load(filename)
y_harmonic,y_percursive = librosa.effects.hpss(y)

print("canais: ",y.shape[0])
print("numero de amostras: ",len(y))
print("taxa de amostragem: ",sr)
print("duração do audio: ",librosa.get_duration(y=y))
print("som harmonico")
Audio(data=y_harmonic, rate=sr)
print("som percursivo")
Audio(data=y_percursive, rate=sr)

onset_env = librosa.onset.onset_strength(y=y,sr=sr,max_size=5)

print(onset_env.shape,type(onset_env))
times = librosa.times_like(onset_env,sr = sr)
print(times.shape,type(times))

onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env,sr=sr)
print(onset_env)

plt.plot(times,onset_env,label="onset strenght")
plt.vlines(times[onset_frames],0,onset_env.max(),colors="r",linestyles="--",label="Onsets")
plt.legend()
plt.show()

onset_times = librosa.onset.onset_detect(onset_envelope=onset_env,sr=sr,units="time")
y_clicks = librosa.clicks(times = onset_times,length=len(y),sr=sr)
Audio(data=y+y_clicks,rate=sr)