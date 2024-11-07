import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


tiempo = 1

service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()

# https://selenium-python.readthedocs.io/waits.html
ad = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')))
ad.click()

time.sleep(tiempo)

driver.close()