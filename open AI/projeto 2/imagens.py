#pip install openai
import openai

openai.api_key=""

search = input("say what you want in english: ")
resultado = openai.Image.create(
    prompt = search,
    n = 2,
    size = "1024x1024"
)
print(resultado)