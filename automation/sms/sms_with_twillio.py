import os
from twillio.rest import Client


account_sid = os.environ("TWILLIO_SID")
account_token = os.environ("TWILLIO__ACCOUNT_TOKEN")
client = Client(account_sid,account_token)

message = client.messages.create(body=input("DIGITE MENSAGEM"),from="NUMBER_IN_TWILLIO",to=input("NUMERO QUE RECEBERA MENSAGEM"))

print(message.sid)
 
