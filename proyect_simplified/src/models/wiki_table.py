"""Modelo de tabla wiki."""
import pandas as pd

class WikiTable:
    def __init__(self, table_id: int, headers: list, rows: list):
        self.table_id = table_id
        self.headers = headers
        self.rows = rows
        self.dataframe = pd.DataFrame(rows, columns=headers)
    
    def to_dataframe(self):
        return self.dataframe
    
    def __str__(self):
        return f"WikiTable(id={self.table_id}, rows={len(self.rows)})"