from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import logging
from dotenv import load_dotenv, dotenv_values
from datetime import datetime


load_dotenv()
logger = logging.getLogger('selenium')
log_path = 'C:/Users/Admin/Desktop/Selenium/logger.log'
handler = logging.FileHandler(log_path)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

## Data Picker
##============================================
data = datetime.today()
data_do_dia = data.strftime("%d/%m/%Y")
mes_ano = data.strftime("%m/%Y")
data_inicio_mes = f"01/{mes_ano}"
##============================================

driver = webdriver.Chrome() 
driver.get("https://evs-admin.tenda.com/Login")

wait = WebDriverWait(driver, 15)

## LOGIN NA TENDA
try:
    entrada_usuario = driver.find_element(By.ID,"Username")
    entrada_usuario.send_keys(f"{os.getenv("login")}")
    entrada_senha = driver.find_element(By.ID,"Password")
    entrada_senha.send_keys(f"{os.getenv("password")}")
    entrada_senha.send_keys(Keys.ENTER)
    print("Login realizado com sucesso")

except Exception as error:
    print(f"Erro Desconhecido, contate o suporte.")
###

driver.get("https://evs-admin.tenda.com/prepropostaaguardandoanalise")


## Seletor Data de Ultimo Envio
try:
    ## DE
    time.sleep(0.5)
    campo_data_ate = driver.find_element(By.XPATH, "//*[@id='DataUltimoEnvioDe']").send_keys(f"{data_inicio_mes}")
    driver.execute_script(f'document.getElementById("DataUltimoEnvioDe").value ="{data_inicio_mes}"')


    ## ATÉ
    time.sleep(0.5)
    campo_data_ate = driver.find_element(By.XPATH, "//*[@id='DataUltimoEnvioAte']").send_keys(f"{data_do_dia}")
    driver.execute_script(f'document.getElementById("DataUltimoEnvioAte").value ="{data_do_dia}"')

    ##

except Exception as error:
    print(f"Erro Desconhecido, contate o suporte.")

## SELETOR DE FILTRO

seletor_de_filtro = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='filtro']/div[1]/div[5]/span/span[1]/span/ul/li[6]/input")))

seletor_de_filtro = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='filtro']/div[1]/div[5]/span/span[1]/span/ul/li[6]/input")))

seletor_de_filtro.click()
seletor_de_filtro.send_keys("Em Análise Simplificada")
seletor_de_filtro.send_keys(Keys.ENTER)
##

## FILTRADOR

while True:
    botao_filtrar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='block_content_page']/div[4]/div/div/button[1]")))
    botao_filtrar.click()
    botao_filtrar = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='block_content_page']/div[4]/div/div/button[1]")))
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    
    
    
    
    
    
    
        
driver.quit()