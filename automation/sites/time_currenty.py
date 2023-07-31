from bs4 import BeautifulSoup
import requests

def get_current(in_currency,out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,"html.parser")
    print(soup)
    currency = soup.find("span",class_="ccOutputRslt")
    print(currency)
    rate = soup.find("span",class_="ccOutputRslt").get_text()[:-4]
    return float(rate)



print(get_current("INR","USD"))