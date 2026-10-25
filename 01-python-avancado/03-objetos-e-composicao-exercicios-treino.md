![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento em cinco temas de treino

Ficha opcional do tema Objetos, composição e comportamento, do módulo 10794, Programação avançada com Python. São cinco temas para treinares em casa o que o [livro de receitas](03-objetos-e-composicao-exercicios-receitas.md) pede. Não contam para a nota.

## O que precisas de saber

O [guia do tema](03-objetos-e-composicao.md), o [laboratório](03-objetos-e-composicao-laboratorio.md) e, de preferência, a [ficha do livro de receitas](03-objetos-e-composicao-exercicios-receitas.md), porque estes temas trabalham da mesma maneira.

## Como trabalhar

Cada exercício é um tema com a mesma estrutura do livro de receitas: um registo, uma variante desse registo, com um dado a mais, e a coleção que os reúne. Como no livro, o enunciado dá as regras, as linhas com que o programa acaba e a saída exata. Os nomes que as linhas finais usam são obrigatórios, e os outros escolhes tu.

Escolhe um tema, ou faz vários. As mensagens de cada recusa estão na saída de cada exercício.

## Exercício 1: Coleção de jogos

Registas os jogos que tens e quantas horas jogaste cada um.

1. Cada jogo tem um código, um título e as horas jogadas. As horas são sempre um número inteiro, 0 ou mais. A regra escreve-se num só sítio e vale também quando alguém escreve `jogo.horas = -3`: nesse caso, as horas ficam como estavam.
2. Um jogo multijogador tem tudo o que um jogo tem e também o número máximo de jogadores. Os jogadores são um número inteiro de 2 a 100, com a regra num só sítio.
3. Cada jogo descreve-se numa linha, como `J01 Corrida Rápida, 12 horas`, e um jogo multijogador acrescenta `, até 8 jogadores`.
4. A coleção cria e guarda os jogos, pela ordem em que entram. Antes de acrescentar, verifica por esta ordem o código, o título, as horas e, num jogo multijogador, os jogadores. Devolve uma mensagem a dizer se aceitou ou porque recusou.
5. A coleção soma as horas de uma sessão a um jogo. As horas de uma sessão são um número inteiro maior do que 0.
6. A coleção mostra os jogos todos, ou só os que têm mais horas do que um limite, pedindo a cada jogo que se descreva.

O teu programa tem de acabar com estas linhas, sem as mudar:

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

E tem de mostrar exatamente isto:

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

Registas as cartas de uma coleção e a raridade de cada uma, de 1, a mais comum, a 5, a mais rara.

1. Cada carta tem um código, um nome e a raridade, um número inteiro de 1 a 5. A regra escreve-se num só sítio e vale também quando alguém escreve `carta.raridade = 6`: nesse caso, a raridade fica como estava.
2. Uma carta de edição limitada tem tudo o que uma carta tem e também o número de cópias da edição. As cópias são um número inteiro de 1 a 1000, com a regra num só sítio.
3. Cada carta descreve-se numa linha, como `C001 Lobo da Neve, raridade 3`, e uma carta de edição limitada acrescenta `, edição de 250 cópias`.
4. A coleção cria e guarda as cartas, pela ordem em que entram. Antes de acrescentar, verifica por esta ordem o código, o nome, a raridade e, numa carta de edição limitada, as cópias. Devolve uma mensagem a dizer se aceitou ou porque recusou.
5. A coleção corrige a raridade de uma carta, com a mesma regra.
6. A coleção mostra as cartas todas, ou só as que têm uma raridade mínima ou mais, pedindo a cada carta que se descreva.

O teu programa tem de acabar com estas linhas, sem as mudar:

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

E tem de mostrar exatamente isto:

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

## Exercício 3: Diário de treinos

Registas os treinos que fizeste e quanto tempo durou cada um.

1. Cada treino tem um código, uma atividade e a duração, em minutos, um número inteiro maior do que 0. A regra escreve-se num só sítio e vale também quando alguém escreve `treino.minutos = 0`: nesse caso, a duração fica como estava.
2. Um treino com distância, como uma corrida, tem tudo o que um treino tem e também a distância, em metros. A distância é um número inteiro maior do que 0, com a regra num só sítio.
3. Cada treino descreve-se numa linha, como `T01 Ginásio, 45 minutos`, e um treino com distância acrescenta `, 5000 metros`.
4. O diário cria e guarda os treinos, pela ordem em que entram. Antes de acrescentar, verifica por esta ordem o código, a atividade, a duração e, num treino com distância, os metros. Devolve uma mensagem a dizer se aceitou ou porque recusou.
5. O diário corrige a duração de um treino, com a mesma regra.
6. O diário mostra os treinos todos, ou só os que duraram mais do que um limite, pedindo a cada treino que se descreva.

O teu programa tem de acabar com estas linhas, sem as mudar:

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

E tem de mostrar exatamente isto:

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

## Exercício 4: Playlist

Registas as músicas de uma lista e a duração de cada uma, em segundos: uma música de 3 minutos e 20 segundos tem 200 segundos.

1. Cada música tem um código, um título e a duração, em segundos, um número inteiro maior do que 0. A regra escreve-se num só sítio e vale também quando alguém escreve `musica.segundos = 0`: nesse caso, a duração fica como estava.
2. Uma música de um álbum tem tudo o que uma música tem e também o número da faixa. A faixa é um número inteiro de 1 a 30, com a regra num só sítio.
3. Cada música descreve-se numa linha, como `M01 Noite de Verão, 200 segundos`, e uma música de um álbum acrescenta `, faixa 3`.
4. A playlist cria e guarda as músicas, pela ordem em que entram. Antes de acrescentar, verifica por esta ordem o código, o título, a duração e, numa música de um álbum, a faixa. Devolve uma mensagem a dizer se aceitou ou porque recusou.
5. A playlist corrige a duração de uma música, com a mesma regra.
6. A playlist mostra as músicas todas, ou só as que duram mais do que um limite, pedindo a cada música que se descreva.

O teu programa tem de acabar com estas linhas, sem as mudar:

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

E tem de mostrar exatamente isto:

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

## Exercício 5: Campeonato

Registas as equipas de um campeonato inventado por ti e os pontos de cada uma.

1. Cada equipa tem uma sigla, um nome e os pontos, um número inteiro, 0 ou mais. A regra escreve-se num só sítio e vale também quando alguém escreve `equipa.pontos = -1`: nesse caso, os pontos ficam como estavam.
2. Uma equipa com estádio tem tudo o que uma equipa tem e também o número de lugares do estádio. Os lugares são um número inteiro de 500 a 90 000, com a regra num só sítio.
3. Cada equipa descreve-se numa linha, como `LBO Leões do Bairro, 12 pontos`, e uma equipa com estádio acrescenta `, estádio de 5000 lugares`.
4. O campeonato cria e guarda as equipas, pela ordem em que entram. Antes de acrescentar, verifica por esta ordem a sigla, o nome, os pontos e, numa equipa com estádio, os lugares. Devolve uma mensagem a dizer se aceitou ou porque recusou.
5. O campeonato soma os pontos ganhos num jogo a uma equipa. Os pontos de um jogo são um número inteiro, 0 ou mais.
6. O campeonato mostra as equipas todas, ou só as que têm um mínimo de pontos ou mais, pedindo a cada equipa que se descreva.

O teu programa tem de acabar com estas linhas, sem as mudar:

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

E tem de mostrar exatamente isto:

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
Recusada: o número de lugares tem de ser um número inteiro de 500 a 90 000.

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

## Apoio

As pistas do livro de receitas servem para todos os temas. Tenta primeiro sozinho, e usa só a pista da regra em que estás preso.

- A regra de um número: onde a escreves para ela valer no construtor, quando alguém muda o valor e quando a coleção verifica os dados?
- A variante: compara as frases "uma carta de edição limitada é uma carta" e "uma carta de edição limitada tem uma carta". Qual das duas é verdadeira?
- A descrição: como é que a variante usa a descrição que a classe base já faz e lhe acrescenta o dado a mais?
- Mostrar a lista: se a coleção perguntar a cada registo de que tipo é, que linhas tens de mudar quando aparecer outro tipo?
- Os limites: num tema com dois limites, experimenta os dois valores aceites e os dois logo fora, antes de executares as linhas finais.

## Desafio opcional

### Uma segunda variante

Escolhe um dos temas que fizeste e acrescenta-lhe uma segunda variante, à tua escolha, com um dado a mais e a sua descrição. Tem de ser uma relação "é um" verdadeira, como as do enunciado. Não mudes o método que mostra a lista. Depois explica, numa frase, porque é que não precisaste de o mudar.

## Critérios de conclusão

Concluíste um tema quando:

- o teu programa acaba com as linhas do enunciado, sem mudanças, e mostra exatamente a saída indicada;
- cada regra de um número está escrita num só sítio, e o que o registo e a variante têm em comum também;
- a coleção mostra os registos sem perguntar de que tipo é cada um.

O desafio é opcional e não entra nestes critérios.

## Autoavaliação

1. Que parte do teu programa ficou igual à do livro de receitas, e que parte tiveste de pensar de novo?
2. Num tema com dois limites, como as cartas ou o campeonato, que valores experimentaste para confirmar a regra?

![Rodapé](../imagens/rodape.png)
