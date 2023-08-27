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

class Prueba_login(unittest.TestCase):
    def setUp(self):
        self.tiempo = 2
        service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_get(self):
        self.driver.get("https://www.saucedemo.com")
        time.sleep(self.tiempo)

    def test_username_error(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        nombre = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        boton = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        nombre.send_keys("dalkfjklasjdf")
        password.send_keys("asdlfjasdff")
        boton.click()
        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        print (error)
        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos")
            print("Prueba OK")

    def test_username_vacio(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        nombre = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        boton = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        boton.click()
        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        print (error)
        if error == "Epic sadface: Username is required":
            print("Los datos no son correctos")
            print("Prueba OK")

    def test_password_vacio(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        nombre = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        boton = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        nombre.send_keys("standard_user")
        boton.click()
        error = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        error = error.text
        print (error)
        if error == "Epic sadface: Password is required":
            print("Los datos no son correctos")
            print("Prueba OK")

    def test_correcto(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")
        nombre = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        boton = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        nombre.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton.click()

        logo = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div')
        if logo.is_displayed():
            print("Prueba OK")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()