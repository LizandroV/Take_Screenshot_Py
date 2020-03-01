import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64


#VARIABLES
msjto="lizandro_131@hotmail.com"
msjcc=""
msjsubject=StringVar()
nameshow=StringVar()
filename=StringVar()
nameshow.set("Seleccionar Archivo...")

#CUENTA CORREO
user = "lizandrovivanco16@gmail.com"
pasw = "lizandrito232114"
de = "Lizandro V"


def enviarmsj():
    dest =  msjto.get()
    copia = msjcc.get()
    asunto =  msjsubject.get()
    mensaje =   mesagetext.get("1.0", END)
    archivo = filename.get()

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.starttls()
    try:
        gmail.login(user,pasw)
        gmail.set_debuglevel(1)

        rcpt = copia.split(",") + [dest]

        header = MIMEMultipart()
        header['Subject'] = asunto
        header['From'] = de
        header['To'] = dest
        header['Cc'] = copia
    
        mensaje = MIMEText(mensaje, 'html')
        header.attach(mensaje)

        if (os.path.isfile(archivo)):
            adjunto = MIMEBase('application', 'octet-stream')
            adjunto.set_payload(open(archivo, "rb").read())
            encode_base64(adjunto)
            adjunto.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo))
            header.attach(adjunto)

        gmail.sendmail(de,rcpt,header.as_string())

        gmail.quit()

        messagebox.showinfo("Email", "Correo enviado con exito")

    except:
        messagebox.showwarning("Atencion", "Error de envio")
        gmail.quit()


def adjuntararchivo():
    global namefile
    namefile =  filedialog.askopenfilename(title = "Seleccionar Archivo...",filetypes = (("Archivos Excel","*.xlsx"),("Todos los Archivos","*.*")))
    try:
        if namefile == "":
            nameshow.set("Seleccionar Archivo...")
        else:
            nameshow.set(os.path.basename(namefile))
            filename.set(namefile)
    except:
        nameshow.set("Seleccionar Archivo...")

