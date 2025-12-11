"""Scraper para sitios retail."""
import time
from playwright.sync_api import sync_playwright
from .base_scraper import Scraper
from ..models.product import Product

class RetailScraper(Scraper):
    def __init__(self, url: str, store_type: str = 'alkosto'):
        super().__init__(url)
        self.store_type = store_type.lower()
        self.products = []
        self.selectors = self._get_selectors()
    
    def _get_selectors(self):
        """Selectores CSS por tienda."""
        selectors = {
            'alkosto': {
                'items': 'ol[class^=ais-InfiniteHits-list] > li',
                'name': 'a > div > h3',
                'brand': 'div.product__item__information__brand',
                'price': 'span.price'
            }
        }
        
        if self.store_type not in selectors:
            raise ValueError(f"Tienda no soportada: {self.store_type}")
        
        return selectors[self.store_type]
    
    def extract_data(self):
        """Extrae productos."""
        print(f"Extrayendo productos de {self.store_type}: {self.url}")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            print("Cargando página...")
            page.goto(self.url, wait_until="domcontentloaded")
            time.sleep(5)
            
            print("Extrayendo productos...")
            items = page.query_selector_all(self.selectors['items'])
            
            for item in items:
                try:
                    name_el = item.query_selector(self.selectors['name'])
                    brand_el = item.query_selector(self.selectors['brand'])
                    price_el = item.query_selector(self.selectors['price'])
                    
                    if name_el and price_el:
                        product = Product(
                            name=name_el.inner_text(),
                            brand=brand_el.inner_text() if brand_el else "Sin marca",
                            price=price_el.inner_text(),
                            store=self.store_type
                        )
                        self.products.append(product)
                except Exception as e:
                    continue
            
            browser.close()
        
        print(f"Productos extraídos: {len(self.products)}")
        self.data = self.products
        return self.products