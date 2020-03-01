import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import pyautogui
import time

#CUENTA CORREO
user = "lizandrovivanco16@gmail.com"
pasw = "lizandrito232114"
de = "Lizandro V"

#VARIABLES
dest="lizandro_131@hotmail.com"
copia="lizandrovivanco16@gmail.com"
asunto="Error Portal"
textomsj="Estimados, se encontro el siguiente error"
name1="Error 1"
name2="Error 2"
archivo1="C:\\Users\\No Tocar!!\\Downloads\\Capturas\\Error 1.png"
archivo2="C:\\Users\\No Tocar!!\\Downloads\\Capturas\\Error 2.png"

def enviarmsj():
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.starttls()
    try:
        print("iniciar")
        gmail.login(user,pasw)
        gmail.set_debuglevel(1)
        rcpt = copia.split(",") + [dest]

        header = MIMEMultipart()
        header['Subject'] = asunto
        header['From'] = de
        header['To'] = dest
        header['Cc'] = copia
    
        mensaje = MIMEText(textomsj, 'html')
        header.attach(mensaje)
        
        print("adjuntar")
        if (os.path.isfile(archivo1)):
            adjunto1 = MIMEBase('application', 'octet-stream')
            adjunto1.set_payload(open(archivo1, "rb").read())
            encode_base64(adjunto1)
            adjunto1.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo1))
            header.attach(adjunto1)

        if (os.path.isfile(archivo2)):
            adjunto2 = MIMEBase('application', 'octet-stream')
            adjunto2.set_payload(open(archivo2, "rb").read())
            encode_base64(adjunto2)
            adjunto2.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo2))
            header.attach(adjunto2)

        gmail.sendmail(de,rcpt,header.as_string())

    except Exception as e:
        print(e)

    finally:
        gmail.quit()
        print("Conexion cerrada")

def screenshot():
    time.sleep(5)
    pyautogui.screenshot("C:\\Users\\No Tocar!!\\Downloads\\Capturas\\" + str(name1) + ".png")
    time.sleep(5)
    pyautogui.screenshot("C:\\Users\\No Tocar!!\\Downloads\\Capturas\\" + str(name2) + ".png")
    time.sleep(5)

screenshot()
enviarmsj()
