"""Programa 2 das dataclasses: o mesmo registo de combate, com @dataclass.

Os três campos escrevem-se com o nome, dois pontos e o tipo, e a classe não
tem nenhum construtor escrito por nós. O programa principal é o do
programa 1, com mais uma linha no fim, que usa o is. Antes de executares,
prevê o que muda em cada um dos quatro print.
"""

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
