![Cabeçalho](../../../imagens/cabecalho.png)

# Exemplo dos Pokémon

O ginásio Pokémon das aulas: treinadores com as suas equipas, um líder e combates, com um histórico que diz quem venceu cada um. Cresce com a matéria, e cada pasta é uma versão completa, que corre sozinha. É usado nos temas [03 Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md), [04 Exceções, depuração e logging](../../../01-python-avancado/04-excecoes-depuracao-e-logging.md) e [05 Testes de comportamento com pytest](../../../01-python-avancado/05-testes-com-pytest.md).

## O que está nesta pasta

Cada versão parte da anterior e acrescenta-lhe a matéria do tema, por isso podes abrir duas pastas seguidas e comparar o que mudou.

- `03-objetos-e-composicao`, a versão do tema 03. No `pokemon.py`, a classe `Pokemon`, com a vida e o ataque protegidos por propriedades, e os tipos por herança. No `ginasio.py`, o treinador, o líder, criado com um método de classe, e o ginásio, que guarda o histórico dos combates por composição; cada combate é uma dataclass, o `Combate`. No `anunciadores.py`, os anunciadores dos combates, que o ginásio usa por duck typing.
- `04-excecoes-depuracao-e-logging`, a versão do tema 04. As recusas do ginásio passam a ser exceções próprias, no `erros.py`, e o `ginasio.py` escreve no registo, com o logging, o que o ginásio faz.
- `05-testes-com-pytest`, a versão do tema 05: os quatro ficheiros da versão 04, sem mudanças, e os testes deles. O `test_pokemon.py` testa as vantagens de tipo, o KO, os limites da vida e do ataque e a recuperação das plantas. O `test_ginasio.py` testa as duas recusas, a escolha do Pokémon do líder e os dois combates ganhos, que ficam no histórico do ginásio: `test_o_desafiante_que_vence_fica_no_historico` e `test_o_lider_que_vence_fica_no_historico`.

## Como correr

Abre o terminal na pasta de uma versão e escreve:

```bash
python3 ginasio.py
```

O que deves ver: os dois combates do Ash contra a Misty, no ginásio de Cerulean, ataque a ataque, e o histórico do ginásio, com quem venceu cada combate. A última linha diz com quantos Pokémon ficam os dois treinadores, que continuam a existir depois de o ginásio ser apagado. Nas versões 04 e 05, o ginásio recusa um terceiro combate, porque a Misty já não tem Pokémon com vida. Aparecem também as linhas do registo, que começam por `[INFO]` ou `[WARNING]`.

Os testes da versão 05 correm-se com o pytest. Abre o terminal na pasta `05-testes-com-pytest` e escreve:

```bash
python3 -m pytest
```

O que deves ver: uma linha por ficheiro de testes, com um ponto por cada teste que passou, e, no fim, `22 passed`. Se aparecer `No module named pytest`, instala o pytest como no passo [Preparar o projeto](../../../01-python-avancado/laboratorios/05-testes-com-pytest-laboratorio.md#preparar-o-projeto) do laboratório do tema 05.

## Versões e compatibilidade

Precisas do Python 3.9 ou mais recente. Foram usados o Python 3.9 e o 3.14, com a mesma saída nas duas. Os testes da versão 05 usam o pytest: o 8.4 com o Python 3.9 e o 9.1 com o 3.14. O pytest 9 já não se instala no Python 3.9, e aí o `pip` instala sozinho o 8. No Windows, o comando pode ser `python` ou `py`, em vez de `python3`.

![Rodapé](../../../imagens/rodape.png)
