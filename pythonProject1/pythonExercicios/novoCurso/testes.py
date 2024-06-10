
#  função decoradoura ...............
def listaTelefonica(funcao):
    def slave():
        print('esses sao os contatos localizados')
        funcao()
    return slave

# decorador ..............
@listaTelefonica
def cade():
    print('ak')



