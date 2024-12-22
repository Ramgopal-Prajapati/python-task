from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode if you don't want the browser UI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver