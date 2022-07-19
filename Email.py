import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_message(text):

    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()

    password = 'imd@2018'
    s.login("italo.domingos@bambui.com.br", password)
    msg = MIMEMultipart()

    msg['From'] = 'italo.domingos@bambui.com.br'
    msg['To'] = 'italo.domingos@bambui.com.br'
    msg['Subject'] = "Error UAUAPI Update"

    msg.attach(MIMEText(text, 'plain'))

    s.send_message(msg)
