from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_object = Service()
driver = webdriver.Chrome(service=service_object)
driver.get("https://rahulshettyacademy.com/dropdownsPractise")

# Select option from Dynamic dropdown (Auto suggestive dropdown)
driver.find_element(By.XPATH, '//*[@id="autosuggest"]').send_keys("in")
time.sleep(2) # interpreter will wait for 2 seconds
countries = driver.find_elements(By.CLASS_NAME, "ui-menu-item")
print(len(countries))
for country in countries:
    if country.text=="India":
        country.click()
        break

option = driver.find_element(By.ID,'autosuggest').get_attribute("value")
assert option == "India1"



time.sleep(3)

