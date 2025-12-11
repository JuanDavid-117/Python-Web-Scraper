"""Procesador de datos."""
import pandas as pd
import re

class DataProcessor:
    def __init__(self, data: list, data_type: str):
        self.data = data
        self.data_type = data_type
        self.df = self._create_dataframe()
    
    def _create_dataframe(self):
        """Crea DataFrame."""
        if not self.data:
            return pd.DataFrame()
        
        if self.data_type == 'product':
            return pd.DataFrame([p.to_dict() for p in self.data])
        elif self.data_type == 'wiki':
            dfs = [t.to_dataframe() for t in self.data]
            return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
    
    def clean_data(self):
        """Limpia datos."""
        if self.data_type == 'product':
            # Limpiar precios (ya se hace en el modelo, pero por si acaso)
            if 'price' in self.df.columns:
                self.df = self.df[self.df['price'] > 0]
            
            # Rellenar valores faltantes
            self.df['brand'].fillna('Desconocido', inplace=True)
            self.df['store'].fillna('Desconocido', inplace=True)
            
            # Eliminar duplicados
            self.df.drop_duplicates(subset=['name', 'brand'], inplace=True)
            
            print(f"Datos limpios: {len(self.df)} productos")
        
        return self.df
    
    def sort_by_price(self, ascending: bool = True):
        """Ordena por precio (min a max o max a min)."""
        if 'price' in self.df.columns:
            self.df.sort_values(by='price', ascending=ascending, inplace=True)
            order = "menor a mayor" if ascending else "mayor a menor"
            print(f"Datos ordenados por precio ({order})")
        return self.df
    
    def sort_by_column(self, column: str, ascending: bool = True):
        """Ordena por cualquier columna."""
        if column in self.df.columns:
            self.df.sort_values(by=column, ascending=ascending, inplace=True)
            print(f"Datos ordenados por '{column}'")
        return self.df
    
    def filter_by_price_range(self, min_price: float = 0, max_price: float = float('inf')):
        """Filtra por rango de precio."""
        if 'price' in self.df.columns:
            original_count = len(self.df)
            self.df = self.df[
                (self.df['price'] >= min_price) & 
                (self.df['price'] <= max_price)
            ]
            print(f"Filtrado: {len(self.df)} de {original_count} productos en rango ${min_price:,.0f} - ${max_price:,.0f}")
        return self.df
    
    def filter_by_brand(self, brands: list):
        """Filtra por marcas."""
        if 'brand' in self.df.columns:
            original_count = len(self.df)
            self.df = self.df[self.df['brand'].isin(brands)]
            print(f"Filtrado: {len(self.df)} de {original_count} productos de marcas: {', '.join(brands)}")
        return self.df
    
    def get_top_n(self, n: int = 10, column: str = 'price', ascending: bool = False):
        """Obtiene top N registros."""
        if column in self.df.columns:
            return self.df.nlargest(n, column) if not ascending else self.df.nsmallest(n, column)
        return self.df.head(n)
    
    def get_dataframe(self):
        """Retorna DataFrame."""
        return self.df
    
    def get_statistics(self):
        """Estadísticas descriptivas."""
        if self.data_type == 'product' and len(self.df) > 0:
            return {
                'total': len(self.df),
                'precio_promedio': round(self.df['price'].mean(), 2),
                'precio_min': round(self.df['price'].min(), 2),
                'precio_max': round(self.df['price'].max(), 2),
                'precio_mediana': round(self.df['price'].median(), 2),
                'marcas_unicas': self.df['brand'].nunique(),
                'tiendas': self.df['store'].unique().tolist()
            }
        return {'total': len(self.df)}
    
    def export_to_csv(self, filename: str):
        """Exporta a CSV."""
        self.df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Exportado a: {filename}")
    
    def get_brand_statistics(self):
        """Estadísticas por marca."""
        if 'brand' in self.df.columns and 'price' in self.df.columns:
            brand_stats = self.df.groupby('brand').agg({
                'price': ['count', 'mean', 'min', 'max']
            }).round(2)
            brand_stats.columns = ['cantidad', 'precio_promedio', 'precio_min', 'precio_max']
            return brand_stats.sort_values('cantidad', ascending=False)
        return None