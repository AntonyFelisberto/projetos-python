#pip install openai
import openai

openai.api_key=""

resultado = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages =[{"role":"user","content":input("say what you want in english: ")}]
)
print(resultado)