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
stereo_data,sample_rate = librosa.load(filename,mono=False,duration=60)

print("vetor: ",stereo_data)
print("canais: ",stereo_data.shape[0])
print("numero de amostras: ",stereo_data.shape[0])
print("taxa de amostragem: ",sample_rate)
print("duração do audio: ",len(stereo_data)/sample_rate)
print("duração do audio: ",librosa.get_duration(y=stereo_data))
Audio(data=stereo_data,rate=sample_rate)