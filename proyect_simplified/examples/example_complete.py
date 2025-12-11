"""Ejemplo completo: Scraping + Reportes + Gráficos + Email."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.report_generator import ReportGenerator
from src.utils.data_processor import DataProcessor
from src.utils.email_sender import EmailSender

def example_complete_workflow():
    """Flujo completo de trabajo."""
    print("=" * 60)
    print("EJEMPLO COMPLETO: Scraping → Análisis → Reportes → Email")
    print("=" * 60)
    
    # === 1. SCRAPING ===
    print("\n[1/4] Extrayendo datos...")
    url = "https://www.alkosto.com/pc-gamer/c/pc-gamer"
    scraper = ScraperFactory.create_scraper('retail', url, store_type='alkosto')
    products = scraper.extract_data()
    print(f"✓ {len(products)} productos extraídos")
    
    # === 2. ANÁLISIS ===
    print("\n[2/4] Analizando datos...")
    processor = DataProcessor(products, 'product')
    processor.clean_data()
    
    stats = processor.get_statistics()
    print("✓ Estadísticas:")
    for key, value in stats.items():
        print(f"  • {key}: {value}")
    
    # === 3. REPORTES Y GRÁFICOS ===
    print("\n[3/4] Generando reportes...")
    report_gen = ReportGenerator(products, 'reporte_completo', 'product')
    files = report_gen.generate_full_report(
        formats=['csv', 'excel', 'json', 'html'],
        with_charts=True
    )
    
    print("✓ Archivos generados:")
    for fmt, filepath in files.items():
        print(f"  • {fmt}: {filepath}")
    
    # === 4. ENVÍO POR EMAIL (OPCIONAL) ===
    print("\n[4/4] Envío por email...")
    SEND_EMAIL = False  # Cambiar a True para enviar
    
    if SEND_EMAIL:
        # Configurar credenciales
        sender = EmailSender(
            smtp_server='smtp.gmail.com',
            smtp_port=587,
            email='tu_email@gmail.com',      # ← CAMBIAR
            password='tu_app_password'        # ← CAMBIAR
        )
        
        subject = f"Reporte de Scraping - {len(products)} productos"
        body = f"""
Hola,

Se ha completado el proceso de scraping.

Resumen:
- Total productos: {stats['total']}
- Precio promedio: ${stats['precio_promedio']:,.0f}
- Precio mínimo: ${stats['precio_min']:,.0f}
- Precio máximo: ${stats['precio_max']:,.0f}

Los reportes detallados están adjuntos.

Saludos,
Sistema de Web Scraping
        """
        
        success = sender.send_email(
            recipient='destinatario@example.com',  # ← CAMBIAR
            subject=subject,
            body=body,
            attachments=list(files.values())
        )
        
        if success:
            print("✓ Email enviado")
        else:
            print("✗ Error enviando email")
    else:
        print("⊗ Envío de email desactivado (configura SEND_EMAIL=True)")
    
    print("\n" + "=" * 60)
    print("✓ PROCESO COMPLETADO")
    print("=" * 60)

if __name__ == '__main__':
    example_complete_workflow()