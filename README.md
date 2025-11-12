# Python-Web-Scraper-System
Sistema de Web Scraping Utilizando Python - Proyecto Final de Programación Orientada a Objetos - UNAL

Permite extraer información de diferentes tipos de sitios web (por ejemplo, artículos estilo *wiki* y tiendas *retail* como MercadoLibre o Éxito), organizar los datos y generar reportes en distintos formatos.

El proyecto aplica conceptos de **Programación Orientada a Objetos (POO)** y utiliza librerías de scraping como `requests` y `BeautifulSoup`.

# 1. Introducción

En la actualidad, los portales web institucionales publican constantemente información relevante, como convocatorias, noticias, eventos académicos y oportunidades de investigación. Sin embargo, muchas veces los estudiantes y docentes no se enteran de estas actualizaciones a tiempo, lo que puede generar pérdida de oportunidades.
Este proyecto propone el desarrollo de una aplicación en Python, basada en el paradigma de Programación Orientada a Objetos (POO), que permita extraer información automáticamente desde la página web de la Universidad Nacional de Colombia, utilizando técnicas de Web Scraping.
El sistema busca recopilar, filtrar y organizar la información de interés, y en versiones futuras, incluso notificar al usuario mediante correo electrónico o mensajería interna.

## Objetivos específicos

Analizar la estructura HTML del portal web de la Universidad Nacional para identificar los elementos a extraer.

Implementar clases y métodos en Python utilizando las librerías Requests y BeautifulSoup.

Diseñar un modelo de clases que permita la extensibilidad del sistema, agregando nuevas fuentes o tipos de información.

Desarrollar funciones que organicen y muestren la información extraída de manera clara para el usuario.

(Opcional para versión avanzada) Implementar un sistema de notificaciones automáticas por correo electrónico o Slack cuando se detecten nuevas convocatorias o noticias.

## Características principales

- Extracción de texto desde sitios estilo **Wiki** (2 o 3 URLs).
- Extracción y organización de datos de **sitios retail** (ecommerce).
- Diseño modular con **clases**, **herencia** y **encapsulación**.
- Compatible con entornos virtuales.
  
## Instalación y ejecución

## Diagrama de Clases UML
```mermaid
classDiagram
   direction TB

   class Controller {
       +config: dict
       +run()
       +load_config(path:str)
       +orchestrate_scraping()
   }

   class BaseScraper {
       +headers: dict
       +get_soup(url:str) BeautifulSoup
       +fetch_html(url:str) str
       +safe_request(url:str, retry:int=2) str
   }

   class UniversityScraper {
       +news_parser: NewsParser
       +program_parser: ProgramParser
       +event_parser: EventParser
       +wiki_scraper: WikiScraper
       +scrape_news_list(source_url:str) List[Article]
       +scrape_article(url:str) Article
       +scrape_programs(url:str) List[Program]
       +scrape_events(url:str) List[Event]
       +scrape_wiki_intro(url:str) str
   }

   class NewsParser {
       +source_name: str
       +parse_list_page(soup:BeautifulSoup) List[dict]
       +parse_article_page(soup:BeautifulSoup) dict
       -_extract_date(text:str) datetime
       -_extract_tags(soup) List[str]
   }

   class ProgramParser {
       +parse_programs(soup:BeautifulSoup) List[dict]
       -_normalize_location(text:str) str
   }

   class EventParser {
       +parse_events(soup:BeautifulSoup) List[dict]
       -_parse_dates(text:str) (date,date)
   }

   class WikiScraper {
       +scrape_intro(url:str) str
       +scrape_sections(url:str, selectors:List[str]) dict
   }

   class Article {
       +title: str
       +lead: str
       +author: str
       +date: datetime
       +section: str
       +tags: List[str]
       +url: str
       +text: str
       +scrape_date: datetime
   }

   class Program {
       +program_name: str
       +level: str
       +sede: str
       +faculty: str
       +snies: str
       +modalidad: str
       +url: str
   }

   class Event {
       +title: str
       +date_start: date
       +date_end: date
       +location: str
       +organizer: str
       +registration_url: str
       +description: str
   }

   class Storage {
       +save_list_of_dicts(data:List[dict], path:str)
       +read_csv(path:str) DataFrame
       +save_sqlite(table_name:str, data:List[dict])
   }

   class CSVStorage {
       +filepath: str
       +save_list_of_dicts(data, columns)
       +read_csv(path)
   }

   class ReportGenerator {
       +out_path: str
       +add_title(text:str)
       +add_paragraph(text:str)
       +add_table_from_csv(csv_path:str, max_rows:int)
       +add_plot_from_csv(csv_path:str, x_col:str, y_col:str)
       +save()
   }

   class Scheduler {
       +add_job(func, cron_expr:str)
       +run_pending()
   }

   class Notifier {
       +send_email(subject:str, body:str, to:list)
       +send_slack(message:str, channel:str)
   }

   Controller --> UniversityScraper : uses
   Controller --> CSVStorage : uses
   Controller --> ReportGenerator : uses
   Controller --> Scheduler : uses
   Controller --> Notifier : uses

   BaseScraper <|-- UniversityScraper
   UniversityScraper --> NewsParser : uses
   UniversityScraper --> ProgramParser : uses
   UniversityScraper --> EventParser : uses
   UniversityScraper --> WikiScraper : uses

   NewsParser --> Article : creates
   ProgramParser --> Program : creates
   EventParser --> Event : creates

   Storage <|-- CSVStorage
   Controller --> Storage : may use
   Scheduler --> Controller : triggers
   Notifier <-- Controller : optional future use

````

## Autores
Proyecto desarrollado por:
- Juan David Moreno Martin
- Yulieth Alexandra Morales Soler
- Roniel David Castro Navarro

**Curso:** Programación Orientada a Objetos  

**Profesor:** Felipe Gonzalez Roldan

**Universidad:** Universidad Nacional de Colombia - Sede Bogota

## Por Implementar
- Agregar soporte para más tipos de sitios (blogs, noticias, etc.)
- Implementar interfaz gráfica (Tkinter o PyQt)
- Añadir hilos (multithreading) para acelerar el scraping
- Contenedor Docker para despliegue
