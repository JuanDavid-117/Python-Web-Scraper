"""Generador de gráficos simple."""
import matplotlib.pyplot as plt
import pandas as pd

class ChartGenerator:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def create_bar_chart(self, x: str, y: str, title: str, filename: str):
        """Crea gráfico de barras."""
        plt.figure(figsize=(12, 6))
        plt.bar(self.df[x], self.df[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.close()
        print(f"Gráfico guardado: {filename}")
        return filename
    
    def create_pie_chart(self, column: str, title: str, filename: str):
        """Crea gráfico de torta."""
        plt.figure(figsize=(10, 8))
        value_counts = self.df[column].value_counts()
        plt.pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
        plt.title(title)
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
        plt.close()
        print(f"Gráfico guardado: {filename}")
        return filename