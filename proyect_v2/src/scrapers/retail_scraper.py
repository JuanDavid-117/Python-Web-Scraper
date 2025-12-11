"""Scraper para sitios retail."""
import time
from playwright.sync_api import sync_playwright
from .base_scraper import Scraper
from ..models.product import Product

class RetailScraper(Scraper):
    def __init__(self, url: str, store_type: str = 'alkosto', headless: bool = True):
        super().__init__(url)
        self.store_type = store_type.lower()
        self.headless = headless
        self.products = []
        self.selectors = self._get_selectors()
    
    def _get_selectors(self):
        """Selectores CSS por tienda."""
        selectors = {
            'alkosto': {
                'items': 'ol[class^=ais-InfiniteHits-list] > li',
                'name': 'a > div > h3',
                'brand': 'div > div.product__item__information__key-features.js-key-features > div.product__item__information__brand',
                'price': 'div > div.product__item__information__price > div.product__item__information__price--wrapper.js-product-item-info-price > div.product__item__information__price-section--container > div.product__item__informatio1n__price-section > div.hidden-sm.hidden-xs > div.product__item__information__base-price > div > div > span.price, div > div.product__item__information__price > div.product__item__information__price--wrapper.js-product-item-info-price > div.product__item__information__price-section--container > div.product__item__informatio1n__price-section > div.hidden-sm.hidden-xs > div.product__item__information__base-price > div > p > span.price',
                'load_more': 'div > button[class^="ais-InfiniteHits-loadMore"]',
                'scroll_target': '#seo-zone'
            },
            'exito': {
                'items': 'article[class^="productCard_"]',
                'name': 'a h3[class*="styles_name"]',
                'brand': 'a h3[class*="styles_brand"]',
                'price': 'div p[class^="ProductPrice_container"]',
                'next_button': 'span',
                'next_button_text': 'Siguiente',
                'scroll_target': 'footer[id*="footerLayout"]'
            }
        }
        
        if self.store_type not in selectors:
            raise ValueError(f"Tienda no soportada: {self.store_type}")
        
        return selectors[self.store_type]
    
    def extract_data(self):
        """Extrae productos."""
        print(f"Extrayendo productos de {self.store_type}: {self.url}")
        print(f"Modo headless: {self.headless}")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            page.set_default_timeout(60000)
            
            print("Cargando página...")
            page.goto(self.url, wait_until="domcontentloaded")
            time.sleep(3)
            
            # Scraping según tienda
            if self.store_type == 'alkosto':
                self._scrape_alkosto(page)
            elif self.store_type == 'exito':
                self._scrape_exito(page)
            
            browser.close()
        
        print(f"✓ Productos extraídos: {len(self.products)}")
        self.data = self.products
        return self.products
    
    def _scrape_alkosto(self, page):
        """Lógica de scraping para Alkosto."""
        print("Cargando todos los productos...")
        
        # Cargar todos los productos
        while True:
            scroll_to = page.locator(self.selectors['scroll_target'])
            scroll_to.scroll_into_view_if_needed()
            time.sleep(3)
            
            next_button = page.locator(self.selectors['load_more'])
            
            if next_button.count() > 0 and next_button.is_visible() and next_button.is_enabled():
                print("  Cargando más productos...")
                next_button.click()
                page.wait_for_load_state("domcontentloaded")
                time.sleep(3)
            else:
                print("  ✓ Todos los productos cargados")
                break
        
        # Extraer productos
        print("Extrayendo información de productos...")
        items = page.query_selector_all(self.selectors['items'])
        
        for i, item in enumerate(items, 1):
            try:
                # Nombre
                title_el = item.query_selector(self.selectors['name'])
                name = title_el.inner_text() if title_el and title_el.is_visible() else "Sin nombre"
                
                # Marca
                brand_el = item.query_selector(self.selectors['brand'])
                brand = brand_el.inner_text() if brand_el and brand_el.is_visible() else "Sin marca"
                
                # Precio
                price_el = item.query_selector(self.selectors['price'])
                price = price_el.inner_text() if price_el and price_el.is_visible() else "0"
                
                product = Product(
                    name=name,
                    brand=brand,
                    price=price,
                    store=self.store_type
                )
                self.products.append(product)
                
                if i % 10 == 0:
                    print(f"  Procesados: {i}/{len(items)}")
                    
            except Exception as e:
                print(f"  Error en producto {i}: {e}")
                continue
    
    def _scrape_exito(self, page):
        """Lógica de scraping para Éxito (mejorada)."""
        page_num = 1
        
        while True:
            print(f"Extrayendo página {page_num}...")
            
            # Scroll
            scroll_to = page.locator(self.selectors['scroll_target'])
            scroll_to.scroll_into_view_if_needed()
            time.sleep(3)
            
            # Extraer productos de la página actual
            titles = page.query_selector_all(f'{self.selectors["items"]} {self.selectors["name"]}')
            brands = page.query_selector_all(f'{self.selectors["items"]} {self.selectors["brand"]}')
            prices = page.query_selector_all(f'{self.selectors["items"]} {self.selectors["price"]}')
            
            # Verificar que tengan la misma cantidad
            min_len = min(len(titles), len(brands), len(prices))
            
            for i in range(min_len):
                try:
                    if titles[i].is_visible() and brands[i].is_visible() and prices[i].is_visible():
                        product = Product(
                            name=titles[i].inner_text(),
                            brand=brands[i].inner_text(),
                            price=prices[i].inner_text(),
                            store=self.store_type
                        )
                        self.products.append(product)
                except Exception as e:
                    continue
            
            print(f"  ✓ {min_len} productos extraídos de página {page_num}")
            
            # Buscar botón siguiente
            next_button = page.locator(
                self.selectors['next_button'], 
                has_text=self.selectors['next_button_text']
            )
            
            if next_button.is_visible() and next_button.is_enabled():
                print(f"  Navegando a página {page_num + 1}...")
                next_button.click()
                page.wait_for_load_state("domcontentloaded")
                time.sleep(3)
                page_num += 1
            else:
                print(f"  ✓ Scraping completado ({page_num} páginas)")
                break