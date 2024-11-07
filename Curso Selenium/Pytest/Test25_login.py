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

tiempo = 2

def test_login1():
    global driver
    service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    funcion_login = Funciones_login(driver)
    funcion_login.login("eduardo@gmail.com", 1234, "No customer account found", "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[1]")
    funcion_login.login("", 1234, "Please enter your email", '//*[@id="Email-error"]')
    funcion_login.login("asdf", 1234, "Wrong email", '//*[@id="Email-error"]')
    funcion_login.login("admin@yourstore.com", "admin", "Dashboard", '/html/body/div[3]/div[1]/div[1]/h1')

# def test_login2():
#     global driver
#     service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#
#     funcion_login = Funciones_login(driver)
#     funcion_login.login("", 1234, "Please enter your email", '//*[@id="Email-error"]')
#
# def test_login3():
#     global driver
#     service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#
#     funcion_login = Funciones_login(driver)
#     funcion_login.login("asdf", 1234, "Wrong email", '//*[@id="Email-error"]')
#
# def test_login4():
#     global driver
#     service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#
#     funcion_login = Funciones_login(driver)
#     funcion_login.login("admin@yourstore.com", "admin", "Dashboard", '/html/body/div[3]/div[1]/div[1]/h1')