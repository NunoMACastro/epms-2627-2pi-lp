from dataclasses import dataclass


@dataclass
class Combate:
    """Engano de propósito: o vencedor não tem tipo."""

    desafiante: str
    pokemon: str
    vencedor = ""


combate = Combate("Ash", "Pikachu", "Ash")
