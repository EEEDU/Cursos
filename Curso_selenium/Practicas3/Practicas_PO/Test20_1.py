import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

from Funciones.Funciones import Funciones_globales

tiempo = 1

class Funciones01(unittest.TestCase):
    def setUp(self):
        self.tiempo = 2
        service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_saludos(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.saludo()
        funciones.despedida()

    def test_tiempo(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar("https://www.saucedemo.com/", tiempo)

    def test_xpath(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar("https://www.saucedemo.com/", tiempo)
        funciones.texto_Xpath_Valida('//*[@id="user-name"]', "asdf", tiempo)
        funciones.texto_Xpath_Valida('//*[@id="password"]', "asdf", tiempo)

    def test_id(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar("https://www.saucedemo.com/", tiempo)
        funciones.texto_Id("user-name", "asdf", tiempo)
        funciones.texto_Id("password", "asdf", tiempo)

    def test_click_xpath(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar("https://www.saucedemo.com/", tiempo)
        funciones.texto_Xpath_Valida('//*[@id="user-name"]', "standard_user", tiempo)
        funciones.texto_Xpath_Valida('//*[@id="password"]', "secret_sauce", tiempo)
        funciones.click_Xpath_Valida('//*[@id="login-button"]', tiempo)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
