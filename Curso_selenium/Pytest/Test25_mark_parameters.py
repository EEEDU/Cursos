import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

from Funciones import Funciones_globales
from Page_login import Funciones_login

tiempo = .5

def get_data():
    return[
        ("rodrigo", "1234"),
        ("eduardo", "1234"),
        ("asdf", "asdf1234"),
        ("Admin", "admin123")
    ]

@pytest.mark.login
@pytest.mark.parametrize("user, password", get_data())
def test_login(user, password):
    global driver, funciones
    service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    funciones = Funciones_globales(driver)
    funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input',
                          user, tiempo)
    funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input',
                          password, tiempo)
    funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button', tiempo)

    print("Entrando al sistema 2")

