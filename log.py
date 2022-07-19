import datetime


def write(text):
    with open(r"C:\UAUAPIUPDATER\log.txt", "a") as log:
        time_now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        log.write(f'{time_now} {text}')
