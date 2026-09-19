import os
import smtplib
from email.message import EmailMessage


class EmailService:
    def enviar_codigo(self, destinatario, codigo):
        host = os.getenv("SMTP_HOST")
        usuario = os.getenv("SMTP_USER")
        # Gmail muestra las contraseñas de aplicación en grupos de cuatro;
        # eliminamos los espacios para enviarla en el formato que espera SMTP.
        clave = os.getenv("SMTP_PASSWORD", "").replace(" ", "")
        remitente = os.getenv("SMTP_FROM", usuario or "")
        if not all((host, usuario, clave, remitente)):
            raise ValueError(
                "El envío de correo no está configurado. Completa las variables SMTP en .env"
            )
        mensaje = EmailMessage()
        mensaje["Subject"] = "Código de acceso - Laboratorio Flask"
        mensaje["From"] = remitente
        mensaje["To"] = destinatario
        mensaje.set_content(f"Tu código de acceso es: {codigo}")
        try:
            with smtplib.SMTP(host, int(os.getenv("SMTP_PORT", "587"))) as servidor:
                servidor.starttls()
                servidor.login(usuario, clave)
                servidor.send_message(mensaje)
            return True
        except (OSError, smtplib.SMTPException) as error:
            raise ValueError(
                "No fue posible enviar el código. Revisa los datos SMTP y vuelve a intentarlo."
            ) from error
