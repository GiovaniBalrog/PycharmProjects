
# Implementação de Pilha com Lista Encadeada em Python

## Conceito de Lista Encadeada
**Lista Encadeada** é uma estrutura de dados onde cada elemento é um nó que contém um valor (dado) e uma referência (ponteiro) para o próximo nó na sequência. Diferente de listas comuns, os elementos não são armazenados em posições contíguas na memória.

## Estrutura de uma Pilha (Stack)
**Pilha** é uma estrutura de dados do tipo **LIFO** (Last In, First Out), onde o último elemento inserido é o primeiro a ser removido.

## Componentes Principais

### Classe `Node`
- Representa um nó na lista encadeada.
- Cada `Node` contém:
  - **`data`**: O valor armazenado no nó.
  - **`next`**: A referência para o próximo nó.

```python
class Node:
    def __init__(self, data):
        self.data = data  # Valor do nó
        self.next = None  # Referência para o próximo nó
```

### Classe `Stack`
- Representa a pilha em si.
- Contém uma referência ao **topo** da pilha (o nó mais recentemente inserido).

#### Métodos da Classe `Stack`
- **`push(data)`**: Adiciona um novo nó ao topo da pilha.
- **`pop()`**: Remove e retorna o nó do topo da pilha.
- **`is_empty()`**: Verifica se a pilha está vazia.
- **`peek()`**: Retorna o valor no topo da pilha sem removê-lo.

```python
class Stack:
    def __init__(self):
        self.top = None  # Inicialmente, a pilha está vazia

    def push(self, data):
        new_node = Node(data)  # Cria um novo nó
        new_node.next = self.top  # Aponta para o antigo topo
        self.top = new_node  # Atualiza o topo para o novo nó

    def pop(self):
        if self.is_empty():
            return None  # Retorna None se a pilha estiver vazia
        popped_node = self.top  # Armazena o nó do topo
        self.top = self.top.next  # Atualiza o topo para o próximo nó
        return popped_node.data  # Retorna o valor do nó removido

    def is_empty(self):
        return self.top is None  # Retorna True se a pilha estiver vazia

    def peek(self):
        if self.is_empty():
            return None  # Retorna None se a pilha estiver vazia
        return self.top.data  # Retorna o valor do topo sem remover
```

## Como Usar a Pilha

### Exemplo de Uso:

```python
if __name__ == "__main__":
    stack = Stack()

    stack.push('A')  # Adiciona 'A' ao topo
    stack.push('B')  # Adiciona 'B' ao topo
    stack.push('C')  # Adiciona 'C' ao topo

    print('Elemento no topo:', stack.peek())  # Saída: 'C'
    print('Elemento removido:', stack.pop())  # Remove 'C'
    print('Elemento no topo:', stack.peek())  # Saída: 'B'

    print('Elemento removido:', stack.pop())  # Remove 'B'
    print('Elemento removido:', stack.pop())  # Remove 'A'

    print('Pilha vazia:', stack.is_empty())  # Saída: True (pilha está vazia)
```

## Vantagens
- **Flexibilidade**: A pilha cresce conforme necessário, sem a limitação de tamanho fixo.
- **Eficiência**: Não há necessidade de redimensionamento como em listas dinâmicas.

## Resumo
A implementação de uma pilha com lista encadeada em Python oferece uma estrutura eficiente e flexível, permitindo a inserção e remoção de elementos no estilo **LIFO**, sem restrições de tamanho fixo.
