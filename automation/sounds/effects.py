from pydub import AudioSegment

beat = AudioSegment.from_wav("beat.wav")

beat_low = beat.low_pass_filter(2000)
beat_low.export("beat_2.wav",format="wav")

beat_left = beat_low.pan(-1)
beat_left.export("beat_left.wav",format="wav")

beat_right = beat_low.pan(1)

beat_final = beat_left + beat_right + beat_low
beat_final.export("beat_final.wav",format="wav")