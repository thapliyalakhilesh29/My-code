import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_object = Service()
driver= webdriver.Chrome(service=service_object) 
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Akhilesh Thapliyal")
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("akhilesh+test@logic-square.com")
driver.find_element(By.XPATH,'//*[@id="exampleInputPassword1"]').send_keys("Qwerty@123")
driver.find_element(By.XPATH,'//*[@id="exampleCheck1"]').click()
dropdown = Select(driver.find_element(By.XPATH, '//*[@id="exampleFormControlSelect1"]'))
dropdown.select_by_index(0)

print("Script is running. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(10)  # Keep the script alive by sleeping or waiting for user input
except KeyboardInterrupt:
    print("Script interrupted. Exiting gracefully.")