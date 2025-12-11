"""Scraper para sitios Wiki."""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from .base_scraper import Scraper
from ..models.wiki_table import WikiTable

class WikiScraper(Scraper):
    def __init__(self, url: str, mode: str = 'all'):
        """
        Args:
            url: URL de la página wiki
            mode: 'all' (todas), 'single' (primera), 'interactive' (elegir)
        """
        super().__init__(url)
        self.mode = mode
        self.soup = None
    
    def extract_data(self):
        """Extrae tablas según el modo."""
        print(f"Extrayendo tablas de: {self.url}")
        
        # Obtener página
        response = requests.get(self.url, timeout=30)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")
        
        # Buscar tablas
        tables = self.soup.find_all("table", class_="wikitable")
        print(f"Tablas encontradas: {len(tables)}")
        
        if not tables:
            print("No se encontraron tablas")
            return []
        
        # Extraer según modo
        if self.mode == 'all':
            return self._extract_all_tables(tables)
        elif self.mode == 'single':
            return self._extract_single_table(tables, 0)
        elif self.mode == 'interactive':
            return self._extract_interactive(tables)
        else:
            return self._extract_all_tables(tables)
    
    def _extract_all_tables(self, tables):
        """Extrae todas las tablas."""
        wiki_tables = []
        for i, table in enumerate(tables):
            try:
                df = pd.read_html(StringIO(str(table)))[0]
                wiki_table = WikiTable(
                    table_id=i + 1,
                    headers=df.columns.tolist(),
                    rows=df.values.tolist()
                )
                wiki_tables.append(wiki_table)
                print(f"Tabla {i+1} extraída")
            except Exception as e:
                print(f"Error en tabla {i+1}: {e}")
        
        self.data = wiki_tables
        return wiki_tables
    
    def _extract_single_table(self, tables, index):
        """Extrae una tabla específica."""
        try:
            df = pd.read_html(StringIO(str(tables[index])))[0]
            wiki_table = WikiTable(
                table_id=index + 1,
                headers=df.columns.tolist(),
                rows=df.values.tolist()
            )
            self.data = [wiki_table]
            return [wiki_table]
        except Exception as e:
            print(f"Error extrayendo tabla {index+1}: {e}")
            return []
    
    def _extract_interactive(self, tables):
        """Permite al usuario elegir qué tabla extraer."""

        print(f"Se encontraron {len(tables)} tablas")

        
        for i in range(len(tables)):
            print(f"  [{i+1}] Tabla {i+1}")
        
        while True:
            try:
                n = int(input(f"¿Qué tabla deseas extraer? (1-{len(tables)}): "))
                if 1 <= n <= len(tables):
                    return self._extract_single_table(tables, n-1)
                else:
                    print(f"Número inválido. Debe ser entre 1 y {len(tables)}")
            except ValueError:
                print("Por favor ingresa un número válido")
            except KeyboardInterrupt:
                print("\nOperación cancelada")
                return []