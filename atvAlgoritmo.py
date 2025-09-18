from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
 
    driver.get("https://the-internet.herokuapp.com/login")
    
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!" + Keys.RETURN)

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text.strip()
    with open("login.log", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

    print("Mensagem capturada e salva no log:", message)

finally:
    driver.quit()