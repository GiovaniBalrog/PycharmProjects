class ItemLista:
    def __init__(self, data=0, nextItem=None):
        """
        Inicializa um novo nó na lista encadeada.

        :param data: Valor armazenado no nó (padrão é 0)
        :param nextItem: Referência para o próximo nó na lista (padrão é None)
        """
        self.data = data
        self.next = nextItem

    def __repr__(self):
        """
        Retorna uma representação em string do nó e de seus nós subsequentes.
        """
        return f'{self.data} => {self.next}'


class ListaEncadeada:
    def __init__(self):
        """
        Inicializa uma lista encadeada vazia.
        """
        self.head = None

    def __repr__(self):
        """
        Retorna uma representação em string da lista encadeada inteira.
        """
        return str(self.head)

    def insere(self, data):
        """
        Insere um novo item no início da lista encadeada.

        :param data: Valor a ser adicionado à lista
        """
        # Cria um novo objeto ItemLista com o valor fornecido
        item = ItemLista(data)
        # O próximo item do novo nó é o atual head da lista
        item.next = self.head
        # O novo nó se torna o novo head da lista
        self.head = item

    def remove(self, valor):
        """
        Remove o primeiro item da lista que contém o valor especificado.

        :param valor: Valor do item a ser removido
        """
        # Verifica se o item a ser removido é o head
        if self.head and self.head.data == valor:
            self.head = self.head.next
            return

        # Inicializa as variáveis de navegação
        navegar = self.head
        before = None

        # Navega pela lista para encontrar o elemento
        while navegar and navegar.data != valor:
            before = navegar
            navegar = navegar.next

        # Remove o item se ele for encontrado
        if navegar:
            before.next = navegar.next

    def busca(self, valor):
        """
        Busca um item na lista que contém o valor especificado.

        :param valor: Valor do item a ser buscado
        :return: Retorna o nó contendo o valor, ou None se não for encontrado
        """
        navegar = self.head
        while navegar and navegar.data != valor:
            navegar = navegar.next
        return navegar


# Criação e uso da lista encadeada
lista = ListaEncadeada()

# Exibe o conteúdo da lista antes de adicionar itens (deve estar vazia)
print("Conteúdo da lista:", lista)

# Inserção de itens na lista
lista.insere("shampoo")
lista.insere("biscoito")
lista.insere("detergente")
lista.insere("abobrinha")
lista.insere("banana")

# Exibe o conteúdo da lista após as inserções
print("Conteúdo da lista após inserções:", lista)

# Exibição da lista antes da remoção
print("Conteúdo da lista antes da remoção:", lista)

# Remoção de itens da lista
lista.remove("detergente")
lista.remove("banana")

# Exibição da lista após as remoções
print("Conteúdo da lista após a remoção:", lista)

# Buscando um item na lista
item_encontrado = lista.busca("biscoito")
if item_encontrado:
    print("Item Encontrado:", item_encontrado)
else:
    print("Item não Encontrado")

# Criando e usando a lista encadeada com números
lista = ListaEncadeada()

# Inserção de itens na lista
lista.insere(1)
lista.insere(2)
lista.insere(3)
lista.insere(4)
lista.insere(5)

# Exibe o conteúdo da lista após as inserções
print("Conteúdo da lista após inserções:", lista)

# Exibição da lista antes da remoção
print("Conteúdo da lista antes da remoção:", lista)

# Remoção de itens da lista
lista.remove(5)
lista.remove(4)

# Exibição da lista após as remoções
print("Conteúdo da lista após a remoção do 4 e do 5:", lista)

# Buscando um item que não está na lista
item_encontrado = lista.busca(4)
if item_encontrado:
    print("Item Encontrado:", item_encontrado)
else:
    print("Item não Encontrado")
