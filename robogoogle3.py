from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pesquisa = input("Digite a pesquisa:")

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://www.google.com")

campo = driver.find_element(By.XPATH, "//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element(By.XPATH, "//*[@id='result-stats']").text
print(resultados)

numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace('.',''))
maximo_paginas = numero_resultados/10

print("Número de páginas: %s"% (maximo_paginas))