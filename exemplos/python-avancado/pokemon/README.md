![Cabeçalho](../../../imagens/cabecalho.png)

# Exemplo dos Pokémon

Este é o exemplo que usamos nas aulas. Começou com uma classe `Pokemon` e vai crescendo à medida que a matéria avança, até ser uma aplicação completa. É usado nos temas [03 Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md) e [04 Exceções, depuração e logging](../../../01-python-avancado/04-excecoes-depuracao-e-logging.md).

## O que está nesta pasta

Cada pasta é uma versão completa, que funciona sozinha. O nome da pasta é o do guia onde essa versão é explicada. Uma versão nova parte da anterior e acrescenta-lhe o que o guia novo ensina, por isso podes abrir duas pastas seguidas e comparar o que mudou.

| Pasta | O que tem | Guia |
| --- | --- | --- |
| `03-objetos-e-composicao` | A classe `Pokemon` com a vida e o ataque protegidos por propriedades, os tipos por herança, o treinador e o ginásio por agregação e os combates por composição; o líder, criado com um método de classe; os anunciadores dos combates, por duck typing; e o registo de cada combate escrito como dataclass | [Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md) |
| `04-excecoes-depuracao-e-logging` | A versão anterior, com as recusas do ginásio feitas com exceções próprias, no ficheiro `erros.py`, e os combates registados com logging | [Exceções, depuração e logging](../../../01-python-avancado/04-excecoes-depuracao-e-logging.md) |

## Como correr

Abre o terminal na pasta de uma versão e escreve:

```bash
python3 ginasio.py
```

No Windows, se `python3` não funcionar, experimenta `python` ou `py`.

O que deves ver: a demonstração do ginásio, com os combates entre os treinadores e o histórico, que diz quem ganhou cada um. Na versão 04, aparecem também as recusas do ginásio e as linhas do registo dos combates.

## Versões com que foi testado

Python 3.9 e Python 3.14, a 18 de outubro de 2026, com a mesma saída nas duas.

![Rodapé](../../../imagens/rodape.png)
