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

@pytest.mark.igual
def test_validar_igual():
    nom1 = "Eduardo"
    nom2 = "Eduardo"

    assert nom1 == nom2, "Los nombres no son iguales"

@pytest.mark.cantidad
def test_validar_cantidad():
    cant1 = 1243
    cant2 = 321

    assert cant1 > cant2, "cant1 es menor que cant2"

@pytest.mark.dentro
def test_validar_dentro():
    frase = "Hola que tal estas"
    palabra = "que"

    assert palabra in frase, "La palbra no esta en la frase"

@pytest.mark.dobleValidacion
def test_validar_dobleValidacion():
    cant1 = 1243
    cant2 = 321

    if (cant1 >= cant2):
        assert True
    else:
        assert False