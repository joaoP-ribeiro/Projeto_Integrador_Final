from time import sleep
from tkinter import *
from tkinter import ttk
import tkinter as tk

from Scraping import Scraping


tela = Tk()

class Tela():
    def __init__(self):
        self.tela = tela
        self.interface()
        self.frame()
        self.label()
        self.botao()
        self.save()
        self.entry()
        tela.mainloop()
    
    def interface(self):
        self.tela.title("Raspando Site")
        self.tela.configure(background="#FFFFFF")
        self.tela.geometry("500x300")
        self.tela.resizable(True, True)
        self.tela.maxsize(width=500, height=300)
        self.tela.minsize(width=500, height=300)
    
    def frame(self):
        bg = "#c7c7c7"
        self.frame_0 = Frame(self.tela, bg=bg)
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.94)

    def label(self):
        self.lbNome = Label(self.frame_0, text="Nome Arquivos",  bg="#dc143c", fg="#FFFFFF")
        self.lbNome.place(relx=0.10, rely=0.25, relwidth=0.2, relheight=0.10)

        self.lbSave = Label(self.frame_0, text="Local Save",  bg="#dc143c", fg="#FFFFFF")
        self.lbSave.place(relx=0.10, rely=0.10, relwidth=0.2, relheight=0.10)

        self.lbStatus = Label(self.frame_0, text="",  bg="#c7c7c7", fg="#dc143c")
        self.lbStatus.place(relx=0.10, rely=0.50, relwidth=0.80, relheight=0.1)


    def botao(self):
        self.btBuscar = Button(self.frame_0, text="BUSCAR",  bg="#dc143c", fg="#FFFFFF", command=self.scraping)
        self.btBuscar.place(relx=0.40, rely=0.60, relwidth=0.2, relheight=0.1)

    def save(self):
        options = [
            "csv",
            "csv_xlsx"
        ]
        self.clicked = StringVar()
        self.clicked.set("csv")
        drop = OptionMenu(self.frame_0, self.clicked, *options)
        drop.place(relx=0.40, rely=0.35, relwidth=0.2, relheight=0.1)

    def entry(self):
        self.enArquivo = Entry(self.frame_0)
        self.enArquivo.place(relx=0.30, rely=0.25, relwidth=0.60, relheight=0.10)

        self.enSave = Entry(self.frame_0)
        self.enSave.place(relx=0.30, rely=0.10, relwidth=0.60, relheight=0.10)
        
    def scraping(self):
        self.lbStatus.config(text="")
        if not self.enArquivo.get() == "" and not self.enSave.get() == "":
            self.lbStatus.config(text="")
            endereco = self.endereco_valido()
            Scraping(endereco, self.enArquivo.get(), self.clicked.get().lower())
            self.lbStatus.config(text="Arquivos criados")

        else:
            self.lbStatus.config(text="Coloque valores válidos!")

    def endereco_valido(self):
        endereco = self.enSave.get().replace("\\", "/") + "/"
        print(endereco)
        return endereco

tela = Tela()