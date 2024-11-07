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

driver.get("https://pixabay.com/es/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

# driver.execute_script("window.scrollTo(0, 2000)")

try:
    buscarMas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[2]/div[2]/a')))
    ir = driver.execute_script("arguments[0].scrollIntoView();", buscarMas)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no se encuentra")

time.sleep(tiempo)
driver.close()