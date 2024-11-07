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
from selenium.webdriver import ActionChains

tiempo = 2
class base_test(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_mouse(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar("https://demoqa.com/buttons", tiempo)

        funciones.mouse_derecho("xpath", '//*[@id="rightClickBtn"]')


    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
