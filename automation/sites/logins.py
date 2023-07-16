from selenium.webdriver.common.keys import Keys
from methods import browser,format
import time

def main():
    #url = input("DIGITE URL: ")
    #xpath = input("DIGITE O XPATH: ")
    driver = browser.get_driver("https://automated.pythonanywhere.com/login/",1)
    browser.add_elements_by_id(driver,"id_username","automated")
    time.sleep(2)
    browser.add_elements_by_id(driver,"id_password","automatedautomated" + Keys.RETURN)
    time.sleep(2)
    print(driver.current_url)
    browser.find_and_click(driver,"/html/body/nav/div/a")
    return format.clean_text(browser.get_elements(driver,"/html/body/div[1]/div/h1[2]").text)

print(main())