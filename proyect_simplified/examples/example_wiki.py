"""Ejemplo de scraping Wiki."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.report_generator import ReportGenerator

def example_wiki():
    """Extraer tablas de wiki."""
    print("=== Scraping Wiki ===")
    
    url = "https://minecraft.fandom.com/wiki/Brewing"
    
    # Crear scraper y extraer datos
    scraper = ScraperFactory.create_scraper('wiki', url)
    tables = scraper.extract_data()
    
    print(f"Tablas extraídas: {len(tables)}")
    
    # Generar reportes
    if tables:
        report_gen = ReportGenerator(tables, 'minecraft_brewing', 'wiki')
        files = report_gen.generate_full_report(formats=['csv', 'excel'])
        
        print("\nReportes generados:")
        for fmt, filepath in files.items():
            print(f"  {fmt}: {filepath}")

if __name__ == '__main__':
    example_wiki()