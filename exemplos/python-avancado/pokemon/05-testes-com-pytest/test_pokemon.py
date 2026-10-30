"""Testes das classes de Pokémon, o código das aulas de Python avançado.

Cada função cujo nome começa por test_ é um teste. O pytest encontra-as
sozinho, corre-as uma a uma e diz quais passaram e quais falharam. Para os
correr, abre o terminal na pasta deste ficheiro e escreve python3 -m pytest.

Os testes estão por esta ordem: as vantagens de tipo, o KO, os limites da
vida e do ataque, e a recuperação das plantas. Cada um cria os Pokémon de que
precisa, por isso nenhum depende de outro nem da ordem por que correm.
"""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


def test_fogo_contra_planta_tira_o_dobro():
    """O fogo tem vantagem contra a planta: o dano é o dobro do ataque."""
    # Preparar: os dois Pokémon do combate.
    charmander = PokemonFogo("Charmander", 90, 40)
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    # Fazer: só a ação que se está a testar.
    dano = charmander.calcular_dano(bulbasaur)
    # Confirmar: o resultado que as regras do jogo pedem.
    assert dano == 80


def test_agua_contra_fogo_tira_o_dobro():
    """A água tem vantagem contra o fogo: o dano é o dobro do ataque."""
    squirtle = PokemonAgua("Squirtle", 100, 30)
    charmander = PokemonFogo("Charmander", 90, 40)

    dano = squirtle.calcular_dano(charmander)

    assert dano == 60


def test_planta_contra_agua_tira_o_dobro():
    """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    dano = bulbasaur.calcular_dano(squirtle)

    assert dano == 50


def test_fogo_contra_agua_tira_so_o_ataque():
    """Sem vantagem, o dano é o próprio ataque."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    dano = charmander.calcular_dano(squirtle)

    assert dano == 40


def test_planta_contra_fogo_tira_so_o_ataque():
    """Teste de regressão: o dano a dobrar do tema 04 não pode voltar.

    Com a multiplicação fora do if, a planta tirava o dobro a qualquer alvo.
    O teste da planta contra a água não dá por isso, porque aí o dobro está
    certo. Só um alvo sem vantagem, como o fogo, distingue as duas versões.
    """
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    charmander = PokemonFogo("Charmander", 90, 40)

    dano = bulbasaur.calcular_dano(charmander)

    assert dano == 25


def test_ataque_que_tira_a_vida_toda_deixa_ko():
    """Um ataque que tira exatamente a vida que resta deixa o alvo com 0."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 40, 30)

    charmander.atacar(squirtle)

    assert squirtle.vida == 0


def test_ataque_maior_do_que_a_vida_nao_deixa_vida_negativa():
    """Um ataque maior do que a vida que resta deixa o alvo com 0, e não abaixo."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 25, 30)

    charmander.atacar(squirtle)

    assert squirtle.vida == 0


def test_pokemon_ko_nao_ataca():
    """Um Pokémon KO não tira vida a ninguém."""
    charmander = PokemonFogo("Charmander", 0, 40)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    charmander.atacar(squirtle)

    assert squirtle.vida == 100


def test_vida_no_maximo_fica_como_esta():
    """150 é o último valor de vida que fica como foi pedido."""
    charmander = PokemonFogo("Charmander", 150, 40)

    assert charmander.vida == 150


def test_vida_acima_do_maximo_fica_no_maximo():
    """151 é o primeiro valor de vida acima do limite, e passa a 150."""
    charmander = PokemonFogo("Charmander", 151, 40)

    assert charmander.vida == 150


def test_vida_negativa_fica_a_zero():
    """-1 é o primeiro valor de vida abaixo do limite, e passa a 0."""
    charmander = PokemonFogo("Charmander", -1, 40)

    assert charmander.vida == 0


def test_ataque_abaixo_do_minimo_fica_no_minimo():
    """O ataque vai de 1 a 50: 0 passa a 1."""
    charmander = PokemonFogo("Charmander", 90, 0)

    assert charmander.ataque == 1


def test_ataque_acima_do_maximo_fica_no_maximo():
    """O ataque vai de 1 a 50: 51 passa a 50."""
    charmander = PokemonFogo("Charmander", 90, 51)

    assert charmander.ataque == 50


def test_planta_recupera_ate_ao_maximo():
    """A recuperação passa pelo set da vida, que não a deixa passar de 150."""
    bulbasaur = PokemonPlanta("Bulbasaur", 140, 25, 20)

    bulbasaur.recuperar()

    assert bulbasaur.vida == 150


def test_planta_ko_nao_recupera():
    """Uma planta KO não recupera: fica com 0 de vida."""
    bulbasaur = PokemonPlanta("Bulbasaur", 0, 25, 20)

    bulbasaur.recuperar()

    assert bulbasaur.vida == 0
