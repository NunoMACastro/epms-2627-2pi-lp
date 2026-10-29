![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Exceções, depuração e logging

Laboratório do tema Exceções, depuração e logging, do módulo 10794, Programação avançada com Python. Vais pegar no ginásio Pokémon do tema 03 e dar-lhe três coisas novas, uma de cada vez. A primeira são exceções próprias para as recusas. A segunda é a investigação de dois erros com o depurador do VS Code. A terceira é um registo do que o ginásio faz. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](04-excecoes-depuracao-e-logging.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, o teu ginásio é igual à versão 04 do exemplo dos Pokémon. O `Treinador` recusa a captura de um sétimo Pokémon, e o `Ginasio` recusa um combate sem Pokémon com vida. As duas recusas são exceções próprias, que estão num ficheiro novo, o `erros.py`. O ginásio regista também os combates, e o programa que o usa escolhe o que quer ver desse registo. Pelo caminho, investigas dois erros com o depurador. Em dois desafios finais, acrescentas uma exceção tua e dás dados à `EquipaCheia`.

A pasta de trabalho acaba assim:

```text
ginasio-com-erros/
├── anunciadores.py
├── capturas.py
├── combates.py
├── erros.py
├── ginasio.py
├── investigar.py
├── pilha.py
├── pokemon.py
├── registo.py
└── teste_erros.py
```

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | O `erros.py` e o `teste_erros.py` | As três exceções do ginásio, em família, confirmadas pelo `isinstance` |
| 2 | O `capturar`, no `ginasio.py`, e o `capturas.py` | A equipa recusa o sétimo Pokémon e fica com seis |
| 3 | O `combater`, no `ginasio.py`, e o `combates.py` | Um combate sem Pokémon com vida é recusado, e o ginásio fica como estava |
| 4 | O `investigar.py` | Um erro de cálculo, sem mensagem de erro, encontrado com o depurador |
| 5 | O `pilha.py` | Um erro que rebenta longe da causa, seguido pela pilha de chamadas |
| 6 | O registo, no `ginasio.py`, e o `registo.py` | O ginásio regista os combates, e o nível escolhe-se no programa |
| 7 | O `registo.py` | O registo vai para um ficheiro, com a hora de cada mensagem |

Em todas as fases trabalhas da mesma maneira. Antes de executares um programa, escreves no papel, ou num ficheiro de texto, o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina. Todos os programas deste laboratório foram executados em Python 3.9 e em Python 3.14, com as mesmas saídas.

## Palavras que vais usar

- Exceção: a forma de o Python avisar que uma linha não pode ser feita. Sobe pelas funções que estão a meio até alguém a apanhar, ou até parar o programa.
- `raise`: a instrução que lança uma exceção. Em inglês quer dizer levantar.
- `try`, `except`, `else` e `finally`: o `try` é o bloco onde se espera uma exceção, e o `except` é o bloco que a trata, se for do tipo indicado. O `else` corre quando o `try` acaba sem exceção, e o `finally` corre sempre.
- Docstring: o texto entre três aspas, logo a seguir ao `def` ou ao `class`, que explica o que a função ou a classe faz.
- Herança: uma classe-filha herda tudo o que a classe-mãe tem. Em `class EquipaCheia(ErroDoGinasio)`, a classe entre parênteses é a classe-mãe.
- Exceção própria: uma classe criada por ti, filha de `Exception`, com um nome que diz o problema. Para saber mais, vê a secção "Uma exceção própria" do [guia](04-excecoes-depuracao-e-logging.md).
- `isinstance`: a função que pergunta se um objeto é de uma classe, ou de uma classe-filha dela, e devolve `True` ou `False`.
- Constante: um valor que o programa não muda, escrito em maiúsculas, como `TAMANHO_MAXIMO_DA_EQUIPA`.
- Sintoma e causa: o sintoma é o que se vê de um erro, como uma mensagem ou um valor errado. A causa é a linha de código que está mal e que provoca o sintoma. Os dois raramente estão no mesmo sítio.
- Hipótese: uma frase que diz o que achas que está a acontecer, e que os valores do programa podem confirmar ou desmentir.
- Erro de execução e erro de lógica: o erro de execução para o programa a meio, com uma mensagem. O erro de lógica deixa o programa correr até ao fim e dá o resultado errado.
- Traceback: a mensagem de erro completa, com o caminho de chamadas até à linha onde a exceção rebentou. Quer dizer, à letra, "o rasto para trás".
- Andar: cada par de linhas `File` de um traceback, com o ficheiro, a linha, a função e o código.
- Pilha de chamadas: a lista das funções e dos métodos que estão a meio, cada um à espera do que chamou.
- Depurador e ponto de paragem: o depurador corre o programa e deixa-o parar. O ponto de paragem é a linha onde ele para, antes de a executar. Para saber mais, vê a secção "O depurador do VS Code" do [guia](04-excecoes-depuracao-e-logging.md).
- Logging, logger e nível: o logging é o registo do que um programa faz, escrito para quem o mantém. O logger é o objeto que escreve as mensagens. O nível diz a importância de cada mensagem: `DEBUG`, `INFO`, `WARNING`, `ERROR` ou `CRITICAL`.
- `basicConfig`: a chamada que configura o registo do programa inteiro, com o nível mínimo, o formato das linhas e, se for preciso, o ficheiro.

## O que precisas

- O Python 3, para executar os programas. Confirma que o tens com o comando `python3 --version`. Deve aparecer `Python 3.` seguido de dois números, o que quer dizer que o Python está instalado. No Windows, se `python3` não funcionar, usa `python --version` ou `py --version`.
- O VS Code com a extensão Python da Microsoft, para escrever os ficheiros, executar os programas e depurá-los. Confirma que a tens: no ícone das extensões da barra lateral, escreve `Python` na caixa de pesquisa. A extensão da Microsoft deve aparecer como instalada.
- Os ficheiros `pokemon.py`, `ginasio.py` e `anunciadores.py` da [pasta 03 dos exemplos](../exemplos/python-avancado/pokemon/03-objetos-e-composicao/), que o laboratório copia na preparação. O [README do exemplo](../exemplos/python-avancado/pokemon/README.md) explica o que tem cada pasta.
- Papel, ou um ficheiro de texto, para as previsões e as respostas.
- O `ginasio.py` que copias já tem uma classe `Combate`, escrita com `@dataclass`, que o laboratório não muda. É por isso que o ficheiro começa por `from dataclasses import dataclass`. Deixa essa linha como está.

## Se alguma coisa falhar

1. Estás na pasta certa? Todos os comandos correm na pasta `ginasio-com-erros`. Se abriste o terminal do VS Code com essa pasta aberta, já lá estás. Para confirmar, escreve `pwd` (na linha de comandos clássica do Windows, `cd`) e vê se o caminho acaba em `ginasio-com-erros`.
2. Guardaste o ficheiro antes de executar? O Python executa o que está guardado no disco. Guarda e executa outra vez.
3. Os ficheiros estão todos na mesma pasta? O `ginasio.py` importa do `erros.py` e do `pokemon.py`, e só os encontra se estiverem na mesma pasta que ele.
4. Apareceu uma mensagem de erro que não esperavas? Lê a última linha: diz o tipo de erro e o que aconteceu. Procura essa linha em [Problemas frequentes](#problemas-frequentes).
5. Cada fase parte do ficheiro como ficou na paragem anterior. Se te perderes, compara o teu `ginasio.py` com o [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) do exemplo 04. Na paragem da fase 6, o teu é igual a ele. Na paragem da fase 3, é igual a ele sem as linhas do logger, que só entram na fase 6. O texto do início e a demonstração do fim do exemplo são diferentes em qualquer dos casos, porque não os mudas.

## Preparar o projeto

1. Cria uma pasta nova no teu computador, com o nome `ginasio-com-erros`, e abre-a no VS Code. No VS Code, o menu File, Open Folder (Ficheiro, Abrir Pasta, se estiver em português) abre uma pasta. Dar à pasta um nome sem espaços nem acentos evita problemas com os comandos.
2. Copia para essa pasta os três ficheiros da [pasta 03 dos exemplos](../exemplos/python-avancado/pokemon/03-objetos-e-composicao/): o `pokemon.py`, o `ginasio.py` e o `anunciadores.py`. Copia os dos exemplos, e não os teus do tema 03, para os testes deste laboratório darem exatamente as saídas indicadas. O VS Code mostra os ficheiros na barra lateral, à esquerda.
3. Abre o terminal do VS Code, que já fica na pasta aberta. Usa o menu Terminal, New Terminal (Terminal, Novo Terminal, em português), ou o atalho Ctrl+\` (a tecla do acento grave). Escreve o comando que executa a demonstração do ginásio:

```bash
python3 ginasio.py
```

O que deves ver: a demonstração do tema 03, com os combates, e uma última linha igual a esta:

```text
Ash continua com 2 Pokémon; Misty continua com 1.
```

Isto quer dizer que os três ficheiros estão no sítio certo e que o ponto de partida funciona. Se aparecer outra coisa, vê as [verificações rápidas](#se-alguma-coisa-falhar).

Ao longo do laboratório, vais mudar o `ginasio.py` e criar ficheiros novos nesta pasta. Os testes ficam em ficheiros à parte, e não no programa principal do `ginasio.py`.

## Fase 1: As exceções do ginásio

Até aqui, quando o ginásio não podia fazer o que lhe pediam, escrevia uma mensagem e saía. Quem o chamou não ficava a saber que o pedido falhou. Uma exceção própria resolve isso: é uma classe criada por ti, filha de `Exception`, que um método lança com `raise` quando recusa um pedido. Como herda de `Exception`, a classe herda tudo o que uma exceção precisa, incluindo a forma de guardar e mostrar a mensagem. Por isso o corpo pode ser só a docstring.

O ginásio vai ter três exceções, em família. O `ErroDoGinasio` é a classe-mãe, e a `EquipaCheia` e a `SemPokemonComVida` são filhas dele. Com uma classe-mãe comum, um só `except ErroDoGinasio` apanha qualquer erro do ginásio, e um `except` com o nome de uma filha apanha só esse caso. Para saber mais, lê a secção "Uma exceção própria" do [guia](04-excecoes-depuracao-e-logging.md).

1. Cria o ficheiro `erros.py`, na pasta `ginasio-com-erros`. Na barra lateral, passa o rato sobre o nome da pasta e clica no ícone do ficheiro com um sinal de mais (New File, Novo Ficheiro). Escreve o nome `erros.py` e carrega em Enter. O ficheiro é novo e fica completo, com este conteúdo:

```python
"""Exceções próprias do ginásio Pokémon, o código das aulas de Python avançado.

Todas herdam de ErroDoGinasio, que herda de Exception. Assim, quem quiser
apanhar qualquer erro do ginásio escreve except ErroDoGinasio, e quem quiser
apanhar só um caso escreve o nome da classe-filha.
"""


class ErroDoGinasio(Exception):
    """Classe-mãe de todos os erros do ginásio Pokémon."""


class EquipaCheia(ErroDoGinasio):
    """Um treinador tentou capturar um Pokémon com a equipa já completa."""


class SemPokemonComVida(ErroDoGinasio):
    """Um combate não pode começar: um dos treinadores não tem Pokémon com vida."""
```

Leitura guiada: o ficheiro abre com uma docstring que diz o que ele é e qual é a regra da família. Depois vêm as três classes. O `ErroDoGinasio` herda de `Exception`, e as outras duas herdam do `ErroDoGinasio`. Nenhuma tem mais do que a docstring, porque tudo o que uma exceção precisa vem da herança.

2. Cria o ficheiro `teste_erros.py`, com este conteúdo. O `isinstance(objeto, classe)` pergunta se o objeto é dessa classe, ou de uma classe-filha dela, e devolve `True` ou `False`. O programa usa-o para confirmar a família.

```python
# teste_erros.py: confirma que as exceções do ginásio formam uma família.
from erros import EquipaCheia, ErroDoGinasio, SemPokemonComVida

print(isinstance(EquipaCheia("teste"), ErroDoGinasio), isinstance(SemPokemonComVida("teste"), ErroDoGinasio))
print(isinstance(ErroDoGinasio("teste"), Exception))
erro = EquipaCheia("A equipa está cheia.")
print(erro)
```

Leitura guiada: a primeira linha faz duas perguntas, uma por cada filha: cada uma é um `ErroDoGinasio`? A segunda pergunta se o próprio `ErroDoGinasio` é uma exceção. As últimas duas linhas criam uma exceção com uma mensagem e mostram-na com `print`.

3. Antes de executares, escreve a tua previsão das três linhas. Depois, no terminal, corre:

```bash
python3 teste_erros.py
```

No Windows, se `python3` não funcionar, o comando é `python teste_erros.py` ou `py teste_erros.py`.

O que deves ver:

```text
True True
True
A equipa está cheia.
```

Isto quer dizer que as duas primeiras linhas confirmam a família: as duas exceções do ginásio são `ErroDoGinasio`, e um `ErroDoGinasio` é uma exceção. A terceira linha mostra que um `print` de uma exceção escreve a sua mensagem. Se aparecer `ModuleNotFoundError`, o `teste_erros.py` não está na mesma pasta que o `erros.py`: vê os [problemas frequentes](#problemas-frequentes).

### Paragem 1

Tens o `erros.py` com a família de exceções, e o teste confirma que as duas filhas são `ErroDoGinasio` e que o `ErroDoGinasio` é uma exceção.

Pensa antes de continuares: porque é que a `EquipaCheia` não precisa de mais código do que a docstring? A resposta: porque herda do `ErroDoGinasio`, que herda de `Exception`, tudo o que uma exceção precisa para guardar e mostrar a mensagem.

## Fase 2: A equipa cheia

Quando um método recusa um pedido, tem de o fazer antes de mexer no estado. Se o `raise` viesse depois do `append`, o Pokémon recusado ficava na equipa, e a mensagem diria uma coisa enquanto o estado diria outra. Nesta fase pões um limite de seis Pokémon na equipa do `Treinador`, guardado numa constante, e fazes o `capturar` lançar a `EquipaCheia` quando a equipa já o atingiu. Quem chama o `capturar` apanha a recusa com `try` e `except`, e o `else` corre só quando a captura correu bem. Para saber mais, lê as secções "raise: uma recusa que não se pode ignorar" e "As exceções do ginásio" do [guia](04-excecoes-depuracao-e-logging.md).

1. Em `ginasio.py`, substitui a linha `from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta` por estas linhas. Trazem para o ficheiro as duas exceções e a constante com o limite da equipa. Ter o limite num só sítio evita repeti-lo na condição e na mensagem.

```python
from erros import EquipaCheia, SemPokemonComVida
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta

TAMANHO_MAXIMO_DA_EQUIPA = 6
```

Leitura guiada: as duas importações trazem para o `ginasio.py` as exceções do `erros.py`. A constante fica logo a seguir, no início do ficheiro, onde qualquer método a lê. A `SemPokemonComVida` ainda não é usada: entra na fase 3.

2. Em `ginasio.py`, substitui o método `capturar` do `Treinador` por este. A verificação vem antes do `append`. A linha `class Treinador:` do bloco só mostra onde o método fica: não a copies.

```python
class Treinador:
    # Só o método capturar muda; o resto da classe fica como estava.

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador.

        Se a equipa já tem TAMANHO_MAXIMO_DA_EQUIPA Pokémon, não junta nada e
        lança EquipaCheia.
        """
        if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
            raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
        self.equipa.append(pokemon)
```

Leitura guiada: a verificação vem primeiro. O `len(self.equipa)` é o número de Pokémon na equipa, e o `>=` compara-o com o limite. Se a equipa já está cheia, o `raise` cria a `EquipaCheia`, com uma mensagem que diz quem, quantos e que Pokémon ficou de fora, e o método para aí. O `append` só corre se a verificação passar.

3. Cria o ficheiro `capturas.py`, com este conteúdo. O Brock tenta capturar oito Pokémon para seis lugares.

```python
# capturas.py: testa o limite da equipa, com oito capturas para seis lugares.
from erros import EquipaCheia
from pokemon import Pokemon
from ginasio import Treinador

brock = Treinador("Brock")
nomes = ["Geodude", "Onix", "Vulpix", "Zubat", "Sandshrew", "Rhyhorn", "Kabuto", "Omanyte"]
for nome in nomes:
    try:
        brock.capturar(Pokemon(nome, "Pedra", 50, 20))
    except EquipaCheia as erro:
        print(f"Recusado: {erro}")
    else:
        print(f"{nome} capturado.")
print(len(brock.equipa))
```

Leitura guiada: o ciclo percorre os oito nomes e tenta capturar cada um dentro de um `try`. Se o `capturar` lança a `EquipaCheia`, o `except` escreve a mensagem. Se não lança, o `else` escreve que o Pokémon foi capturado. O último `print` conta os Pokémon que ficaram na equipa.

4. Antes de executares, escreve quantas linhas "capturado" vão aparecer, quais são os Pokémon recusados e qual é o número da última linha. Depois executa:

```bash
python3 capturas.py
```

O que deves ver:

```text
Geodude capturado.
Onix capturado.
Vulpix capturado.
Zubat capturado.
Sandshrew capturado.
Rhyhorn capturado.
Recusado: Brock já tem 6 Pokémon e não pode capturar Kabuto.
Recusado: Brock já tem 6 Pokémon e não pode capturar Omanyte.
6
```

Isto quer dizer que a equipa aceitou seis Pokémon e recusou os dois últimos. Se aparecer outra coisa, vê os [problemas frequentes](#problemas-frequentes).

5. Responde por escrito: porque é que a última linha diz 6, e não 8, se o ciclo tentou oito capturas?

A resposta: porque o `raise` para o `capturar` antes do `append`. As duas capturas recusadas não chegaram a mexer na equipa. O ciclo continuou, porque o `except` apanhou as duas exceções.

6. Agora uma experiência, com um erro de propósito. Troca no `capturar` a ordem do `append` e da verificação, de forma que o `append` venha primeiro. Antes de executares, prevê o que muda na saída. Em `ginasio.py`, substitui o método `capturar` por esta versão com erro, executa o `capturas.py` outra vez e compara:

```python
class Treinador:
    # Versão com erro de propósito: só o método capturar muda.

    def capturar(self, pokemon):
        """Versão com erro de propósito: o append vem antes da verificação."""
        self.equipa.append(pokemon)
        if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
            raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
```

O que deves ver:

```text
Geodude capturado.
Onix capturado.
Vulpix capturado.
Zubat capturado.
Sandshrew capturado.
Recusado: Brock já tem 6 Pokémon e não pode capturar Rhyhorn.
Recusado: Brock já tem 6 Pokémon e não pode capturar Kabuto.
Recusado: Brock já tem 6 Pokémon e não pode capturar Omanyte.
8
```

Isto acontece porque o Rhyhorn entrou na equipa e foi dado como recusado, e a equipa acaba com oito. A mensagem diz uma coisa e o estado diz outra. A experiência mostra que o `raise` tem de vir antes de qualquer alteração ao estado. Para corrigir, volta a pôr no `ginasio.py` o `capturar` do passo 2 e executa o `capturas.py` para confirmar que a última linha volta a ser 6.

### Paragem 2

O `Treinador` recusa o sétimo Pokémon com uma exceção, e a equipa fica com seis. O `capturas.py` mostra exatamente as nove linhas do passo 4.

Pensa antes de continuares: se o `capturar` escrevesse a mensagem com `print` em vez de lançar a exceção, o `capturas.py` conseguia distinguir os Pokémon capturados dos recusados? A resposta: não. O `else` correria sempre, porque o `capturar` nunca falharia, e o programa escreveria "capturado" para os oito. A exceção é o que avisa o código que chamou.

## Fase 3: O combate recusado

O `combater` do tema 03 escrevia "Não há combate" e saía quando um dos treinadores não tinha Pokémon com vida. Quem o chamava não sabia se tinha havido combate. Nesta fase trocas isso por uma exceção. Há uma segunda mudança, mais subtil: a verificação passa para antes de o desafiante entrar na lista de desafiantes. Assim, um combate recusado deixa o ginásio exatamente como estava. O `finally` de um `try` corre sempre, haja ou não exceção, e vai servir para escrever, depois de cada desafio, quantos desafiantes e quantos combates o ginásio tem. Para saber mais, lê as secções "As exceções do ginásio" e "finally: o que corre sempre" do [guia](04-excecoes-depuracao-e-logging.md).

1. Em `ginasio.py`, no método `combater` do `Ginasio`, substitui as linhas desde `def combater(self, desafiante):` até ao `return` (inclusive) por este bloco. O `print` com os sinais `===` e o resto do método ficam como estão. A linha `class Ginasio:` do bloco só mostra onde o método fica: não a copies.

```python
class Ginasio:
    # Só o início do método combater muda; o resto da classe fica como estava.

    def combater(self, desafiante):
        """Um combate entre o Pokémon escolhido por cada treinador.

        Se um dos dois não tem Pokémon com vida, não há combate: lança
        SemPokemonComVida, e o ginásio fica como estava.
        """
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
```

Leitura guiada: o método começa por perguntar a cada treinador qual é o Pokémon que vai lutar. Se algum devolve `None`, não há combate, e o `raise` lança a `SemPokemonComVida` e o método para. A lista de desafiantes só é alterada depois da verificação, e por isso um combate recusado não deixa rasto. O resto do método, que começa no `print` com os sinais `===`, fica como estava.

2. Cria o ficheiro `combates.py`, com este conteúdo. O Brock entra com um Geodude que já não tem vida nenhuma.

```python
# combates.py: um desafiante sem Pokémon com vida é recusado, e o ginásio fica como estava.
from erros import ErroDoGinasio
from pokemon import Pokemon, PokemonAgua, PokemonFogo
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
gary = Treinador.com_equipa("Gary", [PokemonFogo("Vulpix", 30, 20)])
brock = Treinador.com_equipa("Brock", [Pokemon("Geodude", "Pedra", 0, 10)])
cerulean = Ginasio("Cerulean", misty)
for desafiante in [gary, brock, gary]:
    try:
        cerulean.combater(desafiante)
    except ErroDoGinasio as erro:
        print(f"{desafiante.nome} recusado: {erro}")
    finally:
        print(f"Desafiantes: {len(cerulean.desafiantes)}, combates: {len(cerulean.combates)}")
```

Leitura guiada: o programa cria a líder, dois desafiantes e o ginásio. O ciclo faz três desafios, e o `except ErroDoGinasio` apanha qualquer recusa do ginásio. O `finally` escreve a mesma linha depois de cada desafio, com ou sem recusa.

3. Antes de executares, prevê o que acontece a cada um dos três desafios, e as três linhas com os desafiantes e os combates. Depois executa:

```bash
python3 combates.py
```

O que deves ver. Depois do primeiro combate, que o Gary perde, a saída acaba assim:

```text

=== Gary desafia Misty no ginásio de Cerulean ===
Vulpix ataca Starmie e tira 20 de vida.
Starmie tem 70/150 de vida.
É super eficaz!
Starmie ataca Vulpix e tira 70 de vida.
Vulpix está KO (0/150).
Desafiantes: 1, combates: 1
Brock recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
Desafiantes: 1, combates: 1
Gary recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
Desafiantes: 1, combates: 1
```

Isto quer dizer que o primeiro desafio é um combate a sério, e que os outros dois são recusados. O Brock é recusado porque o Geodude não tem vida. O Gary é recusado porque o Vulpix ficou KO no primeiro combate.

4. Responde por escrito às três perguntas.

O Brock foi recusado e não entrou na lista de desafiantes. Que linha do teu `combater` garante isso? A resposta: a linha `if desafiante not in self.desafiantes:` com o `append` por baixo, porque está depois do `raise`. Quando o combate é recusado, o método para antes de chegar lá.

Na versão do tema 03, o desafiante entrava na lista logo no início do `combater`. Com essa ordem, o que diria a linha dos desafiantes depois do Brock, e porque estaria errado? A resposta: diria `Desafiantes: 2, combates: 1`. O Brock ficava na lista sem ter combatido. Estaria errado porque a lista diz quem desafiou o ginásio, e o Brock não chegou a desafiar. O ginásio mudava, quando a docstring diz que fica como estava.

A linha dos desafiantes e dos combates aparece três vezes, embora só tenha havido um combate. Porquê? A resposta: o `finally` corre em todas as voltas, com ou sem exceção. Houve três desafios, e por isso três linhas.

### Paragem 3

O `Ginasio` recusa um combate sem Pokémon com vida com uma exceção, e fica como estava. Neste ponto, o teu `ginasio.py` tem as duas exceções, a constante, o `capturar` com a verificação e o `combater` novo. O `capturas.py` e o `combates.py` mostram as saídas dos passos 4 da fase 2 e 3 da fase 3. Para o conferires, compara-o com o [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) do exemplo 04, sem as linhas do logger: o `import logging`, o `logger = logging.getLogger(__name__)` e as quatro linhas que começam por `logger.`. O texto do início e a demonstração do fim do exemplo também são diferentes, porque não os mudas.

## Fase 4: Investigar um erro de cálculo com o depurador

Um erro de lógica não tem mensagem de erro: o programa corre até ao fim e dá o resultado errado. Para o encontrar, segue-se uma rotina de cinco passos. Primeiro, observas e reproduzes o erro: escreves o caso que falhou, o resultado esperado e o obtido, e dizes que tipo de erro é. Depois, escreves uma hipótese. Em terceiro lugar, verificas a hipótese, olhando para os valores do programa enquanto corre. Em quarto, corriges a causa. Por fim, voltas a testar todos os casos, também os que já passavam.

O depurador do VS Code é a ferramenta do terceiro passo. Corre o programa e deixa-o parar numa linha que escolhes, para veres os valores das variáveis e avançares uma linha de cada vez. É como a tabela com os valores das variáveis, linha a linha, que podes fazer no papel, mas feita pelo computador, com os valores verdadeiros. Os controlos de que precisas, nesta fase e na seguinte, são estes:

| Para quê | Como |
| --- | --- |
| Pôr um ponto de paragem, a linha onde o programa para antes de a executar | Clicar na margem, à esquerda do número da linha: aparece um ponto vermelho. Clicar outra vez tira-o. Também se põe com F9, na linha onde está o cursor |
| Executar com o depurador, ou continuar até ao próximo ponto de paragem | F5 |
| Avançar uma linha, sem entrar nas funções que ela chama | F10 |
| Parar a depuração | Shift+F5 |

Quando o programa está parado, a linha que vai correr a seguir aparece marcada a amarelo, e a barra lateral mostra três painéis. O painel Variáveis (Variables) tem os valores das variáveis da função onde o programa está parado, e um objeto abre-se com a seta, para ver os seus atributos. O painel Pilha de chamadas (Call Stack) tem os andares do traceback. O painel Vigiar (Watch) tem expressões que escreves tu, que o VS Code recalcula a cada passo.

Em computadores portáteis e em Mac, as teclas F5, F10 e F11 podem precisar da tecla Fn. Na primeira vez que carregas em F5, o VS Code pode perguntar que depurador usar. Escolhe o de Python, e depois a opção de depurar o ficheiro que está aberto (Python Debugger e Python File, em inglês). O botão do triângulo, no canto de cima, corre o programa sem o depurador e ignora os pontos de paragem. Para depurar, usa o F5. Para saber mais, lê as secções "Um erro tem um sintoma e uma causa" e "O depurador do VS Code" do [guia](04-excecoes-depuracao-e-logging.md).

1. Cria o ficheiro `investigar.py`, com este conteúdo. Tem uma cópia da classe `PokemonAgua`, com um erro de propósito. Um Squirtle, de água, ataca um Charmander, de fogo, e a água devia tirar o dobro ao fogo.

```python
# investigar.py: um erro de lógica para encontrar com o depurador.
from pokemon import Pokemon, PokemonFogo


class PokemonAgua(Pokemon):
    """Uma cópia da PokemonAgua do pokemon.py, com um erro de propósito para investigar."""

    def __init__(self, nome, vida, ataque):
        """Cria um Pokémon de água com nome, vida e ataque."""
        super().__init__(nome, "Água", vida, ataque)

    def calcular_dano(self, alvo):
        """Contra Fogo, a água tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "fogo":
            print("É super eficaz!")
            dano = dano * 2
        return dano


squirtle = PokemonAgua("Squirtle", 100, 30)
charmander = PokemonFogo("Charmander", 90, 40)
squirtle.atacar(charmander)
```

Leitura guiada: a classe `PokemonAgua` herda da `Pokemon` e reescreve o `calcular_dano`. Começa por pedir à classe-mãe o dano normal, que é o ataque. Depois, se o tipo do alvo for o que a condição diz, escreve a mensagem e dobra o dano. No fim, o programa cria um Squirtle e um Charmander e faz o Squirtle atacar.

2. Observa e reproduz o erro. Executa o programa normalmente, com `python3 investigar.py`, e regista o sintoma: quanto devia tirar o ataque, quanto tirou, e o que falta na saída. O que deves ver:

```text
Squirtle ataca Charmander e tira 30 de vida.
Charmander tem 60/150 de vida.
```

A resposta: o caso é o Squirtle, com 30 de ataque, a atacar o Charmander. A água tira o dobro ao fogo, por isso devia tirar 60, com a mensagem "É super eficaz!". Tirou 30, e a mensagem não apareceu. O programa correu até ao fim e deu o resultado errado, por isso é um erro de lógica.

3. Antes de abrires o depurador, escreve a tua hipótese: o que achas que está a acontecer, em que linha, e o que esperas ver no depurador se tiveres razão. Escreve-a antes, porque, se a escreveres depois, vais olhar para os valores à procura do que já sabes.

A resposta: uma hipótese que serve é que a condição do `if` está a dar falso, e por isso as duas linhas do bloco do `if` não correm. Se for isso, no depurador o `if` salta diretamente para o `return`, e o `dano` fica em 30. Outras hipóteses bem escritas também servem, mesmo erradas: o que conta é estarem escritas antes e dizerem o que esperas ver.

4. Verifica a hipótese. Põe um ponto de paragem na linha `dano = super().calcular_dano(alvo)`, clicando na margem à esquerda do número dessa linha. Com o `investigar.py` aberto no editor, carrega em F5. Quando o programa parar, abre o `alvo` no painel das variáveis e regista o valor do `tipo`.

O que deves ver: o ponto vermelho na margem, a linha `dano = super().calcular_dano(alvo)` marcada a amarelo, e o `tipo` do `alvo` a valer `'Fogo'`. Isto quer dizer que o programa parou antes de a linha correr, e que o tipo está guardado com a maiúscula do `pokemon.py`. Se o programa correr até ao fim sem parar, executaste sem o depurador: vê os [problemas frequentes](#problemas-frequentes).

5. No painel Vigiar, acrescenta duas expressões: `alvo.tipo` e `alvo.tipo == "fogo"`. Para acrescentar uma, clica no sinal de mais do painel, escreve a expressão e carrega em Enter. Regista o que o VS Code mostra para cada uma.

O que deves ver: `'Fogo'` para a primeira e `False` para a segunda. Isto quer dizer que o tipo do alvo é `'Fogo'`, com maiúscula, e que a comparação com `"fogo"`, em minúsculas, dá falso.

6. Avança com F10, linha a linha, até ao `return`. Regista, depois de cada F10, a linha marcada a amarelo e o valor do `dano`, numa tabela. O que deves ver:

| Depois de | Linha marcada a amarelo | `dano` |
| --- | --- | --- |
| Parar no ponto de paragem | `dano = super().calcular_dano(alvo)` | ainda não existe |
| F10 | `if alvo.tipo == "fogo":` | 30 |
| F10 | `return dano` | 30 |

O depurador salta do `if` diretamente para o `return`: as duas linhas do bloco do `if` não correm. Isto confirma a hipótese de exemplo, a de que a condição do `if` dá falso.

7. Corrige a causa. Carrega em Shift+F5 para parar a depuração. A comparação é com `"fogo"`, em minúsculas, e o tipo está guardado como `"Fogo"`. Para o Python, os dois textos são diferentes, e a condição é simplesmente falsa: não há erro nenhum, só um resultado errado. É por isso que o Python não deu nenhuma mensagem de erro. Em `investigar.py`, substitui o método `calcular_dano` da classe `PokemonAgua` por este. A linha `class PokemonAgua(Pokemon):` do bloco só mostra onde o método fica: não a copies.

```python
class PokemonAgua(Pokemon):
    # Só o método calcular_dano muda; o resto da classe fica como estava.

    def calcular_dano(self, alvo):
        """Contra Fogo, a água tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Fogo":
            print("É super eficaz!")
            dano = dano * 2
        return dano
```

Leitura guiada: o método é o mesmo, e só mudou a grafia do texto na condição, de `"fogo"` para `"Fogo"`. Agora a comparação usa o tipo como o resto do código o escreve, e por isso a condição dá verdadeiro quando o alvo é de fogo.

8. Volta a testar tudo. Executa o programa outra vez. O que deves ver:

```text
É super eficaz!
Squirtle ataca Charmander e tira 60 de vida.
Charmander tem 30/150 de vida.
```

Falta o caso que já funcionava, o de um alvo que não é de fogo. Na linha do `import`, acrescenta `PokemonPlanta`, e no fim do ficheiro acrescenta duas linhas:

```python
from pokemon import Pokemon, PokemonFogo, PokemonPlanta
```

```python
bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
squirtle.atacar(bulbasaur)
```

Executa outra vez. Contra a planta, a água não tem vantagem, por isso o dano é o ataque, 30, e não aparece a mensagem. O que deves ver no fim da saída:

```text
Squirtle ataca Bulbasaur e tira 30 de vida.
Bulbasaur tem 80/150 de vida.
```

Os dois casos passam: o que mudou foi só a grafia de um texto, e o dobro aplica-se agora só contra o fogo.

9. Responde por escrito: a hipótese que escreveste antes de abrir o depurador estava certa? Se não estava, o que é que o depurador te mostrou que não esperavas? E qual era a causa?

A resposta: se a tua hipótese era que a condição do `if` dava falso, estava certa, e o depurador confirmou-a na tabela que fizeste com o F10. Se era outra, o que interessa é dizer o que o depurador mostrou de diferente. A causa era a comparação com `"fogo"`, em minúsculas, quando o tipo está guardado como `"Fogo"`. O Python não deu mensagem de erro porque, para ele, comparar dois textos diferentes não é um erro: o resultado é só `False`.

### Paragem 4

O `investigar.py` corrigido mostra o dobro do dano contra o fogo e o dano normal contra a planta. Tens escritas a hipótese e a tabela que fizeste com o F10.

Pensa antes de continuares: o erro desapareceria se tivesses acrescentado ao `calcular_dano` um `if` para o Squirtle, em vez de corrigires a comparação? A resposta: o resultado desse caso passava a estar certo, mas a causa ficava lá, à espera de outro Pokémon de água contra outro Pokémon de fogo. Corrigir a causa é mudar a instrução que produz o erro, e não o sítio onde ele se vê.

## Fase 5: Um erro que rebenta longe da causa

Um erro de execução para o programa com uma mensagem, o traceback. O traceback mostra onde o erro rebentou e o caminho até lá, mas a causa pode estar numa linha que já acabou. Lê-se de baixo para cima. A última linha diz o quê. O andar de baixo diz onde rebentou, e os andares de cima dizem como se chegou lá. A pilha de chamadas é a lista das funções que estão a meio, cada uma à espera do que chamou, e o depurador mostra-a com os valores de cada andar. Para saber mais, lê as secções "Ler um traceback com três andares" e "A pilha de chamadas no depurador" do [guia](04-excecoes-depuracao-e-logging.md).

1. Cria o ficheiro `pilha.py`, com este conteúdo. Tem um erro de propósito: a equipa do Ash leva o texto `"Squirtle"` no lugar de um Pokémon.

```python
# pilha.py: um erro que rebenta longe da causa. A equipa do Ash tem um erro de propósito.
from pokemon import PokemonAgua, PokemonFogo
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 30, 40), "Squirtle"])
cerulean = Ginasio("Cerulean", misty)
cerulean.combater(ash)
cerulean.combater(ash)
```

Leitura guiada: o programa cria a líder e o Ash, cuja equipa tem um Charmander e um texto. O ginásio faz dois combates seguidos com o Ash. O texto `"Squirtle"` entra na equipa sem queixa, porque a lista aceita qualquer valor.

2. Observa e reproduz o erro. Executa o programa com `python3 pilha.py`. O primeiro combate acontece, o Charmander perde, e o programa para com um traceback. O que deves ver:

```text

=== Ash desafia Misty no ginásio de Cerulean ===
Charmander ataca Starmie e tira 40 de vida.
Starmie tem 50/150 de vida.
É super eficaz!
Starmie ataca Charmander e tira 70 de vida.
Charmander está KO (0/150).
Traceback (most recent call last):
  File "pilha.py", line 9, in <module>
    cerulean.combater(ash)
    ~~~~~~~~~~~~~~~~~^^^^^
  File "ginasio.py", line 125, in combater
    atacante = desafiante.escolher_pokemon()
  File "ginasio.py", line 72, in escolher_pokemon
    if pokemon.vida > 0:
       ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'vida'
```

O traceback tem os caminhos completos do teu computador no lugar dos nomes simples dos ficheiros. As linhas com `~` e `^` só aparecem nas versões recentes do Python. Se o teu `ginasio.py` for diferente do do laboratório, os números das linhas dele podem ser outros. A última linha está em inglês: `'str' object has no attribute 'vida'` quer dizer "um objeto `str` não tem o atributo `vida`", e `str` é o tipo dos textos. É um erro de execução.

3. Lê o traceback de baixo para cima e responde, antes de abrires o depurador: em que linha do `pilha.py` começou o caminho até ao erro? Por que funções passou? Em que linha do `ginasio.py` rebentou?

A resposta: o caminho começou na linha 9 do `pilha.py`, o segundo `cerulean.combater(ash)`. Passou pelo `combater` e pelo `escolher_pokemon`. Rebentou no `if pokemon.vida > 0:` do `escolher_pokemon`, onde o `pokemon` era um texto.

4. Verifica a causa com o depurador. Com o `pilha.py` aberto no editor, executa com o F5, sem nenhum ponto de paragem. Por omissão, quando há uma exceção que ninguém apanha, o depurador não deixa o programa acabar: para na linha onde a exceção rebentou e marca-a. No painel da pilha de chamadas, clica em cada andar. Para o andar do `combater`, regista o que está na `equipa` do `desafiante`.

O que deves ver: o programa parado no `if pokemon.vida > 0:`, com a exceção descrita por cima da linha, e três andares na pilha: `escolher_pokemon`, `combater` e `<module>`. No andar `escolher_pokemon`, o `pokemon` vale `'Squirtle'`. No andar `combater`, abrindo o `desafiante`, a `equipa` tem dois elementos: o Charmander, que é um objeto, e o texto `'Squirtle'`. No andar `<module>`, estás no programa principal, onde o `ash` foi criado.

5. Corrige a causa. Carrega em Shift+F5 para parar a depuração. A causa não está em nenhum dos três andares do traceback, mas na linha onde a equipa do Ash foi criada. O Ash devia ter um Squirtle a sério. No `pilha.py`, substitui a linha do Ash por esta:

```python
ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 30, 40), PokemonAgua("Squirtle", 100, 30)])
```

Leitura guiada: a lista da equipa continua a ter dois elementos, mas agora os dois são Pokémon. O `PokemonAgua` já estava importado no ficheiro, porque a Misty o usa.

6. Volta a testar tudo. Executa outra vez. O primeiro combate é igual, e o segundo passa a acontecer. O Squirtle, de água contra água e sem vantagem, ganha em dois ataques ao Starmie, que só tinha 50 de vida. O que deves ver:

```text

=== Ash desafia Misty no ginásio de Cerulean ===
Charmander ataca Starmie e tira 40 de vida.
Starmie tem 50/150 de vida.
É super eficaz!
Starmie ataca Charmander e tira 70 de vida.
Charmander está KO (0/150).

=== Ash desafia Misty no ginásio de Cerulean ===
Squirtle ataca Starmie e tira 30 de vida.
Starmie tem 20/150 de vida.
Starmie ataca Squirtle e tira 35 de vida.
Squirtle tem 65/150 de vida.
Squirtle ataca Starmie e tira 30 de vida.
Starmie está KO (0/150).
```

7. Responde por escrito às duas perguntas.

O erro está na linha onde a equipa foi criada, e o primeiro combate correu bem. Porque é que só rebentou no segundo? A resposta: o `escolher_pokemon` devolve o primeiro Pokémon com vida e para. No primeiro combate, o Charmander tinha vida e foi devolvido antes de o ciclo chegar ao texto. No segundo, o Charmander já estava KO, o ciclo passou para o elemento seguinte, e foi aí que rebentou. Um erro pode ficar escondido enquanto o caminho do programa não passa por ele.

Um colega propõe corrigir o `escolher_pokemon` para saltar tudo o que não tenha vida. Porque é que isso esconde o erro, em vez de o corrigir? A resposta: o Ash ficava com uma equipa em que o "Squirtle" nunca luta, sem nenhuma mensagem, e ninguém percebia porquê. O erro está na linha onde a equipa foi criada com um texto, e é aí que se corrige.

### Paragem 5

O `pilha.py` corrigido faz os dois combates. Já sabes ler um traceback de baixo para cima e usar a pilha de chamadas no depurador para ver o estado de cada andar.

Pensa antes de continuares: nenhum dos três andares do traceback era a linha que estava mal. Então, para que serve o traceback? A resposta: diz o que falhou, onde rebentou e o caminho até lá. É o ponto de partida da investigação, e a causa procura-se a partir dele, na pilha de chamadas e nos valores de cada andar.

## Fase 6: O registo do ginásio

O `print` é para quem usa o programa, e o registo é para quem o mantém. O módulo `logging` do Python deixa um programa escrever mensagens de registo, cada uma com um nível que diz a importância do que aconteceu. O `DEBUG` é para pormenores que só interessam a quem investiga. O `INFO` é para o programa a funcionar como devia. O `WARNING` é para uma coisa inesperada que o programa conseguiu tratar. O `ERROR` é para uma operação que falhou, e o `CRITICAL` para uma falha tão grave que o programa não pode continuar.

As mensagens ficam no código, escritas por um logger. Quem decide que nível mínimo se mostra, e como se escreve cada linha, é o programa principal, com uma chamada ao `logging.basicConfig`. Assim, para ver mais ou menos mensagens, não se mexe no ginásio. Para saber mais, lê as secções "Os cinco níveis", "O registo do ginásio" e "Quem configura é o programa" do [guia](04-excecoes-depuracao-e-logging.md).

1. Em `ginasio.py`, substitui as linhas desde `from dataclasses import dataclass` até `TAMANHO_MAXIMO_DA_EQUIPA = 6` por estas. Trazem o módulo `logging` e criam o logger do ficheiro. A linha `from dataclasses import dataclass` repete-se porque está dentro do que substituis, e fica igual.

```python
import logging
from dataclasses import dataclass

from erros import EquipaCheia, SemPokemonComVida
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta

TAMANHO_MAXIMO_DA_EQUIPA = 6

logger = logging.getLogger(__name__)
```

Leitura guiada: o `import logging` traz o módulo para o ficheiro. O `logging.getLogger(__name__)` devolve o logger do ficheiro. O `__name__` é o nome do módulo, `"ginasio"` quando outro programa o importa, e é esse nome que aparece nas mensagens, para se saber de onde vieram.

2. Em `ginasio.py`, substitui o método `combater` inteiro por este. É o da fase 3 com quatro mensagens a mais: o aviso antes do `raise`, o `info` e o `debug` do início do combate, e o `info` do fim. A linha `class Ginasio:` do bloco só mostra onde o método fica: não a copies.

```python
class Ginasio:
    # Só o método combater muda; o resto da classe fica como estava.

    def combater(self, desafiante):
        """Um combate entre o Pokémon escolhido por cada treinador.

        Se um dos dois não tem Pokémon com vida, não há combate: lança
        SemPokemonComVida, e o ginásio fica como estava.
        """
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            logger.warning(f"Combate recusado em {self.cidade}: {desafiante.nome} contra {self.lider.nome}, sem Pokémon com vida.")
            raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        logger.info(f"Combate em {self.cidade}: {desafiante.nome} com {atacante.nome} contra {self.lider.nome} com {defensor.nome}.")
        logger.debug(f"Vida no início: {atacante.nome} {atacante.vida}, {defensor.nome} {defensor.vida}.")
        print(f"\n=== {desafiante.nome} desafia {self.lider.nome} no ginásio de {self.cidade} ===")
        while True:
            atacante.atacar(defensor)
            if defensor.vida == 0:
                vencedor = desafiante
                break
            defensor.atacar(atacante)
            if atacante.vida == 0:
                vencedor = self.lider
                break
        # O registo nasce aqui dentro: é o ginásio que o cria e o guarda.
        self.combates.append(Combate(desafiante.nome, atacante.nome, vencedor.nome))
        logger.info(f"Fim do combate em {self.cidade}: venceu {vencedor.nome}.")
```

Leitura guiada: cada nível é um método do logger, com o nome do nível em minúsculas, e recebe a mensagem escrita com uma f-string. O aviso está dentro do `if` que recusa o combate, antes do `raise`, porque depois do `raise` o método já parou. As duas mensagens seguintes só correm quando o combate vai mesmo acontecer. O `info` diz quem combate com quem, e o `debug` guarda um pormenor que só interessa a quem investiga, a vida de cada Pokémon antes do primeiro ataque. A última mensagem, de `info`, diz quem venceu.

3. Cria o ficheiro `registo.py`, com este conteúdo. É o programa principal que configura o registo, com o nível `INFO`.

```python
# registo.py: o ginásio de Celadon regista os combates, e este programa escolhe o que se vê.
import logging

from erros import ErroDoGinasio
from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10)])
misty = Treinador.com_equipa("Misty", [PokemonAgua("Psyduck", 60, 20)])
celadon = Ginasio("Celadon", erika)
for tentativa in range(2):
    try:
        celadon.combater(misty)
    except ErroDoGinasio as erro:
        print(f"Recusado: {erro}")
```

Leitura guiada: a chamada ao `basicConfig` vem antes de tudo o que regista. O `level` é o nível mínimo: com `logging.INFO`, as mensagens de `DEBUG` não aparecem. O `format` diz como se escreve cada linha: `%(levelname)s` é o nível, `%(name)s` é o nome do logger e `%(message)s` é a mensagem. O resto cria a Erika, a Misty e o ginásio, e a Misty desafia duas vezes. O segundo desafio é recusado, porque o Psyduck fica KO no primeiro.

4. Antes de executares, prevê que linhas do registo vão aparecer, com que nível, e onde ficam em relação às linhas do combate. Depois executa:

```bash
python3 registo.py
```

O que deves ver. As linhas do registo são as três que começam por um nível entre parênteses retos: a primeira antes do combate e as outras duas depois dele.

```text
[INFO] ginasio: Combate em Celadon: Misty com Psyduck contra Erika com Tangela.

=== Misty desafia Erika no ginásio de Celadon ===
Psyduck ataca Tangela e tira 20 de vida.
Tangela tem 30/150 de vida.
É super eficaz!
Tangela ataca Psyduck e tira 40 de vida.
Psyduck tem 20/150 de vida.
Psyduck ataca Tangela e tira 20 de vida.
Tangela tem 10/150 de vida.
É super eficaz!
Tangela ataca Psyduck e tira 40 de vida.
Psyduck está KO (0/150).
[INFO] ginasio: Fim do combate em Celadon: venceu Erika.
[WARNING] ginasio: Combate recusado em Celadon: Misty contra Erika, sem Pokémon com vida.
Recusado: Não há combate em Celadon: um dos treinadores não tem Pokémon com vida.
```

Isto quer dizer que o `INFO` do início e do fim, e o `WARNING` do combate recusado, vieram do registo, e que o combate e o "Recusado" vieram dos `print`. A mensagem de `DEBUG` não aparece, porque o nível mínimo é `INFO`.

5. Muda o nível no `registo.py` para `logging.DEBUG`, na linha do `basicConfig`, e executa outra vez. O que deves ver, logo a seguir à primeira linha do registo:

```text
[DEBUG] ginasio: Vida no início: Psyduck 60, Tangela 50.
```

6. Muda o nível para `logging.WARNING` e executa. Das linhas do registo, só fica a do aviso. As do `INFO` e a do `DEBUG` deixam de aparecer, e o combate e o "Recusado" continuam, porque são `print`. O que deves ver, no fim da saída:

```text
[WARNING] ginasio: Combate recusado em Celadon: Misty contra Erika, sem Pokémon com vida.
Recusado: Não há combate em Celadon: um dos treinadores não tem Pokémon com vida.
```

7. Responde por escrito: para ver as mensagens de `DEBUG`, mudaste uma palavra no `registo.py` e nenhuma no `ginasio.py`. Porque é que isso é uma vantagem em relação a acrescentar e apagar `print`?

A resposta: as mensagens ficam no código, num só sítio, e a configuração decide o que se vê. Não é preciso acrescentar `print` para investigar, nem apagá-los depois, nem lembrar onde estavam quando o erro volta. Não se mexe no ginásio para o investigar.

### Paragem 6

O ginásio regista os combates em três níveis, e o programa escolhe o que se vê. Neste ponto, o teu `ginasio.py` é igual ao da pasta 04 dos exemplos, a não ser no texto do início e na demonstração do fim, que não mudaste. Podes conferir o teu com o [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) do exemplo.

Pensa antes de continuares: porque é que o `basicConfig` está no `registo.py`, e não no `ginasio.py`? A resposta: o ginásio é usado por vários programas, e cada um quer o seu registo. Se o `ginasio.py` configurasse o registo, impunha a sua escolha a todos. Como o `basicConfig` só faz efeito da primeira vez que é chamado, a configuração do programa era ignorada.

## Fase 7: O registo num ficheiro

O `basicConfig` pode mandar o registo para um ficheiro, em vez do ecrã, com o parâmetro `filename`. O formato pode acrescentar a data e a hora de cada mensagem, com `%(asctime)s`. Num ficheiro, a hora é o que permite saber quando aconteceu cada coisa, dias depois. Cada execução acrescenta as suas linhas ao fim do ficheiro, sem apagar as anteriores. Um registo é lido por outras pessoas e guarda-se durante muito tempo. Por isso nunca leva palavras-passe, códigos de acesso nem dados pessoais. Para saber mais, lê as secções "Guardar o registo num ficheiro" e "O que nunca se regista" do [guia](04-excecoes-depuracao-e-logging.md).

1. No `registo.py`, substitui a linha do `basicConfig` por esta. Manda o registo para o ficheiro `ginasio.log` e acrescenta a hora de cada mensagem.

```python
logging.basicConfig(filename="ginasio.log", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
```

Leitura guiada: o parâmetro `filename` é o que muda o destino do registo, do ecrã para o ficheiro. O `format` ganhou o `%(asctime)s` à frente. O nível continua a ser `INFO`.

2. Executa o `registo.py` duas vezes seguidas, com `python3 registo.py`. O que deves ver no ecrã, em cada execução: só o que vem dos `print`, isto é, o combate e o "Recusado". As linhas do registo deixaram de aparecer no ecrã.

3. Abre o ficheiro `ginasio.log`, que apareceu na pasta, no VS Code. Antes de o abrires, prevê quantas linhas tem.

O que deves ver: seis linhas, três por execução, com a data e a hora à frente. As datas e as horas são as do teu computador:

```text
2026-10-18 18:26:53,787 [INFO] ginasio: Combate em Celadon: Misty com Psyduck contra Erika com Tangela.
2026-10-18 18:26:53,787 [INFO] ginasio: Fim do combate em Celadon: venceu Erika.
2026-10-18 18:26:53,787 [WARNING] ginasio: Combate recusado em Celadon: Misty contra Erika, sem Pokémon com vida.
```

Estas são as três linhas da primeira execução, e a segunda execução acrescenta outras três por baixo. O ficheiro não é apagado entre execuções.

4. Responde por escrito: quantas linhas tem o ficheiro, e porquê? O que aparece no ecrã, e o que deixou de aparecer?

A resposta: seis, porque cada execução escreve as três linhas do registo, as duas de `INFO` e a de `WARNING`, e acrescenta-as ao fim do ficheiro. No ecrã ficam só os `print`: o combate e o "Recusado". As linhas do registo deixaram de aparecer, porque foram para o ficheiro.

### Paragem 7

O registo vai para o ficheiro `ginasio.log`, com a hora de cada mensagem, e o ecrã mostra só o jogo.

Pensa antes de terminares: o registo do ginásio tem os nomes dos treinadores, que aqui são personagens inventadas. Num programa com pessoas reais, o que teria de mudar? A resposta: o registo usaria um identificador, como um número de inscrição, e não o nome nem o contacto da pessoa. Nunca se escrevem num registo palavras-passe, chaves, números de documentos, moradas ou telefones.

## Problemas frequentes

### `ModuleNotFoundError: No module named 'erros'`

O ficheiro `erros.py` não está na mesma pasta que o `ginasio.py`, ou tem outro nome. Confirma que se chama exatamente `erros.py`.

### `ImportError: cannot import name 'EquipaCheia' from 'erros'`

O ficheiro foi encontrado, mas não tem uma classe com esse nome. A mensagem inclui o caminho do ficheiro. Nas versões recentes do Python, quando há um nome parecido, acaba também com uma sugestão, `Did you mean: ...?`, que quer dizer "querias dizer...?". Confirma a grafia, com as maiúsculas: `EquipaCheia`.

### `NameError: name 'EquipaCheia' is not defined`, quando se captura com a equipa cheia

O `ginasio.py` usa a exceção, mas não a importou. Confirma a linha `from erros import EquipaCheia, SemPokemonComVida` no início do ficheiro. O erro só aparece quando o `raise` corre, e por isso o ficheiro parece estar bem até a equipa encher.

### `TypeError: EquipaCheia() takes no arguments`

Uma das classes do `erros.py` não tem a classe-mãe entre parênteses, e por isso é uma classe normal, e não uma exceção. A `ErroDoGinasio` tem de ser filha de `Exception`, e as outras de `ErroDoGinasio`. A mensagem aparece quando o programa cria a exceção com uma mensagem, como `EquipaCheia("...")`, porque uma classe normal sem construtor não aceita argumentos. Traz o nome da classe que se estava a criar, que pode ser outra das três, como `SemPokemonComVida`.

### `TypeError: catching classes that do not inherit from BaseException is not allowed`

É a mesma causa do problema anterior, vista de outro lado. Acontece a seguir ao `TypeError: EquipaCheia() takes no arguments`, quando isso se passa dentro de um `try`. O `except` tem o nome de uma classe que não é uma exceção, e o Python não consegue apanhar com ela. O Python mostra então as duas mensagens, separadas pela frase `During handling of the above exception, another exception occurred`. Corrige a classe no `erros.py`.

### O teste da fase 3 escreve "Não há combate: um dos treinadores não tem Pokémon com vida." sem a cidade

O `combater` ainda tem o `print` e o `return` da versão anterior. Tira-os e põe o `raise` no lugar deles.

### Na fase 3, a linha dos desafiantes diz 2 depois do Brock

A linha que junta o desafiante à lista está antes da verificação. Passa-a para depois do `raise`.

### O depurador não para no ponto de paragem

Ou executaste sem o depurador, com o triângulo ou com Ctrl+F5, ou o ponto está numa linha que não corre. Usa o F5, e confirma que o ponto vermelho está na linha certa do ficheiro que estás a executar.

### O F5 pergunta que depurador usar e não aparece o de Python

A extensão Python da Microsoft não está instalada, ou está desativada. Instala-a no painel das extensões do VS Code.

### As mensagens do registo não aparecem

O `registo.py` não tem o `basicConfig`, ou tem o nível acima do das mensagens. Sem configuração, só aparecem as de `WARNING`.

### `--- Logging error ---`, com `not all arguments converted during string formatting`

Uma mensagem do registo foi escrita como um `print`, com vírgulas. Escreve-a numa f-string.

### O `ginasio.log` não aparece

O ficheiro é criado na pasta onde o terminal está, que pode não ser a do laboratório. Abre o terminal na pasta `ginasio-com-erros` e executa de lá.

## Desafios

1. Neste momento, nada impede que o mesmo Pokémon seja capturado duas vezes pelo mesmo treinador: o mesmo objeto fica duas vezes na lista da equipa. Acrescenta ao ginásio uma exceção nova para este caso.

- No `erros.py`, uma classe `PokemonRepetido`, filha de `ErroDoGinasio`.
- No `capturar`, se o Pokémon já está na equipa do treinador, o método regista um aviso, com o nível `WARNING`, e lança `PokemonRepetido`, sem juntar nada à equipa.
- A mensagem do aviso é "Ash tentou capturar outra vez o Charmander." A da exceção é "Ash já tem este Charmander na equipa." Ambas levam o nome do treinador e o do Pokémon.

Para testar, cria o ficheiro `repetido.py`:

```python
# repetido.py: testa a exceção PokemonRepetido, do desafio.
import logging

from erros import PokemonRepetido
from pokemon import PokemonFogo
from ginasio import Treinador

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

ash = Treinador("Ash")
charmander = PokemonFogo("Charmander", 90, 40)
ash.capturar(charmander)
try:
    ash.capturar(charmander)
except PokemonRepetido as erro:
    print(f"Recusado: {erro}")
ash.capturar(PokemonFogo("Charmander", 90, 40))
print(len(ash.equipa))
```

Quando estiver certo, o teste mostra:

```text
[WARNING] ginasio: Ash tentou capturar outra vez o Charmander.
Recusado: Ash já tem este Charmander na equipa.
2
```

Antes de escreveres o código, decide duas coisas. A primeira: o terceiro `capturar` junta um Charmander criado de novo, com os mesmos valores do primeiro, e tem de ser aceite. Que pergunta faz a verificação, "é o mesmo objeto?" ou "tem os mesmos valores?", e como se escreve? A segunda: um treinador com a equipa cheia tenta capturar um Pokémon que já tem. Qual das duas exceções deve ser lançada, e o que decide isso no teu código? Pista: pensa no que o `==` faz com dois objetos de uma classe normal, escrita sem `@dataclass`. Pensa também em qual dos dois motivos de recusa dá mais informação a quem chamou.

2. A `EquipaCheia` do teu `erros.py` só tem a docstring, e a mensagem é escrita no `raise` do `capturar`. Dá-lhe dados, como na secção "Uma exceção com dados" do [guia](04-excecoes-depuracao-e-logging.md#uma-exceção-com-dados).

- No `erros.py`, a `EquipaCheia` passa a ter um construtor que recebe o treinador e o Pokémon que ficou de fora. Guarda-os nos atributos `treinador` e `pokemon`, e escreve ela própria a mensagem, com o mesmo texto que tem hoje: "Ash já tem 6 Pokémon e não pode capturar Charmander."
- No `capturar` do `ginasio.py`, o `raise` passa só o treinador e o Pokémon.

Para testar, cria o ficheiro `fora_da_equipa.py`:

```python
# fora_da_equipa.py: testa a EquipaCheia com dados, do desafio 2.
from erros import EquipaCheia
from pokemon import PokemonFogo
from ginasio import Treinador

pokemons = []
for nome in ["Ponyta", "Vulpix", "Growlithe", "Magmar", "Ninetales", "Arcanine", "Charmander"]:
    pokemons.append(PokemonFogo(nome, 50, 20))
try:
    ash = Treinador.com_equipa("Ash", pokemons)
except EquipaCheia as erro:
    print(erro)
    print(f"Ficou de fora: {erro.pokemon.nome}.")
    print(f"Na equipa de {erro.treinador.nome} ficaram {len(erro.treinador.equipa)} Pokémon.")
```

Quando estiver certo, o teste mostra:

```text
Ash já tem 6 Pokémon e não pode capturar Charmander.
Ficou de fora: Charmander.
Na equipa de Ash ficaram 6 Pokémon.
```

Corre também outra vez o `capturas.py`, da fase 2. Tem de mostrar exatamente o mesmo que mostrava antes da mudança, porque a mensagem não mudou.

Antes de escreveres o código, decide duas coisas. A primeira: a mensagem tem o número 6, que o `capturar` escrevia com a constante `TAMANHO_MAXIMO_DA_EQUIPA`, do `ginasio.py`. Dentro do `erros.py`, de onde vem esse número? Pista: o `ginasio.py` já importa o `erros.py`. Pensa no que acontece se o `erros.py` também importar o `ginasio.py`, e no que a equipa do treinador já te diz. A segunda: quando a exceção é lançada, o `com_equipa` ainda não devolveu o treinador, e a variável `ash` nunca chega a ser criada. Então, como é que o teste chega ao treinador e à equipa dele?

## Antes de terminares

- [ ] A pasta `ginasio-com-erros` tem o `erros.py` e o `ginasio.py` na versão final, e os ficheiros de teste: `teste_erros.py`, `capturas.py`, `combates.py`, `investigar.py` já corrigido, `pilha.py` já corrigido e `registo.py`.
- [ ] Tens as previsões, a hipótese e a tabela da fase 4. Tens também as respostas às perguntas das fases 2 a 7, escritas por ti, em papel ou num ficheiro de texto, conforme o professor indicar.
- [ ] Se fizeste o desafio 1, o `erros.py` e o `ginasio.py` têm a `PokemonRepetido`, e o `repetido.py` mostra as três linhas do enunciado.
- [ ] Se fizeste o desafio 2, a `EquipaCheia` tem o construtor com os dados, o `fora_da_equipa.py` mostra as três linhas do enunciado, e o `capturas.py` mostra o mesmo que antes.
- [ ] Consegues explicar, por palavras tuas, porque é que um método recusa com `raise` em vez de `print`. Consegues explicar também a diferença entre o sítio onde um erro rebenta e o sítio onde está a causa.

![Rodapé](../imagens/rodape.png)
