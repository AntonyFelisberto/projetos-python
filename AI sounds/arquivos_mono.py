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
mono_data,sample_rate = librosa.load(filename,duration=60)

print("vetor: ",mono_data)
print("canais: ",mono_data.shape)
print("numero de amostras: ",mono_data.shape[0])
print("taxa de amostragem: ",sample_rate)
print("duração do audio: ",len(mono_data)/sample_rate)
print("duração do audio: ",librosa.get_duration(y=mono_data))
Audio(data=mono_data,rate=sample_rate)