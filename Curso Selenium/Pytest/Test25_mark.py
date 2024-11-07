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

@pytest.mark.uno
def test_uno():
    print("Test uno")

@pytest.mark.dos
def test_dos():
    print("Test dos")

@pytest.mark.tres
def test_tres():
    print("Test tres")

@pytest.mark.cuatro
def test_cuatro():
    print("Test cuatro")

@pytest.mark.cinco
def test_cinco():
    print("Test cinco")

@pytest.mark.seis
def test_seis():
    print("Test seis")