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

class Funciones_globales():

    def __init__(self, driver):
        self.driver = driver

    def saludo(self):
        print("Hola")

    def despedida(self):
        print("Adios")

    def tiempo(self, t):
        tiempo = time.sleep(t)
        return tiempo

    def navegar(self, url, t):
        self.driver.get(url)
        print("Pagina abierta: " + str(url))
        self.tiempo(5)

    def texto_Xpath(self, xpath, texto, t):
        valor = self.driver.find_element(By.XPATH, xpath)
        valor.clear()
        valor.send_keys(texto)
        self.tiempo(t)

    def texto_Xpath_Valida(self, xpath, texto, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.clear()
            valor.send_keys(texto)
            print("Escribiendo en el campo {} el texto {}".format(xpath, texto))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def texto_Id(self, id, texto, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, id)
            valor.clear()
            valor.send_keys(texto)
            print("Escribiendo en el campo {} el texto {}".format(id, texto))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def click_Xpath_Valida(self, xpath, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.click()
            print("Damos click en el campo {}".format(xpath))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def click_Id(self, id, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, id)
            valor.click()
            print("Damos click en el campo {}".format(id))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def select_Xpath_Text(self, xpath, texto, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor = Select(valor)
            valor.select_by_visible_text(texto)
            print("El campo Seleccionado es {}".format(texto))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def select_Xpath_Type(self, xpath, tipo, dato, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor = Select(valor)
            if (tipo == "texto"): valor.select_by_visible_text(dato)
            elif (tipo == "index"): valor.select_by_index(dato)
            elif (tipo == "value"): valor.select_by_value(dato)
            print("El campo Seleccionado es {}".format(tipo))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def upload_Xpath(self, xpath, ruta, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)
            
    def check_Xpath(self, xpath, t):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.click()
            print("Click en el elemento {}".format(xpath))
            self.tiempo(t)
        except TimeoutException as ex:
            print(ex.msg)

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def texto_mixto(self, tipo, selector, texto, tiempo=.1):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento " + selector)
                return t

    def click_mixto(self, tipo, selector, t):
        if (tipo == "xpath"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.XPATH, selector)
                valor.click()
                print("Click en el campo {}".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

        if (tipo == "id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.ID, selector)
                valor.click()
                print("Click en el campo {}".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

    def Mouse_Double(self, tipo, selector, t=.2):
        if (tipo == "xpath"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.XPATH, selector)
                act = ActionChains(self.driver)
                act.double_click(valor).perform()
                print("DoubleClick en {} ".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

        if (tipo == "id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.double_click(valor).perform()
                print("DoubleClick en {} ".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

    def mouse_derecho(self, tipo, selector, t=.2):
        if (tipo == "xpath"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.XPATH, selector)
                act = ActionChains(self.driver)
                act.context_click(valor).perform()
                print("DoubleClick en {} ".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

        if (tipo == "id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.context_click(valor).perform()
                print("Se solto el elemento {} ".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

    def mouse_drag(self, tipo, selector, t=.2):
        if (tipo == "xpath"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.XPATH, selector)
                act = ActionChains(self.driver)
                act.drag_and_drop(valor).perform()
                print("DoubleClick en {} ".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)

        if (tipo == "id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.drag_and_drop(valor).perform()
                print("Se solto el elemento {} ".format(selector))
                self.tiempo(t)
            except TimeoutException as ex:
                print(ex.msg)