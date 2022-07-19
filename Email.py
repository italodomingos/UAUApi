import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import acessos


def send_message(text):

    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()

    password = acessos.senha_outlook
    login = acessos.login_outlook
    s.login(login, password)
    msg = MIMEMultipart()

    msg['From'] = login
    msg['To'] = login
    msg['Subject'] = "Error UAUAPI Update"

    msg.attach(MIMEText(text, 'plain'))

    s.send_message(msg)
