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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

boton = driver.find_element(By.XPATH, '//*[@id="submit"]')
print (boton.is_enabled())

if( boton.is_enabled() == True ):
    print( "Puedes dar click" )
    boton.click()
else:
    print( "No puedes dar click" )

time.sleep(tiempo)
driver.close()