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

driver.get("https://demoqa.com/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

titulo = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/header/a/img')))
print(titulo.is_displayed())

boton = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div')

if( titulo.is_displayed() == True ):
    print( "Existe la imagen" )
    boton.click()
else:
    print( "No existe" )

time.sleep(tiempo)
driver.close()