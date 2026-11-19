![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Testes de comportamento com pytest numa sala de jogo online

Praticas, num programa que já funciona, a troca das recusas feitas com `print` por exceções e os testes dessas recusas com o pytest. Fazes os dois exercícios numa pasta nova, `sala-de-jogo`, com dois ficheiros, `sala.py` e `test_sala.py`. Se trabalhares num computador sem o pytest, instala-o primeiro, como no passo 4 de [Preparar o projeto](../laboratorios/05-testes-com-pytest-laboratorio.md#preparar-o-projeto), no laboratório.

## O cenário

Numa sala de um jogo online entram no máximo 4 jogadores, e só entra quem tem pelo menos o nível mínimo da sala. O programa seguinte já faz isto, mas, quando a sala recusa um pedido, só escreve uma mensagem com `print`. Copia-o para o `sala.py` e corre-o com `python3 sala.py`. Uma das recusas tem também um erro, que os teus testes vão apanhar.

```python
"""Sala de um jogo online: os jogadores entram e saem, até a sala encher.

Duas classes:

- Jogador guarda o nome e o nível de um jogador. É uma dataclass.
- Sala junta jogadores numa lista, no máximo LUGARES_DA_SALA, e só deixa
  entrar quem tem pelo menos o nível mínimo da sala.

Nesta versão, quando a sala não pode fazer o que lhe pedem, escreve uma
mensagem com print.
"""

from dataclasses import dataclass

LUGARES_DA_SALA = 4


@dataclass
class Jogador:
    """Um jogador, com o nome e o nível, um número inteiro."""

    nome: str
    nivel: int


class Sala:
    """Uma sala de jogo: tem um nome, um nível mínimo e os jogadores que lá estão."""

    def __init__(self, nome, nivel_minimo):
        """Cria uma sala vazia, com o nome e o nível mínimo para entrar, de 1 para cima."""
        if nivel_minimo < 1:
            print(f"O nível mínimo tem de ser pelo menos 1, e não {nivel_minimo}.")
        self.nome = nome
        self.nivel_minimo = nivel_minimo
        self.jogadores = []

    def entrar(self, jogador):
        """Junta o Jogador à sala, se houver lugar e se ele tiver o nível mínimo."""
        if len(self.jogadores) >= LUGARES_DA_SALA:
            print(f"A sala {self.nome} está cheia: {jogador.nome} ficou de fora.")
            return
        self.jogadores.append(jogador)
        if jogador.nivel < self.nivel_minimo:
            print(f"{jogador.nome} tem nível {jogador.nivel}, e a sala {self.nome} pede {self.nivel_minimo}.")

    def sair(self, nome):
        """Tira da sala o jogador com este nome, um texto."""
        for jogador in self.jogadores:
            if jogador.nome == nome:
                self.jogadores.remove(jogador)
                return
        print(f"{nome} não está na sala {self.nome}.")


if __name__ == "__main__":
    arena = Sala("Arena", 10)
    for jogador in [Jogador("Ana", 15), Jogador("Rui", 8), Jogador("Bia", 10)]:
        arena.entrar(jogador)
        print(f"{jogador.nome} entrou na sala.")

    arena.sair("Zé")
    print("Zé saiu da sala.")

    print("Na sala:")
    for jogador in arena.jogadores:
        print(f"- {jogador.nome}, nível {jogador.nivel}")
```

## Exercício 1: As recusas passam a exceções

As quatro recusas do `sala.py` passam a lançar exceções, cada uma com a mensagem que o `print` escrevia. Um valor que não serve recusa-se com o `ValueError` do Python. Uma regra da sala recusa-se com uma exceção tua, e as tuas exceções são filhas de `ErroDaSala`. Quando a sala recusa um pedido, fica exatamente como estava.

O programa do fim do ficheiro continua a correr até ao fim. Com `python3 sala.py`, passa a mostrar:

```text
Ana entrou na sala.
Recusado: Rui tem nível 8, e a sala Arena pede 10.
Bia entrou na sala.
Recusado: Zé não está na sala Arena.
Na sala:
- Ana, nível 15
- Bia, nível 10
```

## Exercício 2: Os testes

No `test_sala.py`, escreve um teste com cada nome desta lista. Cada teste confirma o que a descrição diz.

1. `test_entrar_junta_o_jogador_a_sala`: Um jogador com nível acima do mínimo entra numa sala vazia e fica na lista da sala.
2. `test_um_jogador_com_o_nivel_minimo_exato_pode_entrar`: Um jogador com o nível igual ao mínimo da sala é aceite.
3. `test_a_sala_cheia_recusa_o_quinto_e_depois_de_um_jogador_sair_ja_o_aceita`: Numa sala com 4 jogadores, um quinto jogador é recusado. Depois de sair um jogador do meio da lista, o mesmo quinto jogador já entra. No fim, confirma quem está na sala, e por que ordem.
4. `test_sair_um_jogador_que_nao_esta_na_sala_e_recusado`: Pedir a saída de um jogador que não está na sala é recusado, e quem lá estava continua na sala.
5. `test_entrar_com_nivel_abaixo_do_minimo_e_recusado_e_a_sala_fica_igual`: Um jogador com nível abaixo do mínimo é recusado, e a sala fica exatamente com os jogadores que tinha.
6. `test_criar_uma_sala_com_nivel_minimo_0_e_recusado`: Criar uma sala com nível mínimo 0 é recusado.
7. `test_as_recusas_das_regras_da_sala_sao_todas_erros_da_sala`: Cada uma das recusas das regras da sala é da família `ErroDaSala`.

## Critérios de conclusão

- Cada recusa lança uma exceção, e as das regras são filhas de `ErroDaSala`.
- Nenhuma recusa muda a sala.
- `python3 sala.py` mostra exatamente a saída do exercício 1.
- O `test_sala.py` tem os 7 testes da lista, e `python3 -m pytest` passa sem falhas.

![Rodapé](../../imagens/rodape.png)
