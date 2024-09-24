from time import sleep
import pandas as pd

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

listaRelevantes     = []
listaMenorPreco     = []
listaMelhorAvaliado = []

driver = webdriver.Chrome()
driver.get('https://www.zoom.com.br/')

sleep(2)
input = driver.find_element(By.CLASS_NAME, "AutoCompleteStyle_input__WAC2Y")
input.send_keys("Notebook")
input.send_keys(Keys.ENTER)

sleep(2)
filtro = driver.find_element(By.CLASS_NAME, "Select_SelectWrapper__a_ry1")
filtro.click()

sleep(2)
# seleciona mais relevante
opcao = filtro.find_element(By.XPATH, '//option[@value="lowering_percentage_desc"]')
opcao.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaRelevantes.append(titulo.text)

sleep(2)
driver.execute_script("window.scrollBy(0, 3500);")
sleep(3)
ul = driver.find_element(By.CLASS_NAME, "Paginator_paginator__Jmw5q")
li = ul.find_element(By.XPATH, './/li[@data-testid="page-2"]')
li.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaRelevantes.append(titulo.text)

driver.execute_script("window.scrollBy(0, 3200);")
sleep(3)
ul = driver.find_element(By.CLASS_NAME, "Paginator_paginator__Jmw5q")
li = ul.find_element(By.XPATH, './/li[@data-testid="page-3"]')
li.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaRelevantes.append(titulo.text)


# --------------------------------

sleep(2)
filtro = driver.find_element(By.CLASS_NAME, "Select_SelectWrapper__a_ry1")
opcao = filtro.find_element(By.XPATH, '//option[@value="price_asc"]')
opcao.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaMenorPreco.append(titulo.text)

sleep(2)
driver.execute_script("window.scrollBy(0, 3000);")
sleep(3)
ul = driver.find_element(By.CLASS_NAME, "Paginator_paginator__Jmw5q")
li = ul.find_element(By.XPATH, './/li[@data-testid="page-2"]')
li.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaMenorPreco.append(titulo.text)

driver.execute_script("window.scrollBy(0, 3200);")
sleep(3)
ul = driver.find_element(By.CLASS_NAME, "Paginator_paginator__Jmw5q")
li = ul.find_element(By.XPATH, './/li[@data-testid="page-1"]')
li.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaMenorPreco.append(titulo.text)


# ----------------------------------

sleep(2)
filtro = driver.find_element(By.CLASS_NAME, "Select_SelectWrapper__a_ry1")
filtro.click()

sleep(2)
# seleciona mais relevante
opcao = filtro.find_element(By.XPATH, '//option[@value="rating_desc"]')
opcao.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaMelhorAvaliado.append(titulo.text)

sleep(2)
driver.execute_script("window.scrollBy(0, 3500);")
sleep(3)
ul = driver.find_element(By.CLASS_NAME, "Paginator_paginator__Jmw5q")
li = ul.find_element(By.XPATH, './/li[@data-testid="page-2"]')
li.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaMelhorAvaliado.append(titulo.text)

driver.execute_script("window.scrollBy(0, 3200);")
sleep(3)
ul = driver.find_element(By.CLASS_NAME, "Paginator_paginator__Jmw5q")
li = ul.find_element(By.XPATH, './/li[@data-testid="page-3"]')
li.click()

sleep(2)
divPai = driver.find_elements(By.CLASS_NAME, 'Hits_ProductCard__Bonl_')

sleep(2)
for filhos in divPai:
    titulo = filhos.find_element(By.TAG_NAME, 'h2')
    listaMelhorAvaliado.append(titulo.text)


df1 = pd.DataFrame(listaMelhorAvaliado, columns=['item'])
df2 = pd.DataFrame(listaMenorPreco, columns=['item'])
df3 = pd.DataFrame(listaRelevantes, columns=['item'])

itensIguais = pd.merge(pd.merge(df1, df2, on='item'), df3, on='item')

print(itensIguais)

sleep(10000)
driver.close()