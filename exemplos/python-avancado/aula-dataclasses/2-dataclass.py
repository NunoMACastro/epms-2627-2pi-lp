from dataclasses import dataclass


@dataclass
class Combate:
    """Registo de um combate, escrito como dataclass."""

    desafiante: str
    pokemon: str
    vencedor: str


primeiro = Combate("Ash", "Pikachu", "Ash")
repetido = Combate("Ash", "Pikachu", "Ash")

print(primeiro.vencedor)
print(primeiro)
print(primeiro == repetido)
print(primeiro is repetido)
