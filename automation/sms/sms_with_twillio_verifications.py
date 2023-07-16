from methods.browser import get_driver,get_elements
from twillio.rest import Client
import time


def verify_browser():
    driver = get_driver("https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/",1)
    element = get_elements(driver,"/html/body/div[1]/div[2]/div[9]/div[5]/div[4]/div[12]/div[3]/div[1]/span[1]/span[1]")
    return element.text

def send_sms():
    account_sid = os.environ("TWILLIO_SID")
    account_token = os.environ("TWILLIO__ACCOUNT_TOKEN")
    client = Client(account_sid,account_token)
    message = client.messages.create(body=input("DIGITE MENSAGEM"),from="NUMBER_IN_TWILLIO",to=input("NUMERO QUE RECEBERA MENSAGEM"))
    print(message.sid)

def clean_price(price):
    return float(price.replace("BRL",""))

initial_value = verify_browser()
price_initial = clean_price(initial_value)
prices = [price_initial] 

while True:
    time.sleep(5)
    value = verify_browser()
    price_initial = clean_price(value)
    prices.append(price_initial)
    if prices[-1] < prices[-2]: # prices[-1] == last value in list prices[-2] == value before price[-1]
        send_sms()
    del prices[-2]