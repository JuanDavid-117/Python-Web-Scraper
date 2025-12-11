# SISTEMA DE WEB SCRAPING EN PYTHON
**Proyecto Final – Programación Orientada a Objetos – Universidad Nacional de Colombia**

**Autores:**
* Juan David Moreno Martin

* Yulieth Alexandra Morales Soler

* Roniel David Castro Navarro

# Tabla de Contenido
- [Descripción](#Descripción-general)
- [Características](#Características)
- [Herramientas](#Herramientas-usadas)

# Descripción general

Este proyecto implementa un sistema completo de web scraping desarrollado en python, capaz de extraer, procesar y analizar información proveniente de páginas web tanto **estaticas** como **dinámicas**.

El sistema integra herramientas modernas como `Request`, `BeautifulSoup`, `Playwright`, `Pandas`, `Matplotlib`, y librerias para generación de reportes y envio de correos.

Su objetivo es automaizar la recolección de datos, generar analisís utiles y permitir la creación de reportes y alertas personalizadas.

# Características

- **Scraping de múltiples sitios web de mercado**  
  El sistema extrae información desde varias páginas (como precios, productos, descripciones y enlaces).

- **Procesamiento y limpieza de datos**  
  Los datos recolectados se organizan, filtran y normalizan antes de generar la salida final.

- **Exportación automática de resultados**  
  Los datos pueden ser exportados en formatos como CSV o Excel.

- **Envío de información por correo electrónico**  
  El sistema tambien envía automáticamente los archivos generados al correo configurado por el usuario (utilizando contraseña de aplicación).

- **Configuración sencilla mediante archivo de parámetros**  
  URLs, correos y formatos de salida se definen fácilmente en un archivo de configuración.

- **Automatización completa del proceso**  
  El flujo completo —*scraping → procesamiento → exportación → envío*— se ejecuta sin intervención manual.

 # Herramientas usadas

### **Librerías**
- **Playwright (`playwright.sync_api`)**  
  Ha sido utilizada para automatizar el navegador (Chromium). Permite abrir páginas, interactuar con elementos, scrollear y extraer contenido dinámico.

- **Pandas (`pandas`)**  
  Usada para almacenar los datos recolectados en DataFrames y exportarlos como archivos CSV o Excel.

- **Time (`time`)**  
  Empleada para agregar pausas controladas (`sleep`) que aseguran que el contenido de la página cargue correctamente durante el scraping.

---

### **Conceptos de Programación**
- **Programación Orientada a Objetos (POO)**  
  El scraper está estructurado mediante clases y métodos, proporcionando modularidad y una mejor organización del código.

- **Web Scraping Dinámico**  
  Extracción de información desde páginas que cargan elementos mediante JavaScript, utilizando selectores CSS y la API de Playwright.

- **Control de Flujo**  
  Uso de ciclos y condicionales para manejar paginación, botones de “Cargar más” y lógica repetitiva del scraping.

- **Manejo de Archivos**  
  Generación de archivos CSV/XLSX con los datos obtenidos durante la ejecución.

# Instalacion

### 1. Abrir el proyecto en VSCode
```bash
cd Python-Web-Scraper
```

### 2. Crear entorno virtual (Opcional)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Instalar navegadores de Playwright
```bash
playwright install
# Si no funciona:
python -m playwright install
```




