class Pessoa:
    olhos =2

    def __init__(self, *filhos, nome=None, idade = 33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'OlÃ¡ {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 33

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} -olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    lucio = Homem(nome ='Lucio')
    luciano = Pessoa(lucio, nome = 'Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = "Ramalho"
    luciano.olhos = 1
    print(luciano.__dict__)
    print(lucio.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(lucio.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa("anonimo")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(lucio, Pessoa))
    print(isinstance(lucio, Homem))