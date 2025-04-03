'''Gestão de cadastro usando POO com retorno de pessoa por genero e media de idade.'''


class Pessoa:
    def __init__(self, nome, genero, idade):
        self.nome = nome
        self.genero = genero
        self.idade = idade

    def pessoa_info(self):
        print(f'{self.nome},{self.genero},{self.idade}')


class Cadastro:
    def __init__(self):
        self.lista = []

    def cadastrar(self, nova_pessoa):
        self.lista.append(nova_pessoa)

    def mostra(self):
        print(f'\nTemos um total de {len(self.lista)} pessoas cadastras')
        print('\nMostrar todas as pessoas:')
        for p in self.lista:
            p.pessoa_info()

    def listar_por_genero(self, genero):
        print(f'\nPessoas do genero {genero}:')
        for p in self.lista:
            if p.genero.lower() == genero.lower():
                p.pessoa_info()

    def media_idade_por_genero(self, genero):
        total_idade = 0
        contador = 0
        for p in self.lista:
            if p.genero.lower() == genero.lower():
                total_idade += p.idade
                contador += 1

        if contador > 0:
            media = total_idade / contador
            print(f"\nMédia de idade para o gênero {genero}: {media:.2f}")
        else:
            print(f"\nNenhuma pessoa do gênero {genero} cadastrada.\n")


def main():
    cadastro = Cadastro()
    lista_de_pessaos = [{'nome': 'wagner', 'genero': 'masculino', 'idade': 20},
                        {'nome': 'diego', 'genero': 'masculino', 'idade': 30},
                        {'nome': 'robson', 'genero': 'masculino', 'idade': 27},
                        {'nome': 'wanessa', 'genero': 'feminino', 'idade': 20},
                        {'nome': 'carol', 'genero': 'feminino', 'idade': 10}]

    for pessoa in lista_de_pessaos:
        nova_pessoa = Pessoa(pessoa['nome'], pessoa['genero'], pessoa['idade'])
        cadastro.cadastrar(nova_pessoa)
    cadastro.mostra()
    cadastro.listar_por_genero("masculino")
    cadastro.media_idade_por_genero("masculino")
    cadastro.listar_por_genero("feminino")
    cadastro.media_idade_por_genero("feminino")


if __name__ == "__main__":
    main()
