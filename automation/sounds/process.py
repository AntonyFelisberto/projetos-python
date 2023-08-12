from pydub import AudioSegment

original = AudioSegment.from_wav("beat.wav")
print(type(original))
print(original)

reversed = original.reverse()
reversed.export("reversed.wav",format="wav")
reversed = reversed + 15 #increase volume

print(dir(original))

first_two = original[0:2000]
first_two.export("first_two.wav",format="wav")

print(len(original))

merged = original + reversed
merged.export("merged.wav",format="wav")

merged = original * 2 + AudioSegment.silent(1000) + reversed
merged.export("merged_1.wav",format="wav")