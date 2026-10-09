"""Programa 1 das dataclasses: um registo de combate como classe normal.

A classe Combate só guarda três dados, o desafiante, o Pokémon e o vencedor,
mas o construtor tem de os receber e de os guardar um a um. Antes de
executares, prevê o que escrevem os três print, sobretudo o print(primeiro) e
a comparação dos dois combates com ==.
"""


class Combate:
    """Registo de um combate, escrito como uma classe normal."""

    def __init__(self, desafiante, pokemon, vencedor):
        """Cria um combate com o desafiante, o Pokémon e o vencedor."""
        # Cada nome escreve-se três vezes.
        self.desafiante = desafiante
        self.pokemon = pokemon
        self.vencedor = vencedor


primeiro = Combate("Ash", "Pikachu", "Ash")
repetido = Combate("Ash", "Pikachu", "Ash")

print(primeiro.vencedor)
print(primeiro)
print(primeiro == repetido)
