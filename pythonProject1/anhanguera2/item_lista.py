class ItemLista:

    def __init__(self, data, nextItem=None):


        self.data = data
        self.next = nextItem


class ListaEncadeada:

    def __init__(self):

        self.head = None

def insere(self, data):
    novo_item = ItemLista(data)
    novo_item.next = self.head
    self.head = novo_item
