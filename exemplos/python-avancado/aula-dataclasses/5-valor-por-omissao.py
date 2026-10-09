"""Programa 5 das dataclasses: um campo com valor por omissão.

O campo cura tem um valor escrito a seguir ao tipo, que se usa quando quem
cria a poção não dá outro. Antes de executares, prevê quanto cura cada uma
das duas poções e o número da última linha.
"""

from dataclasses import dataclass


@dataclass
class Pocao:
    """Uma poção. Se ninguém disser quanto cura, cura 20."""

    nome: str
    cura: int = 20


normal = Pocao("Poção")
forte = Pocao("Super Poção", 50)

print(normal)
print(forte)
print(normal.cura + forte.cura)
