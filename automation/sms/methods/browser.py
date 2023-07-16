from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver(url,type):
    if type == 1:
        options = webdriver.EdgeOptions()
    else:
        options = webdriver.ChromeOptions()
    options.use_chromium = True
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    if type == 1:
        driver = webdriver.Edge(options=options)
    else:
        driver = webdriver.Chrome(options=options)

    driver.get(url)
    return driver

def add_elements_by_id(driver,xpath,key):
    return driver.find_element(By.ID, xpath).send_keys(key)

def get_elements(driver,xpath):
    return driver.find_element(By.XPATH, xpath)

def get_elements_by_class(driver,xpath):
    return driver.find_element(By.CLASS_NAME, xpath)

def find_and_click(driver,xpath):
    return driver.find_element(By.XPATH, xpath).click()


