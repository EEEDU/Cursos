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
from Funciones.Page_login import Pagina_login

tiempo = .5

class Funciones02(unittest.TestCase):
    def setUp(self):
        self.tiempo = 2
        service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_upload(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar("https://the-internet.herokuapp.com/upload", tiempo)
        funciones.upload_Xpath('//*[@id="file-upload"]', "C://Users//eguerrero//PycharmProjects//Curso_selenium//Imagenes//seta.png", tiempo)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
