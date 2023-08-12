from pydub import AudioSegment

beat = AudioSegment.from_wav("beat.wav")
sax = AudioSegment.from_wav("sax.wav")

print(len(beat),len(sax))
beat_two = beat * 2 #double of the time of the sound
beat_two.export("beat2.wav",format="wav")

mixed = beat_two.overlay(sax) #mixing
mixed.export("mixed.wav",format="wav")

final = beat_two + mixed * 2 + sax + beat_two + sax
final.export("final.wav",format="wav")
