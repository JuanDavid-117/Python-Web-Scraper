"""Envío de emails simple."""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, email: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
    
    def send_email(self, recipient: str, subject: str, body: str, attachments=None):
        """Envía un email con archivos adjuntos."""
        try:
            # Crear mensaje
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Adjuntar archivos
            if attachments:
                for filepath in attachments:
                    try:
                        with open(filepath, 'rb') as f:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(f.read())
                        encoders.encode_base64(part)
                        filename = filepath.split('/')[-1].split('\\')[-1]
                        part.add_header('Content-Disposition', f'attachment; filename={filename}')
                        msg.attach(part)
                    except Exception as e:
                        print(f"Error adjuntando {filepath}: {e}")
            
            # Enviar
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            print(f"✓ Email enviado a {recipient}")
            return True
            
        except Exception as e:
            print(f"✗ Error enviando email: {e}")
            return False