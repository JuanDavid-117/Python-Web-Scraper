from imports import *
from scraper import WebScraper

if __name__ == "__main__": #marcador de posición
    scraper = WebScraper("https://bienestar.bogota.unal.edu.co/eventos.php")
    titulos = scraper.extract_titles()
    parrafos = scraper.extract_paragraphs()
