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

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

# Obtener links de la pagina
links = driver.find_elements(By.TAG_NAME, "a")
print ("El numero de links es ", len(links))

for link in links:
    print (link.text)

driver.find_element(By.LINK_TEXT, "Typos").click()

time.sleep(tiempo)
driver.close()