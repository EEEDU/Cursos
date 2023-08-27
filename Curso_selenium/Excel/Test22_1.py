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

from Excel.Funciones_excel import Funciones_excel
from Funciones.Funciones import Funciones_globales

tiempo = .5

class Test_excel(unittest.TestCase):
    def setUp(self):
        self.tiempo = 2
        service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_excel(self):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones_excel = Funciones_excel()
        funciones.navegar("https://the-internet.herokuapp.com/login", tiempo)
        path = "C://Users//eguerrero/PycharmProjects//Curso_selenium//Excel//Datos.xlsx"
        filas = funciones_excel.getRowCount(path, "Hoja1")

        for fila in range(2, filas + 1):
            username = funciones_excel.readData(path, "Hoja1", fila, 1)
            password = funciones_excel.readData(path, "Hoja1", fila, 2)

            funciones.texto_mixto("xpath", '//*[@id="username"]', username, tiempo)
            funciones.texto_mixto("xpath", '//*[@id="password"]', password, tiempo)

            funciones.click_mixto("xpath", '//*[@id="login"]/button', tiempo)

            resultado = driver.find_element(By.XPATH, '//*[@id="flash"]').text
            funciones_excel.writeData(path, "Hoja1", fila, 3, resultado)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
