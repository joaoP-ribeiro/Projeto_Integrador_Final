import statistics
import pandas as pd


class Excel():
    def __init__(self):
        self.valor_max = []
        self.valor_min = []
        self.valor_med = []
        self.nome_max = []
        self.nome_min = []
        self.quantidade = []

    
    def dashboard(self, lista_valores, lista_nomes):
        self.quantidade.append(len(lista_valores)) 
        lista_convertida = []
        for i in lista_valores:
          if i.count(".") >= 2:
            novo_n= i.replace(".", "", 1)
            lista_convertida.append(float(novo_n))
          else:
            lista_convertida.append(float(i))
        self.valor_med.append(statistics.mean(lista_convertida))
        self.valor_max.append(max(lista_convertida))
        self.nome_max.append(lista_nomes[lista_convertida.index(self.valor_max[0])])
        self.valor_min.append(min(lista_convertida))
        self.nome_min.append(lista_nomes[lista_convertida.index(self.valor_min[0])])
        
        return self.quantidade, self.valor_med, self.valor_max, self.nome_max, self.valor_min, self.nome_min


    def tabela(self, nome, fabricante, valor):
        colunas = {"Nome": nome, "Fabricante": fabricante, "Valor": valor}
        dados = pd.DataFrame(data=colunas)
        return dados
    
    def tabela_dash(self, quantidade, val_med, val_max, nome_max, val_min, nome_min):
        colunas = {"Quantidade Produtos": quantidade, "Valor Medio": val_med, "Nome Max": nome_max, "Valor Max": val_max, "Nome Min": nome_min, "Valor Min": val_min}
        dados_2 = pd.DataFrame(data=colunas)
        return dados_2
 
    def salvar_arquivos(self, tipo, save ,nome_arquivo, dados, dash):
        if tipo =="csv":
            dados.to_csv(f"{save}{nome_arquivo}.csv", sep=";", index = False)
            dash.to_csv(f"{save}dash_{nome_arquivo}.csv", sep=";", index = False)
        elif tipo =="csv_xlsx":
            dados.to_excel(f"{save}{nome_arquivo}.xlsx", index = False)
            dash.to_csv(f"{save}dash_{nome_arquivo}.csv", sep=";", index = False)
            dados.to_csv(f"{save}{nome_arquivo}.csv", sep=";", index = False)

   #"Nome P.Max": self.nome_max, "Valor P.Max": self.valor_max, "Nome P.Min": self.nome_min, "Valor P.Min": self.valor_min