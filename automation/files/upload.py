import requests

url = "https://cgi-lib.berkeley.edu/ex/fup.cgi"
file = open("myfile.txt","rb")
req = requests.post(url,files={"upfile":file}) #upfile é o name que esta no campo da tag name do item que vai postar o comentario

print(req.text)