"""Procesador de datos."""
import pandas as pd

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
            self.df = self.df[self.df['price'] > 0]
            self.df['brand'].fillna('Desconocido', inplace=True)
        return self.df
    
    def get_dataframe(self):
        return self.df
    
    def get_statistics(self):
        """Estadísticas básicas."""
        if self.data_type == 'product':
            return {
                'total': len(self.df),
                'precio_promedio': self.df['price'].mean(),
                'precio_min': self.df['price'].min(),
                'precio_max': self.df['price'].max()
            }
        return {'total': len(self.df)}