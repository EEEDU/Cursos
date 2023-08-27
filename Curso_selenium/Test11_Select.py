import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

tiempo = 1

service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(tiempo)

dropdown = driver.find_element(by=By.XPATH, value='//*[@id="dropdown"]')
selector = Select(dropdown)

selector.select_by_visible_text("Option 1")
time.sleep(tiempo)

selector.select_by_index(2)
time.sleep(tiempo)

selector.select_by_value("1")
time.sleep(tiempo)

driver.close()