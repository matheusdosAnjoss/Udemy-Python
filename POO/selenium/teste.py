from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Inicializa o navegador (Chrome)
driver = webdriver.Chrome()

try:
    # 2. Abre a página do Google
    driver.get("https://www.google.com")
    time.sleep(3)
    
    # 3. Encontra a barra de pesquisa pelo atributo 'name'
    barra_pesquisa = driver.find_element(By.NAME, "q")
    
    # 4. Digita o que queremos buscar e pressiona a tecla ENTER
    barra_pesquisa.send_keys("Gemini")
    barra_pesquisa.send_keys(Keys.ENTER)
    
    # Espera 5 segundos para podermos ver o resultado
    time.sleep(5)

finally:
    # 5. Fecha o navegador de forma segura
    driver.quit()