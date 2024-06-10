import tkinter as tk

def key_press(event):
    label.config(text=f'Tecla pressionada: {event.keysym}')

root = tk.Tk()
root.title('Identificação de Teclas Pressionadas')

label = tk.Label(root, text='Pressione uma tecla')
label.pack()

root.bind('<KeyPress>', key_press)

root.mainloop()
