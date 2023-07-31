import requests

url = "https://filexamples.com/download/aac-sample-file-download"
req = requests.get(url)
content = req.content

with open('download.mp3','wb') as file:
    file.write(content)