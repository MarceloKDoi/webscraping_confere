from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# caminho do driver
driver = webdriver.Chrome(
    executable_path=r"C:\Users\Marcelo\workspaces\python\web_driver\chromedriver.exe")

driver.get("https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm")


sleep(2)

# aceita cookies

driver.find_element_by_id(
    'onetrust-accept-btn-handler').click()


driver.implicitly_wait(2)

# Dicionario

dic = {
    'data': "2021/09/30",
    'ativo_mobilizado': 702228000,
    'ativo_total': 924465000,
    'patrimonio_liquido': 309753000,
    'patrimonio_particular_atribuido_a_controladora': 306252
}

print(dic)

# insere texto para busca

sleep(3)

driver.find_element_by_xpath(
    '/html/body/app-root/app-companies-home/div/div/div/div/div[1]/div[2]/div/app-companies-home-filter-name/form/div/div[1]/input').send_keys('petrobras')
driver.find_element_by_xpath(
    '/html/body/app-root/app-companies-home/div/div/div/div/div[1]/div[2]/div/app-companies-home-filter-name/form/div/div[1]/input').send_keys(Keys.ENTER)

driver.find_element(
    By.CSS_SELECTOR, ".form-group:nth-child(3) > .btn-primary").click()

sleep(3)

driver.find_element(By.CSS_SELECTOR, ".card-text").click()

sleep(2)

driver.find_element(
    By.CSS_SELECTOR, "#accordionHeading h6").click()


# Extração de dados

sleep(2)


page_content = driver.page_source
site = BeautifulSoup(page_content, 'html.parser')
print(site.prettify())

valor_campo = site.find('td', attrs={'class': 'text-right'})
print(valor_campo)
