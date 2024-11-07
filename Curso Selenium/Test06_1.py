import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

nombre = driver.find_element(by=By.CSS_SELECTOR, value="#userName")
nombre.send_keys("Eduardo")

driver.find_element(by=By.CSS_SELECTOR, value="#userEmail").send_keys("Eduardo@gmail.com")

time.sleep(2)

driver.execute_script("window.scrollTo(0, 300);")
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="submit"]').click()

driver.close()