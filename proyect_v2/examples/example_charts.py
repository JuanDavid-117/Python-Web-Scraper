"""Ejemplo de generación de gráficos."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.report_generator import ReportGenerator

def example_with_charts():
    """Genera reportes con gráficos."""
    print("=== Scraping con Gráficos ===")
    
    url = "https://www.alkosto.com/pc-gamer/c/pc-gamer?sort=relevance&q=%3Arelevance%3Acategory%3APort%C3%A1tiles%20Gaming"
    
    # Scraping
    scraper = ScraperFactory.create_scraper('retail', url, store_type='alkosto')
    products = scraper.extract_data()
    
    print(f"Productos extraídos: {len(products)}")
    
    # Generar reportes CON gráficos
    if products:
        report_gen = ReportGenerator(products, 'reporte_con_graficos', 'product')
        files = report_gen.generate_full_report(
            formats=['csv', 'excel', 'html'],
            with_charts=True  # ← Activa la generación de gráficos
        )
        
        print("\n✓ Archivos generados:")
        for fmt, filepath in files.items():
            print(f"  {fmt}: {filepath}")

if __name__ == '__main__':
    example_with_charts()