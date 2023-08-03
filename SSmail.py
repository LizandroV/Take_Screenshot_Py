import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import pyautogui
import time

#CUENTA CORREO
user = "RPA_asdasdadaqf@hotmail.com"
pasw = """123qweASD!"#"""
de = "RPA_asdasdadaqf@hotmail.com"

#VARIABLES
dest="lizandro_131@hotmail.com"
copia="RPA_asdasdadaqf@hotmail.com,informesrpa@yahoo.com"
asunto="Error RPA"
textomsj="Estimado, se envia por adjunto el error encontrado"
name1="Error 1"
archivo1="C:\\Screenshots\\Error 1.png"

def enviarmsj():
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    
    try:
        print("iniciar")
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()
        servidor.login(user,pasw)
        servidor.set_debuglevel(1)
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

        servidor.sendmail(de,rcpt,header.as_string())
        print("Listo enviado")
    except Exception as e:
        print(e)

    finally:
        servidor.quit()
        print("Conexion cerrada")

def screenshot():
    time.sleep(3)
    pyautogui.screenshot("C:\\Screenshots\\" + str(name1) + ".png")
    time.sleep(3)
    print("captura realizada")

screenshot()
enviarmsj()
