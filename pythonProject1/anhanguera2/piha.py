# Pilha
pilha = []

pilha.append('A')  # Adiciona 'A' ao topo da pilha
pilha.append('B')  # Adiciona 'B' ao topo da pilha
pilha.append('C')  # Adiciona 'C' ao topo da pilha

print('pilha:', pilha)  # Imprime a pilha na ordem: ['A', 'B', 'C']

elemento_pilha = pilha.pop()  # Remove o último elemento (topo) da pilha ('C')
print('Elemento removido:', elemento_pilha)  # Imprime o elemento removido: 'C'

print('pilha:', pilha)  # Imprime a pilha depois da remoção: ['A', 'B']

# Fila

from collections import deque

fila = deque()
fila.append('x')  # Enfileirar 'X'
fila.append('y')  # Enfileirar  'Y'
fila.append('z')  # Enfileirar  'Z'
print("\nFila:", list(fila))
elemento_fila = fila.popleft()  # Remove o primeiro elemento da fila
print('elemento removido da fila:', elemento_fila)
print('Fila após remoção', list(fila))

