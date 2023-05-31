#pip install openai
import openai

openai.api_key=""

search = input("say what you want in english: ")

audio_file = open("audio.mp3","rb")

result = openai.Audio.transcribe("whisper-1",audio_file)
print(result)
result = openai.Audio.translate("whisper-1",audio_file)
print(result)