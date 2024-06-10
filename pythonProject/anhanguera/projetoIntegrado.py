# Importa as bibliotecas datetime e timedelta para lidar com datas
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
            copias_disponiveis = int(input("Digite o número de cópias disponíveis: "))
            self.gestao_biblioteca.cadastrar_livro(titulo, autor, ano, copias_disponiveis)
            print("Livro cadastrado com sucesso!")
        except ValueError:
            print("Erro ao cadastrar o livro. Verifique os dados digitados.")

    def cadastrar_novo_usuario(self):
        """Realiza o cadastro de um novo usuário."""
        nome = input("Digite o nome do novo usuário: ")
        identificacao = input("Digite o número de identificação do novo usuário: ")
        contato = input("Digite as informações de contato do novo usuário: ")
        self.gestao_biblioteca.cadastrar_usuario(nome, identificacao, contato)
        print("Usuário cadastrado com sucesso!")

    def emprestar_livro(self):
        """Realiza o empréstimo de um livro."""
        try:
            titulo_livro = input("Digite o título do livro a ser emprestado: ")
            usuario_nome = input("Digite o nome do usuário que irá emprestar o livro: ")

            # Verifica se o livro existe na biblioteca
            livros_encontrados = self.gestao_biblioteca.consultar_livros(titulo_livro)
            if not livros_encontrados:
                print("Livro não encontrado na biblioteca.")
                return

            # Verifica se o usuário está cadastrado na biblioteca
            usuarios_encontrados = [usuario for usuario in self.gestao_biblioteca.usuarios_cadastrados if usuario.nome.lower() == usuario_nome.lower()]
            if not usuarios_encontrados:
                print("Usuário não encontrado na biblioteca.")
                return

            # Realiza o empréstimo do livro
            livro_emprestado = livros_encontrados[0]
            usuario_emprestimo = usuarios_encontrados[0]
            sucesso_emprestimo, data_devolucao = self.gestao_biblioteca.emprestar_livro(livro_emprestado, usuario_emprestimo)
            if sucesso_emprestimo:
                print(f"Empréstimo realizado com sucesso! Data de devolução: {data_devolucao.strftime('%d/%m/%Y')}")
            else:
                print("O livro não está disponível para empréstimo no momento.")

        except Exception as e:
            print(f"Erro ao realizar empréstimo: {e}")

    def devolver_livro(self):
        """Realiza a devolução de um livro."""
        try:
            titulo_livro = input("Digite o título do livro a ser devolvido: ")
            usuario_nome = input("Digite o nome do usuário que irá devolver o livro: ")

            # Verifica se o livro existe na biblioteca
            livros_encontrados = self.gestao_biblioteca.consultar_livros(titulo_livro)
            if not livros_encontrados:
                print("Livro não encontrado na biblioteca.")
                return

            # Verifica se o usuário está cadastrado na biblioteca
            usuarios_encontrados = [usuario for usuario in self.gestao_biblioteca.usuarios_cadastrados if usuario.nome.lower() == usuario_nome.lower()]
            if not usuarios_encontrados:
                print("Usuário não encontrado na biblioteca.")
                return

            # Realiza a devolução do livro
            livro_devolvido = livros_encontrados[0]
            usuario_devolucao = usuarios_encontrados[0]
            sucesso_devolucao = self.gestao_biblioteca.devolver_livro(livro_devolvido, usuario_devolucao)
            if sucesso_devolucao:
                print("Devolução realizada com sucesso!")
            else:
                print("Erro ao devolver o livro.")

        except Exception as e:
            print(f"Erro ao realizar devolução: {e}")

    def consultar_livros(self):
        """Consulta livros na biblioteca."""
        termo_busca = input("Digite o título, autor ou ano de publicação a ser buscado: ")
        encontrados = self.gestao_biblioteca.consultar_livros(termo_busca)
        quebra_de_linha("Livros Encontrados")
        for livro in encontrados:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Disponível: {livro.copias_disponiveis}")

    def gerar_relatorios(self):
        """Gera relatórios da biblioteca."""
        disponiveis, emprestados, usuarios = self.gestao_biblioteca.gerar_relatorio()
        quebra_de_linha("Livros Disponíveis")
        for livro in disponiveis:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Disponível: {livro.copias_disponiveis}")
        quebra_de_linha("Livros Emprestados")
        for emprestimo in emprestados:
            livro, usuario, data_devolucao = emprestimo
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}, Data Devolução: {data_devolucao.strftime('%d/%m/%Y')}")
        quebra_de_linha("Usuários Cadastrados")
        for usuario in usuarios:
            print(f"Nome: {usuario.nome}, Identificação: {usuario.identificacao}, Contato: {usuario.contato}")

# Instanciando e executando a interface do usuário
interface_usuario = InterfaceUsuarioBiblioteca()
interface_usuario.menu_principal()
