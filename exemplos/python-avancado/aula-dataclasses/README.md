![Cabeçalho](../../../imagens/cabecalho.png)

# Programas da aula das dataclasses

Oito programas curtos sobre as dataclasses, cada um com uma ideia só. São mais curtos do que os do guia e correm sozinhos, sem o `pokemon.py`. São usados no tema [03 Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md), na [parte das dataclasses](../../../01-python-avancado/03-objetos-e-composicao.md#parte-7-dataclasses).

## O que está nesta pasta

- [`1-classe-normal.py`](1-classe-normal.py): um combate escrito como classe normal. O construtor repete cada nome, o `print` não mostra os dados e o `==` não compara os valores.
- [`2-dataclass.py`](2-dataclass.py): o mesmo combate com `@dataclass`. O construtor, o `print` e o `==` passam a ser escritos pelo Python.
- [`3-tipos-nao-verificados.py`](3-tipos-nao-verificados.py): o tipo de cada campo diz o que se espera, mas o Python não o verifica. Os valores também se podem dar pelo nome do campo.
- [`4-metodo.py`](4-metodo.py): uma dataclass com um método, como qualquer classe.
- [`5-valor-por-omissao.py`](5-valor-por-omissao.py): um campo com um valor que se usa quando ninguém dá outro.
- [`6-quando-nao-serve.py`](6-quando-nao-serve.py): uma dataclass não protege regras, e um Pokémon criado com 500 de vida fica com 500.
- [`7-campo-sem-tipo.py`](7-campo-sem-tipo.py): um engano de propósito, um campo escrito sem o tipo.
- [`8-sem-dataclass.py`](8-sem-dataclass.py): outro engano de propósito, falta o `@dataclass`.

Os programas 7 e 8 acabam com uma mensagem de erro, e é isso que devem fazer. Os erros frequentes do guia explicam-nos: [Um campo da dataclass sem tipo](../../../01-python-avancado/03-objetos-e-composicao.md#um-campo-da-dataclass-sem-tipo) e [Esquecer o `@dataclass` ou a importação](../../../01-python-avancado/03-objetos-e-composicao.md#esquecer-o-dataclass-ou-a-importação).

## Como correr

Abre o terminal nesta pasta e corre um programa de cada vez, pelo nome. O primeiro corre assim:

```bash
python3 1-classe-normal.py
```

O que deves ver: os programas 1 a 6 escrevem de uma a quatro linhas cada um. No programa 1, uma delas é um endereço de memória, que muda de execução para execução. Os programas 7 e 8 não escrevem nada antes da mensagem de erro, que acaba num `TypeError`.

## Versões e compatibilidade

Precisas do Python 3.9 ou mais recente. Foram usados o Python 3.9 e o 3.14. A mensagem de erro do programa 7 diz só `__init__()` no Python 3.9, e `Combate.__init__()` no 3.14. No Windows, o comando pode ser `python` ou `py`, em vez de `python3`.

![Rodapé](../../../imagens/rodape.png)
