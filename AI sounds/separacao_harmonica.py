import numpy as np
import time
from datetime import datetime
import math
import matplotlib as plt
from IPython.display import Audio,HTML
import librosa 
import librosa.display as ld
import seaborn as sn

plt.rcParams['figure.figsize'] = (14,6)
sn.set()

filename = librosa.util.example("brahms")
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