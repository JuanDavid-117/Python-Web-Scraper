"""Generador de gráficos mejorado."""
import matplotlib.pyplot as plt
import pandas as pd

class ChartGenerator:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe
    
    def create_bar_chart(self, x: str, y: str, title: str, filename: str, 
                        rotation: int = 90, show: bool = False):
        """Crea gráfico de barras."""
        plt.figure(figsize=(14, 7))
        plt.bar(self.df[x], self.df[y], color='steelblue', edgecolor='black')
        plt.xlabel(x, fontsize=12)
        plt.ylabel(y, fontsize=12)
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xticks(rotation=rotation, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        
        if show:
            plt.show()
        else:
            plt.savefig(filename, dpi=200, bbox_inches='tight')
            plt.close()
            print(f"✓ Gráfico guardado: {filename}")
        
        return filename
    
    def create_pie_chart(self, column: str, title: str, filename: str, 
                        top_n: int = 10, show: bool = False):
        """Crea gráfico de torta."""
        plt.figure(figsize=(12, 8))
        value_counts = self.df[column].value_counts().head(top_n)
        
        colors = plt.cm.Set3(range(len(value_counts)))
        plt.pie(value_counts.values, labels=value_counts.index, 
                autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title(title, fontsize=14, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        
        if show:
            plt.show()
        else:
            plt.savefig(filename, dpi=200, bbox_inches='tight')
            plt.close()
            print(f"✓ Gráfico guardado: {filename}")
        
        return filename
    
    def create_horizontal_bar_chart(self, x: str, y: str, title: str, filename: str,
                                    show: bool = False):
        """Crea gráfico de barras horizontales."""
        plt.figure(figsize=(12, 8))
        plt.barh(self.df[x], self.df[y], color='coral', edgecolor='black')
        plt.xlabel(y, fontsize=12)
        plt.ylabel(x, fontsize=12)
        plt.title(title, fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3, axis='x')
        plt.tight_layout()
        
        if show:
            plt.show()
        else:
            plt.savefig(filename, dpi=200, bbox_inches='tight')
            plt.close()
            print(f"✓ Gráfico guardado: {filename}")
        
        return filename
    
    def create_comparison_chart(self, category_col: str, value_col: str, 
                               title: str, filename: str, show: bool = False):
        """Crea gráfico de comparación por categoría."""
        plt.figure(figsize=(14, 7))
        
        # Agrupar datos
        grouped = self.df.groupby(category_col)[value_col].mean().sort_values(ascending=False)
        
        plt.bar(grouped.index, grouped.values, color='seagreen', edgecolor='black')
        plt.xlabel(category_col, fontsize=12)
        plt.ylabel(f'Promedio de {value_col}', fontsize=12)
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        
        if show:
            plt.show()
        else:
            plt.savefig(filename, dpi=200, bbox_inches='tight')
            plt.close()
            print(f"✓ Gráfico guardado: {filename}")
        
        return filename
    
    @staticmethod
    def create_quick_chart(df: pd.DataFrame, x: str, y: str, title: str = None):
        """Crea y muestra un gráfico rápido (sin guardar)."""
        plt.figure(figsize=(12, 6))
        plt.bar(df[x], df[y])
        plt.xlabel(x)
        plt.ylabel(y)
        if title:
            plt.title(title)
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.tight_layout()
        plt.show()