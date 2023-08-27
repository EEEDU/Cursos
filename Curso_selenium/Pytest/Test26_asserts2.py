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

@pytest.fixture(scope='module')
def setup_login():
    global driver, funciones
    service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    funciones = Funciones_globales(driver)
    funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input', "Admin", tiempo)
    funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input', "admin123", tiempo)
    funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button', tiempo)

    print("Entrando al sistema 2")

def teardown():
    print("Fin de los test")
    driver.close()

@pytest.mark.usefixtures("setup_login")
def test_uno():
    etiqueta = funciones.SEX('//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')

    assert etiqueta.text == "Dashboard"

    if (etiqueta.text == "Dashboard"):
        assert True