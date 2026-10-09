"""Programa 7 das dataclasses: um engano de propósito, um campo sem tipo.

Este programa acaba com uma mensagem de erro, e é isso que deve fazer. Compara
a classe com a do programa 2, para veres onde está o campo sem tipo, e lê a
última linha da mensagem.
"""

from dataclasses import dataclass


@dataclass
class Combate:
    """Engano de propósito: o vencedor não tem tipo."""

    desafiante: str
    pokemon: str
    vencedor = ""


combate = Combate("Ash", "Pikachu", "Ash")
