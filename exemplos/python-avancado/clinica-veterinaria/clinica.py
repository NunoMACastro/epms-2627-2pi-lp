"""Clínica veterinária: revisão de POO e primeiro contacto com os métodos de classe.

Este ficheiro junta, num exemplo pequeno, a matéria das aulas:

1. Herança: Cao e Gato SÃO Animais. Herdam tudo da classe Animal e
   reescrevem o som; o Cao reescreve também o preço da consulta, com super().
2. Três tipos de método na classe Animal: métodos do objeto (recebem self),
   um método estático (não recebe nem self nem cls) e um método de classe
   (recebe cls, a própria classe). A idade é uma propriedade (get e set), e
   o set usa o método estático para decidir se a idade é válida.
3. Agregação e composição na classe Clinica: os animais são criados fora da
   clínica e continuam a existir sem ela; as consultas só são criadas e
   guardadas pela clínica.

Para correr: python3 clinica.py. A demonstração do fim do ficheiro mostra os
três tipos de método, a propriedade e a clínica a trabalhar.
"""

IDADE_MAXIMA = 30
PRECO_BASE = 30
PRECO_VACINA = 15


class Animal:
    """Classe-mãe: o que todos os animais da clínica têm e sabem fazer."""

    def __init__(self, nome, idade):
        """Cria um animal com nome e idade.

        nome: texto com o nome do animal.
        idade: número inteiro de anos. Passa pelo set da propriedade idade, por
        isso uma idade inválida não dá erro: o animal fica com 0 anos.
        """
        # O nome vem primeiro, porque o set da idade usa self.nome na mensagem.
        self.nome = nome
        # Passamos pela propriedade para a validação do set também se aplicar
        # quando o objeto é criado.
        self.idade = idade

    @property
    def idade(self):
        """Get da idade: devolve a idade atual, um número inteiro de anos."""
        return self._idade

    @idade.setter
    def idade(self, valor):
        """Set da idade: guarda o valor se for válido; senão, guarda 0.

        valor: número inteiro de anos. É válido se o método estático
        idade_valida disser que sim. Quando não é, escreve uma mensagem com o
        nome do animal e a idade fica 0, em vez de dar erro.
        """
        if Animal.idade_valida(valor):
            self._idade = valor
        else:
            print(f"Idade {valor} inválida para {self.nome}: fica com 0 anos.")
            self._idade = 0

    @staticmethod
    def idade_valida(idade):
        """Método estático: diz se uma idade pode ser a de um animal da clínica.

        Não usa nenhum animal (não tem self) nem a classe (não tem cls): só
        precisa do número que recebe, e por isso funciona sem nenhum animal criado.

        idade: número inteiro de anos que se quer testar.
        Devolve True se a idade estiver entre 0 e IDADE_MAXIMA (inclusive), e
        False se não estiver.
        """
        return idade >= 0 and idade <= IDADE_MAXIMA

    @classmethod
    def recem_nascido(cls, nome):
        """Método de classe: cria um animal acabado de nascer, com 0 anos.

        Recebe a classe em cls. Em Cao.recem_nascido("Bobi"), cls é Cao e o
        objeto criado é um Cao; em Gato.recem_nascido("Tareco"), cls é Gato
        e o objeto criado é um Gato. Serve a todas as classes-filhas porque elas
        se criam com os mesmos argumentos que a mãe.

        nome: texto com o nome do animal.
        Devolve um objeto novo da classe por onde o método foi chamado.
        """
        return cls(nome, 0)

    def fazer_som(self):
        """Método do objeto: devolve o som do animal, em texto.

        Na classe-mãe é só reticências. As classes-filhas reescrevem-no.
        """
        return "..."

    def preco_consulta(self):
        """Método do objeto: devolve quanto custa uma consulta para este animal.

        O preço é um número de euros. Na classe-mãe é o preço base, e as
        classes-filhas podem reescrevê-lo.
        """
        return PRECO_BASE

    def apresentar(self):
        """Método do objeto: escreve o nome, a idade e o som deste animal.

        Não devolve nada: o resultado é a linha que aparece no ecrã.
        """
        print(f"{self.nome}, {self.idade} anos: {self.fazer_som()}")


class Cao(Animal):
    """Um Cao É UM Animal: herda tudo e muda o som e o preço da consulta."""

    def fazer_som(self):
        """Devolve o som de um cão, em texto."""
        return "Ão ão!"

    def preco_consulta(self):
        """Devolve o preço da consulta de um cão, em euros.

        A consulta de um cão inclui a vacina: é o preço base, que vem da
        classe-mãe pelo super(), mais o preço da vacina.
        """
        return super().preco_consulta() + PRECO_VACINA


class Gato(Animal):
    """Um Gato É UM Animal: herda tudo e só muda o som."""

    def fazer_som(self):
        """Devolve o som de um gato, em texto."""
        return "Miau!"


class Consulta:
    """Registo de uma consulta. Só a clínica cria consultas (composição)."""

    def __init__(self, nome_animal, motivo, preco):
        """Guarda o que ficou registado sobre uma consulta.

        nome_animal: texto com o nome do animal atendido.
        motivo: texto com o motivo da consulta.
        preco: número com o preço da consulta, em euros.
        """
        self.nome_animal = nome_animal
        self.motivo = motivo
        self.preco = preco

    def resumo(self):
        """Devolve uma linha de texto que descreve a consulta, com o preço."""
        return f"{self.nome_animal}: {self.motivo} ({self.preco} euros)"


class Clinica:
    """Uma clínica tem pacientes (agregação) e guarda as suas consultas
    (composição)."""

    def __init__(self, nome):
        """Cria uma clínica com um nome e as duas listas vazias.

        nome: texto com o nome da clínica.
        """
        self.nome = nome
        self.pacientes = []   # AGREGAÇÃO: animais criados fora da clínica
        self.consultas = []   # COMPOSIÇÃO: só a clínica cria as consultas

    def registar(self, animal):
        """Junta aos pacientes um animal que foi criado fora da clínica.

        animal: um Animal, ou de uma classe-filha. Se já está registado, não
        volta a ser juntado. Não devolve nada.
        """
        if animal not in self.pacientes:
            self.pacientes.append(animal)

    def atender(self, animal, motivo):
        """Atende um paciente registado e cria o registo da consulta.

        animal: o Animal a atender. Tem de estar registado; se não estiver, o
        método escreve uma mensagem e não cria nenhuma consulta.
        motivo: texto com o motivo da consulta.
        Não devolve nada: a consulta fica na lista consultas da clínica.
        """
        if animal not in self.pacientes:
            print(f"{animal.nome} não está registado na {self.nome}.")
            return
        # O Python chama a versão de preco_consulta que pertence ao objeto:
        # se animal for um Cao, é a versão do Cao que corre.
        preco = animal.preco_consulta()
        # A consulta nasce aqui dentro: é a clínica que a cria e a guarda.
        self.consultas.append(Consulta(animal.nome, motivo, preco))

    def mostrar_consultas(self):
        """Escreve o título e o resumo de todas as consultas desta clínica.

        Não devolve as consultas: quem chama só recebe texto no ecrã.
        """
        print(f"\nConsultas da {self.nome}:")
        for consulta in self.consultas:
            print(" -", consulta.resumo())


if __name__ == "__main__":
    # Método estático: chama-se pela classe, sem nenhum animal criado.
    print(Animal.idade_valida(5))
    print(Animal.idade_valida(-2))

    # Duas formas de criar objetos: o construtor e o método de classe.
    rex = Cao("Rex", 7)
    bobi = Cao.recem_nascido("Bobi")        # cls é Cao: o Bobi é um Cao
    tareco = Gato.recem_nascido("Tareco")   # cls é Gato: o Tareco é um Gato
    print()
    rex.apresentar()
    bobi.apresentar()
    tareco.apresentar()

    # Propriedade: o set valida a idade também depois de o animal existir.
    print()
    rex.idade = 8
    rex.idade = -5
    rex.apresentar()

    clinica = Clinica("Clínica Patudos")
    clinica.registar(rex)
    clinica.registar(tareco)
    clinica.atender(rex, "Dor numa pata")
    clinica.atender(tareco, "Cortar as unhas")
    clinica.atender(bobi, "Primeira consulta")   # o Bobi não foi registado
    clinica.mostrar_consultas()

    # Apagar a clínica apaga as consultas, que só ela guardava.
    # Os animais continuam a existir.
    del clinica
    print()
    rex.apresentar()
