import glob
import os
import pathlib
import random
from datetime import datetime
import librosa
import librosa.display as ld
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
import tensorflow as tf
from keras import layers
from keras import models
import seaborn as sns
from tqdm import tqdm

sns.set()

commands = []
print(glob.glob(str("mini_speech_commands")+"/*"+os.path.sep))
for name in glob.glob(str("mini_speech_commands")+"/*"+os.path.sep):
    print(name.split("\\")[-2])
    commands.append(name.split("\\")[-2])

commands_dict = {i: commands.index(i) for i in commands}
print(commands_dict)

speech_data_list = []
for name in tqdm(glob.glob(str("mini_speech_commands")+"/*/*")):
    speech_data_list.append(name)

random.seed(42)
random.shuffle(speech_data_list)

speech_data_labels = []
for audio in tqdm(speech_data_list):
    speech_data_labels.append(os.path.dirname(audio).split("\\")[-1])

print(speech_data_labels)
print(len(speech_data_labels))
print(speech_data_labels.count("yes"))

speech_label_int = []
for audio in tqdm(speech_data_labels):
    speech_label_int.append(commands_dict[audio])

print(speech_label_int)

loaded_speech_data = []
for audio in tqdm(speech_data_list):
    loaded_speech_data.append(librosa.load(audio,sr=16000))

print(loaded_speech_data)

df = pd.DataFrame([speech_data_labels,loaded_speech_data,speech_data_list]).T
print(df)

df.columns = ["command","waves","paths"]
print(df)