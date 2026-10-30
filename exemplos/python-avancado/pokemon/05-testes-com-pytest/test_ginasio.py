"""Testes do treinador, do líder e do ginásio, o código das aulas de Python avançado.

Os testes das recusas usam o pytest.raises, que confirma que uma linha lança
uma exceção, e depois confirmam que o objeto ficou como estava. Vários testes
precisam de um ginásio igual, e é a fixture cerulean que o prepara: o pytest
chama-a de novo para cada teste que a pede, e por isso cada teste recebe um
ginásio novo, sem combates de outros testes.
"""

import pytest

from erros import EquipaCheia, SemPokemonComVida
from ginasio import Combate, Ginasio, Lider, Treinador
from pokemon import Pokemon, PokemonAgua, PokemonFogo, PokemonPlanta


@pytest.fixture
def cerulean():
    """Devolve um ginásio novo em Cerulean, com a Misty como líder e só a Starmie."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
    return Ginasio("Cerulean", misty)


def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
    """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
    # Preparar: seis capturas, que têm de correr sem exceção.
    brock = Treinador("Brock")
    for numero in range(6):
        brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
    # Fazer e confirmar: a sétima captura tem de lançar EquipaCheia.
    with pytest.raises(EquipaCheia):
        brock.capturar(Pokemon("Onix", "Pedra", 50, 20))
    # Confirmar: a recusa não mexeu na equipa.
    assert len(brock.equipa) == 6


def test_combate_sem_pokemon_com_vida_e_recusado(cerulean):
    """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
    ash = Treinador("Ash")

    with pytest.raises(SemPokemonComVida):
        cerulean.combater(ash)

    assert cerulean.desafiantes == []
    assert cerulean.combates == []


def test_o_desafiante_que_vence_fica_registado(cerulean):
    """Quando o desafiante ganha, o registo do combate diz o nome dele."""
    ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])

    cerulean.combater(ash)

    # Combate é uma dataclass: o == compara os três campos dos dois registos.
    assert cerulean.combates == [Combate("Ash", "Bulbasaur", "Ash")]


def test_o_lider_que_vence_fica_registado(cerulean):
    """Quando o líder ganha, o registo do combate diz o nome do líder."""
    ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])

    cerulean.combater(ash)

    assert cerulean.combates == [Combate("Ash", "Charmander", "Misty")]


def test_o_lider_escolhe_o_pokemon_com_mais_vida():
    """O líder escolhe o Pokémon com mais vida, mesmo que não seja o primeiro."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35), PokemonAgua("Staryu", 120, 20)])

    escolhido = misty.escolher_pokemon()

    assert escolhido.nome == "Staryu"


def test_o_lider_com_todos_ko_nao_escolhe_nenhum():
    """Com todos os Pokémon KO, o líder não escolhe nenhum: devolve None."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Psyduck", 0, 35), PokemonAgua("Goldeen", 0, 20)])

    escolhido = misty.escolher_pokemon()

    assert escolhido is None


def test_o_lider_com_a_equipa_vazia_nao_escolhe_nenhum():
    """Com a equipa vazia, o líder também devolve None, sem dar erro."""
    misty = Lider("Misty")

    escolhido = misty.escolher_pokemon()

    assert escolhido is None
