import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tiempo = 1

service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)

nombre = driver.find_element(by=By.XPATH, value="//*[@id='userNam']")
nombre.send_keys("Eduardo")

driver.find_element(by=By.XPATH, value="//*[@id='userEmail']").send_keys("Eduardo@gmail.com")

time.sleep(tiempo)

driver.execute_script("window.scrollTo(0, 300);")
time.sleep(tiempo)

driver.find_element(by=By.XPATH, value='//*[@id="submit"]').click()

driver.close()