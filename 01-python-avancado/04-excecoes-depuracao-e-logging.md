![Cabeçalho](../imagens/cabecalho.png)

# Exceções, depuração e logging

Módulo 10794, Programação avançada com Python. Neste guia aprendes a fazer um objeto recusar um pedido sem que ninguém o possa ignorar. Aprendes também a encontrar a causa de um erro e a deixar o registo do que um programa faz. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](04-excecoes-depuracao-e-logging-laboratorio.md) e a [ficha de exercícios](04-excecoes-depuracao-e-logging-exercicios.md) deste tema.

Até aqui, quando o ginásio Pokémon não podia fazer o que lhe pediam, escrevia uma mensagem com `print` e saía do método com `return`. Funciona enquanto há alguém a olhar para o ecrã. Deixa de funcionar quando quem chama o método é outro pedaço de código, que não lê o ecrã e continua como se nada fosse.

Este guia trata dos erros de três lados. Primeiro, como um objeto recusa um pedido de forma que ninguém o possa ignorar: as exceções, incluindo exceções criadas por ti. Depois, como se encontra a causa de um erro. Para isso lê-se a mensagem de erro completa, que se chama traceback, e usa-se o depurador do VS Code, para ver o programa a correr linha a linha. Por fim, como um programa deixa registo do que fez, com o logging, sem encher o ecrã de `print` que depois é preciso apagar.

O fio condutor continua a ser o ginásio Pokémon. No fim do guia, o ginásio recusa capturas e combates com exceções próprias e regista os combates por níveis de importância.

O código completo do exemplo está na pasta [04-excecoes-depuracao-e-logging](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/) dos exemplos. É a versão do tema 03 com duas mudanças. Um ficheiro novo, [erros.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/erros.py), tem as exceções do ginásio. O [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) usa-as e regista os combates. O [pokemon.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/pokemon.py) e o [anunciadores.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/anunciadores.py) são iguais aos do tema 03.

Os programas deste guia que usam o ginásio importam do `pokemon.py`, do `ginasio.py` e do `erros.py` dessa pasta. Para os executares, copia a pasta para o teu computador e guarda os programas nela. Para executar um programa, abre o terminal do VS Code na pasta e escreve `python3 nome-do-ficheiro.py`. No Windows, se `python3` não funcionar, experimenta `python` ou `py`.

Antes de executares um programa, escreve o que achas que ele vai mostrar, e só depois compara. Se escreveres a previsão depois de ver o resultado, a comparação concorda sempre contigo e não te ensina nada. Todos os programas foram executados em Python 3.14 e em Python 3.9, e as saídas mostradas são as reais. As saídas são iguais nas duas versões.

Nas mensagens de erro, as secções sobre exceções e sobre logging mostram só a última linha. O único caso diferente é a secção "Registar uma exceção", onde o registo escreve o traceback inteiro. A secção sobre ler a mensagem de erro inteira também a mostra toda. O nome do ficheiro aparece no lugar do caminho completo, que no teu computador é outro. Nas versões recentes do Python, a mensagem tem também linhas com acentos circunflexos (`^^^^`) e com til (`~~~~`) por baixo do código, a apontar a parte da linha que falhou. Nas versões antigas essas linhas não aparecem.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. O try e o except do 10.º ano
4. Uma recusa que ninguém ouve
5. raise: uma recusa que não se pode ignorar
6. Apanhar a recusa: try, except e else
7. Uma pausa: tuplos
8. Quando o except apanha de mais
9. Uma exceção própria
10. As exceções do ginásio
11. Uma família de exceções
12. finally: o que corre sempre
13. Um erro tem um sintoma e uma causa
14. Ler um traceback com três andares
15. Um erro sem mensagem
16. O depurador do VS Code
17. A pilha de chamadas no depurador
18. O print é para quem usa o programa; o registo é para quem o mantém
19. Os cinco níveis
20. O registo do ginásio
21. Quem configura é o programa
22. Mudar o nível sem mudar o código
23. Sem configuração
24. Registar uma exceção
25. Guardar o registo num ficheiro
26. O que nunca se regista
27. Exemplo guiado: o dano a dobrar
28. Erros frequentes
29. Palavras novas deste guia
30. Verificar o que aprendeste
31. O que vem a seguir

## O que vais aprender

No fim deste guia, consegues:

- fazer um método recusar um pedido com `raise`, e apanhar a recusa com `try`, `except`, `else` e `finally`;
- criar exceções próprias, com uma classe-mãe comum, e escolher a ordem dos `except`;
- ler um traceback e dizer onde o erro rebentou e onde está a causa;
- seguir a rotina de cinco passos para encontrar um erro, e usar o depurador do VS Code para ver os valores do programa, linha a linha;
- escolher o nível de uma mensagem do registo e configurar o `logging` no programa principal, para o ecrã ou para um ficheiro;
- dizer o que nunca se escreve num registo.

## O que já sabes e vais usar

- Classes, objetos, atributos e métodos: explicados na parte 1 do guia [Objetos, composição e comportamento](03-objetos-e-composicao.md).
- Herança: explicada na parte 3 desse guia. Uma exceção própria é uma classe-filha, e a herança é a base dela.
- O ginásio Pokémon, com o `Treinador`, o `Lider` e o `Ginasio`, e o método de classe `com_equipa`: explicados nas partes 4 e 5 desse guia.
- Os anunciadores do ginásio e o `Combate`, que é uma dataclass: explicados nas partes 6 e 7 desse guia. Os ficheiros da pasta 04 dos exemplos já os têm, e aqui usas o ginásio com eles sem os alterar.
- A função `type` com `.__name__`, que dá o nome da classe de um objeto, e a linha `if __name__ == "__main__":`: do 10.º ano e do guia 03.
- Exceções, do 10.º ano: o que é uma exceção e como se lê a última linha de uma mensagem de erro.
- O `try` com `except`, do 10.º ano, para apanhar um erro conhecido, como o `ValueError` de um `int("abc")`.
- Chamadas de funções, do 10.º ano: uma função chama outra, e a que foi chamada tem de acabar para a outra continuar.
- Constantes, escritas em maiúsculas, como a `VIDA_MAXIMA` do `pokemon.py`: do 10.º ano e do guia 03.
- Listas, ciclos `for`, f-strings e executar um programa no terminal do VS Code: do 10.º ano.
- O VS Code com a extensão Python da Microsoft, que é a que usas para executar os programas. Essa extensão traz o depurador.

O `raise`, o `else` e o `finally` estavam no 10.º ano como matéria extra. Este guia explica-os desde o início, por isso não faz mal se não os deste.

## O try e o except do 10.º ano

Uma **exceção** é a forma de o Python avisar que uma linha não pode ser feita. Quando o `int` recebe um texto que não é um número, não tem nada para devolver, e lança um `ValueError`. Se ninguém apanhar a exceção, o programa para e escreve a mensagem de erro. Se a linha estiver dentro de um `try`, o Python salta para o `except` desse tipo de erro, e o programa continua.

Antes de correres este programa, tenta prever o que ele escreve.

```python
# O try e o except do 10.º ano: apanhar o ValueError de um int.
texto = "muitos"
try:
    quantidade = int(texto)
except ValueError:
    print(f"{texto} não é um número.")
```

O resultado é:

```text
muitos não é um número.
```

O `int("muitos")` não consegue fazer a conversão. O Python salta o resto do `try` e entra no `except ValueError`, e o programa acaba normalmente.

Leitura guiada: o bloco do `try` tem a linha que pode falhar. O bloco do `except` diz o que fazer se ela falhar com aquele tipo de erro. Se o `int` tivesse funcionado, o Python saltava o `except` por inteiro.

Até agora, apanhaste exceções lançadas pelo próprio Python. A partir daqui vais ver o outro lado: os teus objetos a lançar exceções, quando lhes pedem uma coisa que não podem fazer.

## Uma recusa que ninguém ouve

Imagina um treinador que só pode ter dois Pokémon na equipa. O programa seguinte usa uma versão curta do `Treinador`, com os Pokémon guardados só pelo nome. Recusa a terceira captura como o ginásio fazia até aqui: escreve uma mensagem e sai com `return`.

Antes de executares, prevê a saída, linha a linha.

```python
# Uma recusa que ninguém ouve: a equipa só leva dois Pokémon, e a recusa é um print.
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

O resultado é:

```text
Pikachu capturado.
Charmander capturado.
A equipa está cheia!
Bulbasaur capturado.
['Pikachu', 'Charmander']
```

A quarta linha mente. O Bulbasaur não foi capturado, a lista no fim mostra-o, mas o programa escreveu "Bulbasaur capturado." logo a seguir a "A equipa está cheia!". O `capturar` recusou, mas a única coisa que fez foi escrever no ecrã. O código que o chamou não tem forma de saber que o pedido falhou, e continua como se tivesse corrido bem.

Leitura guiada: lê primeiro o `capturar`, que tem duas saídas. Se a equipa já tem dois Pokémon, escreve a mensagem e sai com `return`, sem acrescentar nada. Se não, acrescenta o nome à lista. Depois lê o ciclo do fim: para cada nome, chama o `capturar` e escreve "capturado" logo a seguir, sem verificar se a captura aconteceu. É essa falta de verificação, e a ausência de qualquer sinal que o `capturar` possa dar, que faz a mensagem mentir.

É o mesmo problema que o ginásio tinha: quando não havia Pokémon com vida, o `combater` escrevia "Não há combate" e saía. Quem chamava o `combater` não sabia se houvera combate ou não.

## raise: uma recusa que não se pode ignorar

A instrução `raise` lança uma exceção. Escreve-se `raise` seguido de um objeto de exceção, que se cria como qualquer objeto, com o nome da classe e, entre parênteses, a mensagem. A partir dessa linha, o método para, e a exceção sobe para quem o chamou. Se esse código também não a apanhar, sobe outra vez, até ao programa principal. Se aí ninguém a apanhar, o programa para e escreve a mensagem de erro.

Esta é a mesma classe, com a recusa feita com `raise`. O `ValueError` é uma exceção que o Python já tem, para valores que não servem. Antes de executares, prevê onde o programa para.

```python
# A recusa feita com raise: o capturar lança um ValueError.
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

O resultado é este (a mensagem de erro está reduzida à última linha):

```text
Pikachu capturado.
Charmander capturado.
ValueError: A equipa de Ash está cheia: Bulbasaur ficou de fora.
```

A mentira desapareceu: o programa parou na terceira captura, antes do `print`, com uma mensagem que diz o que aconteceu. Repara em duas coisas.

O `raise` está antes do `append`. Quando a exceção é lançada, o método para nessa linha, e o `append` não chega a correr: a equipa fica como estava. A regra é a mesma das propriedades do tema 03: verifica-se antes de mudar o estado, e só se muda se a verificação passar.

O programa parou de vez, e a lista do fim nem chegou a ser escrita. Recusar não pode querer dizer acabar com o programa. Quem chama o `capturar` tem de poder decidir o que fazer com a recusa, e é para isso que serve o `try`.

Leitura guiada: o `capturar` é igual ao anterior, menos as duas linhas da recusa. O `print` e o `return` deram lugar ao `raise`, que cria o `ValueError` com a mensagem e o lança. No ciclo do fim, nada mudou: a terceira volta chama o `capturar`, a exceção sobe até ao programa principal, e o `print` dessa volta nunca chega a correr.

## Apanhar a recusa: try, except e else

Com o `capturar` a lançar a exceção, o programa principal apanha-a. Antes de correres, prevê as quatro linhas.

```python
# Apanhar a recusa com try, except e else.
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

O resultado é:

```text
Pikachu capturado.
Charmander capturado.
Não foi possível: A equipa de Ash está cheia: Bulbasaur ficou de fora.
['Pikachu', 'Charmander']
```

Há duas coisas novas no `try`.

O `as erro` dá um nome ao objeto da exceção que foi apanhado. Com ele, o `except` pode usar a mensagem que o `raise` escreveu: um `print` de uma exceção mostra a sua mensagem. A frase sobre a equipa cheia foi escrita uma só vez, dentro do `capturar`, que é quem sabe o que aconteceu. O programa principal só a mostra.

O `else` de um `try` corre quando o bloco do `try` acaba sem exceção nenhuma. Por isso o "capturado" só aparece quando a captura correu bem. Podia estar dentro do `try`, a seguir ao `capturar`, e o resultado era o mesmo. Fica no `else` por uma razão: o bloco do `try` deve ter só as linhas cuja exceção queres apanhar. Uma linha a mais dentro do `try` é uma linha a mais cujos erros vão parar ao `except`, e a secção seguinte mostra o problema que isso traz.

Leitura guiada: em cada volta do ciclo, o Python tenta o `capturar` dentro do `try`. Nas duas primeiras voltas não há exceção, por isso salta o `except` e corre o `else`. Na terceira, o `capturar` lança o `ValueError`, o Python salta o resto do `try` e entra no `except`, e o `else` não corre. O ciclo continua até ao fim, e o `print` da equipa corre.

## Uma pausa: tuplos

O programa da secção seguinte usa um tipo de valor que ainda não viste, o tuplo. Explica-se aqui, e depois voltas ao `except`.

Os pedidos desse programa escrevem-se assim: `pedidos = [("Pikachu", "5"), ("Charmander", "cinco")]`. A lista tem dois elementos, e cada um deles é um conjunto de valores entre parênteses, separados por vírgulas, como `("Pikachu", "5")`. Um conjunto de valores escrito assim chama-se **tuplo**. Um tuplo é parecido com uma lista: guarda vários valores por ordem, e lê-se cada um pela posição, com `[0]` para o primeiro e `[1]` para o segundo. A diferença é que um tuplo não se muda depois de criado: não tem `append` nem `remove`. Serve por isso para juntar valores que andam sempre juntos, como o nome e o nível do mesmo pedido. Um tuplo com dois valores também se chama um **par**.

O `for` desse programa escreve-se com dois nomes: `for nome, texto_do_nivel in pedidos:`. Em cada volta, o `for` tira da lista o pedido seguinte, que é um par. Reparte os dois valores pelos dois nomes, pela ordem em que estão. O primeiro valor do par fica em `nome` e o segundo em `texto_do_nivel`. Repartir os valores de um tuplo por vários nomes chama-se **desempacotar** o tuplo. A tabela mostra o que cada nome tem em cada volta:

| Volta | `nome` | `texto_do_nivel` |
| --- | --- | --- |
| 1 | `"Pikachu"` | `"5"` |
| 2 | `"Charmander"` | `"cinco"` |

O `for` com dois nomes faz o mesmo que um `for` com um nome só, seguido de duas linhas que tiram cada valor pela posição. Este excerto mostra essa forma mais comprida, e não é um programa para executar:

```python
for pedido in pedidos:
    nome = pedido[0]
    texto_do_nivel = pedido[1]
```

Com os dois nomes no `for`, essas duas linhas deixam de ser precisas, e cada valor ganha logo um nome que diz o que é. A regra é haver tantos nomes como valores em cada tuplo: dois nomes para pares, como aqui, e quatro nomes se cada tuplo tiver quatro valores. Se os números não baterem certo, o Python lança um `ValueError`, com uma mensagem a dizer que há valores a mais ou a menos para desempacotar.

## Quando o except apanha de mais

O `ValueError` não é só do `capturar`. O `int` também o lança, quando o texto não é um número. No programa desta secção, cada pedido de captura é um par como os da secção anterior, com o nome do Pokémon e o nível escrito em texto. O `try` tem as duas linhas.

Antes de executares o programa, prevê o que escreve para cada um dos dois pedidos.

```python
# O except ValueError também apanha o erro do int, que não é da captura.
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

O resultado é:

```text
Pikachu capturado, no nível 5.
Equipa cheia? invalid literal for int() with base 10: 'cinco'
['Pikachu']
```

A equipa do Ash tem um só Pokémon, e o programa pergunta se está cheia. O `except ValueError` apanhou o erro do `int("cinco")`, que não tem nada a ver com a equipa, e tratou-o como se fosse uma recusa da captura. A mensagem está em inglês: `invalid literal for int() with base 10` quer dizer "literal inválido para o `int()` na base 10", isto é, o `int` não consegue ler `'cinco'` como um número escrito com algarismos.

O `ValueError` é um nome demasiado geral: diz que um valor não serve, mas não diz qual nem porquê. Quando dois erros diferentes têm o mesmo tipo, o `except` não os consegue separar.

Leitura guiada: o `try` tem agora duas linhas que podem lançar um `ValueError`, a do `int` e a do `capturar`. O `except` só vê o tipo da exceção, e por isso trata as duas da mesma maneira, com a mesma frase. Na segunda volta, o erro vem da primeira linha do `try`, e a frase "Equipa cheia?" está errada.

## Uma exceção própria

A solução é dar à recusa da captura um tipo seu. Uma **exceção própria** é uma classe criada por ti, filha de `Exception`, a classe-mãe das exceções do Python. Não precisa de mais nada: a classe-filha herda tudo o que uma exceção precisa, incluindo a forma de guardar e mostrar a mensagem. O corpo da classe pode ser só a docstring, como o primeiro `Lider` do guia [Objetos, composição e comportamento](03-objetos-e-composicao.md).

O programa desta secção acaba com uma linha que usa a função `isinstance`, que vem com o Python. O nome vem do inglês "is instance", que quer dizer "é instância", e instância é outro nome para objeto. O `isinstance` recebe dois valores, primeiro um objeto e depois uma classe, e pergunta se o objeto é dessa classe ou de uma classe-filha dela. Devolve `True` ou `False`, um `bool`, como uma comparação com `==`.

É a relação "é um" da herança, escrita como pergunta. O `isinstance` responde `True` para a classe com que o objeto foi criado e para todas as classes de que essa classe herda, subindo pela família. Responde `False` para qualquer outra.

Antes de correres este programa com as classes do `pokemon.py`, prevê as três respostas.

```python
# O isinstance com as classes do pokemon.py.
from pokemon import Pokemon, PokemonAgua, PokemonFogo

charmander = PokemonFogo("Charmander", 90, 40)
print(isinstance(charmander, PokemonFogo))
print(isinstance(charmander, Pokemon))
print(isinstance(charmander, PokemonAgua))
```

O resultado é:

```text
True
True
False
```

O Charmander foi criado como `PokemonFogo`, e por isso a primeira resposta é `True`. A segunda também é `True`, porque a `PokemonFogo` é filha da `Pokemon`: um Pokémon de fogo é um Pokémon. A terceira é `False`, porque a `PokemonAgua` é outra filha da `Pokemon`, e um Pokémon de fogo não é um Pokémon de água.

Leitura guiada: o programa cria um só objeto e faz a mesma pergunta a três classes diferentes. A primeira é a classe do próprio objeto, a segunda é a classe-mãe dele, e a terceira é uma classe da mesma família, mas de outro ramo.

No programa seguinte, `isinstance(EquipaCheia("teste"), Exception)` cria um objeto `EquipaCheia`, com uma mensagem qualquer, e pergunta se esse objeto é uma exceção. Antes de executares, prevê o que acontece a cada um dos quatro pedidos.

```python
# Uma exceção própria, a EquipaCheia, e um except para cada tipo de erro.
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

O resultado é:

```text
Pikachu capturado, no nível 5.
O nível de Charmander não é um número: cinco.
Bulbasaur capturado, no nível 3.
Não foi possível: A equipa de Ash está cheia: Squirtle ficou de fora.
['Pikachu', 'Bulbasaur']
True
```

Agora há dois `except`, um por cada tipo, e cada erro vai para o seu. O Python experimenta os `except` por ordem, de cima para baixo, e entra no primeiro cujo tipo corresponde à exceção. O Charmander não chegou a ser capturado, porque o `int` falhou antes do `capturar`. Por isso há lugar para o Bulbasaur, e o Squirtle é que fica de fora.

A última linha confirma a herança: um objeto `EquipaCheia` é também um `Exception`, tal como um `PokemonFogo` é também um `Pokemon`. É essa relação "é um" que deixa o `raise` aceitar a classe. O nome da exceção diz o que aconteceu, em português, como os nomes das tuas classes. Nas bibliotecas escritas em inglês, os nomes das exceções acabam quase sempre em `Error`, como `ValueError`. Aqui a regra é o nome dizer o problema.

Leitura guiada: começa pela classe `EquipaCheia`, que só tem a docstring e herda tudo de `Exception`. O `capturar` lança-a no sítio onde antes lançava o `ValueError`. No ciclo, os dois `except` separam os dois problemas: o do `int` vai para o `ValueError`, e o da equipa cheia vai para a `EquipaCheia`. O `else` continua a correr só quando nada falhou.

## As exceções do ginásio

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

São três classes, e nenhuma tem mais do que a docstring. O `ErroDoGinasio` é a classe-mãe das outras duas, e é filha de `Exception`. É a herança do tema 03 aplicada a erros: uma `EquipaCheia` é um `ErroDoGinasio`, e um `ErroDoGinasio` é uma exceção.

No [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) da pasta 04, o `capturar` do `Treinador` passou a ter um limite de seis Pokémon. O limite está guardado numa constante no início do ficheiro, `TAMANHO_MAXIMO_DA_EQUIPA = 6`. Este excerto mostra só o método, e o resto da classe fica como estava:

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
            raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        # O resto do método, com o combate, fica como estava.
```

Há duas mudanças em relação ao tema 03. A primeira é o `raise` no lugar do `print` e do `return`. A segunda é a ordem: na versão anterior, o desafiante entrava na lista de desafiantes logo no início, antes de se saber se havia combate. Agora, a verificação vem primeiro, e o desafiante só entra na lista quando o combate vai mesmo acontecer. Se o combate for recusado, o ginásio fica exatamente como estava, como diz a docstring.

No ficheiro, o método tem também umas linhas que escrevem mensagens no registo do ginásio, uma delas antes do `raise`. Este excerto deixa-as de fora, porque o registo é o assunto de uma secção mais abaixo.

Nenhuma das duas classes escreve no ecrã que houve um problema, nem decide o que fazer a seguir. Lançam a exceção, com uma mensagem que explica o que aconteceu, e quem chamou o método decide: mostrar a mensagem, tentar outro treinador, guardar o erro num registo. A classe não sabe onde vai ser usada. Num programa de consola, a decisão pode ser um `print`. Numa janela, pode ser uma caixa de mensagem. Numa API web, pode ser uma resposta de erro. A exceção serve às três.

## Uma família de exceções

Com uma classe-mãe comum, um só `except` apanha qualquer erro do ginásio. Neste programa, a Misty é a líder, e o Gary faz três pedidos: dois combates e uma série de capturas. Antes de executares, prevê o que acontece a cada pedido, e os três números da última linha.

```python
# Uma família de exceções: um só except apanha as recusas do ginásio.
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

O resultado é:

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

O primeiro combate acontece, e o Vulpix perde. No segundo, o Gary já não tem Pokémon com vida: o `combater` lança `SemPokemonComVida`. No terceiro pedido, o Gary captura cinco Ponyta e fica com seis Pokémon, contando com o Vulpix. A sexta Ponyta é recusada com `EquipaCheia`. As duas exceções foram apanhadas pelo mesmo `except ErroDoGinasio`, porque as duas são filhas dele. O `type(erro).__name__` mostra de que classe era cada uma.

A linha "Combate recusado em Cerulean..." não vem de um `print`. É um aviso que o próprio ginásio escreve, com o módulo `logging` do Python, quando recusa um combate. É a forma de o ginásio deixar uma nota a quem o mantém. As exceções não dependem dela, e a secção "O registo do ginásio" explica como esse aviso funciona.

A última linha mostra que as recusas não deixaram rasto. O Gary tem os seis Pokémon que cabem na equipa. O ginásio tem um combate registado e um desafiante, porque o combate recusado não chegou a pô-lo na lista.

Apanhar a classe-mãe ou a classe-filha é uma escolha. O `except ErroDoGinasio` serve quando a reação é a mesma para todos os erros do ginásio, como aqui, em que só se mostra a mensagem. O `except EquipaCheia` serve quando a reação é própria desse caso, como sugerir ao treinador que liberte um Pokémon. E quando há dois `except` com tipos da mesma família, o da classe-filha tem de vir primeiro, como mostra a secção dos erros frequentes.

Leitura guiada: o ciclo percorre três pedidos, e o `try` envolve tanto o combate como as capturas. O `if` escolhe o que fazer, e o `except ErroDoGinasio` é o único que apanha as recusas dos dois lados. Na linha do `print`, `type(erro)` dá a classe da exceção apanhada e `.__name__` o nome dela. É por isso que a mesma linha mostra `SemPokemonComVida` num pedido e `EquipaCheia` no outro. Os três números do fim contam a equipa do Gary, os combates do ginásio e os desafiantes dele.

## finally: o que corre sempre

Um `try` pode acabar com um `finally`, que corre sempre: quando não houve exceção, quando houve e foi apanhada, e até quando houve e ninguém a apanhou. Antes de executares, prevê as linhas que o programa escreve em cada uma das duas voltas.

```python
# O finally corre em todas as voltas, com ou sem exceção.
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

O resultado é:

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

Na primeira volta, o combate corre bem, e o `finally` corre a seguir. Na segunda, o combate é recusado, o `except` mostra a mensagem, e o `finally` corre na mesma. A linha "Combate recusado..." é o aviso do registo do ginásio, como na secção anterior.

O `finally` serve para o que tem de acontecer em qualquer caso: escrever um resumo, fechar uma ligação, libertar alguma coisa que se abriu no `try`. Num `try` com `except`, `else` e `finally`, a ordem é sempre esta. Primeiro corre o `try`. Depois corre o `except` ou o `else`, conforme houve exceção ou não. No fim corre o `finally`.

Leitura guiada: o ciclo faz duas tentativas com o mesmo desafiante. A primeira acaba com a Starmie KO. Na segunda, o `combater` já não encontra Pokémon com vida na equipa da Misty, e lança a exceção. O `finally` é o último bloco do `try`, e escreve a mesma linha com o número de combates, haja ou não exceção.

## Um erro tem um sintoma e uma causa

O **sintoma** é o que se vê: uma mensagem de erro, um número errado, um combate que nunca acaba. A **causa** é a linha de código que está mal. Os dois raramente estão no mesmo sítio. Um valor errado pode entrar num objeto numa linha, e só rebentar dez linhas depois, noutro método, quando alguém o usa.

**Depurar** é encontrar a causa a partir do sintoma. A tentação é mudar logo o código no sítio do sintoma, para ver se o erro desaparece. Às vezes resulta, e a causa fica lá, à espera do próximo sintoma.

Os erros são de três tipos, e dizer qual é ajuda a escolher o instrumento. Um **erro de escrita** é recusado pelo Python antes de o programa correr, como uma indentação mal feita. Um **erro de execução** para o programa a meio, com uma mensagem, como o `AttributeError` da secção seguinte. Um **erro de lógica** deixa o programa correr até ao fim e dá o resultado errado, como o do dano a dobrar, mais abaixo.

Para encontrar a causa, a forma que funciona é uma rotina de cinco passos:

1. **Observar e reproduzir o erro.** Escreve o caso que falhou, o resultado que esperavas e o resultado que obtiveste. O resultado esperado tira-se do que o programa devia fazer, e não do código que falha. Diz também que tipo de erro é: de escrita, de execução ou de lógica. Encontra uma forma de fazer o erro acontecer sempre, com o programa mais curto possível.
2. **Formular uma hipótese.** Antes de mexer no código, escreve numa frase o que achas que está a acontecer e porquê. A frase tem de ser uma que os valores possam confirmar ou desmentir, e diz o que esperas ver se tiveres razão.
3. **Verificar a hipótese.** Segue os valores no caso mais curto que ainda mostra o erro, e olha para os valores verdadeiros, e não para os que achas que lá estão. A mensagem de erro, o `print` e o depurador servem para isto.
4. **Corrigir a causa.** Muda a instrução que produz o erro, uma causa de cada vez, e não o sítio onde o erro se vê.
5. **Voltar a testar tudo.** Corre outra vez todos os casos, também os que já passavam, e explica o que mudou.

A mensagem de um erro de execução é uma pista, e não a resposta. A linha que ela aponta mostra onde o programa rebentou, e a causa pode ter nascido noutra linha, antes.

## Ler um traceback com três andares

Este programa tem um erro. O Ash foi criado com o `com_equipa`, mas a lista da equipa tem o nome do Pokémon, em texto, e não um objeto Pokémon. Guarda-o num ficheiro `combate.py`, na pasta copiada.

```python
# combate.py: um erro de execução, para ler com o traceback.
from pokemon import PokemonAgua
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", ["Pikachu"])
cerulean = Ginasio("Cerulean", misty)
cerulean.combater(ash)
```

Antes de o executares, tenta prever: o programa chega a escrever alguma linha de combate? Desta vez, a mensagem de erro aparece inteira, como o Python 3.14 a escreve:

```text
Traceback (most recent call last):
  File "combate.py", line 8, in <module>
    cerulean.combater(ash)
    ~~~~~~~~~~~~~~~~~^^^^^
  File "ginasio.py", line 140, in combater
    atacante = desafiante.escolher_pokemon()
  File "ginasio.py", line 87, in escolher_pokemon
    if pokemon.vida > 0:
       ^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'vida'
```

Não aparece nenhuma linha de combate: o erro rebenta antes de o combate começar. Esta mensagem chama-se **traceback**, que quer dizer, à letra, "o rasto para trás". A primeira linha diz como se lê: "most recent call last" quer dizer "a chamada mais recente fica no fim".

Cada par de linhas que começa por `File` é um **andar**. Tem um ficheiro, um número de linha, o nome da função ou do método que estava a correr, e a linha de código. O andar de cima é o programa principal, que o Python chama `<module>`, a chamar o `combater`. O do meio é o `combater`, a chamar o `escolher_pokemon`. O de baixo é o `escolher_pokemon`, onde o erro rebentou.

A última linha diz o tipo de exceção e a mensagem, em inglês: `'str' object has no attribute 'vida'` quer dizer "um objeto `str` não tem o atributo `vida`". O `str` é o tipo dos textos, e atributo é a palavra que já usas para o que um objeto guarda. Aqui, um texto não tem nenhum atributo `vida`.

Lê-se assim:

1. A última linha diz o quê. Alguém tentou ler `.vida` de um texto.
2. O andar de baixo diz onde rebentou. Foi na linha 87 do `ginasio.py`, no `if pokemon.vida > 0:` do `escolher_pokemon`. Ali, `pokemon` era um texto.
3. Os andares de cima dizem como se chegou lá. O programa principal chamou o `combater`, que chamou o `escolher_pokemon` do desafiante.
4. A causa não está no traceback. Nenhum dos três andares é a linha que está mal. O `escolher_pokemon` está certo: percorre a equipa e lê a vida de cada Pokémon. O problema é a equipa ter um texto lá dentro, e o texto entrou na linha 6 do programa, `Treinador.com_equipa("Ash", ["Pikachu"])`, que já tinha acabado quando o erro rebentou.

O traceback mostra onde o erro rebentou e o caminho até lá. A causa pode estar nesse caminho ou antes dele, numa linha que deixou um valor errado num objeto. Corrigir o sintoma, por exemplo mudando o `escolher_pokemon` para saltar os textos, escondia o erro: o Ash ficava com uma equipa sem Pokémon, e ninguém percebia porquê. A correção é na linha 6: a lista tem de levar um Pokémon a sério, como `[PokemonFogo("Charmander", 90, 40)]`, com a importação do `PokemonFogo`.

Os andares do traceback são a **pilha de chamadas**: a lista das funções e métodos que estão a meio, cada um à espera do que chamou. O programa principal está à espera do `combater`, e o `combater` está à espera do `escolher_pokemon`. É a mesma ideia das chamadas de função do 10.º ano, e vais vê-la outra vez no depurador.

Leitura guiada: lê o traceback de baixo para cima. Começa pela última linha, que diz o quê, passa ao andar de baixo, que diz onde, e sobe pelos andares até ao programa principal, que diz como se chegou lá. Depois sai do traceback e vai ao programa, procurar de onde veio o texto que não devia estar na equipa.

## Um erro sem mensagem

Os erros mais difíceis não têm traceback. O programa corre até ao fim, e o resultado está errado. Este programa tem uma cópia da classe `PokemonPlanta` com uma linha mudada. Um Bulbasaur, de planta, ataca um Charmander, de fogo. Antes de executares, tenta prever quanta vida o Charmander perde.

```python
# investigar.py: um erro de lógica, sem mensagem de erro.
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

O resultado é:

```text
Bulbasaur ataca Charmander e tira 50 de vida.
Charmander tem 40/150 de vida.
```

O Bulbasaur tem 25 de ataque, e a planta só tem vantagem contra a água. Contra fogo, devia tirar 25. Tirou 50, e não apareceu "É super eficaz!". Não há mensagem de erro, porque, para o Python, não há erro nenhum: todas as linhas fazem o que dizem. É aqui que o depurador ajuda.

Se já viste a causa, ótimo. Num programa de 20 linhas, ler com atenção às vezes chega. O exemplo guiado, mais abaixo, usa este erro para mostrar o depurador, porque é um erro pequeno, em que podes confirmar cada passo. Num programa de 500 linhas, ler não chega.

Leitura guiada: o ataque do Bulbasaur é 25, e o `calcular_dano` começa por pedir ao `Pokemon` o dano normal, que é o ataque. Depois vem o `if`, que escreve a mensagem quando o alvo é de água, a linha `dano = dano * 2` e, por fim, o `return`. A causa do erro fica para o exemplo guiado, mais abaixo.

## O depurador do VS Code

Um **depurador** é uma ferramenta que corre o programa e o deixa parar onde quiseres. Nessa paragem vês o valor de cada variável e avanças uma linha de cada vez. É como a tabela com os valores das variáveis, linha a linha, que podes fazer no papel, mas feita pelo computador, com os valores verdadeiros.

O VS Code tem um depurador para Python, que vem com a extensão Python da Microsoft. As ideias são estas:

| Ideia | O que é | Como se faz no VS Code |
| --- | --- | --- |
| Ponto de paragem | Uma linha onde o programa para antes de a executar. Em inglês, breakpoint | Clicar na margem, à esquerda do número da linha: aparece um ponto vermelho. Clicar outra vez tira-o. Também se põe com F9, na linha onde está o cursor |
| Executar com o depurador | Correr o programa de forma que pare nos pontos de paragem | F5, ou o menu Executar, Iniciar Depuração (Run, Start Debugging, se o VS Code estiver em inglês) |
| Continuar | Correr até ao próximo ponto de paragem, ou até ao fim | F5, com o programa parado |
| Avançar uma linha | Executar a linha marcada e parar na seguinte, sem entrar nas funções que ela chama. Em inglês, Step Over | F10 |
| Entrar na chamada | Se a linha marcada chama uma função ou um método, entrar nele e parar na sua primeira linha. Em inglês, Step Into | F11 |
| Sair da chamada | Correr até ao fim da função atual e parar na linha que a chamou. Em inglês, Step Out | Shift+F11 |
| Parar | Acabar a depuração | Shift+F5, ou o quadrado vermelho na barra |

Quando o programa está parado, a linha que vai correr a seguir aparece marcada a amarelo, e a barra lateral da depuração mostra três painéis que vais usar:

- **Variáveis** (Variables): os valores das variáveis da função onde o programa está parado. Um objeto pode ser aberto, com a seta, para ver os seus atributos.
- **Pilha de chamadas** (Call Stack): os andares do traceback, com o programa parado. O de cima é a função onde estás. Clicar noutro mostra as variáveis desse andar.
- **Vigiar** (Watch): expressões que escreves tu, como `alvo.tipo == "Água"`, e que o VS Code recalcula a cada passo.

Em computadores portáteis e em Mac, as teclas F5, F10 e F11 podem precisar da tecla Fn. Na primeira vez que carregas em F5, o VS Code pode perguntar que depurador usar. Escolhe o de Python, e depois a opção para depurar o ficheiro que está aberto (em inglês, Python Debugger e Python File).

O botão de executar, o triângulo no canto de cima, corre o programa sem o depurador, e não para nos pontos de paragem. Ao lado dele há uma seta com a opção de depurar o ficheiro.

## A pilha de chamadas no depurador

O depurador também ajuda nos erros com traceback. Por omissão, quando há uma exceção que ninguém apanha, o depurador do VS Code não deixa o programa acabar. Para na linha onde a exceção rebentou, e marca-a. Abre o `combate.py`, o programa do Ash e do texto `"Pikachu"`, e carrega em F5, sem nenhum ponto de paragem.

O programa para no `if pokemon.vida > 0:` do `escolher_pokemon`, com a exceção descrita por cima da linha. A pilha de chamadas mostra os três andares do traceback: `escolher_pokemon`, `combater` e `<module>`. No painel das variáveis, o `pokemon` é `'Pikachu'`, um texto.

Clica no andar `combater` da pilha: o painel das variáveis passa a mostrar as variáveis desse andar. Abrindo o `desafiante`, vês a `equipa`, com o texto lá dentro. Clica no andar `<module>`: estás no programa principal, onde o `ash` foi criado.

A pilha de chamadas deixa-te subir pelos andares e ver o estado de cada um no momento do erro. É o traceback com os valores à vista.

## O print é para quem usa o programa; o registo é para quem o mantém

Quando se procura um erro sem depurador, a primeira reação é encher o código de `print`: "cheguei aqui", "a vida é 40", "entrei no if". Funciona, e tem três problemas. Os `print` misturam-se com o que o programa mostra a quem o usa. Quando o erro está resolvido, é preciso apagá-los, um a um, e há sempre um que fica. E quando o erro volta, na semana seguinte, é preciso escrevê-los outra vez.

O **logging** é o registo do que um programa faz, escrito para quem o mantém, e não para quem o usa. Cada mensagem do registo tem um **nível**, que diz a importância do que aconteceu. As mensagens ficam no código, e é a configuração, num só sítio, que decide quais aparecem e para onde vão: para o ecrã, para um ficheiro, ou para lado nenhum. O módulo `logging` vem com o Python.

No ginásio, o `print` continua a mostrar o combate, porque é o jogo: é o que o jogador vê. O registo guarda o que alguém que mantém o ginásio quer saber: que combates houve, entre quem, como acabaram, e que pedidos foram recusados.

## Os cinco níveis

| Nível | Quando se usa | Exemplo no ginásio |
| --- | --- | --- |
| `DEBUG` | Pormenores que só interessam a quem está a investigar um problema | A vida de cada Pokémon no início do combate |
| `INFO` | O programa a funcionar como devia: os acontecimentos normais | Um combate começou; um combate acabou, e quem venceu |
| `WARNING` | Uma coisa inesperada, que o programa conseguiu tratar, mas que convém saber | Um combate recusado, porque um treinador não tinha Pokémon com vida |
| `ERROR` | Uma operação falhou e não foi feita | Uma captura que devia ter acontecido e foi recusada; um ficheiro da equipa que não se conseguiu ler |
| `CRITICAL` | Uma falha tão grave que o programa não pode continuar | O ficheiro de configuração do ginásio não existe, e o programa tem de parar |

Os níveis estão por ordem de importância, e a configuração escolhe um nível mínimo: as mensagens desse nível e acima aparecem, as de baixo não. Com o nível `INFO`, aparecem `INFO`, `WARNING`, `ERROR` e `CRITICAL`, e não aparecem as de `DEBUG`.

Escolher o nível é decidir quem precisa de saber. O `WARNING` e o `ERROR` são os que mais se confundem. Num `WARNING`, o programa tratou o problema e seguiu em frente. Num `ERROR`, alguma coisa que devia acontecer não aconteceu.

## O registo do ginásio

No [ginasio.py](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) da pasta 04, o início do ficheiro tem duas linhas novas:

```python
import logging

logger = logging.getLogger(__name__)
```

O `logging.getLogger` devolve um **logger**: o objeto que escreve as mensagens do registo. Cada logger tem um nome, que aparece nas mensagens, para se saber de onde vieram. O nome dado é `__name__`, o nome do próprio módulo. Quando outro programa importa o `ginasio.py`, o `__name__` é `"ginasio"`, e as mensagens dizem que vieram do ginásio. É a mesma variável do `if __name__ == "__main__":`.

O `combater` usa o logger em três níveis. Este é o início do método, já com as linhas do registo:

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
        logger.info(f"Combate em {self.cidade}: {desafiante.nome} com {atacante.nome} contra {self.lider.nome} com {defensor.nome}.")
        logger.debug(f"Vida no início: {atacante.nome} {atacante.vida}, {defensor.nome} {defensor.vida}.")
        # Segue-se o combate, como no tema 03.
```

No fim do combate, depois de criar o registo, há uma última mensagem de `INFO`, com o vencedor: `logger.info(f"Fim do combate em {self.cidade}: venceu {vencedor.nome}.")`.

Cada nível é um método do logger, com o nome do nível em minúsculas: `logger.debug`, `logger.info`, `logger.warning`, `logger.error` e `logger.critical`. Recebem a mensagem, escrita com uma f-string, como num `print`.

Leitura guiada: o aviso está dentro do `if` que recusa o combate, antes do `raise`, porque depois do `raise` o método já parou. As duas mensagens seguintes só correm quando o combate vai mesmo acontecer. O `INFO` diz quem combate com quem, e o `DEBUG` guarda um pormenor que só interessa a quem investiga, a vida de cada Pokémon antes do primeiro ataque.

## Quem configura é o programa

O `ginasio.py` escreve as mensagens, mas não diz que nível mostrar, nem onde. Isso é decidido pelo programa que usa o ginásio, com uma linha no início. Antes de executares este programa, prevê quais das mensagens do ginásio vão aparecer, e quais não.

```python
# Quem configura o registo é o programa principal, e não o ginásio.
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

O resultado é:

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

A configuração fica no programa principal, e só aí, por uma razão: o ginásio pode ser usado por vários programas, e cada um quer o seu registo. Um programa de testes quer só os erros. Um programa a ser investigado quer tudo. Se o `ginasio.py` configurasse o registo, impunha a sua escolha a todos os programas que o importam.

Leitura guiada: a linha do `basicConfig` vem antes de tudo o que regista, e só depois se criam os treinadores e o ginásio. O primeiro `combater` escreve o `INFO` do início, o jogo, e o `INFO` do fim. O segundo é recusado: o ginásio escreve o aviso e lança a exceção, e o `except` mostra a mensagem com um `print`. Os `print` são do programa, e as linhas com o nível entre parênteses retos são do registo.

## Mudar o nível sem mudar o código

Para ver também as mensagens de `DEBUG`, muda-se só o nível na linha do `basicConfig`, para `level=logging.DEBUG`. O resto do programa fica igual. Antes de olhares para o resultado, prevê onde aparece a linha nova.

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

## Sem configuração

Se o programa não tiver nenhum `basicConfig`, o Python usa uma regra por omissão. Mostra só as mensagens de `WARNING` e acima, e escreve só a mensagem, sem o nível nem o nome. Antes de veres o resultado, prevê o que sobra do mesmo programa sem a linha do `basicConfig`.

```text

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 100 de vida.
Starmie está KO (0/150).
Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
Recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
```

É a linha "Combate recusado..." que viste nos programas das secções sobre exceções, que não configuravam o registo. É por isso que um aviso nunca passa despercebido, mesmo num programa que não sabe que o ginásio tem registo. As mensagens de `INFO` e de `DEBUG` só aparecem a quem as pede.

Quando executas o próprio `ginasio.py`, a demonstração do fim do ficheiro configura o registo com `INFO`, e as mensagens aparecem com o nome `__main__`, e não `ginasio`. Executado diretamente, o módulo chama-se `__main__`, que é exatamente o que o `if __name__ == "__main__":` verifica.

## Registar uma exceção

Quando se apanha uma exceção, o método `logger.exception` regista uma mensagem com o nível `ERROR` e, por baixo, o traceback da exceção que foi apanhada. O programa não para: a exceção foi apanhada, e o registo só a guarda. Guarda o programa seguinte num ficheiro `torneio.py`, na pasta copiada, e prevê o que acontece à sétima captura.

```python
# torneio.py: registar uma exceção apanhada, com o traceback.
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

O resultado é:

```text
[ERROR] torneio: Captura recusada
Traceback (most recent call last):
  File "torneio.py", line 14, in <module>
    gary.capturar(PokemonFogo(f"Ponyta {numero + 1}", 50, 20))
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "ginasio.py", line 81, in capturar
    raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
erros.EquipaCheia: Gary já tem 6 Pokémon e não pode capturar Ponyta 7.
6
```

O programa principal tem o seu próprio logger, com o nome `"torneio"`, que é o nome que se quer ver nas mensagens. A sétima captura foi recusada, o registo guardou a mensagem e o traceback, e o programa continuou até ao `print` do fim. Na última linha do traceback, a exceção aparece como `erros.EquipaCheia`: o nome do módulo onde a classe está, seguido do nome da classe.

O `logger.exception` só se usa dentro de um `except`, porque é aí que existe uma exceção para registar. É a forma de não perder a informação de um erro que foi tratado: o programa continua, e quem o mantém pode ver depois o que aconteceu e onde.

Leitura guiada: o ciclo tenta sete capturas, e as seis primeiras correm bem. Na sétima, o `capturar` lança a `EquipaCheia`, e o `except` chama o `logger.exception` com uma mensagem curta. O logger escreve essa mensagem com o nível `ERROR` e acrescenta o traceback, sem parar o programa. O `print` do fim confirma que a equipa ficou com seis Pokémon.

## Guardar o registo num ficheiro

O `basicConfig` pode mandar o registo para um ficheiro, em vez do ecrã, com o parâmetro `filename`. Antes de executares o programa seguinte, prevê o que aparece no ecrã e o que vai para o ficheiro.

```python
# O registo guardado num ficheiro, com a hora de cada mensagem.
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

Leitura guiada: o `basicConfig` ganhou o parâmetro `filename`, e o `format` ganhou o `%(asctime)s` à frente. O resto do programa é igual ao da secção anterior. As mensagens do registo vão para o ficheiro, e só os `print` chegam ao ecrã.

## O que nunca se regista

Um registo é lido por pessoas que não são quem usa o programa, guarda-se durante muito tempo, e às vezes é enviado a outros para ajudar a resolver um problema. Por isso, há coisas que nunca se escrevem num registo: palavras-passe, códigos de acesso, chaves de serviços, números de documentos, moradas e telefones. O mesmo vale para qualquer dado pessoal que não seja preciso para perceber o que aconteceu.

Este programa tem um treinador da Liga, que entra com um código de acesso. O registo da tentativa está mal escrito. Antes de executares, prevê o que fica escrito no registo.

```python
# O registo de uma tentativa de entrada, com o código de acesso à vista.
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

O resultado é:

```text
[INFO] liga: Ash tentou entrar com o código pikachu-4821.
True
```

O código de acesso ficou escrito no registo. Qualquer pessoa que leia o registo, hoje ou daqui a um ano, pode entrar como o Ash. E um código errado também é um problema: muitas vezes é o código certo com um engano, ou o código de outra conta.

O registo deve dizer o que aconteceu, e não o segredo. Esta é a versão certa. Com duas tentativas, uma certa e uma errada, prevê as linhas do registo e os dois valores que o programa escreve.

```python
# O registo de uma tentativa de entrada, sem o código.
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
        """Devolve True se o código está certo; regista o resultado, sem o código."""
        certo = codigo == self.codigo_de_acesso
        if certo:
            logger.info(f"{self.nome} entrou na Liga.")
        else:
            logger.warning(f"{self.nome} falhou o código de acesso.")
        return certo


ash = TreinadorDaLiga("Ash", "pikachu-4821")
print(ash.entrar("pikachu-4821"))
print(ash.entrar("pikachu-0000"))
```

O resultado é:

```text
[INFO] liga: Ash entrou na Liga.
True
[WARNING] liga: Ash falhou o código de acesso.
False
```

Quem mantém a Liga sabe o que precisa de saber: quem entrou, e quem falhou. O código não aparece em lado nenhum. Nos exemplos deste guia, os nomes dos treinadores são personagens inventadas, e por isso podem aparecer no registo. Num programa com pessoas reais, o registo usa um identificador, como um número de inscrição, e não o nome nem o contacto da pessoa.

Leitura guiada: o `entrar` compara primeiro o código e guarda o resultado em `certo`. Só depois decide o que registar: um `INFO` quando entrou, um `WARNING` quando falhou. Nenhuma das duas mensagens usa a variável `codigo`, e é isso que mantém o segredo fora do registo.

## Exemplo guiado: o dano a dobrar

Este exemplo percorre os cinco passos da rotina de depuração num erro de lógica, com o depurador do VS Code. Tem sete etapas, que cobrem os cinco passos. As etapas 1 e 2 são os passos 1 e 2, e as etapas 3, 4 e 5 são o passo 3. A etapa 6 é o passo 4, e a etapa 7 é o passo 5. O erro é o da secção "Um erro sem mensagem". Um Bulbasaur, com 25 de ataque, ataca um Charmander. A planta só tem vantagem contra a água, por isso o ataque devia tirar 25 de vida. O programa tira 50. Vamos encontrar a linha que está mal.

### Etapa 1: Observar e reproduzir o erro

O programa da secção "Um erro sem mensagem" já reproduz o erro. É curto e dá sempre o mesmo resultado. Guarda-o num ficheiro, `investigar.py`, na pasta copiada.

Escreve agora o caso, o resultado esperado e o obtido. O caso é o Bulbasaur, com 25 de ataque, a atacar o Charmander. O resultado esperado tira-se das regras do jogo, e não do código que falha. A planta só tem vantagem contra a água, por isso o Charmander devia perder 25 de vida. O resultado obtido é 50, e a mensagem "É super eficaz!" não aparece. O programa corre até ao fim e dá o resultado errado, por isso é um erro de lógica.

### Etapa 2: Formular uma hipótese

O dano é o dobro do que devia, e o "É super eficaz!" não aparece. A multiplicação por 2 está a acontecer sem a condição da vantagem. Hipótese: no `calcular_dano` da `PokemonPlanta`, o `dano * 2` corre mesmo quando o `if` é falso. Se a hipótese estiver certa, quando o programa passar pelo `calcular_dano`, o `if` vai dar falso e, mesmo assim, o `dano` vai passar de 25 a 50.

Escreve a hipótese antes de abrires o depurador. Se escreveres depois, vais olhar para os valores à procura do que já sabes, e não do que lá está.

### Etapa 3: Pôr o ponto de paragem

O ponto de paragem fica na primeira linha que interessa: `dano = super().calcular_dano(alvo)`, a primeira linha do corpo do `calcular_dano`. Clica na margem, à esquerda do número dessa linha, e confirma que aparece o ponto vermelho.

### Etapa 4: Executar com o depurador

Carrega em F5. O programa corre até ao ponto de paragem e para. A linha `dano = super().calcular_dano(alvo)` fica marcada a amarelo: é a próxima a correr, e ainda não correu.

No painel das variáveis aparecem `self` e `alvo`. Abre o `alvo`, com a seta, e confirma: `nome` é `'Charmander'` e `tipo` é `'Fogo'`. A variável `dano` ainda não aparece, porque a linha que a cria ainda não correu. Na pilha de chamadas, o andar de cima é o `calcular_dano`. Por baixo dele está o `atacar`, que o chamou, e no fim o `<module>`, o programa principal.

### Etapa 5: Avançar linha a linha

Carrega em F10 três vezes, e vê o que muda a cada vez:

| Depois de | Linha marcada a amarelo | `dano` no painel das variáveis |
| --- | --- | --- |
| Parar no ponto de paragem | `dano = super().calcular_dano(alvo)` | ainda não existe |
| F10 | `if alvo.tipo == "Água":` | 25 |
| F10 | `dano = dano * 2` | 25 |
| F10 | `return dano` | 50 |

A linha que confirma a hipótese é a que aparece com o segundo F10: `dano = dano * 2`. O `if` foi avaliado, a condição deu falso, porque o tipo do alvo é `'Fogo'`, e a linha do `print` foi saltada, como devia. Mesmo assim, a linha seguinte a correr é o `dano = dano * 2`, e a seguir o dano passa a 50. Se quiseres ver a condição a dar falso, escreve `alvo.tipo == "Água"` no painel Vigiar: o VS Code mostra `False`.

### Etapa 6: Corrigir a causa

O `dano = dano * 2` corre sempre porque não está dentro do `if`. Está com a mesma indentação do `if`, e não com a do `print`. Para o Python, o bloco do `if` tem uma linha só, o `print`, e a multiplicação é a linha seguinte da função, que corre em qualquer caso. O sintoma estava no ecrã, no número 50. A causa são quatro espaços em falta, uma linha acima do `return`.

Carrega em Shift+F5 para parar a depuração antes de mudares o código. Depois indenta o `dano = dano * 2`, para ficar dentro do `if`, por baixo do `print`. É assim que está na `PokemonPlanta` do `pokemon.py`. Mudaste a instrução que produzia o erro, e uma só.

### Etapa 7: Voltar a testar tudo

Executa outra vez o mesmo programa:

```text
Bulbasaur ataca Charmander e tira 25 de vida.
Charmander tem 65/150 de vida.
```

O dano é 25, como devia. Falta o caso que já funcionava, a vantagem contra a água. Acrescenta `PokemonAgua` à linha do `import`, troca o Charmander por um Pokémon de água, `PokemonAgua("Squirtle", 100, 30)`, e corre outra vez. O dano tem de ser 50, com a mensagem "É super eficaz!":

```text
É super eficaz!
Bulbasaur ataca Squirtle e tira 50 de vida.
Squirtle tem 50/150 de vida.
```

O que mudou foi só a indentação de uma linha. O dobro passou a aplicar-se apenas quando o `if` é verdadeiro: contra o fogo, o dano ficou em 25, e contra a água continua a ser 50. Os dois casos passam.

## Erros frequentes

### Os except pela ordem errada

O Python entra no primeiro `except` que corresponde. Se o da classe-mãe vier primeiro, apanha também as filhas, e o `except` da filha nunca corre. Antes de executares este programa, prevê qual das duas mensagens aparece.

```python
# Os except pela ordem errada: o da classe-mãe apanha tudo.
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

O resultado é:

```text
Um erro qualquer do ginásio.
6
```

Não há erro nem aviso: o segundo `except` está lá, mas nunca vai correr. Os `except` vão do mais específico para o mais geral.

Leitura guiada: a `EquipaCheia` é filha do `ErroDoGinasio`, por isso o primeiro `except` corresponde à exceção da sétima captura e o Python não chega ao segundo. Trocar a ordem dos dois `except` resolve.

### Um except que apanha tudo

O `except Exception` apanha quase qualquer erro, incluindo os teus próprios enganos. Antes de executares, prevê o que o programa escreve.

```python
# Um except Exception esconde os enganos do programa.
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

O resultado é:

```text
Ash tem 1 Pokémon.
Não foi possível capturar.
```

A captura correu bem, como mostra a primeira linha. O erro está na terceira linha do `try`, onde `nome` está mal escrito, e o Python lançou um `AttributeError`. O `except Exception` apanhou-o e escreveu uma mensagem que diz o contrário do que aconteceu. Sem o `try`, a mensagem de erro apontava logo para a linha com `nmoe`. Apanha só os tipos de exceção que sabes tratar, e deixa os outros chegar ao ecrã, onde se veem.

### Um except que não faz nada

Um `except EquipaCheia:` com só um `pass` lá dentro faz desaparecer a recusa, e volta-se ao problema do início: o programa continua como se a captura tivesse corrido bem. Se apanhas uma exceção, faz alguma coisa com ela: mostra a mensagem, regista-a, ou tenta outra coisa.

### Esquecer o Exception na classe

Uma classe sem `(Exception)` é uma classe normal, e o `raise` recusa-a. Antes de executares, prevê a mensagem.

```python
# Uma classe sem Exception não é uma exceção.
class EquipaCheia:
    """Esqueceu-se o (Exception): isto é uma classe normal."""


raise EquipaCheia()
```

O resultado, reduzido à última linha, é:

```text
TypeError: exceptions must derive from BaseException
```

A mensagem diz que as exceções têm de descender de `BaseException`, que é a classe de que a própria `Exception` é filha. Se tentares criar a exceção com uma mensagem, `EquipaCheia("...")`, o erro aparece ainda antes, e é outro: `TypeError: EquipaCheia() takes no arguments`. Uma classe normal sem construtor não aceita argumentos.

### Uma exceção sem mensagem

`raise EquipaCheia()` funciona, mas quem apanha a exceção não tem nada para mostrar: um `print(erro)` escreve uma linha vazia. Escreve sempre na mensagem o que aconteceu, com os dados que ajudam a perceber: quem, o quê, e porque não foi possível.

### Executar sem o depurador

O botão do triângulo, no canto de cima, e o Ctrl+F5 correm o programa normalmente: os pontos de paragem são ignorados, e o programa corre até ao fim. Para parar nos pontos de paragem, usa o F5, ou a opção de depurar.

### Um ponto de paragem numa linha que nunca corre

Se o ponto estiver dentro de um `if` cuja condição é falsa, ou num método que ninguém chama, o programa nunca para. Põe o ponto numa linha que tens a certeza de que corre, mais acima, e avança a partir daí.

### Continuar quando querias avançar

O F5 corre até ao próximo ponto de paragem, ou até ao fim, e passa por cima de tudo o que querias ver. Para ir linha a linha, usa o F10.

### Entrar onde não interessa

O F11 numa linha com `print` ou com `len` pode levar-te para dentro do código do próprio Python. Se isso acontecer, o Shift+F11 sai e volta à tua linha. Usa o F11 só nas linhas que chamam as tuas funções e os teus métodos.

### Mudar o código com a depuração a correr

O programa que está parado é o que foi lido quando a depuração começou. Uma alteração feita a meio só conta na próxima execução. Para a depuração com Shift+F5, muda o código, e começa outra vez.

### Corrigir o sintoma

Acrescentar um `if` para o erro desaparecer, no sítio onde ele rebenta, quase nunca é a correção. Pergunta sempre de onde veio o valor errado.

### As mensagens de INFO não aparecem

Sem `basicConfig`, só aparecem as de `WARNING` e acima. Confirma que o programa principal tem a linha do `basicConfig` com o nível que queres.

### O nível mudou e nada mudou

O `basicConfig` só tem efeito da primeira vez que é chamado, e as chamadas seguintes são ignoradas. Chama-o uma vez, no início do programa principal, antes de qualquer outra coisa que registe.

### O basicConfig dentro de um módulo

Se o `ginasio.py` chamasse o `basicConfig`, qualquer programa que o importasse ficava com a configuração do ginásio. O `basicConfig` do próprio programa era ignorado, pela regra anterior. Os módulos usam um logger, e só o programa principal configura.

### Uma vírgula, como no print

Um `print` aceita várias coisas separadas por vírgulas, e um logger não. A linha `logger.info("Vida do Starmie:", vida)` não dá erro no momento. Quando a mensagem é escrita, o logging escreve um bloco que começa por `--- Logging error ---`, com um `TypeError: not all arguments converted during string formatting` lá dentro, e a mensagem certa nunca aparece. O programa continua. Escreve a mensagem numa f-string: `logger.info(f"Vida do Starmie: {vida}")`.

### Um segredo no registo

Lê cada mensagem do registo como se fosse publicada. Se tiver um código, uma chave ou um dado pessoal que não é preciso, tira-o.

## Palavras novas deste guia

- Exceção: a forma de o Python avisar que uma linha não pode ser feita. Sobe pelas funções que estão a meio até alguém a apanhar, ou até parar o programa.
- `raise`: a instrução que lança uma exceção.
- `try` e `except`: o bloco onde se espera uma exceção, e o bloco que a trata, se for do tipo indicado.
- `else` de um `try`: o bloco que corre quando o `try` acaba sem exceção.
- `finally`: o bloco que corre sempre, com ou sem exceção.
- Exceção própria: uma classe criada por ti, filha de `Exception`, com um nome que diz o problema.
- Tuplo: um conjunto de valores entre parênteses, separados por vírgulas, que se lê pela posição e não se muda depois de criado. Um tuplo com dois valores chama-se par.
- Desempacotar: repartir os valores de um tuplo por vários nomes, como em `for nome, texto_do_nivel in pedidos:`.
- `isinstance`: a função que pergunta se um objeto é de uma classe, ou de uma classe-filha dela, e devolve `True` ou `False`.
- Sintoma: o que se vê de um erro, como uma mensagem ou um valor errado.
- Causa: a linha de código que está mal e que provoca o sintoma.
- Depurar: encontrar a causa de um erro a partir do sintoma.
- Hipótese: uma frase que diz o que achas que está a acontecer, e que os valores do programa podem confirmar ou desmentir.
- Erro de escrita: um erro que o Python recusa antes de o programa correr.
- Erro de execução: um erro que para o programa a meio, com uma mensagem.
- Erro de lógica: um erro em que o programa corre até ao fim e dá o resultado errado.
- Traceback: a mensagem de erro completa, com o caminho de chamadas até à linha onde a exceção rebentou.
- Andar: cada par de linhas `File` de um traceback, com o ficheiro, a linha, a função e o código.
- Pilha de chamadas: a lista das funções e dos métodos que estão a meio, cada um à espera do que chamou. Em inglês, call stack.
- Depurador: a ferramenta que corre o programa e o deixa parar, para ver as variáveis e avançar linha a linha.
- Ponto de paragem: uma linha onde o depurador para antes de a executar. Em inglês, breakpoint.
- Logging: o registo do que um programa faz, escrito para quem o mantém.
- Logger: o objeto que escreve as mensagens do registo, com um nome que diz de onde vieram.
- Nível: a importância de uma mensagem do registo: `DEBUG`, `INFO`, `WARNING`, `ERROR` ou `CRITICAL`.
- `basicConfig`: a chamada que configura o registo do programa inteiro, com o nível mínimo, o formato das linhas e, se for preciso, o ficheiro.

## Verificar o que aprendeste

### Exceções

1. No primeiro programa da secção "Uma recusa que ninguém ouve", porque é que aparece "Bulbasaur capturado." se o Bulbasaur não foi capturado?
2. No `capturar` com `raise`, porque é que o `raise` tem de vir antes do `append`? O que acontecia à equipa se viesse depois?
3. Para que serve o `else` de um `try`? Porque não se põe simplesmente essa linha dentro do `try`?
4. A `EquipaCheia` e a `SemPokemonComVida` são filhas de `ErroDoGinasio`. Escreve dois `except` para um programa que quer mostrar "Liberta um Pokémon primeiro." quando a equipa está cheia, e a mensagem da exceção para qualquer outro erro do ginásio. Por que ordem ficam?
5. Porque é que o `capturar` lança a exceção, em vez de escrever ele próprio a mensagem no ecrã?

### Encontrar a causa de um erro

1. No traceback do Ash, porque é que nenhum dos três andares é a linha que está mal? Onde está a causa?
2. O que quer dizer "most recent call last"? Em que andar está a função onde o erro rebentou?
3. No exemplo guiado, porque é que a hipótese se escreve antes de abrir o depurador?
4. Que diferença há entre o F10 e o F11? Numa linha `dano = self.calcular_dano(alvo)`, qual usavas para ver o que o `calcular_dano` faz?
5. Na etapa 5 do exemplo guiado, que linha da tabela confirmou a hipótese, e porquê?

### Logging

1. Porque é que o combate continua a ser mostrado com `print`, e o início e o fim do combate vão para o registo?
2. Com o nível `WARNING`, que mensagens do ginásio aparecem? E com o nível `DEBUG`?
3. Porque é que o `basicConfig` está no programa principal, e não no `ginasio.py`?
4. Uma captura recusada por equipa cheia é um `WARNING` ou um `ERROR`? Defende uma das respostas, e diz em que situação mudavas de ideia.
5. O que está mal na linha `logger.info(f"{self.nome} tentou entrar com o código {codigo}.")`? Como a reescrevias?

## O que vem a seguir

Para praticar este tema, faz o [laboratório](04-excecoes-depuracao-e-logging-laboratorio.md) e depois a [ficha de exercícios](04-excecoes-depuracao-e-logging-exercicios.md). No laboratório, acrescentas ao teu ginásio as exceções do `erros.py` e o registo, e investigas com o depurador um erro de cálculo noutro tipo de Pokémon. A ficha tem exercícios sobre exceções, sobre encontrar a causa de um erro e sobre logging, para fazeres sem ajuda.

O tema seguinte é o dos testes com pytest. Até aqui, para saber se o ginásio funciona, executavas um programa e comparavas a saída com a tua previsão. Com os testes, essa comparação passa a ser feita por código. Uma das primeiras coisas que vais testar é que o `capturar` lança mesmo a `EquipaCheia` quando a equipa está cheia.

![Rodapé](../imagens/rodape.png)
