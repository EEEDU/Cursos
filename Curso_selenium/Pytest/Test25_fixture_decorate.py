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
def setup_login_uno():
    print ("Empezando el login del sistema")
    yield
    print ("Saliendo del sistema prueba ok")

@pytest.fixture(scope='module')
def setup_login_dos():
    print ("Empezando las pruebas del sistema dos")
    yield
    print ("Saliendo de las pruebas del sistema dos")

def test_uno(setup_login_uno):
    print ("************** Empezando las pruebas del test 1 **************")

def test_dos(setup_login_dos):
    print ("************** Empezando las pruebas del test 2 **************")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("Prueba tres del modulo dos")
