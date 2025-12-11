"""Ejemplo: Ordenamiento y filtrado de datos."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.data_processor import DataProcessor
from src.utils.report_generator import ReportGenerator

def example_sorting():
    """Ejemplo de ordenamiento y filtrado."""

    print("EJEMPLO: ORDENAMIENTO Y FILTRADO DE DATOS")

    
    # Scraping
    url = "https://www.alkosto.com/pc-gamer/c/pc-gamer?sort=relevance&q=%3Arelevance%3Acategory%3APort%C3%A1tiles%20Gaming"
    scraper = ScraperFactory.create_scraper('retail', url, store_type='alkosto')
    products = scraper.extract_data()
    
    print(f"\n✓ {len(products)} productos extraídos")
    
    # Procesar datos
    processor = DataProcessor(products, 'product')
    processor.clean_data()
    
    # === ORDENAMIENTO ===
    print("\n" + "="*60)
    print("ORDENAMIENTO")
    print("="*60)
    
    # Ordenar de menor a mayor precio
    processor.sort_by_price(ascending=True)
    df = processor.get_dataframe()
    
    print("\nTop 10 MÁS BARATOS:")
    print("-" * 60)
    top_10_cheap = df.head(10)
    for i, row in top_10_cheap.iterrows():
        print(f"{i+1}. {row['name'][:50]}")
        print(f"   Marca: {row['brand']} | Precio: ${row['price']:,.0f}")
    
    # Ordenar de mayor a menor precio
    processor.sort_by_price(ascending=False)
    df = processor.get_dataframe()
    
    print("\nTop 10 MÁS CAROS:")
    print("-" * 60)
    top_10_expensive = df.head(10)
    for i, row in top_10_expensive.iterrows():
        print(f"{i+1}. {row['name'][:50]}")
        print(f"   Marca: {row['brand']} | Precio: ${row['price']:,.0f}")
    
    # === FILTRADO POR RANGO DE PRECIO ===
    print("\n" + "="*60)
    print("FILTRADO POR RANGO DE PRECIO")
    print("="*60)
    
    processor = DataProcessor(products, 'product')  # Reiniciar
    processor.clean_data()
    processor.filter_by_price_range(min_price=100000, max_price=500000)
    processor.sort_by_price(ascending=True)
    
    df_filtered = processor.get_dataframe()
    print(f"\nProductos en rango $100,000 - $500,000: {len(df_filtered)}")
    
    # === FILTRADO POR MARCA ===
    print("\n" + "="*60)
    print("FILTRADO POR MARCA")
    print("="*60)
    
    # Obtener todas las marcas
    all_brands = processor.get_dataframe()['brand'].unique()
    print(f"\nMarcas disponibles: {', '.join(all_brands[:10])}...")
    
    # Filtrar por marcas específicas
    selected_brands = ['ASUS', 'HP', 'LENOVO', 'LOGITECH']
    processor = DataProcessor(products, 'product')  # Reiniciar
    processor.clean_data()
    processor.filter_by_brand(selected_brands)
    
    df_brands = processor.get_dataframe()
    print(f"\nProductos de {', '.join(selected_brands)}: {len(df_brands)}")
    
    # === ESTADÍSTICAS POR MARCA ===
    print("\n" + "="*60)
    print("ESTADÍSTICAS POR MARCA")
    print("="*60)
    
    processor = DataProcessor(products, 'product')  # Reiniciar
    processor.clean_data()
    brand_stats = processor.get_brand_statistics()
    
    if brand_stats is not None:
        print("\nTop 10 marcas con más productos:")
        print(brand_stats.head(10))
    
    # === GUARDAR DATOS ORDENADOS ===

    print("\nGUARDANDO REPORTES\n")
    
    # Generar reporte con datos ordenados (menor a mayor precio)
    processor = DataProcessor(products, 'product')
    processor.clean_data()
    processor.sort_by_price(ascending=True)
    
    report_gen = ReportGenerator(products, 'productos_ordenados', 'product')
    files = report_gen.generate_full_report(formats=['csv', 'excel'])
    
    print("\n✓ Reportes generados:")
    for fmt, filepath in files.items():
        print(f"  • {fmt}: {filepath}")

if __name__ == '__main__':
    example_sorting()