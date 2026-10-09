"""Programa 3 das dataclasses: o tipo de um campo e a forma de dar os valores.

A classe Combate é a do programa 2. O primeiro combate dá ao vencedor um
número, em vez de um texto, e o segundo dá os três valores pelo nome dos
campos, por outra ordem. Antes de executares, prevê se o Python aceita o
primeiro combate, e por que ordem aparecem os campos do segundo.
"""

from dataclasses import dataclass


@dataclass
class Combate:
    """Registo de um combate, escrito como dataclass."""

    desafiante: str
    pokemon: str
    vencedor: str


# O tipo diz o que se espera, mas o Python não o verifica.
estranho = Combate("Ash", "Pikachu", 42)
print(estranho)

# Os valores também se podem dar pelo nome do campo.
outro = Combate(vencedor="Misty", desafiante="Gary", pokemon="Vulpix")
print(outro)
