"""Ginásio Pokémon: composição e agregação, o código das aulas de Python avançado.

Três classes que guardam outros objetos:

- Treinador tem uma equipa de Pokémon. É uma agregação: os Pokémon são
  criados fora do treinador e continuam a existir sem ele.
- Ginasio tem um líder e uma lista de desafiantes, que são treinadores criados
  fora (agregação), e guarda o registo dos seus combates (composição): os
  objetos Combate só são criados pelo ginásio, dentro do método combater,
  e só o ginásio os guarda.
- Combate é o registo de um combate: quem desafiou, com que Pokémon e quem
  venceu.

As classes de Pokémon vêm do ficheiro pokemon.py, que tem de estar na mesma
pasta que este.
"""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


class Treinador:
    """Um treinador tem uma equipa de Pokémon (agregação)."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        # AGREGAÇÃO: a equipa começa vazia e recebe Pokémon que já existiam.
        self.equipa = []

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador."""
        self.equipa.append(pokemon)

    def escolher_pokemon(self):
        """Devolve o primeiro Pokémon da equipa que ainda pode lutar, ou None."""
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                return pokemon
        return None


class Combate:
    """Registo de um combate. Só o ginásio cria registos (composição)."""

    def __init__(self, desafiante, pokemon_desafiante, vencedor):
        """Guarda os nomes do desafiante, do seu Pokémon e do vencedor."""
        self.desafiante = desafiante
        self.pokemon_desafiante = pokemon_desafiante
        self.vencedor = vencedor

    def resumo(self):
        """Devolve uma linha de texto que descreve o combate."""
        return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"


class Ginasio:
    """Um ginásio tem um líder e recebe desafiantes (agregação)
    e guarda o registo dos seus combates (composição)."""

    def __init__(self, cidade, lider):
        """Cria um ginásio com a cidade e o líder, e as duas listas vazias."""
        self.cidade = cidade
        self.lider = lider              # AGREGAÇÃO: Treinador criado fora
        self.desafiantes = []           # AGREGAÇÃO: existem sem o ginásio
        self.combates = []              # COMPOSIÇÃO: só o ginásio os cria

    def combater(self, desafiante):
        """Um combate entre o primeiro Pokémon com vida de cada treinador."""
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
        print(f"\n=== {desafiante.nome} desafia {self.lider.nome} no ginásio de {self.cidade} ===")
        while True:
            atacante.atacar(defensor)
            if defensor.vida == 0:
                vencedor = desafiante
                break
            defensor.atacar(atacante)
            if atacante.vida == 0:
                vencedor = self.lider
                break
        # O registo nasce aqui dentro: é o ginásio que o cria e o guarda.
        self.combates.append(Combate(desafiante.nome, atacante.nome, vencedor.nome))

    def mostrar_historico(self):
        """Mostra o resumo de todos os combates deste ginásio."""
        print(f"\nHistórico do ginásio de {self.cidade}:")
        for combate in self.combates:
            print(" -", combate.resumo())


if __name__ == "__main__":
    misty = Treinador("Misty")
    misty.capturar(PokemonAgua("Starmie", 120, 35))
    ash = Treinador("Ash")
    ash.capturar(PokemonFogo("Charmander", 90, 40))
    ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
    cerulean = Ginasio("Cerulean", misty)
    cerulean.combater(ash)
    cerulean.combater(ash)
    cerulean.mostrar_historico()
    # Apagar o ginásio apaga os registos dos combates, que só ele guardava.
    # Os treinadores e os seus Pokémon continuam a existir.
    del cerulean
    print(f"\n{ash.nome} continua com {len(ash.equipa)} Pokémon; {misty.nome} continua com {len(misty.equipa)}.")
