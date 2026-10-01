"""Pokémon com propriedades e herança, o código das aulas de Python avançado.

Este ficheiro junta duas partes da matéria:

1. A classe Pokemon, com propriedades (get e set) que mantêm a vida entre
   0 e 150 e o ataque entre 1 e 50. Um valor fora dos limites é corrigido
   para o limite mais próximo, em vez de dar erro.
2. Três classes-filhas, PokemonFogo, PokemonAgua e PokemonPlanta, que herdam
   tudo da classe Pokemon e reescrevem o cálculo do dano com super().

O ficheiro ginasio.py, na mesma pasta, importa estas classes. Por isso a
demonstração do fim só corre quando este ficheiro é executado diretamente.
"""

VIDA_MINIMA = 0
VIDA_MAXIMA = 150
ATAQUE_MINIMO = 1
ATAQUE_MAXIMO = 50


class Pokemon:
    """Classe-mãe: o que todos os Pokémon têm e sabem fazer."""

    def __init__(self, nome, tipo, vida, ataque):
        """Cria um Pokémon com nome, tipo, vida e ataque."""
        self.nome = nome
        self.tipo = tipo
        # Passamos pelas propriedades para a validação dos sets
        # também se aplicar quando o objeto é criado.
        self.vida = vida
        self.ataque = ataque

    @property
    def vida(self):
        """Get da vida: devolve a vida atual."""
        return self._vida

    @vida.setter
    def vida(self, valor):
        """Set da vida: guarda o valor, sempre entre 0 e 150."""
        if valor < VIDA_MINIMA:
            valor = VIDA_MINIMA
        elif valor > VIDA_MAXIMA:
            valor = VIDA_MAXIMA
        self._vida = valor

    @property
    def ataque(self):
        """Get do ataque: devolve o valor de ataque."""
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        """Set do ataque: guarda o valor, sempre entre 1 e 50."""
        if valor < ATAQUE_MINIMO:
            valor = ATAQUE_MINIMO
        elif valor > ATAQUE_MAXIMO:
            valor = ATAQUE_MAXIMO
        self._ataque = valor

    def verificar_vida(self):
        """Mostra a vida do Pokémon e devolve True se ele ainda pode lutar."""
        if self.vida == 0:
            print(f"{self.nome} está KO (0/{VIDA_MAXIMA}).")
            return False
        print(f"{self.nome} tem {self.vida}/{VIDA_MAXIMA} de vida.")
        return True

    def calcular_dano(self, alvo):
        """Devolve quanta vida este Pokémon tira ao alvo num ataque.

        Na classe-mãe o dano é simplesmente o valor de ataque. As classes-filhas
        vão reescrever este método para aplicar as suas vantagens.
        """
        return self.ataque

    def atacar(self, alvo):
        """Ataca outro Pokémon e tira-lhe a vida calculada por calcular_dano."""
        if self.vida == 0:
            print(f"{self.nome} está KO e não pode atacar.")
            return
        if alvo.vida == 0:
            print(f"{alvo.nome} já está KO.")
            return
        # O Python chama a versão do método que pertence ao objeto: se self for
        # um PokemonFogo, é a versão do PokemonFogo que corre.
        dano = self.calcular_dano(alvo)
        print(f"{self.nome} ataca {alvo.nome} e tira {dano} de vida.")
        alvo.vida = alvo.vida - dano
        alvo.verificar_vida()


class PokemonFogo(Pokemon):
    """Um PokemonFogo É UM Pokemon: herda tudo e só muda o dano."""

    def __init__(self, nome, vida, ataque):
        # Um PokemonFogo é sempre do tipo "Fogo", por isso o tipo não se pede.
        super().__init__(nome, "Fogo", vida, ataque)

    def calcular_dano(self, alvo):
        """Contra Planta, o fogo tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Planta":
            print("É super eficaz!")
            dano = dano * 2
        return dano


class PokemonAgua(Pokemon):
    """Um PokemonAgua É UM Pokemon: herda tudo e só muda o dano."""

    def __init__(self, nome, vida, ataque):
        super().__init__(nome, "Água", vida, ataque)

    def calcular_dano(self, alvo):
        """Contra Fogo, a água tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Fogo":
            print("É super eficaz!")
            dano = dano * 2
        return dano


class PokemonPlanta(Pokemon):
    """Um PokemonPlanta É UM Pokemon, com um atributo e um método a mais."""

    def __init__(self, nome, vida, ataque, regeneracao):
        super().__init__(nome, "Planta", vida, ataque)
        self.regeneracao = regeneracao

    def calcular_dano(self, alvo):
        """Contra Água, a planta tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Água":
            print("É super eficaz!")
            dano = dano * 2
        return dano

    def recuperar(self):
        """Método novo, que só as plantas têm: recupera vida."""
        if self.vida == 0:
            print(f"{self.nome} está KO e não pode recuperar.")
            return
        # self.vida (a propriedade), e não self._vida: o set herdado continua
        # a impedir que a vida passe de 150.
        self.vida = self.vida + self.regeneracao
        print(f"{self.nome} recupera vida.")
        self.verificar_vida()


if __name__ == "__main__":
    # Os valores fora dos limites são corrigidos pelos sets logo na criação:
    # a vida 200 do Bulbasaur passa a 150 e o ataque 70 do Squirtle passa a 50.
    charmander = PokemonFogo("Charmander", 90, 40)
    bulbasaur = PokemonPlanta("Bulbasaur", 200, 25, 20)
    squirtle = PokemonAgua("Squirtle", 100, 70)
    print(f"{bulbasaur.nome}: vida {bulbasaur.vida}, ataque {bulbasaur.ataque}")
    print(f"{squirtle.nome}: vida {squirtle.vida}, ataque {squirtle.ataque}")
    print()
    charmander.atacar(bulbasaur)
    bulbasaur.recuperar()
    squirtle.atacar(charmander)
    charmander.atacar(squirtle)
    squirtle.atacar(charmander)
