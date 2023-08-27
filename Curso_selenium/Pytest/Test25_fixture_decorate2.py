import allure
import pytest
import time

from allure_commons.types import AttachmentType
# from allure_common.types import AttachmentType
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

# Para imagenes de error
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, funciones
    service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

    funciones = Funciones_globales(driver)
    funciones.texto_mixto("id", "Email", "admin@yourstore.com", tiempo)
    funciones.texto_mixto("id", "Password", "admin", tiempo)
    funciones.click_mixto("xpath", "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button", tiempo)

    print("Entrando al sistema 1")
    yield
    print("Salida login 1")
    driver.close()

@pytest.fixture(scope='module')
def setup_login_dos():
    global driver, funciones
    service = Service(executable_path='C:\Cursos\Drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    funciones = Funciones_globales(driver)
    funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input', "Admin", tiempo)
    funciones.texto_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input', "admin123", tiempo)
    funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button', tiempo)

    print("Entrando al sistema 2")
    yield
    print("Salida login 2")
    driver.close()

@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema uno")

    allure.attach(driver.get_screenshot_as_png(), name="customer", attachment_type=AttachmentType.PNG)

    funciones.click_mixto("xpath", '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a', tiempo)
    funciones.click_mixto("xpath", '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a', tiempo)
    funciones.click_mixto("xpath", '/html/body/div[3]/div[1]/form[1]/div/div/a', tiempo)

    funciones.texto_mixto("xpath", '//*[@id="Email"]', "asdf@gmail.com", tiempo)
    funciones.texto_mixto("xpath", '//*[@id="FirstName"]', "asdf", tiempo)

    allure.attach(driver.get_screenshot_as_png(), name="datos", attachment_type=AttachmentType.PNG)

    funciones.click_mixto("xpath", '/html/body/div[3]/div[1]/form/div[1]/div/button[1]', tiempo)

    assert 1==2

    driver.close()

@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema dos")

    # funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a', tiempo)
    # funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span', tiempo)
    # funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li', tiempo)

    # funciones.texto_mixto("xpath", '//*[@id="app"]/d iv[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input', "Anthony.Nolan", tiempo)
    # funciones.click_mixto("xpath", '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]', tiempo)

    driver.close()
