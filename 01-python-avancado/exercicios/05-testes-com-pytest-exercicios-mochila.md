![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Testes de comportamento com pytest na mochila de uma personagem

Praticas, num programa que já funciona, a troca das recusas feitas com `print` por exceções e os testes dessas recusas com o pytest. Fazes os dois exercícios numa pasta nova, `mochila-da-personagem`, com dois ficheiros, `personagem.py` e `test_personagem.py`. Se trabalhares num computador sem o pytest, instala-o primeiro, como no passo 4 de [Preparar o projeto](../laboratorios/05-testes-com-pytest-laboratorio.md#preparar-o-projeto), no laboratório.

## O cenário

Uma personagem de um jogo compra itens com moedas, guarda-os numa mochila com 3 lugares e pode vendê-los pelo mesmo preço. O programa seguinte já faz isto, mas, quando uma compra ou uma venda é recusada, só escreve uma mensagem com `print`. Copia-o para o `personagem.py` e corre-o com `python3 personagem.py`. Uma das recusas tem também um erro, que os teus testes vão apanhar.

```python
"""Personagem de um jogo: compra e vende itens, e guarda-os na mochila.

Duas classes:

- Item guarda o nome e o preço de um item. É uma dataclass.
- Personagem tem moedas e uma mochila, uma lista com no máximo
  LUGARES_DA_MOCHILA itens. Comprar gasta moedas, e vender devolve-as.

Nesta versão, quando a personagem não pode fazer o que lhe pedem, escreve uma
mensagem com print.
"""

from dataclasses import dataclass

LUGARES_DA_MOCHILA = 3


@dataclass
class Item:
    """Um item do jogo, com o nome e o preço, em moedas."""

    nome: str
    preco: int


class Personagem:
    """Uma personagem: tem um nome, as moedas e a mochila com os itens."""

    def __init__(self, nome, moedas):
        """Cria uma personagem com o nome, as moedas, de 0 para cima, e a mochila vazia."""
        if moedas < 0:
            print(f"As moedas não podem ser negativas: {moedas}.")
        self.nome = nome
        self.moedas = moedas
        self.mochila = []

    def comprar(self, item):
        """Guarda o Item na mochila e paga-o com as moedas, se houver lugar e moedas."""
        if len(self.mochila) >= LUGARES_DA_MOCHILA:
            print(f"A mochila de {self.nome} está cheia: {item.nome} ficou de fora.")
            return
        self.mochila.append(item)
        if item.preco > self.moedas:
            print(f"{self.nome} tem {self.moedas} moedas, e {item.nome} custa {item.preco}.")
            return
        self.moedas = self.moedas - item.preco

    def vender(self, nome):
        """Tira da mochila o item com este nome, um texto, e recebe o preço dele em moedas."""
        for item in self.mochila:
            if item.nome == nome:
                self.mochila.remove(item)
                self.moedas = self.moedas + item.preco
                return
        print(f"{nome} não está na mochila de {self.nome}.")


if __name__ == "__main__":
    kai = Personagem("Kai", 30)
    for item in [Item("Espada", 20), Item("Escudo", 15), Item("Poção", 5)]:
        kai.comprar(item)
        print(f"Kai comprou: {item.nome}.")

    kai.vender("Elmo")
    print("Kai vendeu: Elmo.")

    print(f"Moedas: {kai.moedas}")
    print("Na mochila:")
    for item in kai.mochila:
        print(f"- {item.nome}, {item.preco} moedas")
```

## Exercício 1: As recusas passam a exceções

As quatro recusas do `personagem.py` passam a lançar exceções, cada uma com a mensagem que o `print` escrevia. Um valor que não serve recusa-se com o `ValueError` do Python. Uma regra do jogo recusa-se com uma exceção tua, e as tuas exceções são filhas de `ErroDaPersonagem`. Quando uma compra ou uma venda é recusada, as moedas e a mochila ficam exatamente como estavam.

O programa do fim do ficheiro continua a correr até ao fim. Com `python3 personagem.py`, passa a mostrar:

```text
Kai comprou: Espada.
Recusado: Kai tem 10 moedas, e Escudo custa 15.
Kai comprou: Poção.
Recusado: Elmo não está na mochila de Kai.
Moedas: 5
Na mochila:
- Espada, 20 moedas
- Poção, 5 moedas
```

## Exercício 2: Os testes

No `test_personagem.py`, escreve um teste com cada nome desta lista. Cada teste confirma o que a descrição diz.

1. `test_comprar_junta_o_item_a_mochila_e_desconta_as_moedas`: Comprar um item que a personagem consegue pagar põe-no na mochila e tira o preço às moedas.
2. `test_comprar_um_item_com_as_moedas_exatas_deixa_0_moedas`: Uma personagem com as moedas exatas para um item compra-o e fica sem moedas.
3. `test_a_mochila_cheia_recusa_o_quarto_item_e_depois_de_uma_venda_ja_o_aceita`: Com a mochila cheia, a compra de um quarto item é recusada. Depois de se vender um item do meio da mochila, a compra do mesmo quarto item já é aceite. No fim, confirma os itens da mochila, por ordem, e as moedas.
4. `test_vender_um_item_que_nao_esta_na_mochila_e_recusado`: Vender um item que não está na mochila é recusado, e as moedas e a mochila ficam como estavam.
5. `test_comprar_sem_moedas_suficientes_e_recusado_e_a_mochila_fica_igual`: Comprar um item mais caro do que as moedas que a personagem tem é recusado, e as moedas e a mochila ficam como estavam.
6. `test_criar_uma_personagem_com_moedas_negativas_e_recusado`: Criar uma personagem com moedas negativas é recusado.
7. `test_as_recusas_das_regras_da_personagem_sao_todas_erros_da_personagem`: Cada uma das recusas das regras do jogo é da família `ErroDaPersonagem`.

## Critérios de conclusão

- Cada recusa lança uma exceção, e as das regras são filhas de `ErroDaPersonagem`.
- Nenhuma recusa muda as moedas nem a mochila.
- `python3 personagem.py` mostra exatamente a saída do exercício 1.
- O `test_personagem.py` tem os 7 testes da lista, e `python3 -m pytest` passa sem falhas.

![Rodapé](../../imagens/rodape.png)
