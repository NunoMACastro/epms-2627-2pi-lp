"""Programa 6 das dataclasses: o que uma dataclass não faz.

O mesmo Pokémon escrito de duas maneiras: como dataclass, só com os dados, e
como classe normal, com a vida protegida por uma propriedade com o get e o
set. Os dois são criados com 500 de vida. Antes de executares, prevê com
quanta vida fica cada um.
"""

from dataclasses import dataclass


@dataclass
class PokemonDeDados:
    """Um Pokémon só com dados: a vida não tem regras."""

    nome: str
    vida: int


class Pokemon:
    """Um Pokémon com a vida protegida por uma propriedade."""

    def __init__(self, nome, vida):
        """Cria um Pokémon com nome e vida, passando pelo set."""
        self.nome = nome
        self.vida = vida

    @property
    def vida(self):
        """Get da vida."""
        return self._vida

    @vida.setter
    def vida(self, valor):
        """Set da vida: fica sempre entre 0 e 150."""
        if valor < 0:
            valor = 0
        elif valor > 150:
            valor = 150
        self._vida = valor


geodude = PokemonDeDados("Geodude", 500)
onix = Pokemon("Onix", 500)

print(geodude.vida)
print(onix.vida)
