"""Programa 8 das dataclasses: outro engano de propósito, falta o @dataclass.

Este programa também acaba com uma mensagem de erro, e é isso que deve fazer.
Compara-o com o programa 2, para veres onde devia estar o @dataclass, e lê a
última linha da mensagem.
"""


class Combate:
    """Engano de propósito: falta o @dataclass."""

    desafiante: str
    pokemon: str
    vencedor: str


combate = Combate("Ash", "Pikachu", "Ash")
