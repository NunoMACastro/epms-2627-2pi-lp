![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento em cinco temas de treino

Praticas, em cinco exercícios, o que o [livro de receitas](03-objetos-e-composicao-exercicios-receitas.md) pede: um registo, uma variante com um dado a mais e a coleção que os reúne. Nenhum exercício é obrigatório nem conta para a nota: fazes em casa os que quiseres. Cada exercício faz-se num só ficheiro, e não há entrega. Para rever: o [guia do tema](../03-objetos-e-composicao.md) e o [laboratório](../laboratorios/03-objetos-e-composicao-laboratorio.md).

## O cenário

O programa de cada exercício acaba com as linhas que o enunciado dá, sem as mudares, e mostra exatamente a saída que lá está. Os nomes que essas linhas usam são obrigatórios, e os outros escolhes tu.

Em todos os exercícios, como no livro de receitas:

- a regra de cada número, no registo e na variante, vale também quando alguém o muda diretamente, como em `jogo.horas = -3`: nesse caso, o número fica como estava;
- cada registo é a ficha que a coleção faz de uma coisa que existe fora dela, como um jogo, uma carta ou uma música;
- a coleção cria e guarda os registos, pela ordem em que entram, e eles só existem dentro dela, como os registos dos combates do ginásio;
- antes de acrescentar, a coleção verifica os dados pela ordem da lista "O programa recusa" do exercício;
- a coleção devolve uma mensagem a dizer se aceitou ou porque recusou, e, quando recusa, nada muda;
- para mostrar a lista, a coleção pede a cada registo que se descreva, e, quando não há nenhum para mostrar, diz-o, como em `Não há jogos.`.

<details>
<summary>Pista</summary>

A regra de cada número tem de valer no construtor, quando alguém muda o número e quando a coleção verifica os dados. Onde a escreves para ela ficar num só sítio e servir aos três? O `type`, que já usaste no 10.º ano, diz se um valor é um número inteiro.

</details>

## Exercício 1: Coleção de jogos

Queremos um programa para registar os jogos que tens e quantas horas jogaste cada um. Para cada jogo, guardamos um código, um título e as horas jogadas. As horas são sempre um número inteiro, 0 ou mais.

Por exemplo:

| Código | Título | Horas jogadas |
| --- | --- | ---: |
| J01 | Corrida Rápida | 12 |
| J03 | Quebra-Cabeças | 0 |

Um jogo multijogador tem tudo o que um jogo tem, e mais o número máximo de jogadores, um número inteiro de 2 a 100. Por exemplo, o J02, Arena dos Heróis, com 30 horas jogadas, é para até 8 jogadores.

As três classes são `Jogo`, `JogoMultijogador` e `ColecaoDeJogos`.

Na lista, cada jogo aparece numa linha, e um jogo multijogador acrescenta o número de jogadores:

```text
J01 Corrida Rápida, 12 horas
J02 Arena dos Heróis, 30 horas, até 8 jogadores
```

Deves poder:

- acrescentar um jogo, simples ou multijogador;
- somar a um jogo as horas de uma sessão;
- ver os jogos todos;
- ver só os jogos com mais horas do que um limite.

O programa recusa:

- um código que já existe;
- um título vazio;
- horas que não sejam um número inteiro, 0 ou mais;
- um número de jogadores que não seja um número inteiro de 2 a 100;
- ao somar horas, um código que não existe, ou horas de uma sessão que não sejam um número inteiro maior do que 0.

O programa acaba com estas linhas:

```python
teste = Jogo("J00", "Teste", 5)
teste.horas = -3
print("Teste da regra das horas:", teste.horas)
teste_multi = JogoMultijogador("J00", "Teste", 5, 4)
teste_multi.jogadores = 1
print("Teste da regra dos jogadores:", teste_multi.jogadores)
print()

colecao = ColecaoDeJogos()
colecao.mostrar()
print(colecao.acrescentar("J01", "Corrida Rápida", 12))
print(colecao.acrescentar_multijogador("J02", "Arena dos Heróis", 30, 8))
print(colecao.acrescentar("J03", "Quebra-Cabeças", 0))
print(colecao.acrescentar("J01", "Outro Jogo", 3))
print(colecao.acrescentar("J04", "", 7))
print(colecao.acrescentar("J05", "Corrida Lenta", -1))
print(colecao.acrescentar_multijogador("J06", "Batalha Final", 10, 101))
print()
colecao.mostrar()
print()
print(colecao.somar_horas("J01", 3))
print(colecao.somar_horas("J03", 0))
print(colecao.somar_horas("J09", 2))
print()
print("Com mais de 10 horas:")
colecao.mostrar_com_mais_de(10)
```

E mostra exatamente isto:

```text
Teste da regra das horas: 5
Teste da regra dos jogadores: 4

Não há jogos.
Jogo J01 acrescentado.
Jogo J02 acrescentado.
Jogo J03 acrescentado.
Recusado: já existe um jogo com o código J01.
Recusado: o título não pode ficar vazio.
Recusado: as horas têm de ser um número inteiro, 0 ou mais.
Recusado: o número de jogadores tem de ser um número inteiro de 2 a 100.

J01 Corrida Rápida, 12 horas
J02 Arena dos Heróis, 30 horas, até 8 jogadores
J03 Quebra-Cabeças, 0 horas

Horas do J01 passam a 15.
Recusado: as horas de uma sessão têm de ser um número inteiro maior do que 0.
Recusado: não há nenhum jogo com o código J09.

Com mais de 10 horas:
J01 Corrida Rápida, 15 horas
J02 Arena dos Heróis, 30 horas, até 8 jogadores
```

## Exercício 2: Cartas colecionáveis

Queremos um programa para registar as cartas de uma coleção e a raridade de cada uma, de 1, a mais comum, a 5, a mais rara. Para cada carta, guardamos um código, um nome e a raridade, um número inteiro de 1 a 5.

Por exemplo:

| Código | Nome | Raridade |
| --- | --- | ---: |
| C001 | Lobo da Neve | 3 |
| C003 | Rato do Campo | 1 |

Uma carta de edição limitada tem tudo o que uma carta tem, e mais o número de cópias da edição, um número inteiro de 1 a 1000. Por exemplo, a C002, Dragão Dourado, de raridade 5, teve uma edição de 250 cópias.

As três classes são `Carta`, `CartaDeEdicaoLimitada` e `ColecaoDeCartas`.

Na lista, cada carta aparece numa linha, e uma carta de edição limitada acrescenta as cópias:

```text
C001 Lobo da Neve, raridade 3
C002 Dragão Dourado, raridade 5, edição de 250 cópias
```

Deves poder:

- acrescentar uma carta, simples ou de edição limitada;
- corrigir a raridade de uma carta, com a mesma regra;
- ver as cartas todas;
- ver só as cartas com raridade igual ou maior do que um mínimo.

O programa recusa:

- um código que já existe;
- um nome vazio;
- uma raridade que não seja um número inteiro de 1 a 5;
- um número de cópias que não seja um número inteiro de 1 a 1000;
- ao corrigir a raridade, um código que não existe, ou uma raridade fora da regra.

O programa acaba com estas linhas:

```python
teste = Carta("C000", "Teste", 3)
teste.raridade = 6
print("Teste da regra da raridade:", teste.raridade)
teste_edicao = CartaDeEdicaoLimitada("C000", "Teste", 3, 100)
teste_edicao.copias = 0
print("Teste da regra das cópias:", teste_edicao.copias)
print()

colecao = ColecaoDeCartas()
colecao.mostrar()
print(colecao.acrescentar("C001", "Lobo da Neve", 3))
print(colecao.acrescentar_edicao_limitada("C002", "Dragão Dourado", 5, 250))
print(colecao.acrescentar("C003", "Rato do Campo", 1))
print(colecao.acrescentar("C001", "Lobo do Mar", 2))
print(colecao.acrescentar("C004", "", 2))
print(colecao.acrescentar("C005", "Fénix", 6))
print(colecao.acrescentar_edicao_limitada("C006", "Grifo", 4, 1001))
print()
colecao.mostrar()
print()
print(colecao.corrigir_raridade("C003", 4))
print(colecao.corrigir_raridade("C001", 0))
print(colecao.corrigir_raridade("C009", 2))
print()
print("Raridade 4 ou mais:")
colecao.mostrar_raras(4)
```

E mostra exatamente isto:

```text
Teste da regra da raridade: 3
Teste da regra das cópias: 100

Não há cartas.
Carta C001 acrescentada.
Carta C002 acrescentada.
Carta C003 acrescentada.
Recusada: já existe uma carta com o código C001.
Recusada: o nome não pode ficar vazio.
Recusada: a raridade tem de ser um número inteiro de 1 a 5.
Recusada: o número de cópias tem de ser um número inteiro de 1 a 1000.

C001 Lobo da Neve, raridade 3
C002 Dragão Dourado, raridade 5, edição de 250 cópias
C003 Rato do Campo, raridade 1

Raridade da C003 corrigida para 4.
Recusada: a raridade tem de ser um número inteiro de 1 a 5.
Recusada: não há nenhuma carta com o código C009.

Raridade 4 ou mais:
C002 Dragão Dourado, raridade 5, edição de 250 cópias
C003 Rato do Campo, raridade 4
```

<details>
<summary>Pista</summary>

Compara as frases "uma carta de edição limitada é uma carta" e "uma carta de edição limitada tem uma carta". Qual das duas é verdadeira?

</details>

## Exercício 3: Diário de treinos

Queremos um programa para registar os treinos que fizeste e quanto tempo durou cada um. Para cada treino, guardamos um código, uma atividade e a duração, em minutos, um número inteiro maior do que 0.

Por exemplo:

| Código | Atividade | Duração, em minutos |
| --- | --- | ---: |
| T01 | Ginásio | 45 |
| T03 | Ioga | 20 |

Um treino com distância, como uma corrida, tem tudo o que um treino tem, e mais a distância, em metros, um número inteiro maior do que 0. Por exemplo, o T02, Corrida, durou 30 minutos, e foram 5000 metros.

As três classes são `Treino`, `TreinoComDistancia` e `DiarioDeTreinos`.

Na lista, cada treino aparece numa linha, e um treino com distância acrescenta os metros:

```text
T01 Ginásio, 45 minutos
T02 Corrida, 30 minutos, 5000 metros
```

Deves poder:

- acrescentar um treino, simples ou com distância;
- corrigir a duração de um treino, com a mesma regra;
- ver os treinos todos;
- ver só os treinos que duraram mais do que um limite.

O programa recusa:

- um código que já existe;
- uma atividade vazia;
- uma duração, em minutos, que não seja um número inteiro maior do que 0;
- uma distância que não seja um número inteiro maior do que 0;
- ao corrigir a duração de um treino, um código que não existe, ou uma duração fora da regra.

O programa acaba com estas linhas:

```python
teste = Treino("T00", "Teste", 20)
teste.minutos = 0
print("Teste da regra da duração:", teste.minutos)
teste_distancia = TreinoComDistancia("T00", "Teste", 20, 1000)
teste_distancia.metros = -100
print("Teste da regra da distância:", teste_distancia.metros)
print()

diario = DiarioDeTreinos()
diario.mostrar()
print(diario.acrescentar("T01", "Ginásio", 45))
print(diario.acrescentar_com_distancia("T02", "Corrida", 30, 5000))
print(diario.acrescentar("T03", "Ioga", 20))
print(diario.acrescentar("T01", "Natação", 40))
print(diario.acrescentar("T04", "", 15))
print(diario.acrescentar("T05", "Alongamentos", 0))
print(diario.acrescentar_com_distancia("T06", "Bicicleta", 60, 0))
print()
diario.mostrar()
print()
print(diario.corrigir_duracao("T03", 35))
print(diario.corrigir_duracao("T02", 1.5))
print(diario.corrigir_duracao("T09", 30))
print()
print("Mais de 30 minutos:")
diario.mostrar_longos(30)
```

E mostra exatamente isto:

```text
Teste da regra da duração: 20
Teste da regra da distância: 1000

Não há treinos.
Treino T01 acrescentado.
Treino T02 acrescentado.
Treino T03 acrescentado.
Recusado: já existe um treino com o código T01.
Recusado: a atividade não pode ficar vazia.
Recusado: a duração tem de ser um número inteiro maior do que 0.
Recusado: a distância tem de ser um número inteiro maior do que 0.

T01 Ginásio, 45 minutos
T02 Corrida, 30 minutos, 5000 metros
T03 Ioga, 20 minutos

Duração do T03 corrigida para 35 minutos.
Recusado: a duração tem de ser um número inteiro maior do que 0.
Recusado: não há nenhum treino com o código T09.

Mais de 30 minutos:
T01 Ginásio, 45 minutos
T03 Ioga, 35 minutos
```

<details>
<summary>Pista</summary>

Um treino com distância descreve-se como um treino, com os metros no fim. Como é que a variante usa a descrição que o treino já faz e lhe acrescenta o dado a mais?

</details>

## Exercício 4: Playlist

Queremos um programa para registar as músicas de uma lista e a duração de cada uma, em segundos: uma música de 3 minutos e 20 segundos tem 200 segundos. Para cada música, guardamos um código, um título e a duração, um número inteiro maior do que 0.

Por exemplo:

| Código | Título | Duração, em segundos |
| --- | --- | ---: |
| M01 | Noite de Verão | 200 |
| M03 | Manhã Calma | 260 |

Uma música de um álbum tem tudo o que uma música tem, e mais o número da faixa, um número inteiro de 1 a 30. Por exemplo, a M02, Tempestade, com 245 segundos, é a faixa 3 do álbum.

As três classes são `Musica`, `MusicaDeAlbum` e `Playlist`.

Na lista, cada música aparece numa linha, e uma música de um álbum acrescenta a faixa:

```text
M01 Noite de Verão, 200 segundos
M02 Tempestade, 245 segundos, faixa 3
```

Deves poder:

- acrescentar uma música, simples ou de um álbum;
- corrigir a duração de uma música, com a mesma regra;
- ver as músicas todas;
- ver só as músicas que duram mais do que um limite.

O programa recusa:

- um código que já existe;
- um título vazio;
- uma duração, em segundos, que não seja um número inteiro maior do que 0;
- uma faixa que não seja um número inteiro de 1 a 30;
- ao corrigir a duração de uma música, um código que não existe, ou uma duração fora da regra.

O programa acaba com estas linhas:

```python
teste = Musica("M00", "Teste", 100)
teste.segundos = 0
print("Teste da regra da duração:", teste.segundos)
teste_album = MusicaDeAlbum("M00", "Teste", 100, 5)
teste_album.faixa = 31
print("Teste da regra da faixa:", teste_album.faixa)
print()

playlist = Playlist()
playlist.mostrar()
print(playlist.acrescentar("M01", "Noite de Verão", 200))
print(playlist.acrescentar_de_album("M02", "Tempestade", 245, 3))
print(playlist.acrescentar("M03", "Manhã Calma", 260))
print(playlist.acrescentar("M01", "Outra Música", 180))
print(playlist.acrescentar("M04", "", 150))
print(playlist.acrescentar("M05", "Silêncio", 0))
print(playlist.acrescentar_de_album("M06", "Eco", 190, 0))
print()
playlist.mostrar()
print()
print(playlist.corrigir_duracao("M01", 210))
print(playlist.corrigir_duracao("M03", 3.5))
print(playlist.corrigir_duracao("M09", 200))
print()
print("Mais de 240 segundos:")
playlist.mostrar_longas(240)
```

E mostra exatamente isto:

```text
Teste da regra da duração: 100
Teste da regra da faixa: 5

Não há músicas.
Música M01 acrescentada.
Música M02 acrescentada.
Música M03 acrescentada.
Recusada: já existe uma música com o código M01.
Recusada: o título não pode ficar vazio.
Recusada: a duração tem de ser um número inteiro maior do que 0.
Recusada: a faixa tem de ser um número inteiro de 1 a 30.

M01 Noite de Verão, 200 segundos
M02 Tempestade, 245 segundos, faixa 3
M03 Manhã Calma, 260 segundos

Duração da M01 corrigida para 210 segundos.
Recusada: a duração tem de ser um número inteiro maior do que 0.
Recusada: não há nenhuma música com o código M09.

Mais de 240 segundos:
M02 Tempestade, 245 segundos, faixa 3
M03 Manhã Calma, 260 segundos
```

<details>
<summary>Pista</summary>

Se a playlist perguntar a cada música de que tipo é, que linhas tens de mudar quando aparecer outro tipo de música?

</details>

## Exercício 5: Campeonato

Queremos um programa para registar as equipas de um campeonato inventado e os pontos de cada uma. Para cada equipa, guardamos uma sigla, um nome e os pontos, um número inteiro, 0 ou mais.

Por exemplo:

| Sigla | Nome | Pontos |
| --- | --- | ---: |
| LBO | Leões do Bairro | 12 |
| TDV | Tubarões do Vale | 0 |

Uma equipa com estádio tem tudo o que uma equipa tem, e mais o número de lugares do estádio, um número inteiro de 500 a 90000. Por exemplo, a ACR, Águias da Ribeira, com 9 pontos, tem um estádio de 5000 lugares.

As três classes são `Equipa`, `EquipaComEstadio` e `Campeonato`.

Na lista, cada equipa aparece numa linha, e uma equipa com estádio acrescenta os lugares:

```text
LBO Leões do Bairro, 12 pontos
ACR Águias da Ribeira, 9 pontos, estádio de 5000 lugares
```

Deves poder:

- acrescentar uma equipa, simples ou com estádio;
- somar a uma equipa os pontos ganhos num jogo;
- ver as equipas todas;
- ver só as equipas com pontos iguais ou maiores do que um mínimo.

O programa recusa:

- uma sigla que já existe;
- um nome vazio;
- pontos que não sejam um número inteiro, 0 ou mais;
- um número de lugares que não seja um número inteiro de 500 a 90000;
- ao somar pontos, uma sigla que não existe, ou pontos de um jogo que não sejam um número inteiro, 0 ou mais.

O programa acaba com estas linhas:

```python
teste = Equipa("TST", "Teste", 5)
teste.pontos = -1
print("Teste da regra dos pontos:", teste.pontos)
teste_estadio = EquipaComEstadio("TST", "Teste", 5, 1000)
teste_estadio.lugares = 100
print("Teste da regra dos lugares:", teste_estadio.lugares)
print()

campeonato = Campeonato()
campeonato.mostrar()
print(campeonato.acrescentar("LBO", "Leões do Bairro", 12))
print(campeonato.acrescentar_com_estadio("ACR", "Águias da Ribeira", 9, 5000))
print(campeonato.acrescentar("TDV", "Tubarões do Vale", 0))
print(campeonato.acrescentar("LBO", "Lobos da Barra", 4))
print(campeonato.acrescentar("PDS", "", 3))
print(campeonato.acrescentar("RAP", "Raposas do Pinhal", -2))
print(campeonato.acrescentar_com_estadio("COR", "Corvos do Monte", 6, 95000))
print()
campeonato.mostrar()
print()
print(campeonato.somar_pontos("ACR", 3))
print(campeonato.somar_pontos("TDV", -1))
print(campeonato.somar_pontos("XYZ", 1))
print()
print("Com 10 pontos ou mais:")
campeonato.mostrar_com_pelo_menos(10)
```

E mostra exatamente isto:

```text
Teste da regra dos pontos: 5
Teste da regra dos lugares: 1000

Não há equipas.
Equipa LBO acrescentada.
Equipa ACR acrescentada.
Equipa TDV acrescentada.
Recusada: já existe uma equipa com a sigla LBO.
Recusada: o nome não pode ficar vazio.
Recusada: os pontos têm de ser um número inteiro, 0 ou mais.
Recusada: o número de lugares tem de ser um número inteiro de 500 a 90000.

LBO Leões do Bairro, 12 pontos
ACR Águias da Ribeira, 9 pontos, estádio de 5000 lugares
TDV Tubarões do Vale, 0 pontos

Pontos da ACR passam a 12.
Recusada: os pontos de um jogo têm de ser um número inteiro, 0 ou mais.
Recusada: não há nenhuma equipa com a sigla XYZ.

Com 10 pontos ou mais:
LBO Leões do Bairro, 12 pontos
ACR Águias da Ribeira, 12 pontos, estádio de 5000 lugares
```

<details>
<summary>Pista</summary>

Os lugares têm dois limites. Antes de executares as linhas do fim, experimenta os dois valores aceites e os dois logo fora.

</details>

## Desafios

### Desafio 1: Uma segunda variante

Escolhe um dos exercícios que fizeste e acrescenta-lhe uma segunda variante, à tua escolha, com um dado a mais e a sua descrição. Tem de ser uma relação "é um" verdadeira, como as do enunciado. Não mudes o método que mostra a lista. Explica, numa frase, num comentário no início do ficheiro, porque é que não precisaste de o mudar.

## Critérios de conclusão

- O programa de cada exercício que fizeste acaba com as linhas do enunciado, sem mudanças, e mostra exatamente a saída indicada.
- Cada regra de um número está escrita num só sítio, e o que o registo e a variante têm em comum também.
- A coleção mostra os registos sem perguntar de que tipo é cada um.

![Rodapé](../../imagens/rodape.png)
