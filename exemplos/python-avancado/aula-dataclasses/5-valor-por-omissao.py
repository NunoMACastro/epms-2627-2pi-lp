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
