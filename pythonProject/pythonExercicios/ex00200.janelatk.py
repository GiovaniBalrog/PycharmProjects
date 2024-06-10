import requests
from tkinter import *
def pegar_cotacoes():
    requests = requests.get()




janela = Tk()
janela.title("cotação Atual das Moedas")

texto_orientacao = Label(janela, text="Clique no botão para atualizar a cotação das Moedas")
texto_orientacao.grid(column=0, row=0)
botao = Button(janela, texto="Buscar cotações Dolar/Euro/BTC", compound=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_orientacao = Label(janela,)

janela.mainloop()
