from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get("https://wordpress.com/log-in/pt-br?redirect_to=https%3A%2F%2Fwordpress.com%2F")
    driver.implicitly_wait(2) 

    email_login = driver.find_element(By.XPATH, '//*[@id="usernameOrEmail"]')
    email_login.send_keys("joaopedroramoscarneiroo22@gmail.com")

    btn_login = driver.find_element(By.XPATH, '//*[@id="primary"]/div/main/div[3]/div/form/div[1]/div[2]/button')
    btn_login.click()

    senha_login = driver.find_element(By.XPATH, '//*[@id="password"]')
    senha_login.send_keys("Joao32141783")
    
    btn_login = driver.find_element(By.XPATH, '//*[@id="primary"]/div/main/div[3]/div/form/div[1]/div[2]/button')
    btn_login.click()

    driver.get("https://prozds2.wordpress.com/")
    driver.implicitly_wait(2) 

    link_pagina = driver.find_element(By.LINK_TEXT, "The City That Never Sleeps")
    link_pagina.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comentario = driver.find_element(By.XPATH, '//*[@id="comment"]')
    comentario.send_keys("AAAAAAAAAAAAAAAAAA")
    comentario.send_keys(Keys.RETURN)

    print("Teste Passou! Comentário postado.")
except Exception as e:
    print(f"Teste Falhou! Não foi possível postar o comentário. Erro: {str(e)}")

finally:
    driver.quit()