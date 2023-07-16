import os
from twillio.rest import Client
import time
from datetime import datetime as dt

account_sid = os.environ("TWILLIO_SID")
account_token = os.environ("TWILLIO__ACCOUNT_TOKEN")
client = Client(account_sid,account_token)

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 18:
        message = client.messages.create(body=input("DIGITE MENSAGEM"),from="NUMBER_IN_TWILLIO",to=input("NUMERO QUE RECEBERA MENSAGEM"))
        print(message.sid)
    time.sleep(60)
