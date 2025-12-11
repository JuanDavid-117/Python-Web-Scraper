"""Ejemplo de envío de emails."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.report_generator import ReportGenerator
from src.utils.email_sender import EmailSender

def example_send_email():
    """Genera reporte y lo envía por email."""
    print("=== Scraping y Envío por Email ===")
    
    # 1. Hacer scraping
    url = "https://minecraft.fandom.com/wiki/Brewing"
    scraper = ScraperFactory.create_scraper('wiki', url)
    tables = scraper.extract_data()
    
    print(f"Tablas extraídas: {len(tables)}")
    
    # 2. Generar reportes
    report_gen = ReportGenerator(tables, 'minecraft_brewing', 'wiki')
    files = report_gen.generate_full_report(formats=['excel', 'html'])
    
    print("\nReportes generados:")
    for fmt, filepath in files.items():
        print(f"  {fmt}: {filepath}")
    
    # 3. Configurar y enviar email
    # IMPORTANTE: Para Gmail necesitas una "App Password"
    # Ver: https://support.google.com/accounts/answer/185833
    
    # CONFIGURACION DE CREDENCIALES:
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SENDER_EMAIL = 'tu_email@gmail.com'  # ← CAMBIAR
    SENDER_PASSWORD = 'tu_app_password'   # ← CAMBIAR
    RECIPIENT = 'destinatario@example.com'  # ← CAMBIAR
    
    # Crear sender
    sender = EmailSender(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD)
    
    # Enviar email
    subject = 'Reporte de Web Scraping - Minecraft'
    body = """
Hola,

Adjunto encontrarás el reporte de scraping de Minecraft Wiki.
El reporte incluye todas las tablas extraídas.

Saludos,
Sistema de Web Scraping
    """
    
    success = sender.send_email(
        recipient=RECIPIENT,
        subject=subject,
        body=body,
        attachments=list(files.values())
    )
    
    if success:
        print(f"\nEmail enviado exitosamente")
    else:
        print(f"\nError al enviar email")

if __name__ == '__main__':
    print("NOTA: Debes configurar tus credenciales SMTP en el código.")
    print("Para Gmail, necesitas una App Password.")
    print("Ver: https://support.google.com/accounts/answer/185833\n")
    
    # Descomentar para ejecutar:
    # example_send_email()