from tkinter import *
import requests
import json
from datetime import datetime

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Forno de laminação de vidros")
        self.master.geometry("800x600")

        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)
        self.msg = Label(self.widget1, text="Forno de laminação de vidros")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack (side=RIGHT)

        self.widget2 = Frame(master)
        self.widget2.pack(side=LEFT)
        self.gaveta1 = Label(self.widget2, text="Gaveta 1")
        self.gaveta1["font"] = ("Verdana", "10", "italic", "bold")
        self.gaveta1.pack ()
        self.abrir1 = Button(self.widget2)
        self.abrir1["text"] = "Abrir"
        self.abrir1["font"] = ("Verdana", "10")
        self.abrir1["width"] = 5
        self.abrir1.pack (side=LEFT)
        self.fechar1 = Button(self.widget2)
        self.fechar1["text"] = "Fechar"
        self.fechar1["font"] = ("Verdana", "10")
        self.fechar1["width"] = 5
        self.fechar1.pack (side=LEFT)

        self.widget3 = Frame(master)
        self.widget3.pack(side=LEFT)
        self.gaveta2 = Label(self.widget3, text="Gaveta 2")
        self.gaveta2["font"] = ("Verdana", "10", "italic", "bold")
        self.gaveta2.pack ()
        self.abrir2 = Button(self.widget3)
        self.abrir2["text"] = "Abrir"
        self.abrir2["font"] = ("Verdana", "10")
        self.abrir2["width"] = 5
        self.abrir2.pack (side=LEFT)
        self.fechar2 = Button(self.widget3)
        self.fechar2["text"] = "Fechar"
        self.fechar2["font"] = ("Verdana", "10")
        self.fechar2["width"] = 5
        self.fechar2.pack (side=LEFT)

        self.widget4 = Frame(master)
        self.widget4.pack(side=LEFT)
        self.ciclos = Label(self.widget4, text="Ciclos:")
        self.ciclos_entry = Entry(self.widget4)
        self.temperatura = Label(self.widget4, text="Temperatura:")
        self.temperatura_entry = Entry(self.widget4)
        self.tempo = Label(self.widget4, text="Tempo:")
        self.tempo_entry = Entry(self.widget4)
        self.iniciar = Button(self.widget4, text="Iniciar")
        self.parar = Button(self.widget4, text="Parar")

    def atualizar_temperatura_clima(self):
        temperatura = 100 # Substitua este valor pela temperatura real do forno.
        self.temperatura_clima.config(text=f"Temperatura: {temperatura}")
        self.temperatura_clima.after(600000, self.atualizar_temperatura_clima)

    def atualizar_data_hora(self):
        data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.data_hora.config(text=f"Data e hora: {data_hora_atual}")
        self.data_hora.after(1000, self.atualizar_data_hora)

root = Tk()
Application(root)
root.mainloop()