"""Generador de reportes."""
import pandas as pd
import json
from datetime import datetime
from .data_processor import DataProcessor

class ReportGenerator:
    def __init__(self, data: list, filename: str, data_type: str):
        self.data = data
        self.filename = filename
        self.data_type = data_type
        self.processor = DataProcessor(data, data_type)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def generate_csv(self):
        """Genera CSV."""
        df = self.processor.get_dataframe()
        filepath = f"{self.filename}_{self.timestamp}.csv"
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        print(f"CSV generado: {filepath}")
        return filepath
    
    def generate_excel(self):
        """Genera Excel con múltiples hojas."""
        df = self.processor.get_dataframe()
        stats = self.processor.get_statistics()
        filepath = f"{self.filename}_{self.timestamp}.xlsx"
        
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Datos', index=False)
            pd.DataFrame([stats]).to_excel(writer, sheet_name='Estadísticas', index=False)
            
            # Si son productos, agregar top 10
            if self.data_type == 'product' and len(df) > 0:
                top_10 = df.nlargest(10, 'price')
                top_10.to_excel(writer, sheet_name='Top 10 Caros', index=False)
                
                bottom_10 = df.nsmallest(10, 'price')
                bottom_10.to_excel(writer, sheet_name='Top 10 Baratos', index=False)
        
        print(f"Excel generado: {filepath}")
        return filepath
    
    def generate_json(self):
        """Genera JSON."""
        df = self.processor.get_dataframe()
        stats = self.processor.get_statistics()
        filepath = f"{self.filename}_{self.timestamp}.json"
        
        report = {
            'metadata': {
                'fecha': self.timestamp,
                'tipo': self.data_type,
                'total_registros': len(df)
            },
            'estadisticas': stats,
            'datos': df.to_dict(orient='records')
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"JSON generado: {filepath}")
        return filepath
    
    def generate_html(self):
        """Genera HTML con estilos."""
        df = self.processor.get_dataframe()
        stats = self.processor.get_statistics()
        filepath = f"{self.filename}_{self.timestamp}.html"
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Reporte - {self.filename}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        .stats {{ background: #ecf0f1; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .stats h2 {{ color: #2c3e50; margin-top: 0; }}
        .stat-item {{ padding: 8px 0; border-bottom: 1px solid #bdc3c7; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th {{ background: #3498db; color: white; padding: 12px; text-align: left; }}
        td {{ padding: 10px; border-bottom: 1px solid #ecf0f1; }}
        tr:hover {{ background: #f8f9fa; }}
        .footer {{ margin-top: 30px; text-align: center; color: #7f8c8d; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Reporte de Web Scraping</h1>
        <p><strong>Generado:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><strong>Archivo:</strong> {self.filename}</p>
        
        <div class="stats">
            <h2>📈 Estadísticas</h2>
            {''.join([f'<div class="stat-item"><strong>{k}:</strong> {v}</div>' for k, v in stats.items()])}
        </div>
        
        <h2>📋 Datos</h2>
        {df.to_html(index=False, classes='data-table', border=0)}
        
        <div class="footer">
            <p>Generado automáticamente por Web Scraper System</p>
        </div>
    </div>
</body>
</html>
        """
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"HTML generado: {filepath}")
        return filepath
    
    def generate_full_report(self, formats=['csv', 'excel'], with_charts=False):
        """Genera reportes en múltiples formatos."""
        self.processor.clean_data()
        files = {}
        
        if 'csv' in formats:
            files['csv'] = self.generate_csv()
        if 'excel' in formats:
            files['excel'] = self.generate_excel()
        if 'json' in formats:
            files['json'] = self.generate_json()
        if 'html' in formats:
            files['html'] = self.generate_html()
        
        # Generar gráficos si se solicita
        if with_charts and self.data_type == 'product':
            chart_files = self._generate_charts()
            files.update(chart_files)
        
        return files
    
    def _generate_charts(self):
        """Genera gráficos para productos."""
        from .chart_generator import ChartGenerator
        
        df = self.processor.get_dataframe()
        if len(df) == 0:
            return {}
        
        chart_files = {}
        
        try:
            # Gráfico de precios (top 15)
            if 'price' in df.columns and 'name' in df.columns:
                top_15 = df.nlargest(15, 'price')
                chart_gen = ChartGenerator(top_15)
                filename = f"{self.filename}_precios_{self.timestamp}.png"
                chart_gen.create_bar_chart('name', 'price', 'Top 15 Productos Más Caros', filename)
                chart_files['chart_prices'] = filename
            
            # Gráfico de marcas
            if 'brand' in df.columns:
                chart_gen = ChartGenerator(df)
                filename = f"{self.filename}_marcas_{self.timestamp}.png"
                chart_gen.create_pie_chart('brand', 'Distribución por Marca', filename)
                chart_files['chart_brands'] = filename
                
        except Exception as e:
            print(f"Error generando gráficos: {e}")
        
        return chart_files