"""Exceções próprias do ginásio Pokémon, o código das aulas de Python avançado.

Todas herdam de ErroDoGinasio, que herda de Exception. Assim, quem quiser
apanhar qualquer erro do ginásio escreve except ErroDoGinasio, e quem quiser
apanhar só um caso escreve o nome da classe-filha.
"""


class ErroDoGinasio(Exception):
    """Classe-mãe de todos os erros do ginásio Pokémon."""


class EquipaCheia(ErroDoGinasio):
    """Um treinador tentou capturar um Pokémon com a equipa já completa."""


class SemPokemonComVida(ErroDoGinasio):
    """Um combate não pode começar: um dos treinadores não tem Pokémon com vida."""
