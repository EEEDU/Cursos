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
time.sleep(tiempo)

driver.get("https://git.teltronic.es/users/sign_in")
time.sleep(tiempo)

driver.execute_script("window.history.go(-1)")
time.sleep(tiempo)

driver.execute_script("window.history.go(1)")
time.sleep(tiempo)

driver.close()