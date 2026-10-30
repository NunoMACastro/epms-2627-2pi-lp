"""Anunciadores de combates: duck typing, o código das aulas de Python avançado.

O Ginasio, no ficheiro ginasio.py, anuncia os combates com
anunciador.anunciar(combate). Estas duas classes não têm nenhuma classe-mãe em
comum, nem com o ginásio: só têm um método com o mesmo nome e os mesmos
parâmetros. Para o ginásio, é quanto basta.
"""


class Narrador:
    """Anuncia cada combate como um locutor, com entusiasmo."""

    def anunciar(self, combate):
        """Escreve o anúncio do combate, numa frase longa."""
        print(f"E atenção! {combate.desafiante} entrou com {combate.pokemon_desafiante}...")
        print(f"... e o vencedor é {combate.vencedor}! Que combate!")


class Placard:
    """Mostra cada combate numa linha curta, como um placard do ginásio."""

    def __init__(self):
        """Cria o placard com o contador de combates a zero."""
        self.numero = 0

    def anunciar(self, combate):
        """Escreve uma linha numerada com o desafiante e o vencedor."""
        self.numero = self.numero + 1
        print(f"[{self.numero}] {combate.desafiante} | vencedor: {combate.vencedor}")
