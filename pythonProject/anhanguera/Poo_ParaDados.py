import tkinter as tk  # Importa a biblioteca tkinter e a renomeia como tk para facilitar o uso.

def tecla_press(event):  # Define uma função chamada tecla_press que será chamada quando uma tecla for pressionada.
    texto.insert(tk.END, f"Tecla pressionada: {event.keysym}\n")
    texto.see(tk.END)  # Rola a caixa de texto para mostrar o texto mais recente

root = tk.Tk()  # Cria a janela principal da interface gráfica.

texto = tk.Text(root, height=10, width=40)  # Cria uma caixa de texto com 10 linhas de altura e 40 caracteres de largura.
texto.pack()  # Coloca a caixa de texto na janela principal.

root.bind("<KeyPress>", tecla_press)  # Liga o evento de pressionar tecla à função tecla_press.
# Isso significa que toda vez que uma tecla for pressionada na janela, a função tecla_press será chamada.

root.mainloop()  # Inicia o loop principal da interface gráfica para capturar eventos.
# O programa continuará em execução até que a janela seja fechada pelo usuário.
