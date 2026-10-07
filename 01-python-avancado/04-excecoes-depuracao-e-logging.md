![Cabeçalho](../imagens/cabecalho.png)

# Exceções, depuração e logging

Até aqui, quando o ginásio Pokémon não podia fazer o que lhe pediam, escrevia uma mensagem com `print` e saía do método com `return`. Funciona enquanto há alguém a olhar para o ecrã. Deixa de funcionar quando quem chama o método é outro pedaço de código, que não lê o ecrã e continua como se nada fosse.

Este guia trata dos erros de três lados. Primeiro, como um objeto recusa um pedido de forma que ninguém o possa ignorar: as exceções, incluindo exceções criadas por ti. Depois, como se encontra a causa de um erro, lendo o traceback e usando o depurador do VS Code para ver o programa a correr linha a linha. Por fim, como um programa deixa registo do que fez, com o logging, sem encher o ecrã de `print` que depois é preciso apagar.

O fio condutor continua a ser o ginásio Pokémon. No fim do guia, o ginásio recusa capturas e combates com exceções próprias e regista os combates por níveis de importância.

## O que este guia cobre

| Parte | Assunto |
| --- | --- |
| 1 | Exceções: o `raise`, o `try` com `except`, `else` e `finally`, as exceções próprias e uma família de exceções para o ginásio |
| 2 | Encontrar a causa de um erro: ler um traceback, o depurador do VS Code e a pilha de chamadas |
| 3 | Logging: os cinco níveis, quem configura o registo, guardar o registo num ficheiro e o que nunca se regista |

Além deste guia, o tema tem mais dois documentos com o mesmo número:

- o [laboratório](04-excecoes-depuracao-e-logging-laboratorio.md), em que acrescentas ao teu ginásio as exceções e o registo, e investigas um erro com o depurador;
- a [ficha de exercícios](04-excecoes-depuracao-e-logging-exercicios.md), para praticares sem ajuda.

O código completo do exemplo está na pasta [04-excecoes-depuracao-e-logging](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/) dos exemplos. É a versão do tema 03 com duas mudanças: um ficheiro novo, [erros.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/erros.py), com as exceções do ginásio, e o [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) a usá-las e a registar os combates. O [pokemon.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/pokemon.py) e o [anunciadores.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/anunciadores.py) são iguais aos do tema 03.

## O que precisas de saber antes

Do guia [Objetos, composição e comportamento](03-objetos-e-composicao.md), precisas das classes, da herança (parte 3), do ginásio Pokémon (parte 4) e do método de classe `com_equipa` (parte 5). Uma exceção própria é uma classe-filha, e a parte 3 é a base dela.

Do 10.º ano, precisas do que o guia de exceções tinha como essencial: o que é uma exceção, como se lê a última linha de uma mensagem de erro, e o `try` com `except` para apanhar um erro conhecido, como o `ValueError` de um `int("abc")`. Precisas também da ideia de que uma função chama outra, e que a que foi chamada tem de acabar para a outra continuar.

O `raise`, o `else` e o `finally` estavam no 10.º ano como matéria extra. Este guia explica-os desde o início, por isso não faz mal se não os deste.

Para a parte 2 precisas do VS Code com a extensão Python da Microsoft, que é a que usas para executar os programas. Essa extensão traz o depurador.

## Como ler este guia

As regras são as do guia anterior. Antes de executares um programa, escreve o que achas que ele vai mostrar, e só depois compara. Todos os programas foram executados em Python 3.14 e em Python 3.9, e as saídas mostradas são as reais; as saídas são iguais nas duas versões.

Nas mensagens de erro, a parte 1 e a parte 3 mostram só a última linha, como o guia anterior. A parte 2 é sobre ler a mensagem inteira, e por isso mostra-a toda, com o nome do ficheiro no lugar do caminho completo, que no teu computador é outro. Nas versões recentes do Python, a mensagem tem também linhas com acentos circunflexos (`^^^^`) por baixo do código, a apontar a parte da linha que falhou; nas versões antigas essas linhas não aparecem.

Os programas que usam o ginásio importam do `pokemon.py`, do `ginasio.py` e do `erros.py` da pasta 04 dos exemplos. Para os executares, copia essa pasta para o teu computador e guarda os programas nela.

## Parte 1: Exceções

### O que já sabes do 10.º ano

Uma **exceção** é a forma de o Python avisar que uma linha não pode ser feita. Quando o `int` recebe um texto que não é um número, não tem nada para devolver, e lança um `ValueError`. Se ninguém apanhar a exceção, o programa para e escreve a mensagem de erro. Se a linha estiver dentro de um `try`, o Python salta para o `except` desse tipo de erro, e o programa continua:

```python
texto = "muitos"
try:
    quantidade = int(texto)
except ValueError:
    print(f"{texto} não é um número.")
```

```text
muitos não é um número.
```

Até agora, apanhaste exceções lançadas pelo próprio Python. Nesta parte vais ver o outro lado: os teus objetos a lançar exceções, quando lhes pedem uma coisa que não podem fazer.

### Uma recusa que ninguém ouve

Imagina um treinador que só pode ter dois Pokémon na equipa. Este programa usa uma versão curta do `Treinador`, com os Pokémon guardados só pelo nome, e recusa a terceira captura como o ginásio fazia até aqui: escreve uma mensagem e sai com `return`.

```python
class Treinador:
    """Versão curta: a equipa só leva dois Pokémon, e a recusa é um print."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        self.equipa = []

    def capturar(self, nome_do_pokemon):
        """Junta o Pokémon à equipa, se ainda houver lugar."""
        if len(self.equipa) >= 2:
            print("A equipa está cheia!")
            return
        self.equipa.append(nome_do_pokemon)


ash = Treinador("Ash")
for nome in ["Pikachu", "Charmander", "Bulbasaur"]:
    ash.capturar(nome)
    print(f"{nome} capturado.")
print(ash.equipa)
```

Prevê a saída, linha a linha, antes de executares.

```text
Pikachu capturado.
Charmander capturado.
A equipa está cheia!
Bulbasaur capturado.
['Pikachu', 'Charmander']
```

A quarta linha mente. O Bulbasaur não foi capturado, a lista no fim mostra-o, mas o programa escreveu "Bulbasaur capturado." logo a seguir a "A equipa está cheia!". O `capturar` recusou, mas a única coisa que fez foi escrever no ecrã. O código que o chamou não tem forma de saber que o pedido falhou, e continua como se tivesse corrido bem.

É o mesmo problema que o ginásio tinha: quando não havia Pokémon com vida, o `combater` escrevia "Não há combate" e saía. Quem chamava o `combater` não sabia se houvera combate ou não.

### raise: uma recusa que não se pode ignorar

A instrução `raise` lança uma exceção. Escreve-se `raise` seguido de um objeto de exceção, que se cria como qualquer objeto, com o nome da classe e, entre parênteses, a mensagem. A partir dessa linha, o método para, e a exceção sobe para quem o chamou. Se esse código também não a apanhar, sobe outra vez, até ao programa principal; se aí ninguém a apanhar, o programa para e escreve a mensagem de erro.

Esta é a mesma classe, com a recusa feita com `raise`. O `ValueError` é uma exceção que o Python já tem, para valores que não servem:

```python
class Treinador:
    """Versão curta: a equipa só leva dois Pokémon, e a recusa é uma exceção."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        self.equipa = []

    def capturar(self, nome_do_pokemon):
        """Junta o Pokémon à equipa; com a equipa cheia, lança ValueError."""
        if len(self.equipa) >= 2:
            raise ValueError(f"A equipa de {self.nome} está cheia: {nome_do_pokemon} ficou de fora.")
        self.equipa.append(nome_do_pokemon)


ash = Treinador("Ash")
for nome in ["Pikachu", "Charmander", "Bulbasaur"]:
    ash.capturar(nome)
    print(f"{nome} capturado.")
print(ash.equipa)
```

```text
Pikachu capturado.
Charmander capturado.
ValueError: A equipa de Ash está cheia: Bulbasaur ficou de fora.
```

A mentira desapareceu: o programa parou na terceira captura, antes do `print`, com uma mensagem que diz o que aconteceu. Repara em duas coisas.

O `raise` está antes do `append`. Quando a exceção é lançada, o método para nessa linha, e o `append` não chega a correr: a equipa fica como estava. A regra é a mesma das propriedades da parte 2 do guia anterior: verifica-se antes de mudar o estado, e só se muda se a verificação passar.

O programa parou de vez, e a lista do fim nem chegou a ser escrita. Recusar não pode querer dizer acabar com o programa. Quem chama o `capturar` tem de poder decidir o que fazer com a recusa, e é para isso que serve o `try`.

### Apanhar a recusa: try, except e else

Com o `capturar` a lançar a exceção, o programa principal apanha-a:

```python
class Treinador:
    """Versão curta: a equipa só leva dois Pokémon, e a recusa é uma exceção."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        self.equipa = []

    def capturar(self, nome_do_pokemon):
        """Junta o Pokémon à equipa; com a equipa cheia, lança ValueError."""
        if len(self.equipa) >= 2:
            raise ValueError(f"A equipa de {self.nome} está cheia: {nome_do_pokemon} ficou de fora.")
        self.equipa.append(nome_do_pokemon)


ash = Treinador("Ash")
for nome in ["Pikachu", "Charmander", "Bulbasaur"]:
    try:
        ash.capturar(nome)
    except ValueError as erro:
        print(f"Não foi possível: {erro}")
    else:
        print(f"{nome} capturado.")
print(ash.equipa)
```

```text
Pikachu capturado.
Charmander capturado.
Não foi possível: A equipa de Ash está cheia: Bulbasaur ficou de fora.
['Pikachu', 'Charmander']
```

Há duas coisas novas no `try`.

O `as erro` dá um nome ao objeto da exceção que foi apanhado. Com ele, o `except` pode usar a mensagem que o `raise` escreveu: um `print` de uma exceção mostra a sua mensagem. A frase sobre a equipa cheia foi escrita uma só vez, dentro do `capturar`, que é quem sabe o que aconteceu; o programa principal só a mostra.

O `else` de um `try` corre quando o bloco do `try` acaba sem exceção nenhuma. Por isso o "capturado" só aparece quando a captura correu bem. Podia estar dentro do `try`, a seguir ao `capturar`, e o resultado era o mesmo. Fica no `else` por uma razão: o bloco do `try` deve ter só as linhas cuja exceção queres apanhar. Uma linha a mais dentro do `try` é uma linha a mais cujos erros vão parar ao `except`, e a secção seguinte mostra o problema que isso traz.

### Quando o except apanha de mais

O `ValueError` não é só do `capturar`. O `int` também o lança, quando o texto não é um número. Neste programa, cada pedido de captura traz o nível do Pokémon escrito em texto, e o `try` tem as duas linhas:

```python
class Treinador:
    """Versão curta: a equipa só leva dois Pokémon, e a recusa é uma exceção."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        self.equipa = []

    def capturar(self, nome_do_pokemon):
        """Junta o Pokémon à equipa; com a equipa cheia, lança ValueError."""
        if len(self.equipa) >= 2:
            raise ValueError(f"A equipa de {self.nome} está cheia: {nome_do_pokemon} ficou de fora.")
        self.equipa.append(nome_do_pokemon)


ash = Treinador("Ash")
pedidos = [("Pikachu", "5"), ("Charmander", "cinco")]
for nome, texto_do_nivel in pedidos:
    try:
        nivel = int(texto_do_nivel)
        ash.capturar(nome)
    except ValueError as erro:
        print(f"Equipa cheia? {erro}")
    else:
        print(f"{nome} capturado, no nível {nivel}.")
print(ash.equipa)
```

```text
Pikachu capturado, no nível 5.
Equipa cheia? invalid literal for int() with base 10: 'cinco'
['Pikachu']
```

A equipa do Ash tem um só Pokémon, e o programa pergunta se está cheia. O `except ValueError` apanhou o erro do `int("cinco")`, que não tem nada a ver com a equipa, e tratou-o como se fosse uma recusa da captura. O `ValueError` é um nome demasiado geral: diz que um valor não serve, mas não diz qual nem porquê. Quando dois erros diferentes têm o mesmo tipo, o `except` não os consegue separar.

### Uma exceção própria

A solução é dar à recusa da captura um tipo seu. Uma **exceção própria** é uma classe criada por ti, filha de `Exception`, a classe-mãe das exceções do Python. Não precisa de mais nada: a classe-filha herda tudo o que uma exceção precisa, incluindo a forma de guardar e mostrar a mensagem. O corpo da classe pode ser só a docstring, como o primeiro `Lider` do guia anterior.

```python
class EquipaCheia(Exception):
    """Um treinador tentou capturar um Pokémon com a equipa já completa."""


class Treinador:
    """Versão curta: a equipa só leva dois Pokémon, e a recusa é EquipaCheia."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        self.equipa = []

    def capturar(self, nome_do_pokemon):
        """Junta o Pokémon à equipa; com a equipa cheia, lança EquipaCheia."""
        if len(self.equipa) >= 2:
            raise EquipaCheia(f"A equipa de {self.nome} está cheia: {nome_do_pokemon} ficou de fora.")
        self.equipa.append(nome_do_pokemon)


ash = Treinador("Ash")
pedidos = [("Pikachu", "5"), ("Charmander", "cinco"), ("Bulbasaur", "3"), ("Squirtle", "7")]
for nome, texto_do_nivel in pedidos:
    try:
        nivel = int(texto_do_nivel)
        ash.capturar(nome)
    except ValueError:
        print(f"O nível de {nome} não é um número: {texto_do_nivel}.")
    except EquipaCheia as erro:
        print(f"Não foi possível: {erro}")
    else:
        print(f"{nome} capturado, no nível {nivel}.")
print(ash.equipa)
print(isinstance(EquipaCheia("teste"), Exception))
```

Antes de executares, prevê o que acontece a cada um dos quatro pedidos.

```text
Pikachu capturado, no nível 5.
O nível de Charmander não é um número: cinco.
Bulbasaur capturado, no nível 3.
Não foi possível: A equipa de Ash está cheia: Squirtle ficou de fora.
['Pikachu', 'Bulbasaur']
True
```

Agora há dois `except`, um por cada tipo, e cada erro vai para o seu. O Python experimenta os `except` por ordem, de cima para baixo, e entra no primeiro cujo tipo corresponde à exceção. O Charmander não chegou a ser capturado, porque o `int` falhou antes do `capturar`; por isso há lugar para o Bulbasaur, e o Squirtle é que fica de fora.

A última linha confirma a herança: um objeto `EquipaCheia` é também um `Exception`, tal como um `PokemonFogo` é também um `Pokemon`. É essa relação "é um" que deixa o `raise` aceitar a classe. O nome da exceção diz o que aconteceu, em português, como os nomes das tuas classes. Nas bibliotecas escritas em inglês, os nomes das exceções acabam quase sempre em `Error`, como `ValueError`; aqui a regra é o nome dizer o problema.

### As exceções do ginásio

No exemplo dos Pokémon, as exceções do ginásio estão num ficheiro só delas, [erros.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/erros.py):

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

São três classes, e nenhuma tem mais do que a docstring. O `ErroDoGinasio` é a classe-mãe das outras duas, e é filha de `Exception`. É a herança do guia anterior aplicada a erros: uma `EquipaCheia` é um `ErroDoGinasio`, e um `ErroDoGinasio` é uma exceção.

No [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) da pasta 04, o `capturar` do `Treinador` passou a ter um limite de seis Pokémon, guardado numa constante no início do ficheiro, `TAMANHO_MAXIMO_DA_EQUIPA = 6`:

```python
class Treinador:
    # O construtor, o com_equipa e o escolher_pokemon ficam como estavam.

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador.

        Se a equipa já tem TAMANHO_MAXIMO_DA_EQUIPA Pokémon, não junta nada e
        lança EquipaCheia.
        """
        if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
            raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
        self.equipa.append(pokemon)
```

E o `combater` do `Ginasio`, que antes escrevia "Não há combate" e saía, começa agora assim:

```python
class Ginasio:
    # O construtor fica como estava.

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
        # O resto do método, com o combate e o registo, fica como estava.
```

Há duas mudanças em relação ao tema 03. A primeira é o `raise` no lugar do `print` e do `return`. A segunda é a ordem: na versão anterior, o desafiante entrava na lista de desafiantes logo no início, antes de se saber se havia combate. Agora, a verificação vem primeiro, e o desafiante só entra na lista quando o combate vai mesmo acontecer. Se o combate for recusado, o ginásio fica exatamente como estava, como diz a docstring. As linhas com `logger` são o registo do ginásio, que a parte 3 explica; por agora, basta saber que escrevem uma linha de aviso.

Nenhuma das duas classes escreve no ecrã que houve um problema, nem decide o que fazer a seguir. Lançam a exceção, com uma mensagem que explica o que aconteceu, e quem chamou o método decide: mostrar a mensagem, tentar outro treinador, guardar o erro num registo. A classe não sabe onde vai ser usada. Num programa de consola, a decisão pode ser um `print`; numa janela, uma caixa de mensagem; numa API web, uma resposta de erro. A exceção serve às três.

### Uma família de exceções

Com uma classe-mãe comum, um só `except` apanha qualquer erro do ginásio. Neste programa, a Misty é a líder, e o Gary faz três pedidos: dois combates e uma série de capturas.

```python
from erros import EquipaCheia, ErroDoGinasio, SemPokemonComVida
from pokemon import PokemonAgua, PokemonFogo
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
gary = Treinador.com_equipa("Gary", [PokemonFogo("Vulpix", 30, 20)])
cerulean = Ginasio("Cerulean", misty)

pedidos = ["combate", "combate", "captura"]
for pedido in pedidos:
    try:
        if pedido == "combate":
            cerulean.combater(gary)
        else:
            for numero in range(6):
                gary.capturar(PokemonFogo(f"Ponyta {numero + 1}", 50, 20))
    except ErroDoGinasio as erro:
        print(f"Pedido recusado ({type(erro).__name__}): {erro}")
print(len(gary.equipa), len(cerulean.combates), len(cerulean.desafiantes))
```

Prevê o que acontece a cada pedido, e os três números da última linha.

```text

=== Gary desafia Misty no ginásio de Cerulean ===
Vulpix ataca Starmie e tira 20 de vida.
Starmie tem 70/150 de vida.
É super eficaz!
Starmie ataca Vulpix e tira 70 de vida.
Vulpix está KO (0/150).
Combate recusado em Cerulean: Gary contra Misty, sem Pokémon com vida.
Pedido recusado (SemPokemonComVida): Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
Pedido recusado (EquipaCheia): Gary já tem 6 Pokémon e não pode capturar Ponyta 6.
6 1 1
```

O primeiro combate acontece, e o Vulpix perde. No segundo, o Gary já não tem Pokémon com vida: o `combater` lança `SemPokemonComVida`. No terceiro pedido, o Gary captura cinco Ponyta e fica com seis Pokémon, contando com o Vulpix; a sexta Ponyta é recusada com `EquipaCheia`. As duas exceções foram apanhadas pelo mesmo `except ErroDoGinasio`, porque as duas são filhas dele. O `type(erro).__name__`, que já usaste na parte 5 do guia anterior, mostra de que classe era cada uma.

A linha "Combate recusado em Cerulean..." vem do registo do ginásio, e não de um `print`. A parte 3 explica porque aparece assim.

A última linha mostra que as recusas não deixaram rasto: o Gary tem os seis Pokémon que cabem na equipa, o ginásio tem um combate registado, e um desafiante, porque o combate recusado não chegou a pô-lo na lista.

Apanhar a classe-mãe ou a classe-filha é uma escolha. O `except ErroDoGinasio` serve quando a reação é a mesma para todos os erros do ginásio, como aqui, em que só se mostra a mensagem. O `except EquipaCheia` serve quando a reação é própria desse caso, como sugerir ao treinador que liberte um Pokémon. E quando há dois `except` com tipos da mesma família, o da classe-filha tem de vir primeiro, como mostra a secção dos erros frequentes.

### finally: o que corre sempre

Um `try` pode acabar com um `finally`, que corre sempre: quando não houve exceção, quando houve e foi apanhada, e até quando houve e ninguém a apanhou.

```python
from erros import SemPokemonComVida
from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 50, 20)])
cerulean = Ginasio("Cerulean", misty)
for tentativa in range(2):
    try:
        cerulean.combater(ash)
    except SemPokemonComVida as erro:
        print(f"Recusado: {erro}")
    finally:
        print(f"Combates registados em {cerulean.cidade}: {len(cerulean.combates)}")
```

```text

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
Combates registados em Cerulean: 1
Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
Recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
Combates registados em Cerulean: 1
```

Na primeira volta, o combate corre bem, e o `finally` corre a seguir. Na segunda, o combate é recusado, o `except` mostra a mensagem, e o `finally` corre na mesma. O `finally` serve para o que tem de acontecer em qualquer caso: escrever um resumo, fechar uma ligação, libertar alguma coisa que se abriu no `try`. Num `try` com `except`, `else` e `finally`, a ordem é sempre esta: primeiro o `try`, depois o `except` ou o `else`, conforme houve exceção ou não, e no fim o `finally`.

### Erros frequentes com exceções

**Os except pela ordem errada.** O Python entra no primeiro `except` que corresponde. Se o da classe-mãe vier primeiro, apanha também as filhas, e o `except` da filha nunca corre:

```python
from erros import EquipaCheia, ErroDoGinasio
from pokemon import PokemonFogo
from ginasio import Treinador

gary = Treinador("Gary")
try:
    for numero in range(7):
        gary.capturar(PokemonFogo(f"Ponyta {numero + 1}", 50, 20))
except ErroDoGinasio:
    print("Um erro qualquer do ginásio.")
except EquipaCheia:
    print("A equipa está cheia.")
print(len(gary.equipa))
```

```text
Um erro qualquer do ginásio.
6
```

Não há erro nem aviso: o segundo `except` está lá, mas nunca vai correr. Os `except` vão do mais específico para o mais geral.

**Um except que apanha tudo.** O `except Exception` apanha quase qualquer erro, incluindo os teus próprios enganos:

```python
from pokemon import PokemonFogo
from ginasio import Treinador

ash = Treinador("Ash")
try:
    ash.capturar(PokemonFogo("Charmander", 90, 40))
    print(f"{ash.nome} tem {len(ash.equipa)} Pokémon.")
    print(f"O primeiro é {ash.equipa[0].nmoe}.")
except Exception:
    print("Não foi possível capturar.")
```

```text
Ash tem 1 Pokémon.
Não foi possível capturar.
```

A captura correu bem, como mostra a primeira linha. O erro está na terceira linha do `try`, onde `nome` está mal escrito, e o Python lançou um `AttributeError`. O `except Exception` apanhou-o e escreveu uma mensagem que diz o contrário do que aconteceu. Sem o `try`, a mensagem de erro apontava logo para a linha com `nmoe`. Apanha só os tipos de exceção que sabes tratar, e deixa os outros chegar ao ecrã, onde se veem.

**Um except que não faz nada.** Um `except EquipaCheia:` com só um `pass` lá dentro faz desaparecer a recusa, e volta-se ao problema do início: o programa continua como se a captura tivesse corrido bem. Se apanhas uma exceção, faz alguma coisa com ela: mostra a mensagem, regista-a, ou tenta outra coisa.

**Esquecer o Exception na classe.** Uma classe sem `(Exception)` é uma classe normal, e o `raise` recusa-a:

```python
class EquipaCheia:
    """Esqueceu-se o (Exception): isto é uma classe normal."""


raise EquipaCheia()
```

```text
TypeError: exceptions must derive from BaseException
```

A mensagem diz que as exceções têm de descender de `BaseException`, que é a classe de que a própria `Exception` é filha. Se tentares criar a exceção com uma mensagem, `EquipaCheia("...")`, o erro aparece ainda antes, e é outro: `TypeError: EquipaCheia() takes no arguments`, porque uma classe normal sem construtor não aceita argumentos.

**Uma exceção sem mensagem.** `raise EquipaCheia()` funciona, mas quem apanha a exceção não tem nada para mostrar: um `print(erro)` escreve uma linha vazia. Escreve sempre na mensagem o que aconteceu, com os dados que ajudam a perceber: quem, o quê, e porque não foi possível.

### Verifica se percebeste: exceções

1. No primeiro programa desta parte, porque é que aparece "Bulbasaur capturado." se o Bulbasaur não foi capturado?
2. No `capturar` com `raise`, porque é que o `raise` tem de vir antes do `append`? O que acontecia à equipa se viesse depois?
3. Para que serve o `else` de um `try`? Porque não se põe simplesmente essa linha dentro do `try`?
4. A `EquipaCheia` e a `SemPokemonComVida` são filhas de `ErroDoGinasio`. Escreve dois `except` para um programa que quer mostrar "Liberta um Pokémon primeiro." quando a equipa está cheia, e a mensagem da exceção para qualquer outro erro do ginásio. Por que ordem ficam?
5. Porque é que o `capturar` lança a exceção, em vez de escrever ele próprio a mensagem no ecrã?

## Parte 2: Encontrar a causa de um erro

### Um erro tem um sintoma e uma causa

O **sintoma** é o que se vê: uma mensagem de erro, um número errado, um combate que nunca acaba. A **causa** é a linha de código que está mal. Os dois raramente estão no mesmo sítio. Um valor errado pode entrar num objeto numa linha, e só rebentar dez linhas depois, noutro método, quando alguém o usa.

**Depurar** é encontrar a causa a partir do sintoma. A tentação é mudar logo o código no sítio do sintoma, para o erro desaparecer, e ver se resulta. Às vezes resulta, e a causa fica lá, à espera do próximo sintoma. A forma que funciona tem quatro passos:

1. **Reproduzir.** Encontrar uma forma de fazer o erro acontecer sempre, com o programa mais curto possível.
2. **Formular uma hipótese.** Antes de mexer no código, escrever o que achas que está a acontecer e porquê, e o que esperas ver se tiveres razão.
3. **Confirmar com evidência.** Olhar para os valores verdadeiros enquanto o programa corre, e não para os que achas que lá estão. A mensagem de erro e o depurador servem para isto.
4. **Corrigir a causa e voltar a reproduzir.** Mudar a linha que está mal, e confirmar que o erro desapareceu com o mesmo programa do passo 1.

### Ler um traceback com três andares

Este programa tem um erro. O Ash foi criado com o `com_equipa`, mas a lista da equipa tem o nome do Pokémon, em texto, e não um objeto Pokémon:

```python
from pokemon import PokemonAgua
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", ["Pikachu"])
cerulean = Ginasio("Cerulean", misty)
cerulean.combater(ash)
```

Desta vez, a mensagem de erro aparece inteira, como o Python 3.14 a escreve:

```text
Traceback (most recent call last):
  File "combate.py", line 7, in <module>
    cerulean.combater(ash)
    ~~~~~~~~~~~~~~~~~^^^^^
  File "ginasio.py", line 140, in combater
    atacante = desafiante.escolher_pokemon()
  File "ginasio.py", line 87, in escolher_pokemon
    if pokemon.vida > 0:
       ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'vida'
```

Esta mensagem chama-se **traceback**, que quer dizer, à letra, "o rasto para trás". A primeira linha diz como se lê: "most recent call last", a chamada mais recente fica no fim.

Cada par de linhas que começa por `File` é um **andar**: um ficheiro, um número de linha, o nome da função ou do método que estava a correr, e a linha de código. O andar de cima é o programa principal, que o Python chama `<module>`, a chamar o `combater`. O do meio é o `combater`, a chamar o `escolher_pokemon`. O de baixo é o `escolher_pokemon`, onde o erro rebentou. A última linha diz o tipo de exceção e a mensagem: um objeto `str`, um texto, não tem nenhum atributo `vida`.

Lê-se assim:

1. **A última linha diz o quê.** Alguém tentou ler `.vida` de um texto.
2. **O andar de baixo diz onde rebentou.** Na linha 87 do `ginasio.py`, no `if pokemon.vida > 0:` do `escolher_pokemon`. Ali, `pokemon` era um texto.
3. **Os andares de cima dizem como se chegou lá.** O programa principal chamou o `combater`, que chamou o `escolher_pokemon` do desafiante.
4. **A causa não está no traceback.** Nenhum dos três andares é a linha que está mal. O `escolher_pokemon` está certo: percorre a equipa e lê a vida de cada Pokémon. O problema é a equipa ter um texto lá dentro, e o texto entrou na linha 5 do programa, `Treinador.com_equipa("Ash", ["Pikachu"])`, que já tinha acabado quando o erro rebentou.

O traceback mostra onde o erro rebentou e o caminho até lá. A causa pode estar nesse caminho ou antes dele, numa linha que deixou um valor errado num objeto. Corrigir o sintoma, por exemplo mudando o `escolher_pokemon` para saltar os textos, escondia o erro: o Ash ficava com uma equipa sem Pokémon, e ninguém percebia porquê. A correção é na linha 5: a lista tem de levar um Pokémon a sério, como `[PokemonFogo("Charmander", 90, 40)]`, com a importação do `PokemonFogo`.

Os andares do traceback são a **pilha de chamadas**: a lista das funções e métodos que estão a meio, cada um à espera do que chamou. O programa principal está à espera do `combater`, e o `combater` está à espera do `escolher_pokemon`. É a mesma ideia das chamadas de função do 10.º ano, e vais vê-la outra vez no depurador.

### Um erro sem mensagem

Os erros mais difíceis não têm traceback. O programa corre até ao fim, e o resultado está errado. Este programa tem uma cópia da classe `PokemonPlanta` com uma linha mudada. Um Bulbasaur, de planta, ataca um Charmander, de fogo:

```python
from pokemon import Pokemon, PokemonFogo


class PokemonPlanta(Pokemon):
    """Uma cópia da PokemonPlanta do pokemon.py, com um erro para investigar."""

    def __init__(self, nome, vida, ataque, regeneracao):
        """Cria um Pokémon de planta com nome, vida, ataque e regeneração."""
        super().__init__(nome, "Planta", vida, ataque)
        self.regeneracao = regeneracao

    def calcular_dano(self, alvo):
        """Contra Água, a planta tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Água":
            print("É super eficaz!")
        dano = dano * 2
        return dano


bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
charmander = PokemonFogo("Charmander", 90, 40)
bulbasaur.atacar(charmander)
```

```text
Bulbasaur ataca Charmander e tira 50 de vida.
Charmander tem 40/150 de vida.
```

O Bulbasaur tem 25 de ataque, e a planta só tem vantagem contra a água. Contra fogo, devia tirar 25. Tirou 50, e não apareceu "É super eficaz!". Não há mensagem de erro, porque, para o Python, não há erro nenhum: todas as linhas fazem o que dizem. É aqui que o depurador ajuda.

Se já viste a causa, ótimo. Num programa de 20 linhas, ler com atenção às vezes chega. O exemplo guiado mais abaixo usa este erro para mostrar o depurador, porque é um erro pequeno, em que podes confirmar cada passo; num programa de 500 linhas, ler não chega.

### O depurador do VS Code

Um **depurador** é uma ferramenta que corre o programa e o deixa parar onde quiseres, para veres o valor de cada variável nesse momento e avançares uma linha de cada vez. É como a tabela de traço que fazias no papel, mas feita pelo computador, com os valores verdadeiros.

O VS Code tem um depurador para Python, que vem com a extensão Python da Microsoft. As ideias são estas:

| Ideia | O que é | Como se faz no VS Code |
| --- | --- | --- |
| **Ponto de paragem** | Uma linha onde o programa para antes de a executar. Em inglês, breakpoint | Clicar na margem, à esquerda do número da linha: aparece um ponto vermelho. Clicar outra vez tira-o. Também se põe com F9, na linha onde está o cursor |
| Executar com o depurador | Correr o programa de forma que pare nos pontos de paragem | F5, ou o menu Executar, Iniciar Depuração (Run, Start Debugging, se o VS Code estiver em inglês) |
| Continuar | Correr até ao próximo ponto de paragem, ou até ao fim | F5, com o programa parado |
| Avançar uma linha | Executar a linha marcada e parar na seguinte, sem entrar nas funções que ela chama. Em inglês, Step Over | F10 |
| Entrar na chamada | Se a linha marcada chama uma função ou um método, entrar nele e parar na sua primeira linha. Em inglês, Step Into | F11 |
| Sair da chamada | Correr até ao fim da função atual e parar na linha que a chamou. Em inglês, Step Out | Shift+F11 |
| Parar | Acabar a depuração | Shift+F5, ou o quadrado vermelho na barra |

Quando o programa está parado, a linha que vai correr a seguir aparece marcada a amarelo, e a barra lateral da depuração mostra três painéis que vais usar:

- **Variáveis** (Variables): os valores das variáveis da função onde o programa está parado. Um objeto pode ser aberto, com a seta, para ver os seus atributos.
- **Pilha de chamadas** (Call Stack): os andares do traceback, com o programa parado. O de cima é a função onde estás; clicar noutro mostra as variáveis desse andar.
- **Vigiar** (Watch): expressões que escreves tu, como `alvo.tipo == "Água"`, e que o VS Code recalcula a cada passo.

Em computadores portáteis e em Mac, as teclas F5, F10 e F11 podem precisar da tecla Fn. Na primeira vez que carregas em F5, o VS Code pode perguntar que depurador usar: escolhe o de Python, e depois a opção para depurar o ficheiro que está aberto (em inglês, Python Debugger e Python File). O botão de executar, o triângulo no canto de cima, corre o programa sem o depurador, e não para nos pontos de paragem; ao lado dele há uma seta com a opção de depurar o ficheiro.

### Exemplo guiado: o dano a dobrar

#### Passo 1: Reproduzir

O programa da secção "Um erro sem mensagem" já reproduz o erro: um Bulbasaur, com 25 de ataque, ataca um Charmander. É curto e dá sempre o mesmo resultado, 50 em vez de 25. Guarda-o num ficheiro, `investigar.py`, na pasta 04 dos exemplos.

#### Passo 2: Escrever a hipótese

O dano é o dobro do que devia, e o "É super eficaz!" não aparece. A multiplicação por 2 está a acontecer sem a condição da vantagem. Hipótese: no `calcular_dano` da `PokemonPlanta`, o `dano * 2` corre mesmo quando o `if` é falso. Se a hipótese estiver certa, quando o programa passar pelo `calcular_dano`, o `if` vai dar falso e, mesmo assim, o `dano` vai passar de 25 a 50.

Escreve a hipótese antes de abrires o depurador. Se escreveres depois, vais olhar para os valores à procura do que já sabes, e não do que lá está.

#### Passo 3: Pôr o ponto de paragem

O ponto de paragem fica na primeira linha que interessa: `dano = super().calcular_dano(alvo)`, a primeira linha do corpo do `calcular_dano`. Clica na margem, à esquerda do número dessa linha, e confirma que aparece o ponto vermelho.

#### Passo 4: Executar com o depurador

Carrega em F5. O programa corre até ao ponto de paragem e para. A linha `dano = super().calcular_dano(alvo)` fica marcada a amarelo: é a próxima a correr, e ainda não correu.

No painel das variáveis aparecem `self` e `alvo`. Abre o `alvo`, com a seta, e confirma: `nome` é `'Charmander'` e `tipo` é `'Fogo'`. A variável `dano` ainda não aparece, porque a linha que a cria ainda não correu. Na pilha de chamadas, o andar de cima é o `calcular_dano`, por baixo dele o `atacar`, que o chamou, e no fim o `<module>`, o programa principal.

#### Passo 5: Avançar linha a linha

Carrega em F10 três vezes, e vê o que muda a cada passo:

| Depois de | Linha marcada a amarelo | `dano` no painel das variáveis |
| --- | --- | --- |
| Parar no ponto de paragem | `dano = super().calcular_dano(alvo)` | ainda não existe |
| F10 | `if alvo.tipo == "Água":` | 25 |
| F10 | `dano = dano * 2` | 25 |
| F10 | `return dano` | 50 |

A segunda linha da tabela é a que confirma a hipótese. O `if` foi avaliado, a condição deu falso, porque o tipo do alvo é `'Fogo'`, e a linha do `print` foi saltada, como devia. Mas a linha seguinte a correr é o `dano = dano * 2`, e a seguir o dano passa a 50. Se quiseres ver a condição a dar falso, escreve `alvo.tipo == "Água"` no painel Vigiar: o VS Code mostra `False`.

#### Passo 6: Encontrar a causa

O `dano = dano * 2` corre sempre porque não está dentro do `if`. Está com a mesma indentação do `if`, e não com a do `print`. Para o Python, o bloco do `if` tem uma linha só, o `print`, e a multiplicação é a linha seguinte da função, que corre em qualquer caso. O sintoma estava no ecrã, no número 50; a causa são quatro espaços em falta, uma linha acima do `return`.

Carrega em Shift+F5 para parar a depuração antes de mudares o código.

#### Passo 7: Corrigir e voltar a reproduzir

Indenta o `dano = dano * 2`, para ficar dentro do `if`, por baixo do `print`. É assim que está na `PokemonPlanta` do `pokemon.py`. Executa outra vez o mesmo programa:

```text
Bulbasaur ataca Charmander e tira 25 de vida.
Charmander tem 65/150 de vida.
```

O dano é 25, como devia. Para confirmar que a vantagem continua a funcionar, troca o Charmander por um Pokémon de água, `PokemonAgua("Squirtle", 100, 30)`, que tem de levar 50 e mostrar "É super eficaz!".

### A pilha de chamadas no depurador

O depurador também ajuda nos erros com traceback. Por omissão, quando há uma exceção que ninguém apanha, o depurador do VS Code para na linha onde ela rebentou, em vez de deixar o programa acabar, e marca essa linha. Com o programa do Ash e do texto `"Pikachu"` aberto, carrega em F5, sem nenhum ponto de paragem.

O programa para no `if pokemon.vida > 0:` do `escolher_pokemon`, com a exceção descrita por cima da linha. A pilha de chamadas mostra os três andares do traceback: `escolher_pokemon`, `combater` e `<module>`. No painel das variáveis, o `pokemon` é `'Pikachu'`, um texto. Clica no andar `combater` da pilha: o painel das variáveis passa a mostrar as variáveis desse andar, e abrindo o `desafiante` vês a `equipa`, com o texto lá dentro. Clica no andar `<module>`: estás no programa principal, onde o `ash` foi criado.

A pilha de chamadas deixa-te subir pelos andares e ver o estado de cada um no momento do erro. É o traceback com os valores à vista.

### Erros frequentes na depuração

**Executar sem o depurador.** O botão do triângulo, no canto de cima, e o Ctrl+F5 correm o programa normalmente: os pontos de paragem são ignorados, e o programa corre até ao fim. Para parar nos pontos de paragem, usa o F5, ou a opção de depurar.

**Um ponto de paragem numa linha que nunca corre.** Se o ponto estiver dentro de um `if` cuja condição é falsa, ou num método que ninguém chama, o programa nunca para. Põe o ponto numa linha que tens a certeza de que corre, mais acima, e avança a partir daí.

**Continuar quando querias avançar.** O F5 corre até ao próximo ponto de paragem, ou até ao fim, e passa por cima de tudo o que querias ver. Para ir linha a linha, usa o F10.

**Entrar onde não interessa.** O F11 numa linha com `print` ou com `len` pode levar-te para dentro do código do próprio Python. Se isso acontecer, o Shift+F11 sai e volta à tua linha. Usa o F11 só nas linhas que chamam as tuas funções e os teus métodos.

**Mudar o código com a depuração a correr.** O programa que está parado é o que foi lido quando a depuração começou. Uma alteração feita a meio só conta na próxima execução. Para a depuração com Shift+F5, muda o código, e começa outra vez.

**Corrigir o sintoma.** Acrescentar um `if` para o erro desaparecer, no sítio onde ele rebenta, quase nunca é a correção. Pergunta sempre de onde veio o valor errado.

### Verifica se percebeste: depuração

1. No traceback do Ash, porque é que nenhum dos três andares é a linha que está mal? Onde está a causa?
2. O que quer dizer "most recent call last"? Em que andar está a função onde o erro rebentou?
3. No exemplo guiado, porque é que a hipótese se escreve antes de abrir o depurador?
4. Que diferença há entre o F10 e o F11? Numa linha `dano = self.calcular_dano(alvo)`, qual usavas para ver o que o `calcular_dano` faz?
5. No passo 5, que linha da tabela confirmou a hipótese, e porquê?

## Parte 3: Logging

### O print é para quem usa o programa; o registo é para quem o mantém

Quando se procura um erro sem depurador, a primeira reação é encher o código de `print`: "cheguei aqui", "a vida é 40", "entrei no if". Funciona, e tem três problemas. Os `print` misturam-se com o que o programa mostra a quem o usa. Quando o erro está resolvido, é preciso apagá-los, um a um, e há sempre um que fica. E quando o erro volta, na semana seguinte, é preciso escrevê-los outra vez.

O **logging** é o registo do que um programa faz, escrito para quem o mantém, e não para quem o usa. Cada mensagem do registo tem um **nível**, que diz a importância do que aconteceu. As mensagens ficam no código, e é a configuração, num só sítio, que decide quais aparecem e para onde vão: para o ecrã, para um ficheiro, ou para lado nenhum. O módulo `logging` vem com o Python.

No ginásio, o `print` continua a mostrar o combate, porque é o jogo: é o que o jogador vê. O registo guarda o que alguém que mantém o ginásio quer saber: que combates houve, entre quem, como acabaram, e que pedidos foram recusados.

### Os cinco níveis

| Nível | Quando se usa | Exemplo no ginásio |
| --- | --- | --- |
| `DEBUG` | Pormenores que só interessam a quem está a investigar um problema | A vida de cada Pokémon no início do combate |
| `INFO` | O programa a funcionar como devia: os acontecimentos normais | Um combate começou; um combate acabou, e quem venceu |
| `WARNING` | Uma coisa inesperada, que o programa conseguiu tratar, mas que convém saber | Um combate recusado, porque um treinador não tinha Pokémon com vida |
| `ERROR` | Uma operação falhou e não foi feita | Uma captura que devia ter acontecido e foi recusada; um ficheiro da equipa que não se conseguiu ler |
| `CRITICAL` | Uma falha tão grave que o programa não pode continuar | O ficheiro de configuração do ginásio não existe, e o programa tem de parar |

Os níveis estão por ordem de importância, e a configuração escolhe um nível mínimo: as mensagens desse nível e acima aparecem, as de baixo não. Com o nível `INFO`, aparecem `INFO`, `WARNING`, `ERROR` e `CRITICAL`, e não aparecem as de `DEBUG`.

Escolher o nível é decidir quem precisa de saber. O `WARNING` e o `ERROR` são os que mais se confundem: num `WARNING` o programa tratou o problema e seguiu em frente; num `ERROR`, alguma coisa que devia acontecer não aconteceu.

### O registo do ginásio

No [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) da pasta 04, o início do ficheiro tem duas linhas novas:

```python
import logging

logger = logging.getLogger(__name__)
```

O `logging.getLogger` devolve um **logger**: o objeto que escreve as mensagens do registo. Cada logger tem um nome, que aparece nas mensagens, para se saber de onde vieram. O nome dado é `__name__`, o nome do próprio módulo: quando outro programa importa o `ginasio.py`, o `__name__` é `"ginasio"`, e as mensagens dizem que vieram do ginásio. É a mesma variável do `if __name__ == "__main__":`.

O `combater` usa o logger em três níveis. Este é o início do método, já com as linhas do registo:

```python
class Ginasio:
    # O construtor fica como estava.

    def combater(self, desafiante):
        """Um combate entre o Pokémon escolhido por cada treinador."""
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            logger.warning(f"Combate recusado em {self.cidade}: {desafiante.nome} contra {self.lider.nome}, sem Pokémon com vida.")
            raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        logger.info(f"Combate em {self.cidade}: {desafiante.nome} com {atacante.nome} contra {self.lider.nome} com {defensor.nome}.")
        logger.debug(f"Vida no início: {atacante.nome} {atacante.vida}, {defensor.nome} {defensor.vida}.")
        # Segue-se o combate, como no tema 03.
```

No fim do combate, depois de criar o registo, há uma última mensagem de `INFO`, com o vencedor: `logger.info(f"Fim do combate em {self.cidade}: venceu {vencedor.nome}.")`.

Cada nível é um método do logger, com o nome do nível em minúsculas: `logger.debug`, `logger.info`, `logger.warning`, `logger.error` e `logger.critical`. Recebem a mensagem, escrita com uma f-string, como num `print`.

### Quem configura é o programa

O `ginasio.py` escreve as mensagens, mas não diz que nível mostrar, nem onde. Isso é decidido pelo programa que usa o ginásio, com uma linha no início:

```python
import logging

from erros import SemPokemonComVida
from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 50, 20)])
cerulean = Ginasio("Cerulean", misty)
cerulean.combater(ash)
try:
    cerulean.combater(ash)
except SemPokemonComVida as erro:
    print(f"Recusado: {erro}")
```

Prevê quais das mensagens do ginásio vão aparecer, e quais não.

```text
[INFO] ginasio: Combate em Cerulean: Ash com Bulbasaur contra Misty com Starmie.

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
[INFO] ginasio: Fim do combate em Cerulean: venceu Ash.
[WARNING] ginasio: Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
Recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
```

O `logging.basicConfig` configura o registo do programa inteiro, e recebe duas coisas. O `level` é o nível mínimo: com `logging.INFO`, a mensagem de `DEBUG` com a vida no início não aparece. O `format` diz como se escreve cada linha: `%(levelname)s` é substituído pelo nome do nível, `%(name)s` pelo nome do logger e `%(message)s` pela mensagem. As linhas do registo distinguem-se agora das do jogo: começam pelo nível entre parênteses retos e dizem que vieram do `ginasio`.

A configuração fica no programa principal, e só aí, por uma razão: o ginásio pode ser usado por vários programas, e cada um quer o seu registo. Um programa de testes quer só os erros; um programa a ser investigado quer tudo. Se o `ginasio.py` configurasse o registo, impunha a sua escolha a todos os programas que o importam.

### Mudar o nível sem mudar o código

Para ver também as mensagens de `DEBUG`, muda-se só o nível na linha do `basicConfig`, para `level=logging.DEBUG`. O resto do programa fica igual:

```text
[INFO] ginasio: Combate em Cerulean: Ash com Bulbasaur contra Misty com Starmie.
[DEBUG] ginasio: Vida no início: Bulbasaur 110, Starmie 90.

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
[INFO] ginasio: Fim do combate em Cerulean: venceu Ash.
[WARNING] ginasio: Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
Recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
```

E com `level=logging.WARNING`, só fica o aviso:

```text

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
[WARNING] ginasio: Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
Recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
```

É a diferença para os `print` de depuração: as mensagens de `DEBUG` ficam no código para sempre, e ninguém as vê até alguém mudar uma palavra na configuração. Quando o erro voltar, na semana seguinte, basta pôr o nível em `DEBUG` outra vez.

### Sem configuração

Se o programa não tiver nenhum `basicConfig`, o Python usa uma regra por omissão: mostra só as mensagens de `WARNING` e acima, e escreve só a mensagem, sem o nível nem o nome. Com o mesmo programa, sem a linha do `basicConfig`:

```text

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
Recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
```

É a linha "Combate recusado..." que viste na parte 1, nos programas que não configuravam o registo. É por isso que um aviso nunca passa despercebido, mesmo num programa que não sabe que o ginásio tem registo, e as mensagens de `INFO` e de `DEBUG` só aparecem a quem as pede.

Quando executas o próprio `ginasio.py`, a demonstração do fim do ficheiro configura o registo com `INFO` e as mensagens aparecem com o nome `__main__`, e não `ginasio`. Executado diretamente, o módulo chama-se `__main__`, que é exatamente o que o `if __name__ == "__main__":` verifica.

### Registar uma exceção

Quando se apanha uma exceção, o método `logger.exception` regista uma mensagem com o nível `ERROR` e, por baixo, o traceback da exceção que foi apanhada. O programa não para: a exceção foi apanhada, e o registo só a guarda.

```python
import logging

from erros import EquipaCheia
from pokemon import PokemonFogo
from ginasio import Treinador

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("torneio")

gary = Treinador("Gary")
for numero in range(7):
    try:
        gary.capturar(PokemonFogo(f"Ponyta {numero + 1}", 50, 20))
    except EquipaCheia:
        logger.exception("Captura recusada")
print(len(gary.equipa))
```

```text
[ERROR] torneio: Captura recusada
Traceback (most recent call last):
  File "torneio.py", line 13, in <module>
    gary.capturar(PokemonFogo(f"Ponyta {numero + 1}", 50, 20))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "ginasio.py", line 81, in capturar
    raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
erros.EquipaCheia: Gary já tem 6 Pokémon e não pode capturar Ponyta 7.
6
```

O programa principal tem o seu próprio logger, com o nome `"torneio"`, que é o nome que se quer ver nas mensagens. A sétima captura foi recusada, o registo guardou a mensagem e o traceback, e o programa continuou até ao `print` do fim. Na última linha do traceback, a exceção aparece como `erros.EquipaCheia`: o nome do módulo onde a classe está, seguido do nome da classe.

O `logger.exception` só se usa dentro de um `except`, porque é aí que existe uma exceção para registar. É a forma de não perder a informação de um erro que foi tratado: o programa continua, e quem o mantém pode ver depois o que aconteceu e onde.

### Guardar o registo num ficheiro

O `basicConfig` pode mandar o registo para um ficheiro, em vez do ecrã, com o parâmetro `filename`:

```python
import logging

from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador

logging.basicConfig(filename="combates.log", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 50, 20)])
cerulean = Ginasio("Cerulean", misty)
cerulean.combater(ash)
print("O combate acabou. O registo está em combates.log.")
```

No ecrã, só aparece o que vem dos `print`:

```text

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
O combate acabou. O registo está em combates.log.
```

E na pasta aparece um ficheiro novo, `combates.log`, com as linhas do registo:

```text
2026-10-08 00:21:39,968 [INFO] ginasio: Combate em Cerulean: Ash com Bulbasaur contra Misty com Starmie.
2026-10-08 00:21:39,968 [INFO] ginasio: Fim do combate em Cerulean: venceu Ash.
```

O `%(asctime)s` acrescenta a data e a hora de cada mensagem, que no teu ficheiro vão ser outras. Num ficheiro, a hora é o que permite saber quando aconteceu cada coisa, dias depois. Cada execução acrescenta as suas linhas ao fim do ficheiro, sem apagar as anteriores: depois de executares o programa três vezes, o ficheiro tem seis linhas.

### O que nunca se regista

Um registo é lido por pessoas que não são quem usa o programa, guarda-se durante muito tempo, e às vezes é enviado a outros para ajudar a resolver um problema. Por isso, há coisas que nunca se escrevem num registo: palavras-passe e códigos de acesso, chaves de serviços, números de documentos, moradas, telefones, e qualquer dado pessoal que não seja preciso para perceber o que aconteceu.

Este programa tem um treinador da Liga, que entra com um código de acesso. O registo da tentativa está mal escrito:

```python
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("liga")


class TreinadorDaLiga:
    """Um treinador inscrito na Liga, com um código de acesso que é segredo."""

    def __init__(self, nome, codigo_de_acesso):
        """Guarda o nome e o código de acesso do treinador."""
        self.nome = nome
        self.codigo_de_acesso = codigo_de_acesso

    def entrar(self, codigo):
        """Devolve True se o código está certo; regista a tentativa."""
        logger.info(f"{self.nome} tentou entrar com o código {codigo}.")
        return codigo == self.codigo_de_acesso


ash = TreinadorDaLiga("Ash", "pikachu-4821")
print(ash.entrar("pikachu-4821"))
```

```text
[INFO] liga: Ash tentou entrar com o código pikachu-4821.
True
```

O código de acesso ficou escrito no registo. Qualquer pessoa que leia o registo, hoje ou daqui a um ano, pode entrar como o Ash. E um código errado também é um problema: muitas vezes é o código certo com um engano, ou o código de outra conta.

O registo deve dizer o que aconteceu, e não o segredo:

```python
class TreinadorDaLiga:
    # O construtor fica como estava.

    def entrar(self, codigo):
        """Devolve True se o código está certo; regista o resultado, sem o código."""
        certo = codigo == self.codigo_de_acesso
        if certo:
            logger.info(f"{self.nome} entrou na Liga.")
        else:
            logger.warning(f"{self.nome} falhou o código de acesso.")
        return certo
```

Com duas tentativas, uma certa e uma errada, o registo fica assim:

```text
[INFO] liga: Ash entrou na Liga.
True
[WARNING] liga: Ash falhou o código de acesso.
False
```

Quem mantém a Liga sabe o que precisa de saber: quem entrou, e quem falhou. O código não aparece em lado nenhum. Nos exemplos deste guia, os nomes dos treinadores são personagens inventadas, e por isso podem aparecer no registo. Num programa com pessoas reais, o registo usa um identificador, como um número de inscrição, e não o nome nem o contacto da pessoa.

### Erros frequentes com logging

**As mensagens de INFO não aparecem.** Sem `basicConfig`, só aparecem as de `WARNING` e acima. Confirma que o programa principal tem a linha do `basicConfig` com o nível que queres.

**O nível mudou e nada mudou.** O `basicConfig` só tem efeito da primeira vez que é chamado, e as chamadas seguintes são ignoradas. Chama-o uma vez, no início do programa principal, antes de qualquer outra coisa que registe.

**O basicConfig dentro de um módulo.** Se o `ginasio.py` chamasse o `basicConfig`, qualquer programa que o importasse ficava com a configuração do ginásio, e o seu próprio `basicConfig` era ignorado, pela regra anterior. Os módulos usam um logger; só o programa principal configura.

**Uma vírgula, como no print.** Um `print` aceita várias coisas separadas por vírgulas; um logger não. A linha `logger.info("Vida do Starmie:", vida)` não dá erro no momento, mas, quando a mensagem é escrita, o logging escreve um bloco que começa por `--- Logging error ---`, com um `TypeError: not all arguments converted during string formatting` lá dentro, e a mensagem certa nunca aparece. O programa continua. Escreve a mensagem numa f-string: `logger.info(f"Vida do Starmie: {vida}")`.

**Um segredo no registo.** Lê cada mensagem do registo como se fosse publicada. Se tiver um código, uma chave ou um dado pessoal que não é preciso, tira-o.

### Verifica se percebeste: logging

1. Porque é que o combate continua a ser mostrado com `print`, e o início e o fim do combate vão para o registo?
2. Com o nível `WARNING`, que mensagens do ginásio aparecem? E com o nível `DEBUG`?
3. Porque é que o `basicConfig` está no programa principal, e não no `ginasio.py`?
4. Uma captura recusada por equipa cheia é um `WARNING` ou um `ERROR`? Defende uma das respostas, e diz em que situação mudavas de ideia.
5. O que está mal na linha `logger.info(f"{self.nome} tentou entrar com o código {codigo}.")`? Como a reescrevias?

## A seguir

O [laboratório](04-excecoes-depuracao-e-logging-laboratorio.md) leva-te a acrescentar ao teu ginásio as exceções do `erros.py` e o registo, e a investigar com o depurador um erro de cálculo noutro tipo de Pokémon. A [ficha de exercícios](04-excecoes-depuracao-e-logging-exercicios.md) tem exercícios das três partes deste guia, para fazeres sem ajuda.

O tema seguinte é o dos testes com pytest. Até aqui, para saber se o ginásio funciona, executavas um programa e comparavas a saída com a tua previsão. Com os testes, essa comparação passa a ser feita por código, e uma das primeiras coisas que vais testar é que o `capturar` lança mesmo a `EquipaCheia` quando a equipa está cheia.

## Vocabulário

| Palavra | O que quer dizer |
| --- | --- |
| Exceção | A forma de o Python avisar que uma linha não pode ser feita. Sobe pelas funções que estão a meio até alguém a apanhar, ou até parar o programa |
| `raise` | A instrução que lança uma exceção |
| `try` e `except` | O bloco onde se espera uma exceção, e o bloco que a trata, se for do tipo indicado |
| `else` de um `try` | O bloco que corre quando o `try` acaba sem exceção |
| `finally` | O bloco que corre sempre, com ou sem exceção |
| Exceção própria | Uma classe criada por ti, filha de `Exception`, com um nome que diz o problema |
| Sintoma | O que se vê de um erro: uma mensagem, um valor errado |
| Causa | A linha de código que está mal e que provoca o sintoma |
| Depurar | Encontrar a causa de um erro a partir do sintoma |
| Traceback | A mensagem de erro completa, com o caminho de chamadas até à linha onde a exceção rebentou |
| Pilha de chamadas | A lista das funções e dos métodos que estão a meio, cada um à espera do que chamou. Em inglês, call stack |
| Depurador | A ferramenta que corre o programa e o deixa parar, para ver as variáveis e avançar linha a linha |
| Ponto de paragem | Uma linha onde o depurador para antes de a executar. Em inglês, breakpoint |
| Logging | O registo do que um programa faz, escrito para quem o mantém |
| Logger | O objeto que escreve as mensagens do registo, com um nome que diz de onde vieram |
| Nível | A importância de uma mensagem do registo: `DEBUG`, `INFO`, `WARNING`, `ERROR` ou `CRITICAL` |

![Rodapé](../imagens/rodape.png)
