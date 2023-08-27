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

from ..Funciones.Funciones import Funciones_globales
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
        funciones.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", tiempo)

        funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input', "Admin", tiempo)
        funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input', "admin123", tiempo)
        funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button', tiempo)

        admin = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        sub1 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
        sub2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a')

        act = ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
