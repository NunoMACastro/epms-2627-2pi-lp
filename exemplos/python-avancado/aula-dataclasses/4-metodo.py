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
