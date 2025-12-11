"""Factory de scrapers."""
from ..scrapers.wiki_scraper import WikiScraper
from ..scrapers.retail_scraper import RetailScraper

class ScraperFactory:
    @staticmethod
    def create_scraper(scraper_type: str, url: str, **kwargs):
        """Crea scraper según tipo."""
        scraper_type = scraper_type.lower()
        
        if scraper_type == 'wiki':
            return WikiScraper(url)
        
        elif scraper_type == 'retail':
            store_type = kwargs.get('store_type', 'alkosto')
            return RetailScraper(url, store_type)
        
        else:
            raise ValueError(f"Tipo inválido: {scraper_type}")