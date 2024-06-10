from tkinter import *
import random
import time

# Configurações iniciais do jogo
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
length = 500 / level

root = Tk()
root.title("Ping Pong")
root.resizable(0, 0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

root.update()

# Variáveis globais
count = 0  # Pontuação
lost = False  # Verifica se o jogo acabou


# Classe Bola: representa a bola do jogo
class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)  # Cria a bola
        self.canvas.move(self.id, 245, 200)  # Posição inicial da bola

        # Lista de velocidades iniciais da bola
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]  # Velocidade inicial em X
        self.y = -3  # Velocidade inicial em Y

        # Dimensões do canvas
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # Move a bola

        pos = self.canvas.coords(self.id)  # Posição atual da bola

        # Colisão com as bordas do canvas
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Verifica colisão com a barra
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count += 1
                score()  # Atualiza a pontuação

        if pos[3] <= self.canvas_height:
            # Se a bola não atingir o fundo, continua o movimento
            self.canvas.after(10, self.draw)
        else:
            game_over()  # Se atingir o fundo, o jogo acaba
            global lost
            lost = True


# Classe Barra: representa a barra de controle do jogo
class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)  # Cria a barra
        self.canvas.move(self.id, 200, 400)  # Posição inicial da barra

        self.x = 0  # Velocidade da barra

        self.canvas_width = self.canvas.winfo_width()

        # Associa teclas de movimento da barra
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)  # Move a barra

        self.pos = self.canvas.coords(self.id)  # Posição atual da barra

        # Limita movimento da barra dentro do canvas
        if self.pos[0] <= 0:
            self.x = 0
        if self.pos[2] >= self.canvas_width:
            self.x = 0

        global lost

        if not lost:
            # Se o jogo não acabou, continua movimento da barra
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3  # Move para a esquerda

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3  # Move para a direita


# Função para iniciar o jogo
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()  # Atualiza a pontuação
    canvas.itemconfig(game, text=" ")  # Limpa mensagem de fim de jogo

    time.sleep(1)  # Aguarda um segundo antes de começar
    Barra.draw()  # Desenha a barra
    Bola.draw()  # Desenha a bola


# Função para exibir a pontuação
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))


# Função para exibir mensagem de fim de jogo
def game_over():
    canvas.itemconfig(game, text="Game over!")  # Exibe mensagem


# Instância da classe Barra para controle do jogo
Barra = Barra(canvas, "orange")
# Instância da classe Bola para movimento da bola
Bola = Bola(canvas, Barra, "purple")

# Elemento para exibir pontuação
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill="green", font=("Arial", 16))
# Elemento para exibir mensagem de fim de jogo
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

# Inicia o jogo ao clicar no botão
canvas.bind_all("<Button-1>", start_game)

root.mainloop()  # Inicia a interface gráfica
