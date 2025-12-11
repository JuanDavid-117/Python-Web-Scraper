"""Modelo de producto."""
import re

class Product:
    def __init__(self, name: str, brand: str, price: str, store: str = ""):
        self.name = name
        self.brand = brand
        self.price = self.clean_price(price)
        self.store = store
    
    @staticmethod
    def clean_price(price_str: str) -> float:
        """Convierte precio a float."""
        try:
            cleaned = re.sub(r'[^\d,.]', '', price_str)
            cleaned = cleaned.replace('.', '').replace(',', '.')
            return float(cleaned) if cleaned else 0.0
        except:
            return 0.0
    
    def to_dict(self):
        return {
            'name': self.name,
            'brand': self.brand,
            'price': self.price,
            'store': self.store
        }
    
    def __str__(self):
        return f"{self.name} - {self.brand} - ${self.price:,.0f}"