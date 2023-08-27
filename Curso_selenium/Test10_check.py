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

driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(tiempo)

check1 = driver.find_element(by=By.XPATH, value='//*[@id="checkboxes"]/input[1]')
check1.click()

time.sleep(tiempo)

check2 = driver.find_element(by=By.XPATH, value='//*[@id="checkboxes"]/input[2]')
check2.click()

time.sleep(tiempo)

driver.close()