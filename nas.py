from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configura el controlador de Chrome
driver_path = "/path/to/chromedriver"  # reemplaza con la ruta a tu controlador de Chrome
driver = webdriver.Chrome(driver_path)

# Abre Google y realiza una búsqueda
driver.get("https://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

# Espera unos segundos antes de cerrar el navegador
time.sleep(5)

# Cierra el navegador
driver.quit()
