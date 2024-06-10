import tkinter as tk
from tkinter import messagebox

# Dados pré-cadastrados para clientes e tipos de vidro
clientes_cadastrados = ["Cliente A", "Cliente B", "Cliente C"]  # Adicione aqui os clientes existentes
vidros_cadastrados = ["Tipo 1", "Tipo 2", "Tipo 3"]  # Adicione aqui os tipos de vidro existentes
dados_pedidos = []  # Aqui você pode armazenar os dados dos pedidos

def cadastrar_pedido():
    # Obter os dados do pedido selecionados
    numero_pedido = entry_numero_pedido.get()
    data_pedido = entry_data_pedido.get()

    # Obter o cliente e o tipo de vidro selecionados
    cliente_selecionado = dropdown_clientes.get()
    vidro_selecionado = dropdown_vidros.get()

    # Salvar os dados do pedido
    dados_pedidos.append({
        "Número do Pedido": numero_pedido,
        "Data do Pedido": data_pedido,
        "Cliente": cliente_selecionado,
        "Tipo de Vidro": vidro_selecionado
    })

    # Exibindo as informações para fins de demonstração
    messagebox.showinfo("Pedido Cadastrado", f"Número do Pedido: {numero_pedido}\nData do Pedido: {data_pedido}\n"
                                             f"Cliente: {cliente_selecionado}\nTipo de Vidro: {vidro_selecionado}")

def adicionar_cliente():
    novo_cliente = entry_novo_cliente.get()
    clientes_cadastrados.append(novo_cliente)
    menu_clientes['menu'].add_command(label=novo_cliente, command=tk._setit(dropdown_clientes, novo_cliente))
    entry_novo_cliente.delete(0, tk.END)
    messagebox.showinfo("Cliente Adicionado", f"Novo cliente '{novo_cliente}' adicionado com sucesso!")

def adicionar_vidro():
    novo_vidro = entry_novo_vidro.get()
    vidros_cadastrados.append(novo_vidro)
    menu_vidros['menu'].add_command(label=novo_vidro, command=tk._setit(dropdown_vidros, novo_vidro))
    entry_novo_vidro.delete(0, tk.END)
    messagebox.showinfo("Tipo de Vidro Adicionado", f"Novo tipo de vidro '{novo_vidro}' adicionado com sucesso!")

def exibir_dados():
    window = tk.Toplevel(root)
    window.title("Dados Cadastrados")

    label_clientes = tk.Label(window, text="Clientes Cadastrados:")
    label_clientes.pack()

    for cliente in clientes_cadastrados:
        lbl_cliente = tk.Label(window, text=cliente)
        lbl_cliente.pack()

    label_vidros = tk.Label(window, text="\nTipos de Vidro Cadastrados:")
    label_vidros.pack()

    for vidro in vidros_cadastrados:
        lbl_vidro = tk.Label(window, text=vidro)
        lbl_vidro.pack()

    label_pedidos = tk.Label(window, text="\nPedidos Cadastrados:")
    label_pedidos.pack()

    for pedido in dados_pedidos:
        lbl_pedido = tk.Label(window, text=str(pedido))
        lbl_pedido.pack()

root = tk.Tk()
root.title("Cadastro de Pedidos")

label_numero_pedido = tk.Label(root, text="Número do Pedido:")
label_numero_pedido.pack()
entry_numero_pedido = tk.Entry(root)
entry_numero_pedido.pack()

label_data_pedido = tk.Label(root, text="Data do Pedido:")
label_data_pedido.pack()
entry_data_pedido = tk.Entry(root)
entry_data_pedido.pack()

label_cliente = tk.Label(root, text="Selecione o Cliente:")
label_cliente.pack()
dropdown_clientes = tk.StringVar(root)
dropdown_clientes.set(clientes_cadastrados[0])
menu_clientes = tk.OptionMenu(root, dropdown_clientes, *clientes_cadastrados)
menu_clientes.pack()

label_vidro = tk.Label(root, text="Selecione o Tipo de Vidro:")
label_vidro.pack()
dropdown_vidros = tk.StringVar(root)
dropdown_vidros.set(vidros_cadastrados[0])
menu_vidros = tk.OptionMenu(root, dropdown_vidros, *vidros_cadastrados)
menu_vidros.pack()

label_novo_cliente = tk.Label(root, text="Adicionar Novo Cliente:")
label_novo_cliente.pack()
entry_novo_cliente = tk.Entry(root)
entry_novo_cliente.pack()

btn_adicionar_cliente = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)
btn_adicionar_cliente.pack()

label_novo_vidro = tk.Label(root, text="Adicionar Novo Tipo de Vidro:")
label_novo_vidro.pack()
entry_novo_vidro = tk.Entry(root)
entry_novo_vidro.pack()

btn_adicionar_vidro = tk.Button(root, text="Adicionar Tipo de Vidro", command=adicionar_vidro)
btn_adicionar_vidro.pack()

btn_exibir_dados = tk.Button(root, text="Exibir Dados Cadastrados", command=exibir_dados)
btn_exibir_dados.pack()

btn_cadastrar = tk.Button(root, text="Cadastrar Pedido", command=cadastrar_pedido)
btn_cadastrar.pack()

root.mainloop()
