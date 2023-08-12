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
data,sample_rate = librosa.load(filename,duration=60,sr=8000)

print("taxa amostragem: ",sample_rate)
print("amostras: ",data)
print("quantidade amostras: ",len(data))

