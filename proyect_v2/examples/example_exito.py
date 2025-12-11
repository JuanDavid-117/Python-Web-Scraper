"""Ejemplo específico para Éxito (mejorado)."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.data_processor import DataProcessor
from src.utils.report_generator import ReportGenerator

def example_exito():


    print("\n SCRAPING ÉXITO - COMPUTADORES GAMING\n ")
    
    url = "https://www.exito.com/tecnologia/computadores/computadores-gaming"
    
    # Scraping con navegador visible para verificar
    print("\n  Configuración:")
    print("  • Tienda: Éxito")
    print("  • URL: " + url)
    print("  • Modo: Headless")
    print()
    
    scraper = ScraperFactory.create_scraper(
        'retail', 
        url, 
        store_type='exito',
        headless=True  # Cambiar a False para ver el navegador
    )
    
    products = scraper.extract_data()
    
    if not products:
        print("No se encontraron productos")
        return
    
    print(f"\n✓ Total de productos extraídos: {len(products)}")
    
    # === PROCESAMIENTO ===
    print("\n" + "="*60)
    print("PROCESAMIENTO DE DATOS")
    print("="*60)
    
    processor = DataProcessor(products, 'product')
    processor.clean_data()
    
    # Estadísticas
    stats = processor.get_statistics()
    print("\nEstadísticas:")
    print(f"  • Total productos: {stats['total']}")
    print(f"  • Precio promedio: ${stats['precio_promedio']:,.0f}")
    print(f"  • Precio mínimo: ${stats['precio_min']:,.0f}")
    print(f"  • Precio máximo: ${stats['precio_max']:,.0f}")
    print(f"  • Marcas únicas: {stats['marcas_unicas']}")
    
    # === ORDENAMIENTO ===
    processor.sort_by_price(ascending=True)
    df = processor.get_dataframe()
    
    print("\n" + "="*60)
    print("TOP 10 MÁS BARATOS")
    print("="*60)
    
    for i, row in df.head(10).iterrows():
        print(f"\n{i+1}. {row['name']}")
        print(f"    ${row['price']:,.0f}")
        print(f"    {row['brand']}")
    
    # === ANÁLISIS POR MARCA ===

    print("\nANÁLISIS POR MARCA\n")

    
    brand_stats = processor.get_brand_statistics()
    if brand_stats is not None:
        print("\nEstadísticas por marca:")
        print(brand_stats)
    
    # === GENERAR REPORTES ===

    print("\nGENERANDO REPORTES\n")
    
    report_gen = ReportGenerator(products, 'exito_computadores', 'product')
    files = report_gen.generate_full_report(
        formats=['csv', 'excel', 'html'],
        with_charts=True
    )
    
    print("\n✓ Archivos generados:")
    for fmt, filepath in files.items():
        print(f"  • {fmt}: {filepath}")
    
    print("\n" + "="*60)
    print("✓ PROCESO COMPLETADO")
    print("="*60)

if __name__ == '__main__':
    example_exito()