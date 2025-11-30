from driver import get_driver
from selenium.webdriver.common.by import By
import time

# -----------------------------
#  SCRAPERS DE CADA PÁGINA (en construcción)
# -----------------------------

def scrape_unal(driver):
    print("\n=== SCRAPING: unal.edu.co ===")

    driver.get("https://unal.edu.co/")

    time.sleep(2)  # mientras luego lo reemplazan por WebDriverWait

    # Ejemplo: extraer titulares
    titles = driver.find_elements(By.CSS_SELECTOR, ".item > h3")
    for t in titles:
        print("-", t.text)


def scrape_bienestar_eventos(driver):
    print("\n=== SCRAPING: bienestar.bogota.unal.edu.co/eventos ===")

    driver.get("https://bienestar.bogota.unal.edu.co/eventos.php")

    time.sleep(2)

    eventos = driver.find_elements(By.CSS_SELECTOR, ".card-title")
    for e in eventos:
        print("-", e.text)


# -----------------------------
#  SUB-MENÚ POR CADA SITIO
# -----------------------------

def menu_unal(driver):
    while True:
        print("\n--- Menú UNAL ---")
        print("1. Extraer noticias")
        print("2. Extraer otra cosa")
        print("0. Volver")
        op = input("Elige: ")

        if op == "1":
            scrape_unal(driver)
        elif op == "2":
            print("Aquí metes otra función...")
        elif op == "0":
            break
        else:
            print("Opción inválida, bro.")


def menu_bienestar(driver):
    while True:
        print("\n--- Menú Bienestar ---")
        print("1. Extraer eventos")
        print("2. Otra extracción")
        print("0. Volver")
        op = input("Elige: ")

        if op == "1":
            scrape_bienestar_eventos(driver)
        elif op == "2":
            print("Aquí metes otra función…")
        elif op == "0":
            break
        else:
            print("Opción inválida, my friend.")


# -----------------------------
#  MENÚ PRINCIPAL
# -----------------------------

def main():
    driver = get_driver()

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Eventos")
        print("2. Programas")
        print("3. Articulos")
        print("4. Eventos")
        print("0. Salir")
        
        op = input("Elige: ")

        if op == "1":
            menu_unal(driver)
        elif op == "2":
            menu_bienestar(driver)
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

    driver.quit()


if __name__ == "__main__":
    main()
