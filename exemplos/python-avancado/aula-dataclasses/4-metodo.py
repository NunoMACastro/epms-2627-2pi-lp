"""Programa 4 das dataclasses: uma dataclass com um método.

O método resumo escreve-se como em qualquer classe, com o self como primeiro
parâmetro, e chega aos campos do combate através do self.
"""

from dataclasses import dataclass


@dataclass
class Combate:
    """Registo de um combate, com um método como numa classe normal."""

    desafiante: str
    pokemon: str
    vencedor: str

    def resumo(self):
        """Devolve uma frase com o combate."""
        return f"{self.desafiante} com {self.pokemon}: venceu {self.vencedor}"


combate = Combate("Ash", "Pikachu", "Ash")
print(combate.resumo())
