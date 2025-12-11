"""Ejemplo de scraping Retail."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.report_generator import ReportGenerator

def example_alkosto():
    """Extraer productos de Alkosto."""
    print("=== Scraping Alkosto ===")
    
    url = "https://www.alkosto.com/pc-gamer/c/pc-gamer?sort=relevance&q=%3Arelevance%3Acategory%3APort%C3%A1tiles%20Gaming"
    
    # Crear scraper y extraer datos
    scraper = ScraperFactory.create_scraper('retail', url, store_type='alkosto')
    products = scraper.extract_data()
    
    print(f"Productos extraídos: {len(products)}")
    
    # Mostrar primeros 5
    print("\nPrimeros 5 productos:")
    for product in products[:5]:
        print(f"  - {product}")
    
    # Generar reportes
    if products:
        report_gen = ReportGenerator(products, 'alkosto_products', 'product')
        files = report_gen.generate_full_report(formats=['csv', 'excel'])
        
        print("\nReportes generados:")
        for fmt, filepath in files.items():
            print(f"  {fmt}: {filepath}")

if __name__ == '__main__':
    example_alkosto()