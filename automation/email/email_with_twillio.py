from methods.browser import get_driver,get_elements
from twillio.rest import Client
import yagmail
import os
import time


def verify_browser():
    driver = get_driver("https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/",1)
    element = get_elements(driver,"/html/body/div[1]/div[2]/div[9]/div[5]/div[4]/div[12]/div[3]/div[1]/span[1]/span[1]")
    return element.text

def send_sms():
    sender = input("DIGITE EMAIL DE QUEM ENVIA ")
    receiver = input("DIGITE EMAIL DO RECEBEDOR ")
    subject = input("DIGITE MENSAGEM ")
    content = input("DIGITE CONTEUDO DO EMAIL ")
    yag = yagmail.SMTP(user=sender,password=os.getenv("PASSWORD"))
    yag.send(to=receiver,subject=subject,contents=content)

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