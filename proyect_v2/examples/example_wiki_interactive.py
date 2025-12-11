import sys
sys.path.append('..')

from src.utils.scraper_factory import ScraperFactory
from src.utils.report_generator import ReportGenerator

def example_interactive():
    """Permite al usuario elegir qué tabla extraer."""
    
    print("\nSCRAPING WIKI\n")
    
    
    url = "https://minecraft.fandom.com/wiki/Brewing"
    
    # Crear scraper en modo interactivo
    scraper = ScraperFactory.create_scraper('wiki', url, mode='interactive')
    tables = scraper.extract_data()
    
    if tables:
        print(f"\nTabla extraída exitosamente")
        
        # Mostrar preview
        table = tables[0]
        df = table.to_dataframe()
        print(f"\nColumnas: {', '.join(df.columns.tolist())}")
        print(f"Filas: {len(df)}")
        print("\nPrimeras 5 filas:")
        print(df.head())
        
        # Preguntar si desea guardar
        save = input("\n¿Deseas guardar esta tabla? (s/n): ").lower()
        
        if save == 's':
            report_gen = ReportGenerator(tables, f'tabla_{table.table_id}', 'wiki')
            files = report_gen.generate_full_report(formats=['csv', 'excel'])
            
            print("\nArchivos generados:")
            for fmt, filepath in files.items():
                print(f"  • {fmt}: {filepath}")
    else:
        print("\nNo se extrajo ninguna tabla")

if __name__ == '__main__':
    example_interactive()