"""Factory de scrapers."""
from ..scrapers.wiki_scraper import WikiScraper
from ..scrapers.retail_scraper import RetailScraper

class ScraperFactory:
    @staticmethod
    def create_scraper(scraper_type: str, url: str, **kwargs):
        """
        Crea scraper según tipo.
        
        Args:
            scraper_type: 'wiki' o 'retail'
            url: URL a scrapear
            **kwargs: Parámetros adicionales
                Para wiki:
                    - mode: 'all', 'single', 'interactive' (default: 'all')
                Para retail:
                    - store_type: 'alkosto', 'exito' (default: 'alkosto')
                    - headless: True/False (default: True)
        
        Returns:
            Instancia de Scraper
        """
        scraper_type = scraper_type.lower()
        
        if scraper_type == 'wiki':
            mode = kwargs.get('mode', 'all')
            return WikiScraper(url, mode)
        
        elif scraper_type == 'retail':
            store_type = kwargs.get('store_type', 'alkosto')
            headless = kwargs.get('headless', True)
            return RetailScraper(url, store_type, headless)
        
        else:
            raise ValueError(f"Tipo inválido: {scraper_type}. Usa 'wiki' o 'retail'.")