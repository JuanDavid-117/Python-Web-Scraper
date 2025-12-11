"""Scraper para sitios Wiki."""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from .base_scraper import Scraper
from ..models.wiki_table import WikiTable

class WikiScraper(Scraper):
    def __init__(self, url: str):
        super().__init__(url)
        self.soup = None
    
    def extract_data(self):
        """Extrae todas las tablas de la página."""
        print(f"Extrayendo tablas de: {self.url}")
        
        # Obtener página
        response = requests.get(self.url, timeout=30)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")
        
        # Buscar tablas
        tables = self.soup.find_all("table", class_="wikitable")
        print(f"Tablas encontradas: {len(tables)}")
        
        wiki_tables = []
        for i, table in enumerate(tables):
            try:
                df = pd.read_html(str(table))[0]
                wiki_table = WikiTable(
                    table_id=i + 1,
                    headers=df.columns.tolist(),
                    rows=df.values.tolist()
                )
                wiki_tables.append(wiki_table)
            except Exception as e:
                print(f"Error en tabla {i+1}: {e}")
        
        self.data = wiki_tables
        return wiki_tables