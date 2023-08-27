import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

tiempo = 1

service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

driver.find_element(By.XPATH, '//*[@id="login"]/button').click()

def login(username, password):
    time.sleep(tiempo)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(tiempo)
    driver.find_element(By.XPATH, '//*[@id="login"]/button').click()



if driver.find_element(By.XPATH, '//*[@id="flash"]').text == "Your username is invalid!\n×":
    print("El usuario es invalido")
    login("tomsmith", "")
else:
    print("Usuario correcto")

if driver.find_element(By.XPATH, '//*[@id="flash"]').text == "Your password is invalid!\n×":
    print("La contraseña es invalida")
    login("tomsmith", "SuperSecretPassword!")
else:
    print("Contraseña correcta")

if driver.find_element(By.XPATH, '//*[@id="flash"]').text == "You logged into a secure area!\n×":
    print("OK")
else:
    print("ERROR")

time.sleep(tiempo)
driver.close()