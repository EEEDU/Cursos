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
from Funciones.Funciones import Funciones_globales


class Pagina_login():

    def __init__(self, driver):
        self.driver = driver

    def Login_master(self, url, username, password,  tiempo):
        driver = self.driver
        funciones = Funciones_globales(driver)
        funciones.navegar(url, tiempo)
        funciones.texto_Xpath_Valida('//*[@id="user-name"]', username, tiempo)
        funciones.texto_Xpath_Valida('//*[@id="password"]', password, tiempo)
        funciones.click_Xpath_Valida('//*[@id="login-button"]', tiempo)