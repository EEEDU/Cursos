import unittest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

from Funciones import Funciones_globales

class Funciones_login():

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, clave, message, error, tiempo = 2):
        global driver
        service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()

        funciones = Funciones_globales(driver)
        funciones.navegar('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F', 2)
        funciones.texto_mixto("id", "Email", email)
        funciones.texto_mixto("id", "Password", clave)
        funciones.click_mixto("xpath", "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", tiempo)

        error1 = funciones.SEX(error)
        error1 = error1.text
        if (message in error1):
            print("Prueba de validacion exitosa")
        else:
            print("Prueba de validacion incorrecta")

        driver.close()
