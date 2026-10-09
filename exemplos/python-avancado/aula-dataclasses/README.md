![Cabeçalho](../../../imagens/cabecalho.png)

# Programas da aula das dataclasses

Estes são os programas preparados para a aula das dataclasses, que o guia [Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md) explica na parte 7. São mais curtos do que os do guia: correm sozinhos, sem precisar do `pokemon.py`, e cada um mostra uma ideia só.

Para executar um programa, abre o terminal nesta pasta e escreve, por exemplo, `python3 1-classe-normal.py`. No Windows, se `python3` não funcionar, experimenta `python` ou `py`. Antes de executares, escreve o que achas que vai acontecer, e só depois compara.

| Programa | O que mostra |
| --- | --- |
| [`1-classe-normal.py`](1-classe-normal.py) | Um registo de combate escrito como classe normal: o construtor repete cada nome, o `print` não mostra os dados e o `==` não compara os valores |
| [`2-dataclass.py`](2-dataclass.py) | O mesmo registo com `@dataclass`: o construtor, o `print` e o `==` passam a ser escritos pelo Python |
| [`3-tipos-nao-verificados.py`](3-tipos-nao-verificados.py) | O tipo de cada campo diz o que se espera, mas o Python não o verifica; e os valores também se podem dar pelo nome |
| [`4-metodo.py`](4-metodo.py) | Uma dataclass pode ter métodos, como qualquer classe |
| [`5-valor-por-omissao.py`](5-valor-por-omissao.py) | Um campo com um valor que se usa quando ninguém dá outro |
| [`6-quando-nao-serve.py`](6-quando-nao-serve.py) | Uma dataclass não protege regras: um Pokémon com 500 de vida fica com 500 |
| [`7-campo-sem-tipo.py`](7-campo-sem-tipo.py) | Um engano de propósito: um campo escrito sem o tipo |
| [`8-sem-dataclass.py`](8-sem-dataclass.py) | Outro engano de propósito: falta o `@dataclass` |

Os programas 7 e 8 acabam com uma mensagem de erro, e é isso que devem fazer. Lê a última linha da mensagem e procura, na parte 7 do guia, a secção dos erros frequentes.

![Rodapé](../../../imagens/rodape.png)
