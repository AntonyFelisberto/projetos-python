import requests
import json

token = "YOUR_TOKEN"
url = f"https://graph.facebook.com/v13.0/105360698771730?fields=link%2Cimages&access_token={token}"

response = requests.get(url)
print(response.text)

data_dict = json.loads(response.text)
print(data_dict)

image_bytes = requests.get(data_dict["images"][0]["source"]).content

with open("image.jpg","wb") as file:
    file.write(image_bytes)