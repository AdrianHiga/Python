from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import win32com.client as win32
import logging
import os

logging.basicConfig(level=logging.INFO, filename="log.txt",format="%(asctime)s -  %(message)s")

options = webdriver.ChromeOptions()

options.add_experimental_option("prefs", {
                                "download.default_directory": "C:\\Users\\adria\\OneDrive\\Área de Trabalho\\Bot_scania_speed\\Comprovantes"})


# options.add_argument("--headless")
navegador = webdriver.Chrome( options=options, executable_path="C:\\chromedriver\\chromedriver.exe")
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(options=options, service=servico)


# Passo 1: entrar no site
logging.info("Acessando site")
navegador.get("https://www.mercadolivre.com.br/")
time.sleep(2)

# Passo 2: Clicar em logar
navegador.find_element(By.ID, 'login').click
time.sleep(2)