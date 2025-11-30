from selenium import webdriver #Esto inicializa el navegador (Chrome, Firefox, etc.).
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # actívarlo si se quiere el modo oculto

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver
