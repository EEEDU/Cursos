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

@pytest.mark.run
def test_validar_igual():
    print("Primer test")
    assert True

@pytest.mark.run
def test_dos():
    a = 10
    b = 10
    assert a == b, "No son iguales"

@pytest.mark.run
def test_tres():
    a = 5
    b = 10
    assert a <= b, "A es mayor que B"

@pytest.mark.run
def test_cuatro():
    a = 15
    b = 10
    assert a >= b, "A es menor que B"

@pytest.mark.run
def test_cinco():
    nombre = "Eduardo"
    assert nombre == "Eduardo", "El nombre no es Eduardo"