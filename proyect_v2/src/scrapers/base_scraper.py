"""Clase base para scrapers."""
from abc import ABC, abstractmethod

class Scraper(ABC):
    def __init__(self, url: str):
        self.url = url
        self.data = []
        
        if not (url.startswith('http://') or url.startswith('https://')):
            raise ValueError(f"URL inválida: {url}")
    
    @abstractmethod
    def extract_data(self):
        """Extrae datos. Implementar en subclases."""
        pass