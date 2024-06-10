class Livro:


# OopCompanion:suppressRename


# OopCompanion:suppressRename


# OopCompanion:suppressRename
    lista_livros = []  # Lista para armazenar todos os livros da biblioteca
    livros_emprestados = []  # Lista para armazenar os livros emprestados e a quantidade

    def __init__(self, titulo, autor, ano, quantidade):
        """Inicializa um objeto Livro com os atributos título, autor, ano e quantidade."""
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        Livro.lista_livros.append(self)  # Adiciona o livro à lista de livros da biblioteca

    @staticmethod
    def cadastrar_livros():
        """Permite ao usuário adicionar múltiplos livros à biblioteca."""
        print('Adicione os livros à biblioteca:')
        num_livros = int(input('Quantos livros deseja adicionar? '))
        for _ in range(num_livros):
            titulo = input('Digite o título do livro: ')
            autor = input('Digite o autor do livro: ')
            ano = int(input('Digite o ano que o livro foi publicado: '))
            quantidade = int(input('Digite a quantidade de livros disponíveis: '))
            Livro(titulo, autor, ano, quantidade)  # Cria um novo livro e o adiciona à biblioteca
        print('Livros cadastrados com sucesso.')

    @staticmethod
    def listar_livros():
        """Lista os livros disponíveis na biblioteca."""
        print('--- Livros Disponíveis ---')
        for index, livro in enumerate(Livro.lista_livros, start=1):
            print(f"{index}. {livro.titulo} - {livro.autor} ({livro.ano}) - Disponíveis: {livro.quantidade}")

    @staticmethod
    def emprestimo():
        """Permite ao usuário emprestar um livro da biblioteca."""
        Livro.listar_livros()
        escolha = int(input('Escolha o número correspondente ao livro que deseja emprestar: '))
        livro_escolhido = Livro.lista_livros[escolha - 1]
        quantidade = int(input(f'Quantos exemplares de "{livro_escolhido.titulo}" deseja emprestar? '))
        if quantidade <= livro_escolhido.quantidade:
            livro_escolhido.quantidade -= quantidade  # Atualiza a quantidade de livros disponíveis na biblioteca
            Livro.livros_emprestados.append((livro_escolhido, quantidade))  # Adiciona à lista de emprestados
            print(f'Empréstimo de "{livro_escolhido.titulo}" realizado com sucesso.')
        else:
            print('Quantidade de livros não disponível.')

    @staticmethod
    def listar_livros_emprestados():
        """Lista os livros que estão emprestados no momento."""
        print('--- Livros Emprestados ---')
        for livro, quantidade in Livro.livros_emprestados:
            print(f"{livro.titulo} - {quantidade} exemplar(es)")

# Exemplo de uso:
Livro.cadastrar_livros()
Livro.emprestimo()
Livro.listar_livros_emprestados()
