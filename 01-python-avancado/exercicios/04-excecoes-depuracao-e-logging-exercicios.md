![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Exceções, depuração e logging

Praticas o `raise` e o `try`, a leitura de um traceback, a procura da causa de um erro com o depurador e o que um programa escreve no registo. Os exercícios 1 a 8 são obrigatórios. Cada exercício fica num ficheiro com o número dele no nome, como `exercicio1.py`, na pasta da ficha, a não ser que o enunciado lhe dê outro nome. As explicações que um exercício pedir ficam num comentário, no ficheiro dele. Para rever: o [guia do tema](../04-excecoes-depuracao-e-logging.md) e o [laboratório](../laboratorios/04-excecoes-depuracao-e-logging-laboratorio.md).

## O cenário

Os exercícios usam os Pokémon das aulas. Cria uma pasta para a ficha e copia para lá o [pokemon.py](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/pokemon.py), o [ginasio.py](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) e o [erros.py](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/erros.py) dos exemplos. Os programas que importam do `pokemon.py` ou do `ginasio.py` só correm nessa pasta.

## Exceções

### Exercício 1: O caminho de um try

Num Centro Pokémon, as poções do dia são divididas pelos treinadores que lá estão. O número de poções chega em texto, como o que o `input` lê. O operador `//` é a divisão inteira do 10.º ano, e dividir por zero lança um `ZeroDivisionError`.

```python
# Exercício 1: as poções do dia divididas pelos treinadores do Centro.
def dividir_pocoes(texto_das_pocoes, treinadores):
    """Divide as poções pelos treinadores e devolve quantas recebe cada um."""
    try:
        cada_um = int(texto_das_pocoes) // treinadores
    except ZeroDivisionError:
        print("Não há treinadores.")
        return 0
    else:
        print(f"Cada treinador recebe {cada_um}.")
        return cada_um
    finally:
        print("Fim da divisão.")


print(dividir_pocoes("10", 3))
print(dividir_pocoes("10", 0))
try:
    print(dividir_pocoes("dez", 3))
except ValueError:
    print("Pedido recusado: as poções não vêm em algarismos.")
```

Descobre, sem executar, o que o programa mostra, e confirma executando. Cada linha em que falhaste leva um comentário com a razão.

Rever: [finally: o que corre sempre](../04-excecoes-depuracao-e-logging.md#finally-o-que-corre-sempre).

<details>
<summary>Pista</summary>

Na terceira chamada, procura a linha do `try` que falha e a classe da exceção que ela lança. Algum `except` da função é dessa classe?

</details>

### Exercício 2: Uma baga que recusa a cura errada

Escreve a classe `Baga`, que recebe o nome e a cura quando é criada. A cura vai de 1 a 50, e uma baga pedida com outra cura não é criada: o construtor lança um `ValueError`. A mensagem diz a regra, o nome e a cura pedida, como "A cura de uma baga vai de 1 a 50, e a Baga Gigante pedia 80.".

Linhas de teste, no fim do ficheiro:

```python
def pedir_baga(nome, cura):
    """Tenta criar a baga e diz se foi criada ou recusada."""
    try:
        baga = Baga(nome, cura)
    except ValueError as erro:
        print(f"Recusada: {erro}")
    else:
        print(f"Criada: {baga.nome}, que cura {baga.cura}.")


pedir_baga("Baga Oran", 10)
pedir_baga("Baga Gigante", 80)
pedir_baga("Baga Seca", 0)
pedir_baga("Baga Mínima", 1)
pedir_baga("Baga Máxima", 50)
```

O teste deve mostrar:

```text
Criada: Baga Oran, que cura 10.
Recusada: A cura de uma baga vai de 1 a 50, e a Baga Gigante pedia 80.
Recusada: A cura de uma baga vai de 1 a 50, e a Baga Seca pedia 0.
Criada: Baga Mínima, que cura 1.
Criada: Baga Máxima, que cura 50.
```

No tema 03, o set da vida corrigia um valor fora dos limites, e a `Baga` recusa-o. Pensa em dois casos: um ataque que deixaria a vida de um Pokémon em -20, e uma baga pedida com cura 80. Em qual dos dois corrigias o valor, e em qual o recusavas? Explica porquê num comentário.

Rever: [raise: uma recusa que não se pode ignorar](../04-excecoes-depuracao-e-logging.md#raise-uma-recusa-que-não-se-pode-ignorar), [A recusa vem antes da mudança](../04-excecoes-depuracao-e-logging.md#a-recusa-vem-antes-da-mudança) e, no guia 03, [Propriedades: o get e o set com cara de atributo](../03-objetos-e-composicao.md#propriedades-o-get-e-o-set-com-cara-de-atributo).

<details>
<summary>Pista</summary>

Escreve primeiro, numa frase, quando é que uma cura está fora do intervalo, e só depois a condição. Se a Baga Mínima ou a Baga Máxima forem recusadas, olha para os sinais da tua condição.

</details>

### Exercício 3: Os except da loja

A loja Pokémon tem três exceções próprias, filhas de uma classe-mãe comum, e uma função que as lança:

```python
# Exercício 3: a loja Pokémon, com três exceções próprias e uma compra.
class ErroDaLoja(Exception):
    """Classe-mãe dos erros da loja Pokémon."""


class SemDinheiro(ErroDaLoja):
    """O treinador não tem dinheiro para a compra."""


class Esgotado(ErroDaLoja):
    """O artigo acabou."""


class PrecoErrado(ErroDaLoja):
    """O artigo tem um preço que não pode ser."""


def comprar(artigo, preco, stock, dinheiro):
    """Devolve o dinheiro que sobra depois da compra, ou lança um erro da loja."""
    if preco <= 0:
        raise PrecoErrado(f"{artigo} tem um preço errado: {preco} moedas.")
    if stock == 0:
        raise Esgotado(f"Já não há {artigo} na loja.")
    if dinheiro < preco:
        raise SemDinheiro(f"Faltam {preco - dinheiro} moedas para {artigo}.")
    return dinheiro - preco
```

Escreve a função `pedir(artigo, preco, stock, dinheiro)`, que tenta a compra com o `comprar` e escreve o resultado. Quando falta dinheiro, escreve "Junta mais moedas e volta.". Com qualquer outro erro da loja, escreve "Erro da loja:" e a mensagem da exceção. Quando a compra corre bem, escreve o artigo e o dinheiro que sobra.

Linhas de teste, no fim do ficheiro:

```python
pedir("Poção", 20, 5, 100)
pedir("Pokébola", 200, 3, 100)
pedir("Super Poção", 70, 0, 100)
pedir("Pokébola Dourada", 0, 2, 100)
```

O teste deve mostrar:

```text
Compra feita: Poção. Sobram 80 moedas.
Junta mais moedas e volta.
Erro da loja: Já não há Super Poção na loja.
Erro da loja: Pokébola Dourada tem um preço errado: 0 moedas.
```

Rever: [Apanhar a recusa: try, except e else](../04-excecoes-depuracao-e-logging.md#apanhar-a-recusa-try-except-e-else) e [Os except pela ordem errada](../04-excecoes-depuracao-e-logging.md#os-except-pela-ordem-errada).

<details>
<summary>Pista</summary>

Se a Pokébola mostra "Erro da loja", segue os teus `except` pela ordem em que o Python os experimenta.

</details>

## Depurar

### Exercício 4: Ler um traceback

Este é o programa do ficheiro `cerulean.py`:

```python
# cerulean.py: um combate no ginásio de Cerulean, com um erro de propósito.
from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])
cerulean = Ginasio(misty, "Cerulean")
cerulean.combater(ash)
```

Quando se executa, o Python escreve isto:

```text
Traceback (most recent call last):
  File "cerulean.py", line 8, in <module>
    cerulean.combater(ash)
    ~~~~~~~~~~~~~~~~~^^^^^
  File "ginasio.py", line 141, in combater
    defensor = self.lider.escolher_pokemon()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'escolher_pokemon'
```

Responde num comentário, no fim do `cerulean.py`: em que método e em que linha rebentou o erro, e o que era o `self.lider` nessa linha. Diz também em que linha do `cerulean.py` está a causa, e corrige-a. O programa passa a mostrar o combate, que acaba com a linha `Starmie está KO (0/150).`.

Rever: [Ler um traceback com três andares](../04-excecoes-depuracao-e-logging.md#ler-um-traceback-com-três-andares) e [Um erro que rebenta longe da causa](../04-excecoes-depuracao-e-logging.md#um-erro-que-rebenta-longe-da-causa).

<details>
<summary>Pista</summary>

O andar de baixo está certo. Procura, no `ginasio.py`, a linha que dá valor ao `self.lider`, e pergunta de onde veio esse valor.

</details>

### Exercício 5: Uma hipótese antes do depurador

O Centro Pokémon trata primeiro o Pokémon mais ferido de cada equipa, entre os que ainda podem lutar. A função `mais_ferido` devia encontrá-lo:

```python
# Exercício 5: o Pokémon mais ferido de uma equipa. Tem um erro de propósito.
from pokemon import PokemonAgua, PokemonPlanta


def mais_ferido(equipa):
    """Devolve o Pokémon com menos vida entre os que ainda podem lutar, ou None se estão todos KO."""
    escolhido = equipa[0]
    for pokemon in equipa:
        if pokemon.vida > 0:
            if pokemon.vida < escolhido.vida:
                escolhido = pokemon
    return escolhido


equipa_da_misty = [PokemonAgua("Staryu", 60, 20), PokemonAgua("Starmie", 90, 35), PokemonAgua("Psyduck", 40, 20)]
equipa_da_erika = [PokemonPlanta("Oddish", 0, 20, 10), PokemonPlanta("Tangela", 80, 25, 10), PokemonPlanta("Gloom", 50, 25, 10)]
print(mais_ferido(equipa_da_misty).nome)
print(mais_ferido(equipa_da_erika).nome)

# 1. O caso, o esperado, o obtido e o tipo de erro:
# 2. A hipótese, escrita antes de abrires o depurador:
# 3. O que o depurador mostrou:
# 4. O que mudaste:
# 5. Os dois casos, depois da correção:
```

Encontra a causa com o depurador e corrige-a. A investigação segue a rotina dos cinco passos, no comentário do fim do ficheiro, que já tem um título para cada passo. No passo 3, escreve uma linha por volta do ciclo, no caso que falha, com o nome do `pokemon` e o do `escolhido` no início da volta.

Rever: [A rotina dos cinco passos](../04-excecoes-depuracao-e-logging.md#a-rotina-dos-cinco-passos), [O depurador para num ponto de paragem](../04-excecoes-depuracao-e-logging.md#o-depurador-para-num-ponto-de-paragem) e [Exemplo guiado: o dano a dobrar](../04-excecoes-depuracao-e-logging.md#exemplo-guiado-o-dano-a-dobrar).

<details>
<summary>Pista</summary>

Põe o ponto de paragem na primeira linha dentro do `for`: com o programa parado, o F5 continua até à volta seguinte. Quando o `escolhido` já é um Pokémon, abre-o com a seta, no painel das variáveis, para veres o nome e a vida.

</details>

## O registo

### Exercício 6: Escolher o nível

O programa de um Centro Pokémon escreve no registo o que acontece. Para cada acontecimento da tabela, escolhe o nível da mensagem: `DEBUG`, `INFO`, `WARNING`, `ERROR` ou `CRITICAL`. Justifica cada escolha num comentário, numa frase. Diz se o programa fez o que queria fazer e se continuou, e quem precisa de saber, com que urgência.

| | Acontecimento |
| --- | --- |
| a) | A vida de um Pokémon depois de cada poção, uma linha por poção |
| b) | Um treinador pediu o tratamento de um Pokémon que não está na lista de espera, e o programa passou ao pedido seguinte |
| c) | O talão de um tratamento não se imprimiu, porque a impressora está sem papel, e o Pokémon foi tratado na mesma |
| d) | A máquina que cura os Pokémon deixou de responder, e o programa não consegue tratar mais nenhum |

Rever: [Os cinco níveis](../04-excecoes-depuracao-e-logging.md#os-cinco-níveis).

<details>
<summary>Pista</summary>

Para cada acontecimento, pergunta primeiro se o programa fez o que queria fazer, e só depois se continuou.

</details>

### Exercício 7: De print para o registo

Esta função trata uma lista de Pokémon, e tem `print` espalhados, que alguém pôs para perceber o que ela fazia:

```python
# centro.py: o tratamento dos Pokémon do Centro, com print espalhados.
def tratar(pokemons, cura):
    """Cura cada Pokémon da lista e devolve quantos ficaram com a vida cheia."""
    print("a começar o tratamento")
    cheios = 0
    for pokemon in pokemons:
        print(pokemon.nome, "tinha", pokemon.vida)
        if pokemon.vida == 0:
            print(pokemon.nome, "estava KO e não pode ser tratado")
            continue
        pokemon.vida = pokemon.vida + cura
        if pokemon.vida == 150:
            cheios = cheios + 1
    print("Tratamento acabado:", cheios, "com a vida cheia")
    return cheios
```

Cria o `centro.py` com esta função e troca cada `print` por uma mensagem do registo, num logger com o nome `"centro"`, com o nível que a mensagem merece. As mensagens são as dos `print`, com ponto final, como o teste as mostra. O `centro.py` não configura o registo.

Testa com o `teste_centro.py`, na mesma pasta:

```python
# teste_centro.py: testa o tratamento do Centro, com o registo configurado aqui.
import logging

from pokemon import PokemonAgua, PokemonFogo
from centro import tratar

logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")
equipa = [PokemonAgua("Squirtle", 120, 30), PokemonFogo("Charmander", 0, 40), PokemonAgua("Psyduck", 50, 20)]
print(tratar(equipa, 50))
```

O teste deve mostrar:

```text
centro: Charmander estava KO e não pode ser tratado.
centro: Tratamento acabado: 1 com a vida cheia.
1
```

Com `level=logging.WARNING` no teste, fica só a mensagem do KO:

```text
centro: Charmander estava KO e não pode ser tratado.
1
```

Com `level=logging.DEBUG`, aparecem também as mensagens dos outros dois `print`: a do começo e uma por Pokémon.

Rever: [O ginásio escreve no registo](../04-excecoes-depuracao-e-logging.md#o-ginásio-escreve-no-registo) e [Quem configura é o programa](../04-excecoes-depuracao-e-logging.md#quem-configura-é-o-programa).

<details>
<summary>Pista</summary>

Se uma linha aparece com `root` no lugar de `centro`, não foi o logger do `centro.py` que a escreveu. Se aparece um bloco `--- Logging error ---`, compara a forma como o `print` recebe os valores com a forma como o logger os recebe.

</details>

### Exercício 8: O que não se regista

Estas linhas são do registo de uma aplicação de trocas de Pokémon entre jogadores reais. Os dados são inventados, mas imagina que eram verdadeiros:

```text
[INFO] trocas: O jogador 2210 propôs uma troca ao jogador 3051: Pikachu por Eevee.
[INFO] trocas: O jogador 3051 confirmou a idade para trocar: nasceu a 14/03/2011.
[INFO] trocas: O jogador 3051 recusou a troca, com a mensagem "hoje não, estou de castigo até sexta".
[WARNING] trocas: O jogador 2210 falhou o código de acesso 3 vezes seguidas, e a conta fica bloqueada 10 minutos.
```

Num ficheiro só com comentários, diz se cada linha pode ficar no registo tal como está, e porquê. Reescreve as que não podem ficar, de forma que quem mantém a aplicação continue a saber o que aconteceu.

Rever: [O que nunca se regista](../04-excecoes-depuracao-e-logging.md#o-que-nunca-se-regista).

<details>
<summary>Pista</summary>

Lê cada linha como se fosse publicada. A pessoa de quem se fala gostava de a ver lá? E quem mantém a aplicação precisa daquele pormenor para perceber o que aconteceu?

</details>

## Desafios

### Desafio 1: A sala que ficou ocupada

O Centro Pokémon tem uma sala de treino que só recebe um treinador de cada vez. Quando um treinador entra, a sala fica ocupada por ele, e quando sai, fica livre. Quem decide se um Pokémon pode treinar é o próprio Pokémon: o método `treinar` lança `SemEnergia` quando a energia não chega para um treino.

Copia este programa para um ficheiro `sala_de_treino.py`:

```python
# sala_de_treino.py: a sala de treino do Centro Pokémon. Tem um erro de propósito.
ENERGIA_POR_TREINO = 30


class ErroDoCentro(Exception):
    """Classe-mãe dos erros do Centro Pokémon."""


class SalaOcupada(ErroDoCentro):
    """Um treinador tentou entrar na sala de treino com ela ocupada."""


class SemEnergia(ErroDoCentro):
    """Um Pokémon não tem energia para treinar."""


class PokemonEmTreino:
    """Um Pokémon que sobe um nível em cada treino e gasta energia."""

    def __init__(self, nome, energia):
        """Cria o Pokémon no nível 1, com a energia dada."""
        self.nome = nome
        self.energia = energia
        self.nivel = 1

    def treinar(self):
        """Gasta a energia de um treino e sobe um nível; sem energia, lança SemEnergia."""
        if self.energia < ENERGIA_POR_TREINO:
            raise SemEnergia(f"{self.nome} só tem {self.energia} de energia, e um treino gasta {ENERGIA_POR_TREINO}.")
        self.energia = self.energia - ENERGIA_POR_TREINO
        self.nivel = self.nivel + 1


class SalaDeTreino:
    """A sala de treino do Centro Pokémon, que só recebe um treinador de cada vez."""

    def __init__(self):
        """Cria a sala vazia."""
        self.ocupada_por = None

    def usar(self, treinador, pokemon):
        """O treinador entra, o Pokémon treina, e o treinador sai."""
        if self.ocupada_por is not None:
            raise SalaOcupada(f"{treinador} não pode entrar: a sala está ocupada por {self.ocupada_por}.")
        self.ocupada_por = treinador
        print(f"{treinador} entra na sala.")
        pokemon.treinar()
        print(f"{pokemon.nome} subiu para o nível {pokemon.nivel}.")
        self.ocupada_por = None
        print(f"{treinador} sai da sala.")


def pedir_treino(sala, treinador, pokemon):
    """Pede a sala para o treino e escreve a recusa, se a houver."""
    try:
        sala.usar(treinador, pokemon)
    except ErroDoCentro as erro:
        print(f"Recusado: {erro}")


sala = SalaDeTreino()
pedir_treino(sala, "Ash", PokemonEmTreino("Pikachu", 50))
pedir_treino(sala, "Brock", PokemonEmTreino("Onix", 10))
pedir_treino(sala, "Misty", PokemonEmTreino("Staryu", 40))
print(f"Quem está na sala: {sala.ocupada_por}")
# O Gary está a treinar quando a Erika chega.
sala.ocupada_por = "Gary"
pedir_treino(sala, "Erika", PokemonEmTreino("Oddish", 40))
print(f"Quem está na sala: {sala.ocupada_por}")
```

**a)** Descobre, sem executar, as linhas que o programa escreve, e confirma executando, com um comentário para cada linha em que falhaste. Explica também o sintoma e a causa do erro: que linhas do `usar` não chegaram a correr, e porquê?

**b)** Corrige o método `usar` com um `finally`, para que o treinador saia e a sala fique livre, quer o treino corra bem, quer corra mal. O `usar` não trata o erro do treino: o "Recusado" continua a ser escrito pelo `pedir_treino`. Um `try` pode ter só o `finally`, sem `except`. Muda só o `usar`. O programa passa a mostrar:

```text
Ash entra na sala.
Pikachu subiu para o nível 2.
Ash sai da sala.
Brock entra na sala.
Brock sai da sala.
Recusado: Onix só tem 10 de energia, e um treino gasta 30.
Misty entra na sala.
Staryu subiu para o nível 2.
Misty sai da sala.
Quem está na sala: None
Recusado: Erika não pode entrar: a sala está ocupada por Gary.
Quem está na sala: Gary
```

<details>
<summary>Pista</summary>

Procura as linhas do `usar` que fazem o treinador sair da sala. Em que casos têm de correr, e em que casos não podem correr?

</details>

### Desafio 2: As inscrições na Liga

Queremos as inscrições numa Liga Pokémon, num ficheiro `liga.py`. A Liga tem um número de vagas, que recebe quando é criada, e a lista dos nomes inscritos, que começa vazia. As inscrições começam abertas.

Deves poder:

- inscrever um treinador pelo nome, com o método `inscrever(nome)`;
- fechar as inscrições, com o método `fechar()`.

O programa recusa, sem mudar nada, com uma exceção da família `ErroDaLiga`, filha de `Exception`:

- uma inscrição depois de as inscrições fecharem, com `InscricaoFechada`;
- um nome que já está na lista, mesmo escrito com outras maiúsculas e minúsculas, como `"ash"` com o Ash inscrito, com `NomeRepetido`;
- uma inscrição sem vagas, com `LigaCheia`.

Cada inscrição e o fecho ficam no registo, com o nível `INFO`, num logger com o nome `"liga"`. O `liga.py` não configura o registo. As mensagens são as do teste.

Testa com este programa, num ficheiro à parte:

```python
# teste_liga.py: testa as inscrições na Liga, com três vagas e seis pedidos.
import logging

from liga import ErroDaLiga, Liga, NomeRepetido

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("inscricoes")

liga = Liga(3)
for nome in ["Ash", "Misty", "ash", "Brock", "Gary"]:
    try:
        liga.inscrever(nome)
    except NomeRepetido as erro:
        logger.warning(f"Pedido repetido: {erro}")
    except ErroDaLiga as erro:
        logger.warning(f"Inscrição recusada: {erro}")
liga.fechar()
try:
    liga.inscrever("Erika")
except ErroDaLiga as erro:
    logger.warning(f"Inscrição recusada: {erro}")
print(liga.inscritos)
```

O teste deve mostrar:

```text
[INFO] liga: Ash entra na Liga (1/3).
[INFO] liga: Misty entra na Liga (2/3).
[WARNING] inscricoes: Pedido repetido: ash já está na lista.
[INFO] liga: Brock entra na Liga (3/3).
[WARNING] inscricoes: Inscrição recusada: Não há vagas para Gary.
[INFO] liga: Inscrições fechadas.
[WARNING] inscricoes: Inscrição recusada: As inscrições fecharam: Erika ficou de fora.
['Ash', 'Misty', 'Brock']
```

<details>
<summary>Pista</summary>

Repara no número de inscritos na mensagem de cada inscrição: quando a mensagem é escrita, o nome já está na lista? Para o `"ash"`, pensa numa forma de pôr os dois nomes iguais antes de os comparar.

</details>

### Desafio 3: A volta estragada

Um jogo de corridas guarda o tempo de cada volta em segundos, escrito em texto. Num ficheiro `corridas.py`, escreve a função `melhor_volta(tempos)`, que recebe a lista dos tempos e devolve o menor. Um tempo que não é um número, como `"1:23"`, fica de fora, e a corrida continua com as outras voltas. Quem mantém o jogo encontra o erro no registo, com o traceback, num logger com o nome `"corridas"`. O `corridas.py` não configura o registo.

Testa com o `teste_corridas.py`, na mesma pasta:

```python
# teste_corridas.py: testa a melhor volta, com uma volta estragada.
import logging

from corridas import melhor_volta

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")
tempos = ["1:23", "95", "88", "102"]
print(f"Melhor volta: {melhor_volta(tempos)} segundos.")
```

O teste deve mostrar, por esta ordem:

- a linha `[ERROR] corridas: Tempo inválido, deixado de fora: 1:23.`;
- por baixo, o traceback, com o andar do teu `melhor_volta` e a última linha `ValueError: invalid literal for int() with base 10: '1:23'`;
- a linha `Melhor volta: 88 segundos.`.

Rever: [Registar uma exceção apanhada](../04-excecoes-depuracao-e-logging.md#registar-uma-exceção-apanhada).

<details>
<summary>Pista</summary>

Se a melhor volta sair 0 ou `None`, ou se o programa parar com outro erro, olha para o `except`. O que faz ele à volta estragada, além de a registar?

</details>

## Critérios de conclusão

- Os exercícios 2, 3 e 7 correm e mostram exatamente o que o enunciado diz.
- Depois de corrigidos, o exercício 4 mostra o combate de Cerulean, e o 5 encontra o Pokémon mais ferido das duas equipas.
- No exercício 1, cada linha que falhaste tem um comentário com a razão.
- O comentário do fim do exercício 5 tem os cinco passos, com a hipótese escrita antes de abrires o depurador.
- As explicações dos exercícios 2 e 4 e as escolhas dos exercícios 6 e 8 estão em comentários, e cada nível do exercício 6 tem a sua justificação.

![Rodapé](../../imagens/rodape.png)
