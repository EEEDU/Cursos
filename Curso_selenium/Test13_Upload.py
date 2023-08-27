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

driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

try:
    buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="file-upload"]')))
    buscar.send_keys("C://Users//eguerrero//PycharmProjects//Curso_selenium//Imagenes//seta.png")

    driver.find_element(by=By.XPATH, value='//*[@id="file-submit"]').click()
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no se encuentra")

time.sleep(tiempo)
driver.close()