
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
from Excel import Excel
from openpyxl.workbook import Workbook



class Scraping():
    def __init__(self, save, nome_arquivo, tipo):#, save, nome_arquivo
        self.site = r"https://projetosemds.com.br/jpedro/produtos.html"
        self.map = {
            "nome": {
                "xpath": "/html/body/main/div/div/div[2]/div[$nome$]/p[1]"
            },
            "valor": {
                "xpath": "/html/body/main/div/div/div[2]/div[$valor$]/p[2]"
            },
        }
        self.tipo = tipo
        self.save = save
        self.nome_arquivo = nome_arquivo
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Edge(options=options)#options=options
        self.varrer_site()
        self.driver.close()
    

    def varrer_site(self):
        self.driver.get(self.site)
        nome_lista=[]
        fabricante_lista=[]
        valor_lista=[]
        i = 0
        while True:
            i += 1
            try:
                n = self.driver.find_element(By.XPATH, self.map["nome"]["xpath"].replace("$nome$", f"{i}")).text
                nome = n.split("'")[0]
                fabricante = n.split("'")[1]
                v = self.driver.find_element(By.XPATH, self.map["valor"]["xpath"].replace("$valor$", f"{i}")).text
                valor = v.split(" ")[1].replace(",", ".")
                nome_lista.append(nome)
                fabricante_lista.append(fabricante)
                valor_lista.append(valor)
            except:
                break
        
        quantidade, val_med, val_max, nome_max, val_min, nome_min = Excel().dashboard(valor_lista, nome_lista)
        dados = Excel().tabela(nome_lista, fabricante_lista, valor_lista)
        dash = Excel().tabela_dash(quantidade, val_med, val_max, nome_max, val_min, nome_min)
        Excel().salvar_arquivos(self.tipo, self.save,self.nome_arquivo, dados, dash)
        


#/html/body/main/div/div/div[2]/div[1]/p[1]
#/html/body/main/div/div/div[2]/div[4]/p[1]

#/html/body/main/div/div/div[2]/div[1]/p[2]
#/html/body/main/div/div/div[2]/div[9]/p[2]