from datetime import datetime, timedelta

def quebra_de_linha(titulo):
    """Função para gerar uma quebra de linha personalizada."""
    print('\n' + '-' * 20 + f' {titulo} ' + '-' * 20)

class Livro:
    def __init__(self, titulo, autor, ano, copias):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias = copias

class Usuario:
    def __init__(self, nome, identificacao, contato):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato

class SistemaBiblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def verificar_disponibilidade(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro.copias > 0
        return False

    def cadastrar_livro(self, titulo, autor, ano, copias):
        livro = Livro(titulo, autor, ano, copias)
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi cadastrado na biblioteca.')

    def cadastrar_usuario(self, nome, identificacao, contato):
        usuario = Usuario(nome, identificacao, contato)
        self.usuarios.append(usuario)
        print(f'O usuário "{usuario.nome}" foi cadastrado no sistema.')

    def emprestar_livro(self, titulo, nome_usuario):
        if self.verificar_disponibilidade(titulo):
            for livro in self.livros:
                if livro.titulo == titulo:
                    livro.copias -= 1
                    data_devolucao = datetime.now() + timedelta(days=90)
                    emprestimo = (livro, nome_usuario, data_devolucao)
                    self.emprestimos.append(emprestimo)
                    print(f'O livro "{livro.titulo}" foi emprestado para {nome_usuario}.')
                    print(f'Lembre-se: a data de devolução é {data_devolucao.strftime("%d/%m/%Y")}.')
                    return
        else:
            print('Livro não disponível para empréstimo.')

    def devolver_livro(self, titulo, nome_usuario):
        for emprestimo in self.emprestimos:
            if emprestimo[0].titulo == titulo and emprestimo[1] == nome_usuario:
                self.emprestimos.remove(emprestimo)
                emprestimo[0].copias += 1
                print(f'O livro "{titulo}" foi devolvido com sucesso.')
                return
        print('Livro não encontrado na lista de empréstimos ou não foi emprestado por este usuário.')

    def consultar_livros(self, criterio, termo):
        livros_encontrados = [livro for livro in self.livros if termo in getattr(livro, criterio)]
        if livros_encontrados:
            quebra_de_linha('Livros Encontrados')
            for livro in livros_encontrados:
                print(f"{livro.titulo} - {livro.autor} ({livro.ano}) - Cópias Disponíveis: {livro.copias}")
        else:
            print('Nenhum livro encontrado.')

    def gerar_relatorios(self):
        quebra_de_linha('Livros Disponíveis')
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} ({livro.ano}) - Cópias Disponíveis: {livro.copias}")

        quebra_de_linha('Livros Emprestados')
        for emprestimo in self.emprestimos:
            print(
                f"Livro: {emprestimo[0].titulo}, Nome do Usuário: {emprestimo[1]}, Data de Devolução: {emprestimo[2].strftime('%d/%m/%Y')}")

        quebra_de_linha('Usuários Cadastrados')
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}, ID: {usuario.identificacao}, Contato: {usuario.contato}")

    def menu(self):
        while True:
            print("\nMenu do Sistema de Biblioteca:")
            print("1. Cadastrar Livro")
            print("2. Cadastrar Usuário")
            print("3. Emprestar Livro")
            print("4. Devolver Livro")
            print("5. Consultar Livros")
            print("6. Gerar Relatórios")
            print("7. Sair")
            opcao = input("Digite sua escolha: ")
            if opcao == '1':
                titulo = input('Digite o título do livro: ')
                autor = input('Digite o autor do livro: ')
                ano = int(input('Digite o ano de publicação do livro: '))
                copias = int(input('Digite o número de cópias disponíveis: '))
                self.cadastrar_livro(titulo, autor, ano, copias)
            elif opcao == '2':
                nome = input('Digite o nome do usuário: ')
                identificacao = input('Digite a identificação do usuário: ')
                contato = input('Digite o contato do usuário: ')
                self.cadastrar_usuario(nome, identificacao, contato)
            elif opcao == '3':
                titulo = input('Digite o título do livro a ser emprestado: ')
                nome_usuario = input('Digite o nome do usuário que está pegando emprestado: ')
                self.emprestar_livro(titulo, nome_usuario)
            elif opcao == '4':
                titulo = input('Digite o título do livro a ser devolvido: ')
                nome_usuario = input('Digite o nome do usuário que está devolvendo: ')
                self.devolver_livro(titulo, nome_usuario)
            elif opcao == '5':
                criterio = input('Digite o critério de busca (titulo, autor, ano): ').lower()
                termo = input('Digite o termo de busca: ').lower()
                self.consultar_livros(criterio, termo)
            elif opcao == '6':
                self.gerar_relatorios()
            elif opcao == '7':
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    biblioteca = SistemaBiblioteca()
    biblioteca.menu()
