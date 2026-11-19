![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Testes de comportamento com pytest numa estação de trotinetes

Praticas, num programa que já funciona, a troca das recusas feitas com `print` por exceções e os testes dessas recusas com o pytest. Fazes os dois exercícios numa pasta nova, `estacao-de-trotinetes`, com dois ficheiros, `estacao.py` e `test_estacao.py`. Se trabalhares num computador sem o pytest, instala-o primeiro, como no passo 4 de [Preparar o projeto](../laboratorios/05-testes-com-pytest-laboratorio.md#preparar-o-projeto), no laboratório.

## O cenário

Numa estação de trotinetes elétricas, as trotinetes estacionam até a estação encher, e só se aluga uma trotinete com pelo menos 20% de bateria. O programa seguinte já faz isto, mas, quando a estação recusa um pedido, só escreve uma mensagem com `print`. Copia-o para o `estacao.py` e corre-o com `python3 estacao.py`. Uma das recusas tem também um erro, que os teus testes vão apanhar.

```python
"""Estação de trotinetes elétricas: estacionam-se e alugam-se trotinetes.

Duas classes:

- Trotinete guarda o código e a bateria de uma trotinete. É uma dataclass.
- Estacao guarda trotinetes numa lista, até encher os lugares, e só aluga
  uma trotinete com pelo menos BATERIA_MINIMA de bateria.

Nesta versão, quando a estação não pode fazer o que lhe pedem, escreve uma
mensagem com print.
"""

from dataclasses import dataclass

BATERIA_MINIMA = 20


@dataclass
class Trotinete:
    """Uma trotinete, com o código, como "T1", e a bateria, em percentagem."""

    codigo: str
    bateria: int


class Estacao:
    """Uma estação de trotinetes: tem um nome, os lugares e as trotinetes que lá estão."""

    def __init__(self, nome, lugares):
        """Cria uma estação vazia, com o nome e o número de lugares, de 1 para cima."""
        if lugares < 1:
            print(f"Uma estação tem de ter pelo menos 1 lugar, e não {lugares}.")
        self.nome = nome
        self.lugares = lugares
        self.trotinetes = []

    def estacionar(self, trotinete):
        """Junta a Trotinete à estação, se houver lugar."""
        if len(self.trotinetes) >= self.lugares:
            print(f"A estação {self.nome} está cheia: {trotinete.codigo} ficou de fora.")
            return
        self.trotinetes.append(trotinete)

    def alugar(self, codigo):
        """Tira da estação a trotinete com este código, um texto, e devolve-a.

        Só se aluga uma trotinete com bateria suficiente. Quando não aluga,
        devolve None.
        """
        for trotinete in self.trotinetes:
            if trotinete.codigo == codigo:
                self.trotinetes.remove(trotinete)
                if trotinete.bateria < BATERIA_MINIMA:
                    print(f"A trotinete {codigo} só tem {trotinete.bateria}% de bateria; são precisos {BATERIA_MINIMA}%.")
                    return None
                return trotinete
        print(f"A trotinete {codigo} não está na estação {self.nome}.")
        return None


if __name__ == "__main__":
    central = Estacao("Central", 3)
    for trotinete in [Trotinete("T1", 80), Trotinete("T2", 15), Trotinete("T3", 50)]:
        central.estacionar(trotinete)

    for codigo in ["T1", "T2", "T9"]:
        central.alugar(codigo)
        print(f"{codigo} alugada.")

    print("Na estação:")
    for trotinete in central.trotinetes:
        print(f"- {trotinete.codigo}, {trotinete.bateria}% de bateria")
```

## Exercício 1: As recusas passam a exceções

As quatro recusas do `estacao.py` passam a lançar exceções, cada uma com a mensagem que o `print` escrevia. Um valor que não serve recusa-se com o `ValueError` do Python. Uma regra da estação recusa-se com uma exceção tua, e as tuas exceções são filhas de `ErroDaEstacao`. Quando a estação recusa um pedido, fica exatamente como estava.

O programa do fim do ficheiro continua a correr até ao fim. Com `python3 estacao.py`, passa a mostrar:

```text
T1 alugada.
Recusado: A trotinete T2 só tem 15% de bateria; são precisos 20%.
Recusado: A trotinete T9 não está na estação Central.
Na estação:
- T2, 15% de bateria
- T3, 50% de bateria
```

## Exercício 2: Os testes

No `test_estacao.py`, escreve um teste com cada nome desta lista. Cada teste confirma o que a descrição diz.

1. `test_estacionar_junta_a_trotinete_a_estacao`: Uma trotinete estacionada numa estação vazia fica na lista da estação.
2. `test_uma_trotinete_com_20_de_bateria_pode_ser_alugada`: Uma trotinete com 20% de bateria, o mínimo, é alugada: o `alugar` devolve-a, e ela sai da estação.
3. `test_a_estacao_cheia_recusa_a_quarta_e_depois_de_um_aluguer_ja_a_aceita`: Numa estação de 3 lugares cheia, uma quarta trotinete é recusada. Depois de se alugar uma trotinete do meio da lista, a mesma quarta trotinete já estaciona. No fim, confirma que trotinetes estão na estação, e por que ordem.
4. `test_alugar_uma_trotinete_que_nao_esta_na_estacao_e_recusado`: Pedir uma trotinete que não está na estação é recusado, e as trotinetes que lá estavam continuam na estação.
5. `test_alugar_uma_trotinete_com_menos_de_20_de_bateria_e_recusado_e_ela_fica_na_estacao`: Uma trotinete com menos de 20% de bateria não é alugada e continua na estação.
6. `test_criar_uma_estacao_com_0_lugares_e_recusado`: Criar uma estação com 0 lugares é recusado.
7. `test_as_recusas_das_regras_da_estacao_sao_todas_erros_da_estacao`: Cada uma das recusas das regras da estação é da família `ErroDaEstacao`.

## Critérios de conclusão

- Cada recusa lança uma exceção, e as das regras são filhas de `ErroDaEstacao`.
- Nenhuma recusa muda a estação.
- `python3 estacao.py` mostra exatamente a saída do exercício 1.
- O `test_estacao.py` tem os 7 testes da lista, e `python3 -m pytest` passa sem falhas.

![Rodapé](../../imagens/rodape.png)
