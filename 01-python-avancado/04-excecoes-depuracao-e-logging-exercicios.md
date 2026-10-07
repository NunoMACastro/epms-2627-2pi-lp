![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Exceções, depuração e logging

## Objetivos e organização

Esta ficha serve para praticares sem ajuda o que o [guia](04-excecoes-depuracao-e-logging.md) explica. Está dividida em três grupos, um por cada parte do guia, e cada grupo só precisa da parte que lhe corresponde.

Cada exercício treina uma coisa só, e o enunciado diz qual é. O primeiro exercício de cada grupo é o mais próximo do guia, e os seguintes pedem-te uma decisão pequena que o guia não tomou por ti. O desafio, no fim, é opcional.

| Grupo | Parte do guia | Exercícios | Tempo |
| --- | --- | --- | ---: |
| Exceções | Parte 1 | 1, 2 e 3 | 40 min |
| Encontrar a causa de um erro | Parte 2 | 4 e 5 | 25 min |
| Logging | Parte 3 | 6, 7 e 8 | 35 min |
| Desafio opcional | Partes 1 e 3 | | 30 min |

Os tempos são para quem leu a parte do guia antes de começar o grupo.

## Antes de começar

Material: o computador com o Python 3 e o VS Code, e o guia aberto ao lado.

Cria uma pasta para esta ficha e copia para lá os quatro ficheiros da pasta [04-excecoes-depuracao-e-logging dos exemplos](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/): o `pokemon.py`, o `ginasio.py`, o `erros.py` e o `anunciadores.py`. Vários exercícios usam as classes desses ficheiros.

As regras são as das fichas anteriores. Quando um exercício pedir uma previsão, escreve-a antes de executar. Quando pedir uma explicação, responde em frases completas, com as tuas palavras.

## Exceções

### Exercício 1: Prever o caminho de um try (10 min)

Treina: seguir um `try` com `except`, `else` e `finally` (guia, [Apanhar a recusa: try, except e else](04-excecoes-depuracao-e-logging.md#apanhar-a-recusa-try-except-e-else) e [finally: o que corre sempre](04-excecoes-depuracao-e-logging.md#finally-o-que-corre-sempre)).

Num Centro Pokémon, as poções do dia são divididas pelos treinadores que lá estão. O operador `//` é a divisão inteira, que usaste no 10.º ano, e dividir por zero lança um `ZeroDivisionError`.

```python
def dividir_pocoes(pocoes, treinadores):
    try:
        cada_um = pocoes // treinadores
    except ZeroDivisionError:
        print("Não há treinadores.")
        return 0
    else:
        print(f"Cada treinador recebe {cada_um}.")
        return cada_um
    finally:
        print("Divisão feita.")


print(dividir_pocoes(10, 3))
print(dividir_pocoes(10, 0))
```

**a)** Sem executar, escreve as seis linhas que o programa mostra.

**b)** O `else` e o `except` têm os dois um `return`, e mesmo assim aparece "Divisão feita." nas duas chamadas. Porquê? Em que ordem aparecem a mensagem do `finally` e o número que a função devolve?

**c)** Executa e compara. Se falhaste alguma linha, diz em que parte do `try` o teu raciocínio se afastou do programa.

### Exercício 2: Uma regra que recusa a sério (15 min)

Treina: lançar uma exceção quando um valor não respeita uma regra (guia, [raise: uma recusa que não se pode ignorar](04-excecoes-depuracao-e-logging.md#raise-uma-recusa-que-não-se-pode-ignorar)).

Nas fichas do tema 03, a cura de uma baga ia de 1 a 50. Escreve uma classe `Baga` cujo construtor recebe o nome e a cura, e que lança um `ValueError` quando a cura está fora desse intervalo, antes de guardar qualquer atributo. A mensagem é "A cura de uma baga vai de 1 a 50, e a Baga Gigante pedia 80.", com o nome e a cura pedidos.

Testa com estas linhas, no fim do ficheiro:

```python
pedidos = [("Baga Oran", 10), ("Baga Gigante", 80), ("Baga Seca", 0), ("Baga Sitrus", 30)]
bagas = []
for nome, cura in pedidos:
    try:
        baga = Baga(nome, cura)
    except ValueError as erro:
        print(f"Recusada: {erro}")
    else:
        bagas.append(baga)
        print(f"Criada: {baga.nome}")
print(len(bagas))
```

Quando a classe estiver certa, o teste mostra:

```text
Criada: Baga Oran
Recusada: A cura de uma baga vai de 1 a 50, e a Baga Gigante pedia 80.
Recusada: A cura de uma baga vai de 1 a 50, e a Baga Seca pedia 0.
Criada: Baga Sitrus
2
```

Depois de o teste funcionar, responde: no tema 03, a propriedade da vida corrigia os valores fora dos limites, e o 500 passava a 150. Aqui, a baga com 80 é recusada. Em que situação preferias cada uma das duas formas?

### Exercício 3: A ordem dos except (15 min)

Treina: escolher a ordem dos `except` numa família de exceções (guia, [Uma família de exceções](04-excecoes-depuracao-e-logging.md#uma-família-de-exceções) e [Erros frequentes com exceções](04-excecoes-depuracao-e-logging.md#erros-frequentes-com-exceções)).

A loja Pokémon tem duas exceções próprias, filhas de uma classe-mãe comum, e uma função que as lança:

```python
class ErroDaLoja(Exception):
    """Classe-mãe dos erros da loja Pokémon."""


class SemDinheiro(ErroDaLoja):
    """O treinador não tem dinheiro para a compra."""


class Esgotado(ErroDaLoja):
    """O artigo acabou."""


def comprar(artigo, preco, stock, dinheiro):
    """Devolve o dinheiro que sobra depois da compra, ou lança um erro da loja."""
    if stock == 0:
        raise Esgotado(f"{artigo} esgotado.")
    if dinheiro < preco:
        raise SemDinheiro(f"Faltam {preco - dinheiro} moedas para {artigo}.")
    return dinheiro - preco


compras = [("Poção", 20, 5, 100), ("Pokébola", 200, 3, 100), ("Super Poção", 70, 0, 100)]
for artigo, preco, stock, dinheiro in compras:
    try:
        sobra = comprar(artigo, preco, stock, dinheiro)
        print(f"{artigo} comprado. Sobram {sobra} moedas.")
    except ErroDaLoja as erro:
        print(f"Erro da loja: {erro}")
    except SemDinheiro:
        print("Junta mais moedas e volta.")
```

**a)** Sem executar, escreve as três linhas que o programa mostra. A frase "Junta mais moedas e volta." aparece alguma vez? Porquê?

**b)** Muda o `try` para que, quando falta dinheiro, apareça "Junta mais moedas e volta.", e, para qualquer outro erro da loja, a mensagem da exceção. Muda também o `print` da compra feita para um `else`. Quando estiver certo, o programa mostra:

```text
Poção comprado. Sobram 80 moedas.
Junta mais moedas e volta.
Erro da loja: Super Poção esgotado.
```

**c)** A Super Poção custa 70 e o treinador tem 100, mas a compra foi recusada por estar esgotada. Se o stock fosse 0 e o dinheiro não chegasse, qual das duas exceções era lançada? O que decide isso na função?

## Encontrar a causa de um erro

### Exercício 4: Ler um traceback (10 min)

Treina: ler um traceback de cima para baixo e encontrar a causa (guia, [Ler um traceback com três andares](04-excecoes-depuracao-e-logging.md#ler-um-traceback-com-três-andares)).

Este programa, guardado no ficheiro `liga.py`, usa o ginásio da pasta 04:

```python
from pokemon import PokemonPlanta
from ginasio import Ginasio, Treinador

ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])
cerulean = Ginasio("Cerulean", "Misty")
cerulean.combater(ash)
```

Quando se executa, o Python escreve isto:

```text
Traceback (most recent call last):
  File "liga.py", line 6, in <module>
    cerulean.combater(ash)
    ~~~~~~~~~~~~~~~~~^^^^^
  File "ginasio.py", line 141, in combater
    defensor = self.lider.escolher_pokemon()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'escolher_pokemon'
```

Responde, sem executar:

**a)** Que tipo de exceção é, e o que diz a mensagem, por palavras tuas?

**b)** Quantos andares tem o traceback? Em que função rebentou o erro, e quem a chamou?

**c)** Na linha 141 do `ginasio.py`, o que era o `self.lider`? Em que linha do `liga.py` está a causa, e como a corriges?

### Exercício 5: Uma hipótese antes do depurador (15 min)

Treina: escrever uma hipótese e confirmá-la com o depurador (guia, [Um erro tem um sintoma e uma causa](04-excecoes-depuracao-e-logging.md#um-erro-tem-um-sintoma-e-uma-causa) e [Exemplo guiado: o dano a dobrar](04-excecoes-depuracao-e-logging.md#exemplo-guiado-o-dano-a-dobrar)).

Este `Lider` devia escolher sempre o Pokémon da equipa com mais vida, como o do guia do tema 03:

```python
from pokemon import PokemonAgua


class Lider:
    """Um líder que devia escolher sempre o Pokémon com mais vida."""

    def __init__(self, nome, equipa):
        """Cria o líder com o nome e a equipa dados."""
        self.nome = nome
        self.equipa = equipa

    def escolher_pokemon(self):
        """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
        escolhido = None
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                if escolhido is None or pokemon.vida < escolhido.vida:
                    escolhido = pokemon
        return escolhido


misty = Lider("Misty", [PokemonAgua("Staryu", 60, 20), PokemonAgua("Starmie", 90, 35), PokemonAgua("Psyduck", 40, 20)])
print(misty.escolher_pokemon().nome)
```

O programa escreve `Psyduck`, e devia escrever `Starmie`.

**a)** Antes de abrires o depurador, escreve a tua hipótese: que linha achas que está mal, e o que esperas ver no `escolhido` ao longo do ciclo, se tiveres razão.

**b)** Põe um ponto de paragem na linha `if pokemon.vida > 0:` e executa com o depurador. Em cada volta do ciclo, regista o nome do `pokemon` e o nome do `escolhido`, numa tabela com uma linha por volta.

**c)** A tabela confirma a tua hipótese? Corrige a linha que está mal e confirma que o programa escreve `Starmie`.

## Logging

### Exercício 6: Escolher o nível (10 min)

Treina: escolher o nível de uma mensagem pelo que ela significa (guia, [Os cinco níveis](04-excecoes-depuracao-e-logging.md#os-cinco-níveis)).

Um programa de um Centro Pokémon regista o que acontece. Para cada acontecimento, escolhe o nível da mensagem, entre `DEBUG`, `INFO`, `WARNING`, `ERROR` e `CRITICAL`, e justifica numa frase: quem precisa de saber, e o programa continuou ou não?

| | Acontecimento |
| --- | --- |
| a) | Um Pokémon foi tratado e ficou com a vida cheia |
| b) | O valor de cada variável no início do tratamento, para quem está a procurar um erro |
| c) | Um Pokémon chegou KO e não pode ser tratado; o programa passa ao seguinte |
| d) | O ficheiro onde se guarda a lista de espera não se conseguiu escrever, e a lista de hoje perdeu-se |
| e) | O Centro abriu, às 9 horas |
| f) | O ficheiro de configuração do Centro não existe, e o programa não pode arrancar |

### Exercício 7: De print para logging (15 min)

Treina: trocar os `print` de depuração por mensagens do registo, com o nível certo (guia, [O registo do ginásio](04-excecoes-depuracao-e-logging.md#o-registo-do-ginásio) e [Quem configura é o programa](04-excecoes-depuracao-e-logging.md#quem-configura-é-o-programa)).

Esta função trata uma lista de Pokémon, e tem `print` espalhados, que alguém pôs para perceber o que ela fazia:

```python
def tratar(pokemons, cura):
    """Cura cada Pokémon da lista e devolve quantos ficaram com a vida cheia."""
    print("DEBUG: a começar o tratamento")
    cheios = 0
    for pokemon in pokemons:
        print("DEBUG:", pokemon.nome, "tinha", pokemon.vida)
        if pokemon.vida == 0:
            print("AVISO:", pokemon.nome, "estava KO e não pode ser tratado")
            continue
        pokemon.vida = pokemon.vida + cura
        if pokemon.vida == 150:
            cheios = cheios + 1
    print("Tratamento acabado:", cheios, "com a vida cheia")
    return cheios
```

Cria o ficheiro `centro.py` com esta função, e troca cada `print` por uma mensagem do registo, num logger com o nome `"centro"`. Escolhe o nível de cada uma pelo que ela significa. Escreve as mensagens com f-strings e termina cada uma com um ponto final, como "Tratamento acabado: 1 com a vida cheia.". O `centro.py` não configura o registo.

Para testar, cria o ficheiro `teste_centro.py`:

```python
import logging

from pokemon import PokemonAgua, PokemonFogo
from centro import tratar

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
equipa = [PokemonAgua("Squirtle", 120, 30), PokemonFogo("Charmander", 0, 40), PokemonAgua("Psyduck", 50, 20)]
print(tratar(equipa, 50))
```

Quando estiver certo, o teste mostra:

```text
[WARNING] centro: Charmander estava KO e não pode ser tratado.
[INFO] centro: Tratamento acabado: 1 com a vida cheia.
1
```

Depois muda o nível do `basicConfig` para `logging.DEBUG`. O teste tem de mostrar, antes da linha do aviso, três linhas de `DEBUG`: a do começo do tratamento, a do Squirtle e a do Charmander. E outra, a do Psyduck, entre o aviso e a linha do fim. Responde: porque é que o `basicConfig` está no `teste_centro.py`, e não no `centro.py`?

### Exercício 8: O que não se regista (10 min)

Treina: reconhecer dados que não podem ficar num registo (guia, [O que nunca se regista](04-excecoes-depuracao-e-logging.md#o-que-nunca-se-regista)).

Estas linhas são de um registo de uma aplicação de inscrições na Liga, com treinadores reais. Os dados da primeira linha são inventados, e o telefone está tapado, mas imagina que eram verdadeiros:

```text
[INFO] liga: Nova inscrição: Joana Silva, joana.silva@example.com, telefone 9XX XXX XXX.
[INFO] liga: Inscrição 1043 confirmada.
[WARNING] liga: Entrada falhada para a inscrição 1043 com a palavra-passe Pikachu2026.
[ERROR] liga: Não foi possível enviar o email de confirmação da inscrição 1043.
```

**a)** Para cada linha, diz se pode ficar no registo tal como está. Se não pode, diz que dado não devia estar lá e porquê.

**b)** Reescreve as linhas que não podem ficar, de forma que quem mantém a aplicação continue a saber o que aconteceu.

## Desafio opcional: as inscrições na Liga (30 min)

As inscrições numa Liga Pokémon têm três regras: não se inscreve ninguém depois de as inscrições fecharem, não se inscreve duas vezes o mesmo nome, e não se inscreve ninguém depois de as vagas acabarem.

Num ficheiro `liga.py`, escreve:

- uma família de exceções: `ErroDaLiga`, filha de `Exception`, e três filhas dela, `InscricaoFechada`, `NomeRepetido` e `LigaCheia`;
- uma classe `Liga`, cujo construtor recebe o número de vagas e começa com a lista de inscritos vazia e as inscrições abertas;
- um método `fechar`, que fecha as inscrições e regista "Inscrições fechadas.", com o nível `INFO`;
- um método `inscrever(nome)`, que lança a exceção certa quando uma das regras não deixa inscrever o treinador, e, quando deixa, junta-o aos inscritos e regista "Ash inscrito (1/3).", com o nível `INFO`, o número de inscritos e o de vagas.

O registo usa um logger com o nome `"liga"`. As mensagens das exceções são "As inscrições fecharam: Erika ficou de fora.", "Ash já está inscrito." e "Não há vagas para Gary.", com o nome do treinador.

Testa com este programa, num ficheiro à parte:

```python
import logging

from liga import ErroDaLiga, Liga, NomeRepetido

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("inscricoes")

liga = Liga(3)
for nome in ["Ash", "Misty", "Ash", "Brock", "Gary"]:
    try:
        liga.inscrever(nome)
    except NomeRepetido as erro:
        logger.warning(f"Pedido repetido: {erro}")
    except ErroDaLiga as erro:
        logger.error(f"Inscrição recusada: {erro}")
liga.fechar()
try:
    liga.inscrever("Erika")
except ErroDaLiga as erro:
    logger.error(f"Inscrição recusada: {erro}")
print(liga.inscritos)
```

Quando estiver certo, o teste mostra:

```text
[INFO] liga: Ash inscrito (1/3).
[INFO] liga: Misty inscrito (2/3).
[WARNING] inscricoes: Pedido repetido: Ash já está inscrito.
[INFO] liga: Brock inscrito (3/3).
[ERROR] inscricoes: Inscrição recusada: Não há vagas para Gary.
[INFO] liga: Inscrições fechadas.
[ERROR] inscricoes: Inscrição recusada: As inscrições fecharam: Erika ficou de fora.
['Ash', 'Misty', 'Brock']
```

Antes de escreveres o `inscrever`, decide a ordem das três verificações. Com a Liga cheia, o Ash pede para se inscrever outra vez: deve receber `NomeRepetido` ou `LigaCheia`? O teste não verifica este caso. Escreve a tua escolha e a razão, e confirma que o teu código faz o que escolheste.

## Critérios de conclusão

Concluíste a ficha quando:

- os testes dos exercícios 2, 3 e 7 mostram exatamente as linhas indicadas no enunciado;
- as tuas previsões do exercício 1 e as respostas do exercício 4 foram escritas antes de executares;
- a hipótese do exercício 5 foi escrita antes de abrires o depurador, e a tabela tem os valores que o depurador mostrou;
- as justificações dos exercícios 6 e 8 dizem quem precisa de saber e porquê, e não só o nível ou a resposta.

![Rodapé](../imagens/rodape.png)
