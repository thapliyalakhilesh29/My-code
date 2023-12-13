import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
Service_object= Service()
driver= webdriver.Chrome(service=Service_object) 
#driver= webdriver.Firefox(service=Service_object)

driver.maximize_window()
driver.get("https://closewise-nna.surge.sh")
print(driver.title)
print(driver.current_url)
driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/form/div[1]/input').send_keys("closewisedemo4@gmail.com")
driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div/form/div[2]/div/input').send_keys("poiuyt@123")
driver.find_element(By.XPATH,'//*[@id="root"]/div[3]/div/div[2]/div/form/button').click()
print("Script is running. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(10)  # Keep the script alive by sleeping or waiting for user input
except KeyboardInterrupt:
    print("Script interrupted. Exiting gracefully.")









