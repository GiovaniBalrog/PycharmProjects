class Node:
    def __init__(self, data):
        self.data = data  # Armazena o valor do nó.
        self.next = None  # Inicialmente, o próximo nó é None.

class Stack:
    def __init__(self):
        self.top = None  # O topo da pilha, inicialmente vazio.

    def push(self, data):
        new_node = Node(data)  # Cria um novo nó com o dado fornecido.
        new_node.next = self.top  # O próximo nó do novo nó é o antigo topo.
        self.top = new_node  # Atualiza o topo da pilha para o novo nó.

    def pop(self):
        if self.is_empty():
            return None  # Se a pilha estiver vazia, retorne None.

        popped_node = self.top  # Armazene o nó do topo.
        self.top = self.top.next  # Atualize o topo para o próximo nó.
        return popped_node.data  # Retorne o dado do nó removido.

    def is_empty(self):
        return self.top is None  # Se top for None, a pilha está vazia.

    def peek(self):
        if self.is_empty():
            return None  # Se a pilha estiver vazia, retorne None.
        return self.top.data  # Retorne o valor do topo.

# Testando a classe Stack
if __name__ == "__main__":
    stack = Stack()

    stack.push('A')  # Adiciona 'A' ao topo da pilha
    stack.push('B')  # Adiciona 'B' ao topo da pilha
    stack.push('C')  # Adiciona 'C' ao topo da pilha

    print('Elemento no topo:', stack.peek())  # Deve imprimir 'C'

    print('Elemento removido:', stack.pop())  # Deve remover e imprimir 'C'
    print('Elemento no topo:', stack.peek())  # Deve imprimir 'B'

    print('Elemento removido:', stack.pop())  # Deve remover e imprimir 'B'
    print('Elemento removido:', stack.pop())  # Deve remover e imprimir 'A'

    print('Pilha vazia:', stack.is_empty())  # Deve imprimir True (pilha está vazia)

