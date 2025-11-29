import requests # para hacer peticiones HTTP SIN abrir un navegador real
from bs4 import BeautifulSoup # es para parsear HTML (limpiarlo, leerlo, buscar elementos).
from datetime import datetime, date #Para manejar fechas
from typing import List #Sirve para dar tipos en Python:
from selenium import webdriver #Esto inicializa el navegador (Chrome, Firefox, etc.).
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
