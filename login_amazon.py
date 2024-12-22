import time
from selenium.webdriver.common.by import By

def login_amazon(driver, username, password):
    driver.get("https://www.amazon.in/ap/signin")
    time.sleep(2)
    email_field = driver.find_element(By.ID, "ap_email")
    email_field.send_keys(username)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)
    password_field = driver.find_element(By.ID, "ap_password")
    password_field.send_keys(password)
    driver.find_element(By.ID, "signInSubmit").click()
    time.sleep(5)