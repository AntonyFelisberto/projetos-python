from selenium.webdriver.common.keys import Keys
from methods import browser,format
import time

def main():
    #url = input("DIGITE URL: ")
    #xpath = input("DIGITE O XPATH: ")
    driver = browser.get_driver("https://titan22.com/account/login?return_url=%2Faccount",1)
    browser.add_elements_by_id(driver,"CustomerEmail","app7flask@gmail.com")
    time.sleep(2)
    browser.add_elements_by_id(driver,"CustomerPassword","??!65EhGMg8.WwY" + Keys.RETURN)
    time.sleep(2)
    print(driver.current_url)
    browser.find_and_click(driver,"/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a")
    return driver.current_url

print(main())