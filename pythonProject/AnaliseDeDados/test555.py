from tkinter import *

class Gaveta1:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack(side=LEFT)
        self.gaveta1 = Label(self.widget1, text="Gaveta 1")
        self.gaveta1["font"] = ("Verdana", "10", "italic", "bold")
        self.gaveta1.pack ()
        self.abrir1 = Button(self.widget1)
        self.abrir1["text"] = "Abrir"
        self.abrir1["font"] = ("Verdana", "10")
        self.abrir1["width"] = 5
        self.abrir1.pack (side=LEFT)
        self.fechar1 = Button(self.widget1)
        self.fechar1["text"] = "Fechar"
        self.fechar1["font"] = ("Verdana", "10")
        self.fechar1["width"] = 5
        self.fechar1.pack (side=LEFT)

class Gaveta2:
    def __init__(self, master=None):
        self.widget2 = Frame(master)
        self.widget2.pack(side=LEFT)
        self.gaveta2 = Label(self.widget2, text="Gaveta 2")
        self.gaveta2["font"] = ("Verdana", "10", "italic", "bold")
        self.gaveta2.pack ()
        self.abrir2 = Button(self.widget2)
        self.abrir2["text"] = "Abrir"
        self.abrir2["font"] = ("Verdana", "10")
        self.abrir2["width"] = 5
        self.abrir2.pack (side=LEFT)
        self.fechar2 = Button(self.widget2)
        self.fechar2["text"] = "Fechar"
        self.fechar2["font"] = ("Verdana", "10")
        self.fechar2["width"] = 5
        self.fechar2.pack (side=LEFT)

class Receita:
    def __init__(self, master=None):
        self.widget3 = Frame(master)
        self.widget3.pack(side=LEFT)
        self.ciclos = Label(self.widget3, text="Número de ciclos:")
        self.ciclos["font"] = ("Verdana", "10", "italic", "bold")
        self.ciclos.pack ()
        self.ciclos_entry = Entry(self.widget3)
        self.ciclos_entry.pack()

        self.widget4 = Frame(master)
        self.widget4.pack(side=LEFT)
        self.temperatura = Label(self.widget4, text="Temperatura:")
        self.temperatura["font"] = ("Verdana", "10", "italic", "bold")
        self.temperatura.pack ()
        self.temperatura_entry = Entry(self.widget4)
        self.temperatura_entry.pack()

        self.widget5 = Frame(master)
        self.widget5.pack(side=LEFT)
        self.tempo = Label(self.widget5, text="Tempo:")
        self.tempo["font"] = ("Verdana", "10", "italic", "bold")
        self.tempo.pack ()
        self.tempo_entry = Entry(self.widget5)
        self.tempo_entry.pack()

        self.widget6 = Frame(master)
        self.widget6.pack(side=LEFT)
        self.iniciar = Button(self.widget6)
        self.iniciar["text"] = "Iniciar"
        self.iniciar["font"] = ("Verdana", "10")
        self.iniciar["width"] = 5
        self.iniciar.pack (side=LEFT)
        self.parar = Button(self.widget6)
        self.parar["text"] = "Parar"
        self.parar["font"] = ("Verdana", "10")
        self.parar["width"] = 5
        self.parar.pack (side=LEFT)

root = Tk()
Gaveta1(root)
Gaveta2(root)
Receita(root)
root.mainloop()