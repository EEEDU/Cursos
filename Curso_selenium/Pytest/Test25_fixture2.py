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

def setup_function(fucntion):
    global driver, funciones
    service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

    funciones = Funciones_globales(driver)
    funciones.texto_mixto("id", "Email", "admin@yourstore.com", tiempo)
    funciones.texto_mixto("id", "Password", "admin", tiempo)
    funciones.click_mixto("xpath", "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", tiempo)

    print("Iniciando nuestro test")

def teardown_function(function):
    print("Fin de los test")
    driver.close()

def test_uno():
    funciones.click_mixto("xpath", "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a", tiempo)
    funciones.click_mixto("xpath", "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a", tiempo)
    funciones.texto_mixto("id", "SearchProductName", "Computer", tiempo)
    funciones.click_mixto("id", "search-products", tiempo)

def test_dos():
    funciones.click_mixto("xpath", "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a", tiempo)
    funciones.click_mixto("xpath", "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a", 2)
    funciones.click_mixto("xpath", "/html/body/div[3]/div[1]/form[1]/div/div/a", 3)
    funciones.texto_mixto("xpath", '//*[@id="Name"]', "Laptop dell", tiempo)
    driver.switch_to.frame(0)
    funciones.texto_mixto("xpath", '//*[@id="tinymce"]', "Descripcion larga", tiempo)


