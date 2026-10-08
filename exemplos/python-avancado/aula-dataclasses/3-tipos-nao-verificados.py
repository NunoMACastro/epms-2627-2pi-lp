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
