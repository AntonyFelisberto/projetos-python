from methods import browser,format
from datetime import datetime as dt
from selenium.webdriver.common.by import By
import time

def write_file(text):
    """Write input text into a file"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(str(text))

def main():
    driver = browser.get_driver("https://automated.pythonanywhere.com/",1)
    while True:
        time.sleep(2)
        element = browser.get_elements(driver,"/html/body/div[1]/div/h1[1]")
        element = browser.get_elements(driver,"/html/body/div[1]/div/h1[2]")
        text = format.clean_text(element.text)
        write_file(text)

main()