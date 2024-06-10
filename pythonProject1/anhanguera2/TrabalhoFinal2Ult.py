from datetime import datetime, timedelta

# Função para gerar uma quebra de linha personalizada
def quebra_de_linha(titulo):
    """Função para gerar uma quebra de linha personalizada."""
    print('\n' + '-' * 20 + f' {titulo} ' + '-' * 20)

# Classe LivroBiblioteca para representar livros na biblioteca
class LivroBiblioteca:
    def __init__(self, titulo, autor, ano, copias_disponiveis):
        """Inicializa um livro com título, autor, ano de publicação e número de cópias disponíveis."""
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias_disponiveis = copias_disponiveis

    def disponibilidade(self):
        """Verifica se o livro está disponível para empréstimo."""
        return self.copias_disponiveis > 0

# Classe UsuarioBiblioteca para representar usuários da biblioteca
class UsuarioBiblioteca:
    def __init__(self, nome, identificacao, contato):
        """Inicializa um usuário com nome, identificação e informações de contato."""
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato

# Classe SistemaBibliotecaGestao para gerenciar a biblioteca
class SistemaBibliotecaGestao:
    def __init__(self):
        """Inicializa o sistema de gestão da biblioteca."""
        self.livros_disponiveis = []
        self.usuarios_cadastrados = []
        self.emprestimos_ativos = []

    def cadastrar_livro(self, titulo, autor, ano, copias_disponiveis):
        """Cadastra um novo livro na biblioteca."""
        livro = LivroBiblioteca(titulo, autor, ano, copias_disponiveis)
        self.livros_disponiveis.append(livro)
        return livro

    def cadastrar_usuario(self, nome, identificacao, contato):
        """Cadastra um novo usuário na biblioteca."""
        usuario = UsuarioBiblioteca(nome, identificacao, contato)
        self.usuarios_cadastrados.append(usuario)
        return usuario

    def emprestar_livro(self, livro, usuario):
        """Realiza o empréstimo de um livro para um usuário."""
        if livro.disponibilidade():
            livro.copias_disponiveis -= 1
            data_devolucao = datetime.now() + timedelta(days=90)
            emprestimo = (livro, usuario, data_devolucao)
            self.emprestimos_ativos.append(emprestimo)
            return True, data_devolucao
        else:
            return False, None

    def devolver_livro(self, livro, usuario):
        """Realiza a devolução de um livro por um usuário."""
        for emprestimo in self.emprestimos_ativos:
            if emprestimo[0] == livro and emprestimo[1] == usuario:
                self.emprestimos_ativos.remove(emprestimo)
                livro.copias_disponiveis += 1
                return True
        return False

    def consultar_livros(self, termo_busca):
        """Consulta livros na biblioteca com base em um termo de busca."""
        encontrados = [livro for livro in self.livros_disponiveis if termo_busca.lower() in livro.titulo.lower() or termo_busca.lower() in livro.autor.lower()]
        return encontrados

    def gerar_relatorio(self):
        """Gera um relatório com livros disponíveis, emprestados e usuários cadastrados."""
        disponiveis = [livro for livro in self.livros_disponiveis if livro.disponibilidade()]
        emprestados = [emprestimo for emprestimo in self.emprestimos_ativos]
        return disponiveis, emprestados, self.usuarios_cadastrados

# Classe InterfaceUsuarioBiblioteca para interação com o usuário
class InterfaceUsuarioBiblioteca:
    def __init__(self):
        """Inicializa a interface do usuário."""
        self.gestao_biblioteca = SistemaBibliotecaGestao()

    def menu_principal(self):
        """Exibe o menu principal e realiza a interação com o usuário."""
        while True:
            print("\n### Bem-vindo à Biblioteca Digital ###")
            print("Selecione uma opção:")
            print("1. Cadastrar um novo livro")
            print("2. Cadastrar um novo usuário")
            print("3. Emprestar um livro")
            print("4. Devolver um livro")
            print("5. Consultar livros disponíveis")
            print("6. Gerar relatórios")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            try:
                opcao = int(opcao)
                if opcao == 1:
                    self.cadastrar_novo_livro()
                elif opcao == 2:
                    self.cadastrar_novo_usuario()
                elif opcao == 3:
                    self.emprestar_livro()
                elif opcao == 4:
                    self.devolver_livro()
                elif opcao == 5:
                    self.consultar_livros()
                elif opcao == 6:
                    self.gerar_relatorios()
                elif opcao == 7:
                    print("Encerrando o sistema...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Digite um número.")

    def cadastrar_novo_livro(self):
        """Realiza o cadastro de um novo livro."""
        try:
            titulo = input("Digite o título do novo livro: ")
            autor = input("Digite o nome do autor do novo livro: ")
            ano = input("Digite o ano de publicação do novo livro: ")
            ano = int(ano)  # Convertendo para inteiro
            copias_disponiveis = int(input("Digite o número de cópias disponíveis do novo livro: "))
            livro = self.gestao_biblioteca.cadastrar_livro(titulo, autor, ano, copias_disponiveis)
            print(f'O livro "{livro.titulo}" foi cadastrado com sucesso.')
        except ValueError:
            print("Erro ao cadastrar livro. Certifique-se de digitar um ano válido e um número de cópias válido.")

    def cadastrar_novo_usuario(self):
        """Realiza o cadastro de um novo usuário."""
        nome = input("Digite o nome do novo usuário: ")
        identificacao = input("Digite a identificação do novo usuário: ")
        contato = input("Digite o contato do novo usuário: ")
        usuario = self.gestao_biblioteca.cadastrar_usuario(nome, identificacao, contato)
        print(f'O usuário "{usuario.nome}" foi cadastrado com sucesso.')

    def emprestar_livro(self):
        """Realiza o empréstimo de um livro."""
        try:
            titulo = input("Digite o título do livro a ser emprestado: ")
            termo_busca = input("Digite o termo de busca para identificar o usuário: ")
            livros_encontrados = self.gestao_biblioteca.consultar_livros(termo_busca)
            if livros_encontrados:
                livro = livros_encontrados[0]  # Supondo que o primeiro livro encontrado seja o desejado
                resultado, data_devolucao = self.gestao_biblioteca.emprestar_livro(livro, termo_busca)
                if resultado:
                    print(f'O livro "{livro.titulo}" foi emprestado para "{termo_busca}" até {data_devolucao.strftime("%d/%m/%Y")}.')
                else:
                    print(f'O livro "{livro.titulo}" não está disponível para empréstimo.')
            else:
                print('Nenhum livro encontrado com o termo de busca fornecido.')
        except ValueError:
            print("Erro ao emprestar livro. Certifique-se de digitar um título válido e um termo de busca válido.")

    def devolver_livro(self):
        """Realiza a devolução de um livro."""
        try:
            titulo = input("Digite o título do livro a ser devolvido: ")
            termo_busca = input("Digite o termo de busca para identificar o usuário: ")
            livros_encontrados = self.gestao_biblioteca.consultar_livros(termo_busca)
            if livros_encontrados:
                livro = livros_encontrados[0]  # Supondo que o primeiro livro encontrado seja o desejado
                resultado = self.gestao_biblioteca.devolver_livro(livro, termo_busca)
                if resultado:
                    print(f'O livro "{livro.titulo}" foi devolvido com sucesso por "{termo_busca}".')
                else:
                    print(f'O livro "{livro.titulo}" não foi encontrado nos empréstimos ativos ou não foi emprestado por "{termo_busca}".')
            else:
                print('Nenhum livro encontrado com o termo de busca fornecido.')
        except ValueError:
            print("Erro ao devolver livro. Certifique-se de digitar um título válido e um termo de busca válido.")

    def consultar_livros(self):
        """Consulta livros disponíveis na biblioteca."""
        termo_busca = input("Digite o termo de busca para encontrar livros disponíveis: ")
        livros_encontrados = self.gestao_biblioteca.consultar_livros(termo_busca)
        if livros_encontrados:
            quebra_de_linha('Livros Encontrados')
            for livro in livros_encontrados:
                print(f"{livro.titulo} - {livro.autor} ({livro.ano}) - Cópias Disponíveis: {livro.copias_disponiveis}")
        else:
            print('Nenhum livro encontrado com o termo de busca fornecido.')

    def gerar_relatorios(self):
        """Gera relatórios com livros disponíveis, emprestados e usuários cadastrados."""
        disponiveis, emprestados, usuarios = self.gestao_biblioteca.gerar_relatorio()
        quebra_de_linha('Livros Disponíveis')
        for livro in disponiveis:
            print(f"{livro.titulo} - {livro.autor} ({livro.ano}) - Cópias Disponíveis: {livro.copias_disponiveis}")

        quebra_de_linha('Livros Emprestados')
        for emprestimo in emprestados:
            print(f"Livro: {emprestimo[0].titulo}, Usuário: {emprestimo[1].nome}, Data de Devolução: {emprestimo[2].strftime('%d/%m/%Y')}")

        quebra_de_linha('Usuários Cadastrados')
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, ID: {usuario.identificacao}, Contato: {usuario.contato}")

# Instanciando a Interface do Usuário da Biblioteca
interface_usuario = InterfaceUsuarioBiblioteca()
interface_usuario.menu_principal()
