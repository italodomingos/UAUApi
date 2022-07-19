import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from pathlib import Path
import chromedriver_autoinstaller as chrome_update
from selenium.webdriver.chrome.options import Options

LOGIN = 'tin002-799'
PASSWORD = '123'


class TimeOutException(Exception):

    def __init__(self, message):
        super().__init__(message)


def inicialize_chrome():
    chrome_update.install()
    options = Options()
    options.add_argument("--safebrowsing-disable-download-protection")
    options.add_argument("safebrowsing-disable-extension-blacklist")
    options.add_experimental_option("prefs", {'safebrowsing.enabled': 'false'})
    return webdriver.Chrome(options=options)


def download_update():
    wd = inicialize_chrome()
    wd.get("https://clientes.uau.com.br/wbfhome.aspx")
    wd.find_element(By.ID, "ucMenuUsuario1_txtUsuario").send_keys(LOGIN)
    wd.find_element(By.ID, "ucMenuUsuario1_txtSenha").send_keys(PASSWORD)
    wd.find_element(By.ID, "ucMenuUsuario1_btnOk").click()
    wd.find_element(By.LINK_TEXT, "Downloads").click()
    wd.find_element(By.LINK_TEXT, "UAUAPI").click()
    table_lines = wd.find_element(By.ID, "MainContent_dgArquivos").find_elements(By.TAG_NAME, "tr")
    for i, line in enumerate(table_lines):
        if 'atualizador' in line.text.lower():
            table_lines[i].find_element(By.LINK_TEXT, "Módulo UAUAPI").click()
            file_name = table_lines[i].find_elements(By.TAG_NAME, "td")[1].text
            print(file_name)
            time.sleep(2)
            return wait_download(file_name, 300)


def wait_download(file_name, waiting_time):
    download_path = Path.home() / "Downloads" / file_name
    count = 1
    while not os.path.exists(download_path):
        time.sleep(1)
        if count >= waiting_time:
            print("tempo de download excedido")
            raise TimeOutException('Tempo excedido')
        count += 1
    print("download terminado")

    return download_path
