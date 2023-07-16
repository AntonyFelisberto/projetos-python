from selenium.webdriver.common.keys import Keys
from methods import browser,format
import time

def main():
    #url = input("DIGITE URL: ")
    #xpath = input("DIGITE O XPATH: ")
    driver = browser.get_driver("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6",1)
    time.sleep(2)
    print(driver.current_url)
    element = browser.get_elements(driver,'/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]')
    return float(element.text.replace("%",""))

if main() < -0.12:
    print("enviar e-mail")
else:
    print("valor acima")