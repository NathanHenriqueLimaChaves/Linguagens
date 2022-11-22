from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class pesquisa_automatica():
    def __init__(self):
        self.input_da_pesquisa()
        self.executando_varredura_na_web()

    def input_da_pesquisa(self):
        pesquisa = input("O que deseja pesquisar? ")
        if (pesquisa != ''):
            pesquisa = pesquisa.replace(' ', '+')
            self.pesquisa = pesquisa
            return self.pesquisa
        else:
            self.input_da_pesquisa()

    def executando_varredura_na_web(self):
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        navegador.get("https://www.google.com/")
        navegador.maximize_window()
        self.pesquisa
        navegador.find_element(
            "xpath", '/ html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(self.pesquisa)
        navegador.find_element(
            "xpath", '/ html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
        navegador.find_element(
            "xpath", '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        resultados = navegador.find_elements(By.CLASS_NAME, 'SoaBEf')
        for resultado in resultados:
            print(resultado)
            resultado.click()

        time.sleep(10000)


pesquisa_automatica()
