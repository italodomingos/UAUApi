import datetime
import time
import pyautogui
import os
import UAUDownload
import subprocess
import threading

import log


class TimeOutException(Exception):

    def __init__(self, message):
        super().__init__(message)


class ClickThread(threading.Thread):
    def __init__(self, image):
        threading.Thread.__init__(self)
        self.image = image

    def run(self):

        log.write('Iniciando a Thread')
        pyautogui.click(locate_element(self.image))
        log.write('Fim da Thread')


def locate_element(image):
    count = 1
    while not pyautogui.locateOnScreen(image):
        log.write('Procurando imagem')
        time.sleep(1)
        if count >= 10:
            raise TimeOutException('Tempo de procura da imagem excedido')
        count += 1

    return pyautogui.locateOnScreen(image)


def update_uauapi():
    download_path = UAUDownload.download_update()
    subprocess.call([r'C:\Windows\System32\inetsrv\appcmd.exe', 'stop', 'apppool', 'uauAPI'])

    time.sleep(1)

    _, file_name = os.path.split(download_path)

    new_path = f"C:/inetpub/wwwroot/uauAPI/{file_name}"
    remove_old_updater()
    time.sleep(1)
    os.rename(download_path, new_path)
    ClickThread(r"C:\UAUAPIUPDATER\instalar.png").start()
    os.system(new_path)
    os.system(r"cd C:\inetpub\wwwroot\uauAPI\bin && regCompsWS.bat")
    os.system(r"cd C:\inetpub\wwwroot\uauAPI\bin && GerModulosUAU.exe")
    ClickThread(r"C:\UAUAPIUPDATER\ok.png").start()
    os.system(r"cd C:\inetpub\wwwroot\uauAPI\bin && regsvr32 ParcelasTemp.dll")

    time.sleep(1)

    subprocess.call([r'C:\Windows\System32\inetsrv\appcmd.exe', 'start', 'apppool', 'uauAPI'])


def remove_old_updater():

    for _, _, files in os.walk(r'C:\inetpub\wwwroot\uauAPI'):
        for file_name in files:
            if 'uauapi-atualizador' in file_name.lower():
                arquivo = rf'C:\inetpub\wwwroot\uauAPI\{file_name}'
                os.remove(arquivo)
                log.write(f'Arquivo {arquivo} removido')


# def remove_bitrix():
#     while True:
#         if not pyautogui.locateOnScreen("resources/marcado.png", confidence=0.9):
#             all = locate_element("resources/all.png")
#             x, y = pyautogui.center(all)
#             pyautogui.click(x-10, y)
#             time.sleep(0.5)
#             pyautogui.click(locate_element("resources/excluir.png"))
#             time.sleep(0.5)
#             pyautogui.click(locate_element("resources/continuar.png"))
#             time.sleep(0.5)

# remove_bitrix()
