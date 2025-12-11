"""Ejemplo: Generación rápida de gráficos."""
import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.data_processor import DataProcessor
from src.utils.chart_generator import ChartGenerator

def example_quick_chart():
    """Genera un gráfico rápido y lo muestra en pantalla."""

    print("EJEMPLO: GRÁFICO RÁPIDO")
    
    # Opción 1: Cargar desde CSV existente
    try:
        import pandas as pd
        print("\n¿Deseas cargar datos desde un CSV existente? (s/n): ", end="")
        choice = input().lower()
        
        if choice == 's':
            filename = input("Nombre del archivo CSV: ")
            df = pd.read_csv(filename)
            print(f"✓ {len(df)} registros cargados")
            
            # Mostrar columnas disponibles
            print(f"\nColumnas disponibles: {', '.join(df.columns)}")
            
            # Preguntar qué graficar
            x_col = input("Columna para eje X: ")
            y_col = input("Columna para eje Y: ")
            
            # Limitar a top 20 para mejor visualización
            if len(df) > 20:
                print(f"\nMostrando solo top 20 de {len(df)} registros")
                df = df.head(20)
            
            # Crear y mostrar gráfico
            ChartGenerator.create_quick_chart(
                df, x_col, y_col, 
                f'{y_col} por {x_col}'
            )
            
        else:
            # Opción 2: Hacer scraping y graficar
            example_scraping_and_chart()
            
    except Exception as e:
        print(f"Error: {e}")

def example_scraping_and_chart():
    """Hace scraping y muestra gráfico directamente."""
    print("\nHaciendo scraping...")
    
    url = "https://www.exito.com/tecnologia/computadores/computadores-gaming"
    scraper = ScraperFactory.create_scraper('retail', url, store_type='exito')
    products = scraper.extract_data()
    
    if not products:
        print("No se encontraron productos")
        return
    
    # Procesar
    processor = DataProcessor(products, 'product')
    processor.clean_data()
    processor.sort_by_price(ascending=False)
    
    df = processor.get_dataframe()
    
    # Limitar a top 15
    df_top = df.head(15)
    
    print(f"\n✓ Mostrando gráfico de top 15 productos más caros")
    
    # Mostrar gráfico
    ChartGenerator.create_quick_chart(
        df_top, 'name', 'price',
        'Top 15 Computadores Gaming Más Caros - Éxito'
    )

if __name__ == '__main__':
    print("\nGenerador de Gráficos Rápido")
    print("\nEste script te permite:")
    print("1. Cargar un CSV existente y graficarlo")
    print("2. Hacer scraping y visualizar resultados al instante")
    print("\n" + "=" * 60)
    
    example_quick_chart()