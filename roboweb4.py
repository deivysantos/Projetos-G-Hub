from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import time
import xlrd

workbook = xlrd.open_workbook('C:/Users/deivy/OneDrive/Área de Trabalho/Python/excelpython.xls')
sheet = workbook.sheet_by_name('Plan1')
linhas = sheet.nlinhas
colunas = sheet.ncols

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://registro.br/")


for curr_linhas in range(0, linhas):
    x = sheet.cell_value(curr_linhas, 0)
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    print("Domínio %s %s" %(x, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text))


driver.close()