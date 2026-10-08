class Combate:
    """Registo de um combate, escrito como uma classe normal."""

    def __init__(self, desafiante, pokemon, vencedor):
        # Cada nome escreve-se três vezes.
        self.desafiante = desafiante
        self.pokemon = pokemon
        self.vencedor = vencedor


primeiro = Combate("Ash", "Pikachu", "Ash")
repetido = Combate("Ash", "Pikachu", "Ash")

print(primeiro.vencedor)
print(primeiro)
print(primeiro == repetido)
