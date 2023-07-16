from methods import browser,format
from selenium.webdriver.common.by import By
import time

def main():
    #url = input("DIGITE URL: ")
    #xpath = input("DIGITE O XPATH: ")
    driver = browser.get_driver("https://automated.pythonanywhere.com/",1)
    time.sleep(2)
    element = browser.get_elements(driver,"/html/body/div[1]/div/h1[1]")
    element = browser.get_elements(driver,"/html/body/div[1]/div/h1[2]")
    return format.clean_text(element.text)

print(main())