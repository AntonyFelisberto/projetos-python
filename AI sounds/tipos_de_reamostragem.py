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

start = time.time()
data,sample_rate = librosa.load(filename,duration=60,res_type="kaiser_best")
best = time.time() - start

start = time.time()
data,sample_rate = librosa.load(filename,duration=60,res_type="kaiser_fast")
fast = time.time() - start

start = time.time()
data,sample_rate = librosa.load(filename,duration=60,res_type="scipy")
scipy = time.time() - start

start = time.time()
data,sample_rate = librosa.load(filename,duration=60,res_type="polyphase")
poly = time.time() - start

print("tempo de carregamento por tipo de reamostragem")
print("kaise best: ",best)
print("kaise fast: ",fast)
print("scipy: ",scipy)
print("polyphase: ",poly)