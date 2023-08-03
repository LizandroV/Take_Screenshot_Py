import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(usuario_yahoo, contrasena, destinatario, asunto, cuerpo):
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    try:
        servidor = smtplib.SMTP(smtp_server, smtp_port)
        servidor.starttls()
        servidor.login(usuario_yahoo, contrasena)

        mensaje = MIMEMultipart()
        mensaje['From'] = usuario_yahoo
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto

        mensaje.attach(MIMEText(cuerpo, 'plain'))

        servidor.sendmail(usuario_yahoo, destinatario, mensaje.as_string())

        servidor.quit()
        print("¡Correo enviado correctamente!")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    usuario_yahoo = "RPA_asdasdadaqf@hotmail.com"  # Reemplaza con tu dirección de correo Yahoo
    contrasena = """123qweASD!"#"""  # Reemplaza con tu contraseña de Yahoo
    destinatario = "lizandro_131@hotmail.com"  # Reemplaza con la dirección del destinatario
    asunto = "Correo de prueba desde Python"
    cuerpo = "Hola, este es un correo de prueba enviado desde Python 3."

    enviar_correo(usuario_yahoo, contrasena, destinatario, asunto, cuerpo)