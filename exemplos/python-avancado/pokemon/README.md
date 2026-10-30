![Cabeçalho](../../../imagens/cabecalho.png)

# Exemplo dos Pokémon

Este é o exemplo que usamos nas aulas. Começou com uma classe `Pokemon` e vai crescendo à medida que a matéria avança, até ser uma aplicação completa. É usado nos temas [03 Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md), [04 Exceções, depuração e logging](../../../01-python-avancado/04-excecoes-depuracao-e-logging.md) e [05 Testes de comportamento com pytest](../../../01-python-avancado/05-testes-com-pytest.md).

## O que está nesta pasta

Cada pasta é uma versão completa, que funciona sozinha. O nome da pasta é o do guia onde essa versão é explicada. Uma versão nova parte da anterior e acrescenta-lhe o que o guia novo ensina, por isso podes abrir duas pastas seguidas e comparar o que mudou.

| Pasta | O que tem | Guia |
| --- | --- | --- |
| `03-objetos-e-composicao` | A classe `Pokemon` com a vida e o ataque protegidos por propriedades, os tipos por herança, o treinador e o ginásio por agregação e os combates por composição; o líder, criado com um método de classe; os anunciadores dos combates, por duck typing; e o registo de cada combate escrito como dataclass | [Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md) |
| `04-excecoes-depuracao-e-logging` | A versão anterior, com as recusas do ginásio feitas com exceções próprias, no ficheiro `erros.py`, e os combates registados com logging | [Exceções, depuração e logging](../../../01-python-avancado/04-excecoes-depuracao-e-logging.md) |
| `05-testes-com-pytest` | A versão anterior, com o mesmo código, e os testes dele: o `test_pokemon.py`, com as vantagens de tipo, o KO e os limites da vida e do ataque, e o `test_ginasio.py`, com as recusas, os registos dos combates e a escolha do líder | [Testes de comportamento com pytest](../../../01-python-avancado/05-testes-com-pytest.md) |

## Como correr

Abre o terminal na pasta de uma versão e escreve:

```bash
python3 ginasio.py
```

No Windows, se `python3` não funcionar, experimenta `python` ou `py`.

O que deves ver: a demonstração do ginásio, com os combates entre os treinadores e o histórico, que diz quem ganhou cada um. Na versão 04, aparecem também as recusas do ginásio e as linhas do registo dos combates.

A versão 05 tem também os testes. Para os correres, abre o terminal na pasta `05-testes-com-pytest` e escreve:

```bash
python3 -m pytest
```

O que deves ver: uma linha com o nome de cada ficheiro de testes, seguida de um ponto por cada teste que passou, e no fim `22 passed`. Se aparecer `No module named pytest`, o pytest ainda não está instalado no teu computador: o laboratório do tema 05 explica como o instalares.

## Versões com que foi testado

Python 3.9 e Python 3.14, com a mesma saída nas duas. Os testes da versão 05 correram com o pytest 8.4 no Python 3.9 e com o pytest 9.1 no Python 3.14. O pytest 9 já não se instala no Python 3.9, e no 3.9 o comando de instalação escolhe sozinho a versão 8.

![Rodapé](../../../imagens/rodape.png)
