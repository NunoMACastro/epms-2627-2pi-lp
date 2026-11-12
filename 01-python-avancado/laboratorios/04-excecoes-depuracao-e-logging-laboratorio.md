![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Exceções, depuração e logging

## O que vais construir

Vais dar ao ginásio Pokémon do tema 03 exceções próprias para as recusas e investigar dois erros com o depurador do VS Code. Depois, o ginásio passa a escrever no registo, primeiro no ecrã e a seguir num ficheiro. No fim, a pasta tem estes ficheiros:

```text
ginasio-com-erros/
├── capturas.py
├── combates.py
├── erros.py
├── ginasio.log
├── ginasio.py
├── investigar.py
├── pilha.py
├── pokemon.py
├── registo.py
└── teste_erros.py
```

1. [Fase 1: As exceções do ginásio](#fase-1-as-exceções-do-ginásio)
2. [Fase 2: A recusa vem antes da mudança](#fase-2-a-recusa-vem-antes-da-mudança)
3. [Fase 3: finally: o que corre sempre](#fase-3-finally-o-que-corre-sempre)
4. [Fase 4: O depurador para num ponto de paragem](#fase-4-o-depurador-para-num-ponto-de-paragem)
5. [Fase 5: Um erro que rebenta longe da causa](#fase-5-um-erro-que-rebenta-longe-da-causa)
6. [Fase 6: O ginásio escreve no registo](#fase-6-o-ginásio-escreve-no-registo)
7. [Fase 7: O registo num ficheiro](#fase-7-o-registo-num-ficheiro)

## O que precisas

- O Python 3.9 ou mais recente. O comando `python3 --version` deve mostrar `Python 3.9.6` ou uma versão maior. No Windows, se o `python3` não existir, usa `python` ou `py` em todos os comandos.
- O VS Code com a extensão Python, da Microsoft, que traz o depurador. No painel Extensions, à esquerda, escreve `Python` na pesquisa: a extensão da Microsoft deve aparecer como instalada.
- O `pokemon.py` e o `ginasio.py` da [pasta 03 dos exemplos](../../exemplos/python-avancado/pokemon/03-objetos-e-composicao/), que copias em [Preparar o projeto](#preparar-o-projeto).

## Preparar o projeto

1. Cria uma pasta nova, `ginasio-com-erros`, onde guardas os trabalhos da disciplina, e abre-a no VS Code, com a opção `Open Folder...` do menu File. No menu Terminal, escolhe New Terminal e escreve `pwd`. O que deves ver: o caminho da pasta, a acabar em `ginasio-com-erros`.

2. Copia para a pasta o [`pokemon.py`](../../exemplos/python-avancado/pokemon/03-objetos-e-composicao/pokemon.py) e o [`ginasio.py`](../../exemplos/python-avancado/pokemon/03-objetos-e-composicao/ginasio.py) dos exemplos. Abre cada um e copia o conteúdo todo; no painel Explorer, cria um ficheiro com o mesmo nome, cola e guarda. Copia os dos exemplos, e não os teus do laboratório 03, para as saídas e os números das linhas serem os deste laboratório.

3. Corre o ginásio, para confirmares o ponto de partida:

   ```bash
   python3 ginasio.py
   ```

   O que deves ver: os combates do tema 03 e, na última linha, `Ash continua com 2 Pokémon; Misty continua com 1.` Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

## Fase 1: As exceções do ginásio

Crias o `erros.py`, com as três exceções do ginásio, e confirmas com o `isinstance` que formam uma família, com o `ErroDoGinasio` como classe-mãe. Rever: [As exceções do ginásio](../04-excecoes-depuracao-e-logging.md#as-exceções-do-ginásio).

1. Cria o ficheiro `erros.py`, na pasta do projeto, com este conteúdo:

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

2. Cria o ficheiro `teste_erros.py`, que pergunta ao Python se a família está certa:

   ```python
   # teste_erros.py: confirma que as exceções do ginásio formam uma família.
   from erros import EquipaCheia, ErroDoGinasio, SemPokemonComVida

   # A primeira linha pergunta se cada filha é um ErroDoGinasio; a segunda, se a mãe é uma exceção.
   print(isinstance(EquipaCheia("teste"), ErroDoGinasio), isinstance(SemPokemonComVida("teste"), ErroDoGinasio))
   print(isinstance(ErroDoGinasio("teste"), Exception))
   erro = EquipaCheia("A equipa está cheia.")
   print(erro)
   ```

   Corre `python3 teste_erros.py`. O que deves ver:

   ```text
   True True
   True
   A equipa está cheia.
   ```

   O `print` de uma exceção escreve a mensagem dela. Se aparecer um `ModuleNotFoundError` ou um `TypeError`, vê [`No module named 'erros'`](#modulenotfounderror-no-module-named-erros) ou [`EquipaCheia() takes no arguments`](#typeerror-equipacheia-takes-no-arguments).

3. Tira, de propósito, a `EquipaCheia` da família: no `erros.py`, muda a linha `class EquipaCheia(ErroDoGinasio):` para `class EquipaCheia(Exception):`. Antes de correres, prevê o que muda nas três linhas. Corre outra vez o `teste_erros.py`. O que deves ver:

   ```text
   False True
   True
   A equipa está cheia.
   ```

   A `EquipaCheia` continua a ser uma exceção, com a sua mensagem, mas já não é um `ErroDoGinasio`, e um `except ErroDoGinasio` deixava de a apanhar. Volta a pôr `ErroDoGinasio` entre os parênteses e corre outra vez: a primeira linha volta a `True True`.

### Paragem 1

O `erros.py` tem as três exceções, e o `teste_erros.py` confirma a família.

Pensa antes de continuares: a `EquipaCheia` só tem a docstring. De onde vem o que o `print(erro)` usou para escrever a mensagem? A resposta: da `Exception`, através do `ErroDoGinasio`. A classe herda tudo o que uma exceção precisa, e a forma de guardar e mostrar a mensagem vem com isso.

## Fase 2: A recusa vem antes da mudança

Pões um limite de seis Pokémon na equipa, e o `capturar` passa a recusar o sétimo com a `EquipaCheia`. O `raise` fica antes do `append`, para a recusa vir antes da mudança. Rever: [A recusa vem antes da mudança](../04-excecoes-depuracao-e-logging.md#a-recusa-vem-antes-da-mudança).

1. No `ginasio.py`, substitui a linha `from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta` por estas:

   ```python
   from erros import EquipaCheia
   from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta

   # O limite da equipa, num só sítio: a condição e a mensagem do capturar usam-no.
   TAMANHO_MAXIMO_DA_EQUIPA = 6
   ```

2. Na classe `Treinador`, substitui o método `capturar` inteiro por este, com o `def` alinhado com os outros métodos:

   ```python
       def capturar(self, pokemon):
           """Junta à equipa um Pokémon que foi criado fora do treinador.

           Se a equipa já tem TAMANHO_MAXIMO_DA_EQUIPA Pokémon, não junta nada e
           lança EquipaCheia.
           """
           # A verificação vem antes do append: com a equipa cheia, o raise para o
           # método aqui, e o Pokémon recusado nunca entra na equipa.
           if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
               raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
           self.equipa.append(pokemon)
   ```

3. Cria o ficheiro `capturas.py`, em que o Brock tenta capturar oito Pokémon para seis lugares:

   ```python
   # capturas.py: testa o limite da equipa, com oito capturas para seis lugares.
   from erros import EquipaCheia
   from pokemon import Pokemon
   from ginasio import Treinador

   brock = Treinador("Brock")
   nomes = ["Geodude", "Onix", "Graveler", "Golem", "Sandshrew", "Rhyhorn", "Kabuto", "Omanyte"]
   for nome in nomes:
       try:
           brock.capturar(Pokemon(nome, "Pedra", 50, 20))
       except EquipaCheia as erro:
           print(f"Recusado: {erro}")
       else:
           # O else só corre quando o capturar acaba sem exceção.
           print(f"{nome} capturado.")
   print(len(brock.equipa))
   ```

4. Antes de correres, prevê o número da última linha: o ciclo tenta oito capturas. Corre `python3 capturas.py`. O que deves ver:

   ```text
   Geodude capturado.
   Onix capturado.
   Graveler capturado.
   Golem capturado.
   Sandshrew capturado.
   Rhyhorn capturado.
   Recusado: Brock já tem 6 Pokémon e não pode capturar Kabuto.
   Recusado: Brock já tem 6 Pokémon e não pode capturar Omanyte.
   6
   ```

   A última linha diz 6: as duas recusas pararam o `capturar` antes do `append`, e o ciclo continuou porque o `except` as apanhou. Se aparecer um `NameError`, vê [`name 'EquipaCheia' is not defined`](#nameerror-name-equipacheia-is-not-defined).

5. Põe, de propósito, a mudança antes da recusa: no `capturar`, passa a linha `self.equipa.append(pokemon)` para logo a seguir ao comentário, por cima do `if`. Corre outra vez o `capturas.py`. O que deves ver:

   ```text
   Geodude capturado.
   Onix capturado.
   Graveler capturado.
   Golem capturado.
   Sandshrew capturado.
   Recusado: Brock já tem 6 Pokémon e não pode capturar Rhyhorn.
   Recusado: Brock já tem 6 Pokémon e não pode capturar Kabuto.
   Recusado: Brock já tem 6 Pokémon e não pode capturar Omanyte.
   8
   ```

   Cada Pokémon entra na equipa antes da verificação. O Rhyhorn é dado como recusado e ficou na equipa, que acaba com oito: a mensagem diz uma coisa e a equipa diz outra. Volta a pôr o `append` por baixo do `if` e corre outra vez: a última linha volta a 6.

### Paragem 2

O `Treinador` recusa o sétimo Pokémon com a `EquipaCheia`, e a equipa fica com seis.

Pensa antes de continuares: se o `capturar` recusasse com um `print` e um `return`, como o `combater` do tema 03, o que escrevia o `capturas.py` para o Kabuto? A resposta: `Kabuto capturado.` O `capturar` acabava sem exceção, e o `else` corria. A última linha dizia 6 na mesma, e o programa contradizia-se sem dar por isso.

## Fase 3: finally: o que corre sempre

O `combater` passa a recusar com a `SemPokemonComVida`, e um programa com três desafios escreve o estado do ginásio num `finally`, que corre sempre, haja ou não exceção. Rever: [finally: o que corre sempre](../04-excecoes-depuracao-e-logging.md#finally-o-que-corre-sempre).

1. No início do `ginasio.py`, substitui a linha `from erros import EquipaCheia` por esta:

   ```python
   from erros import EquipaCheia, SemPokemonComVida
   ```

2. Na classe `Ginasio`, no método `combater`, substitui as linhas desde `def combater(self, desafiante):` até ao `return`, inclusive, por estas. O resto do método, a partir do `print` com os sinais `===`, fica como está:

   ```python
       def combater(self, desafiante):
           """Um combate entre o Pokémon escolhido por cada treinador.

           Se um dos dois não tem Pokémon com vida, não há combate: lança
           SemPokemonComVida, e o ginásio fica como estava.
           """
           atacante = desafiante.escolher_pokemon()
           defensor = self.lider.escolher_pokemon()
           if atacante is None or defensor is None:
               raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
           # O desafiante só entra na lista depois da verificação: um combate
           # recusado deixa o ginásio como estava.
           if desafiante not in self.desafiantes:
               self.desafiantes.append(desafiante)
   ```

3. Cria o ficheiro `combates.py`. O Gary desafia a Misty duas vezes, e o Brock entra pelo meio com um Geodude sem vida nenhuma:

   ```python
   # combates.py: três desafios a Cerulean, e o estado do ginásio depois de cada um.
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
           # O finally corre no fim de cada volta, com ou sem exceção.
           print(f"Desafiantes: {len(cerulean.desafiantes)}, combates: {len(cerulean.combates)}")
   ```

4. Corre `python3 combates.py`. O que deves ver:

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

   O Brock, sem vida, e o Gary, com o Vulpix KO, são recusados, e o ginásio fica com um desafiante e um combate. Se a recusa aparecer sem a cidade, ou com os desafiantes a 2, vê [a recusa sem a cidade](#a-recusa-aparece-sem-a-cidade) ou [os desafiantes a 2](#a-linha-dos-desafiantes-diz-2-depois-do-brock).

5. Tira, de propósito, o `except`: no `combates.py`, põe um `#` no início das duas linhas do `except`, a do `except` e a do `print` por baixo dele. Antes de correres, prevê se a linha dos desafiantes ainda aparece depois do desafio do Brock, que já ninguém apanha. Corre outra vez. Depois do combate do Gary, o que deves ver é:

   ```text
   Desafiantes: 1, combates: 1
   Desafiantes: 1, combates: 1
   Traceback (most recent call last):
   ```

   E a mensagem de erro acaba nesta linha:

   ```text
   erros.SemPokemonComVida: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
   ```

   A linha dos desafiantes aparece duas vezes, a segunda já com a exceção a subir. O `finally` correu antes de a exceção parar o programa, e o terceiro desafio nunca aconteceu. Tira os dois `#` e corre outra vez: a saída volta à do passo 4.

### Paragem 3

O `Ginasio` recusa um combate sem Pokémon com vida com a `SemPokemonComVida`, e o `combates.py` mostra o estado do ginásio depois de cada desafio. O `ginasio.py` completo, como deve estar agora:

```python
"""Ginásio Pokémon: composição e agregação, o código das aulas de Python avançado.

Três classes que guardam outros objetos:

- Treinador tem uma equipa de Pokémon. É uma agregação: os Pokémon são
  criados fora do treinador e continuam a existir sem ele.
- Ginasio tem um líder e uma lista de desafiantes, que são treinadores criados
  fora (agregação), e guarda o registo dos seus combates (composição): os
  objetos Combate só são criados pelo ginásio, dentro do método combater,
  e só o ginásio os guarda.
- Combate é o registo de um combate: quem desafiou, com que Pokémon e quem
  venceu.

E três coisas que vieram depois, com as partes 5, 6 e 7 do guia:

- Lider É UM Treinador que escolhe sempre o Pokémon com mais vida. O
  Treinador tem um método de classe, com_equipa, que cria um treinador já com
  a equipa; chamado em Lider, cria um Lider.
- O Ginasio anuncia os seus combates através de um anunciador, que pode ser
  qualquer objeto com o método anunciar(combate). É o duck typing: os
  anunciadores estão no ficheiro anunciadores.py.
- Combate passou a ser uma dataclass: o @dataclass escreve o construtor, a
  forma de mostrar um registo com print e a comparação de registos com ==.

As classes de Pokémon vêm do ficheiro pokemon.py, que tem de estar na mesma
pasta que este.
"""

from dataclasses import dataclass

from erros import EquipaCheia, SemPokemonComVida
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta

# O limite da equipa, num só sítio: a condição e a mensagem do capturar usam-no.
TAMANHO_MAXIMO_DA_EQUIPA = 6


class Treinador:
    """Um treinador tem uma equipa de Pokémon (agregação)."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        # AGREGAÇÃO: a equipa começa vazia e recebe Pokémon que já existiam.
        self.equipa = []

    @classmethod
    def com_equipa(cls, nome, pokemons):
        """Cria um treinador da classe cls, já com os Pokémon da lista na equipa.

        É um construtor alternativo. Em Treinador.com_equipa(...), cls é
        Treinador; em Lider.com_equipa(...), cls é Lider, e o objeto criado
        é um Lider.
        """
        treinador = cls(nome)
        for pokemon in pokemons:
            treinador.capturar(pokemon)
        return treinador

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador.

        Se a equipa já tem TAMANHO_MAXIMO_DA_EQUIPA Pokémon, não junta nada e
        lança EquipaCheia.
        """
        # A verificação vem antes do append: com a equipa cheia, o raise para o
        # método aqui, e o Pokémon recusado nunca entra na equipa.
        if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
            raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
        self.equipa.append(pokemon)

    def escolher_pokemon(self):
        """Devolve o primeiro Pokémon da equipa que ainda pode lutar, ou None."""
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                return pokemon
        return None


class Lider(Treinador):
    """Um Lider É UM Treinador que escolhe sempre o Pokémon com mais vida."""

    def escolher_pokemon(self):
        """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
        escolhido = None
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                if escolhido is None or pokemon.vida > escolhido.vida:
                    escolhido = pokemon
        return escolhido


@dataclass
class Combate:
    """Registo de um combate. Só o ginásio cria registos (composição).

    É uma dataclass: guarda os nomes do desafiante, do seu Pokémon e do
    vencedor, e o @dataclass escreve sozinho o construtor, a forma de o
    mostrar com print e a comparação com ==.
    """

    desafiante: str
    pokemon_desafiante: str
    vencedor: str

    def resumo(self):
        """Devolve uma linha de texto que descreve o combate."""
        return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"


class Ginasio:
    """Um ginásio tem um líder e recebe desafiantes (agregação)
    e guarda o registo dos seus combates (composição)."""

    def __init__(self, cidade, lider):
        """Cria um ginásio com a cidade e o líder, e as duas listas vazias."""
        self.cidade = cidade
        self.lider = lider              # AGREGAÇÃO: Treinador criado fora
        self.desafiantes = []           # AGREGAÇÃO: existem sem o ginásio
        self.combates = []              # COMPOSIÇÃO: só o ginásio os cria

    def combater(self, desafiante):
        """Um combate entre o Pokémon escolhido por cada treinador.

        Se um dos dois não tem Pokémon com vida, não há combate: lança
        SemPokemonComVida, e o ginásio fica como estava.
        """
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
        # O desafiante só entra na lista depois da verificação: um combate
        # recusado deixa o ginásio como estava.
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
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

    def mostrar_historico(self):
        """Mostra o resumo de todos os combates deste ginásio."""
        print(f"\nHistórico do ginásio de {self.cidade}:")
        for combate in self.combates:
            print(" -", combate.resumo())

    def anunciar_combates(self, anunciador):
        """Entrega cada combate ao anunciador, para ele o anunciar.

        O anunciador pode ser um objeto de qualquer classe, desde que tenha o
        método anunciar(combate). O ginásio não quer saber de que classe é.
        """
        for combate in self.combates:
            anunciador.anunciar(combate)


if __name__ == "__main__":
    misty = Treinador("Misty")
    misty.capturar(PokemonAgua("Starmie", 120, 35))
    ash = Treinador("Ash")
    ash.capturar(PokemonFogo("Charmander", 90, 40))
    ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
    cerulean = Ginasio("Cerulean", misty)
    cerulean.combater(ash)
    cerulean.combater(ash)
    cerulean.mostrar_historico()
    # Apagar o ginásio apaga os registos dos combates, que só ele guardava.
    # Os treinadores e os seus Pokémon continuam a existir.
    del cerulean
    print(f"\n{ash.nome} continua com {len(ash.equipa)} Pokémon; {misty.nome} continua com {len(misty.equipa)}.")
```

As duas recusas, a do `capturar` e a do `combater`, verificam primeiro e lançam a exceção antes de mexerem no estado. O resto do ficheiro, com o texto do início e o programa principal, é o da pasta 03.

Pensa antes de continuares: no passo 4, um `print` a seguir ao `try`, sem `finally`, escrevia o mesmo. Então, quando é que o `finally` faz diferença? A resposta: quando há uma exceção que nenhum `except` apanha, como no passo 5, ou quando o `try` sai da função com `return`. No passo 5, o `finally` correu na mesma, e um `print` a seguir ao `try` nunca chegava a correr.

## Fase 4: O depurador para num ponto de paragem

Investigas um ataque que tira metade do que devia, um erro de lógica, com a rotina dos cinco passos e o depurador do VS Code. O depurador para num ponto de paragem, antes de a linha correr, e mostra-te os valores das variáveis. Rever: [O depurador para num ponto de paragem](../04-excecoes-depuracao-e-logging.md#o-depurador-para-num-ponto-de-paragem).

1. Cria o ficheiro `investigar.py`, com uma cópia da `PokemonAgua` que tem um erro de propósito:

   ```python
   # investigar.py: um erro de lógica para encontrar com o depurador.
   from pokemon import Pokemon, PokemonFogo, PokemonPlanta


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
   bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
   squirtle.atacar(bulbasaur)
   ```

2. Observa e reproduz o erro: corre `python3 investigar.py`. O que deves ver:

   ```text
   Squirtle ataca Charmander e tira 30 de vida.
   Charmander tem 60/150 de vida.
   Squirtle ataca Bulbasaur e tira 30 de vida.
   Bulbasaur tem 80/150 de vida.
   ```

   Escreve o caso num comentário no fim do `investigar.py`, a seguir à última linha de código. Rever: [A rotina dos cinco passos](../04-excecoes-depuracao-e-logging.md#a-rotina-dos-cinco-passos). O comentário leva o resultado esperado, tirado da regra do jogo, e o obtido, como este:

   ```python
   # Caso: o Squirtle, de água e com 30 de ataque, ataca o Charmander, de fogo.
   # Esperado: tira 60, com "É super eficaz!", porque a água tira o dobro ao fogo.
   # Obtido: tira 30, sem a mensagem. Contra o Bulbasaur, de planta, tira 30, como deve.
   # Tipo de erro: de lógica, porque o programa corre até ao fim e o resultado está errado.
   ```

3. Formula uma hipótese, antes de abrires o depurador, e acrescenta-a ao comentário. Diz o que esperas ver nos valores se tiveres razão, como esta:

   ```python
   # Hipótese: contra o Charmander, o if dá False e o dano fica em 30. Se for isso,
   # as duas linhas do bloco do if não correm.
   ```

4. Põe um ponto de paragem na linha 14, `dano = super().calcular_dano(alvo)`: clica na margem, à esquerda do número da linha, e aparece um ponto vermelho. Com o separador do `investigar.py` à frente no editor, carrega em F5 (Start Debugging), porque o F5 depura o ficheiro que está à frente.

   Na primeira vez, o VS Code pode perguntar que depurador usar: escolhe Python Debugger e, a seguir, Python File. Num portátil ou num Mac, as teclas F5 e F10 podem precisar da tecla Fn.

   O que deves ver: a linha 14 marcada a amarelo, que ainda não correu, e o terminal ainda sem nenhuma linha do ataque. O programa parou no primeiro ataque, o do Charmander. No painel Variáveis (Variables), abre o `alvo` com a seta: o `tipo` vale `'Fogo'`. Se o programa correr até ao fim sem parar, vê [O depurador não para no ponto de paragem](#o-depurador-não-para-no-ponto-de-paragem).

5. Verifica a condição no painel Vigiar (Watch). Na barra lateral da depuração, por baixo das Variáveis, passa o rato pelo título Vigiar (Watch) e clica no `+`. Escreve `alvo.tipo == "fogo"` e carrega em Enter. O que deves ver: `False`. A comparação é com `"fogo"`, em minúsculas, e o tipo está guardado com maiúscula. Rever: [Verificar a hipótese](../04-excecoes-depuracao-e-logging.md#verificar-a-hipótese).

6. Avança com F10, o botão Step Over da barra de depuração, que corre a linha marcada e para na seguinte, até chegares ao `return`. Rever: [F10 passa por cima, F11 entra](../04-excecoes-depuracao-e-logging.md#f10-passa-por-cima-f11-entra). O que deves ver:

   | Depois de | Linha marcada a amarelo | `dano` no painel Variáveis |
   | --- | --- | --- |
   | Parar no ponto de paragem | `dano = super().calcular_dano(alvo)` | ainda não existe |
   | F10 | `if alvo.tipo == "fogo":` | 30 |
   | F10 | `return dano` | 30 |

   O depurador saltou do `if` para o `return`, e as duas linhas do bloco do `if` não correram: a hipótese confirma-se. Se passares à frente do `return`, ou se a linha marcada aparecer no `pokemon.py`, para com Shift+F5, volta ao separador do `investigar.py` e carrega em F5. O programa volta a parar na linha 14.

7. Para a depuração com Shift+F5, ou com o quadrado vermelho (Stop) da barra de depuração, antes de mudares o ficheiro. Depois, acrescenta ao comentário o que o depurador mostrou:

   ```python
   # Verificação: parado na linha 14, o Vigiar mostrou alvo.tipo == "fogo" como False.
   # Com o F10, o if saltou para o return, e o dano ficou em 30.
   ```

8. Corrige a causa: na linha 15, muda `"fogo"` para `"Fogo"`, como o `pokemon.py` escreve o tipo. O `if` e o seu bloco ficam assim:

   ```python
           if alvo.tipo == "Fogo":
               print("É super eficaz!")
               dano = dano * 2
   ```

9. Volta a testar tudo: corre `python3 investigar.py` no terminal. O que deves ver:

   ```text
   É super eficaz!
   Squirtle ataca Charmander e tira 60 de vida.
   Charmander tem 30/150 de vida.
   Squirtle ataca Bulbasaur e tira 30 de vida.
   Bulbasaur tem 80/150 de vida.
   ```

   Os dois casos estão certos, também o do Bulbasaur, que já passava. Acaba o comentário com o que mudou:

   ```python
   # O que mudou: no if, "fogo" passou a "Fogo". Agora tira 60 ao Charmander, com a
   # mensagem, e 30 ao Bulbasaur, sem a mensagem: os dois casos certos.
   ```

### Paragem 4

O `investigar.py` corrigido tira 60 ao Charmander e 30 ao Bulbasaur, e acaba com o comentário com o caso, a hipótese, a verificação e o que mudou. Confere o teu com este:

```python
# investigar.py: um erro de lógica para encontrar com o depurador.
from pokemon import Pokemon, PokemonFogo, PokemonPlanta


class PokemonAgua(Pokemon):
    """Uma cópia da PokemonAgua do pokemon.py, com um erro de propósito para investigar."""

    def __init__(self, nome, vida, ataque):
        """Cria um Pokémon de água com nome, vida e ataque."""
        super().__init__(nome, "Água", vida, ataque)

    def calcular_dano(self, alvo):
        """Contra Fogo, a água tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Fogo":
            print("É super eficaz!")
            dano = dano * 2
        return dano


squirtle = PokemonAgua("Squirtle", 100, 30)
charmander = PokemonFogo("Charmander", 90, 40)
squirtle.atacar(charmander)
bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
squirtle.atacar(bulbasaur)

# Caso: o Squirtle, de água e com 30 de ataque, ataca o Charmander, de fogo.
# Esperado: tira 60, com "É super eficaz!", porque a água tira o dobro ao fogo.
# Obtido: tira 30, sem a mensagem. Contra o Bulbasaur, de planta, tira 30, como deve.
# Tipo de erro: de lógica, porque o programa corre até ao fim e o resultado está errado.
# Hipótese: contra o Charmander, o if dá False e o dano fica em 30. Se for isso,
# as duas linhas do bloco do if não correm.
# Verificação: parado na linha 14, o Vigiar mostrou alvo.tipo == "fogo" como False.
# Com o F10, o if saltou para o return, e o dano ficou em 30.
# O que mudou: no if, "fogo" passou a "Fogo". Agora tira 60 ao Charmander, com a
# mensagem, e 30 ao Bulbasaur, sem a mensagem: os dois casos certos.
```

O código só mudou numa palavra, e o comentário, no fim, não mudou nenhuma linha de sítio. A tua hipótese pode ter sido outra: o que conta é estar escrita antes do depurador e dizer o que esperavas ver.

Pensa antes de continuares: porque é que o ponto de paragem ficou no `dano = super().calcular_dano(alvo)`, e não no `print("É super eficaz!")`? A resposta: com o erro, o `print` nunca corre, porque a condição dá `False`. O depurador nunca parava nele, e o programa corria até ao fim.

## Fase 5: Um erro que rebenta longe da causa

Segues um erro de execução com o traceback e com a pilha de chamadas do depurador. A causa está numa linha que já acabou quando o erro rebenta. Rever: [Um erro que rebenta longe da causa](../04-excecoes-depuracao-e-logging.md#um-erro-que-rebenta-longe-da-causa).

1. Cria o ficheiro `pilha.py`. Tem um erro de propósito: a equipa do Ash leva o texto `"Squirtle"` no lugar de um Pokémon.

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

2. Antes de correres, prevê se o programa rebenta no primeiro combate ou no segundo. Corre `python3 pilha.py`. O que deves ver:

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
     File "ginasio.py", line 128, in combater
       atacante = desafiante.escolher_pokemon()
     File "ginasio.py", line 75, in escolher_pokemon
       if pokemon.vida > 0:
          ^^^^^^^^^^^^
   AttributeError: 'str' object has no attribute 'vida'
   ```

   Rebenta no segundo. No primeiro, o `escolher_pokemon` devolveu o Charmander antes de chegar ao texto, e o erro ficou escondido até o Charmander ficar KO. No teu terminal, cada `File` tem o caminho completo do ficheiro, e no Python 3.9 faltam as linhas com `~` e `^`. Se os números das linhas do `ginasio.py` forem outros, vê [as linhas do traceback](#o-traceback-tem-outros-números-de-linha).

3. Lê o traceback de baixo para cima e encontra três coisas: o que falhou, onde rebentou e por onde passou o programa até lá. Rever: [Ler um traceback com três andares](../04-excecoes-depuracao-e-logging.md#ler-um-traceback-com-três-andares). A resposta: a última linha diz que se tentou ler a `vida` de um texto, um `str`. O andar de baixo diz que rebentou na linha 75 do `ginasio.py`, no `escolher_pokemon`. Os andares de cima dizem que a linha 9 do `pilha.py` chamou o `combater`, e que o `combater` chamou o `escolher_pokemon`.

4. Vê a pilha de chamadas no depurador: com o separador do `pilha.py` à frente, carrega em F5, sem nenhum ponto de paragem. O programa para na linha onde a exceção rebentou, o `if pokemon.vida > 0:` do `ginasio.py`, com a exceção descrita numa caixa junto da linha. Rever: [A pilha de chamadas no depurador](../04-excecoes-depuracao-e-logging.md#a-pilha-de-chamadas-no-depurador).

   O que deves ver no painel Pilha de chamadas (Call Stack): três andares, pela ordem contrária à do traceback: `escolher_pokemon` em cima, `combater` e `<module>`. No `escolher_pokemon`, o painel Variáveis mostra o `pokemon` a valer `'Squirtle'`. Clica no andar `combater` e abre o `desafiante`: a `equipa` tem dois elementos, o Charmander, um objeto `PokemonFogo`, e o texto `'Squirtle'`. Clica no andar `<module>`: estás no `pilha.py`, onde o `ash` foi criado.

5. Corrige a causa: carrega em Shift+F5, para parar a depuração. A causa não está em nenhum andar do traceback, mas na linha 6 do `pilha.py`, onde a equipa do Ash foi criada com um texto. Substitui essa linha por esta, com um Squirtle a sério:

   ```python
   ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 30, 40), PokemonAgua("Squirtle", 100, 30)])
   ```

6. Volta a testar: corre `python3 pilha.py`. O que deves ver:

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

   O segundo combate passa a acontecer: o Squirtle, de água contra água, vence o Starmie, que só tinha 50 de vida.

### Paragem 5

O `pilha.py` corrigido faz os dois combates, e o `escolher_pokemon`, onde o erro rebentava, não mudou.

Pensa antes de continuares: com o erro, se a equipa do Ash fosse `["Squirtle", PokemonFogo("Charmander", 30, 40)]`, com o texto primeiro, que linha do `pilha.py` aparecia no andar de cima do traceback? A resposta: a linha 8, o primeiro `cerulean.combater(ash)`. O `escolher_pokemon` lia logo o texto, e o erro rebentava no primeiro combate, com a mesma causa na linha 6.

## Fase 6: O ginásio escreve no registo

O ginásio passa a escrever no registo, com um logger e uma mensagem com o nível certo para cada acontecimento, e um programa novo escolhe que níveis se veem. Rever: [O ginásio escreve no registo](../04-excecoes-depuracao-e-logging.md#o-ginásio-escreve-no-registo).

1. No `ginasio.py`, substitui tudo desde o início do ficheiro até à linha `TAMANHO_MAXIMO_DA_EQUIPA = 6` pelas linhas seguintes. O texto do início passa a dizer o que o ficheiro faz neste tema, e chama histórico aos combates guardados, porque daqui em diante o registo é o do logger. São novos também o `import logging` e as duas últimas linhas, com o logger:

   ```python
   """ginasio.py: o ginásio Pokémon, com exceções para as recusas e um registo.

   - Treinador tem uma equipa de Pokémon e recusa a captura com a equipa cheia,
     com a exceção EquipaCheia. Lider É UM Treinador que escolhe sempre o
     Pokémon com mais vida.
   - Ginasio tem um líder, recebe desafiantes e guarda o histórico dos seus
     combates, um objeto Combate por combate. Recusa um combate sem Pokémon com
     vida, com a exceção SemPokemonComVida.
   - O ginásio escreve no registo, com o logger deste ficheiro, cada combate e
     cada recusa. Quem configura o registo é o programa que usa o ginásio.

   As exceções vêm do ficheiro erros.py, e as classes de Pokémon do pokemon.py,
   que têm de estar na mesma pasta que este.
   """

   import logging
   from dataclasses import dataclass

   from erros import EquipaCheia, SemPokemonComVida
   from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta

   # O limite da equipa, num só sítio: a condição e a mensagem do capturar usam-no.
   TAMANHO_MAXIMO_DA_EQUIPA = 6

   # O logger deste ficheiro. O __name__ dá-lhe o nome do módulo, "ginasio".
   logger = logging.getLogger(__name__)
   ```

   Troca também, mais abaixo, as três linhas que ainda chamam registo aos combates:

   - na docstring da `Combate`, a primeira linha passa a `"""Um combate do histórico. Só o ginásio cria combates (composição).`;
   - na docstring do `Ginasio`, a segunda linha passa a `e guarda o histórico dos seus combates (composição)."""`;
   - no programa principal, o primeiro comentário passa a dizer "o histórico dos combates", em vez de "os registos dos combates".

2. No método `combater`, acrescenta as quatro mensagens do registo, em três sítios. Dentro do `if` que recusa o combate, por cima do `raise`, acrescenta o aviso, com doze espaços, como o `raise`:

   ```python
               # O aviso vem antes do raise: depois dele, o método já parou.
               logger.warning(f"Combate recusado em {self.cidade}: {desafiante.nome} contra {self.lider.nome}, sem Pokémon com vida.")
   ```

   A seguir ao `append` dos desafiantes, por cima do `print` com os sinais `===`, acrescenta o início do combate, com oito espaços:

   ```python
           logger.info(f"Combate em {self.cidade}: {desafiante.nome} com {atacante.nome} contra {self.lider.nome} com {defensor.nome}.")
           logger.debug(f"Vida no início: {atacante.nome} {atacante.vida}, {defensor.nome} {defensor.vida}.")
   ```

   No fim do método, substitui as duas últimas linhas, o comentário e o `append` dos combates, por estas três:

   ```python
           # O combate entra no histórico, que só o ginásio guarda (composição).
           self.combates.append(Combate(desafiante.nome, atacante.nome, vencedor.nome))
           logger.info(f"Fim do combate em {self.cidade}: venceu {vencedor.nome}.")
   ```

3. Cria o ficheiro `registo.py`, o programa que configura o registo. Rever: [Quem configura é o programa](../04-excecoes-depuracao-e-logging.md#quem-configura-é-o-programa).

   ```python
   # registo.py: o ginásio de Celadon escreve no registo, e este programa escolhe o que se vê.
   import logging

   from erros import ErroDoGinasio
   from pokemon import PokemonAgua, PokemonPlanta
   from ginasio import Ginasio, Lider, Treinador

   # Quem configura o registo é o programa: o level é o nível mínimo, e o format
   # põe o nível e o nome do logger à frente de cada mensagem.
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

4. Antes de correres, prevê quantas das quatro mensagens do ginásio vão aparecer, com o nível mínimo `INFO`. A Misty desafia duas vezes, e o Psyduck fica KO no primeiro combate. Corre `python3 registo.py`. O que deves ver:

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

   Aparecem três: as duas de `INFO` e o aviso do combate recusado. A de `DEBUG` fica escondida, porque está abaixo do nível mínimo. Se as linhas do registo não aparecerem, ou aparecer um `--- Logging error ---`, vê [o registo que não aparece](#as-linhas-do-registo-não-aparecem) ou [o `Logging error`](#----logging-error-----com-not-all-arguments-converted-during-string-formatting).

5. No `registo.py`, muda o nível do `basicConfig` para `logging.DEBUG` e corre outra vez. O que deves ver, no início:

   ```text
   [INFO] ginasio: Combate em Celadon: Misty com Psyduck contra Erika com Tangela.
   [DEBUG] ginasio: Vida no início: Psyduck 60, Tangela 50.
   ```

   A mensagem de `DEBUG` estava no ginásio desde o passo 2, e aparece porque a configuração passou a pedi-la.

### Paragem 6

O ginásio escreve no registo quatro mensagens, em três níveis, e o `registo.py` escolhe quais se veem. O `ginasio.py` inteiro, para conferires o teu:

```python
"""ginasio.py: o ginásio Pokémon, com exceções para as recusas e um registo.

- Treinador tem uma equipa de Pokémon e recusa a captura com a equipa cheia,
  com a exceção EquipaCheia. Lider É UM Treinador que escolhe sempre o
  Pokémon com mais vida.
- Ginasio tem um líder, recebe desafiantes e guarda o histórico dos seus
  combates, um objeto Combate por combate. Recusa um combate sem Pokémon com
  vida, com a exceção SemPokemonComVida.
- O ginásio escreve no registo, com o logger deste ficheiro, cada combate e
  cada recusa. Quem configura o registo é o programa que usa o ginásio.

As exceções vêm do ficheiro erros.py, e as classes de Pokémon do pokemon.py,
que têm de estar na mesma pasta que este.
"""

import logging
from dataclasses import dataclass

from erros import EquipaCheia, SemPokemonComVida
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta

# O limite da equipa, num só sítio: a condição e a mensagem do capturar usam-no.
TAMANHO_MAXIMO_DA_EQUIPA = 6

# O logger deste ficheiro. O __name__ dá-lhe o nome do módulo, "ginasio".
logger = logging.getLogger(__name__)


class Treinador:
    """Um treinador tem uma equipa de Pokémon (agregação)."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        # AGREGAÇÃO: a equipa começa vazia e recebe Pokémon que já existiam.
        self.equipa = []

    @classmethod
    def com_equipa(cls, nome, pokemons):
        """Cria um treinador da classe cls, já com os Pokémon da lista na equipa.

        É um construtor alternativo. Em Treinador.com_equipa(...), cls é
        Treinador; em Lider.com_equipa(...), cls é Lider, e o objeto criado
        é um Lider.
        """
        treinador = cls(nome)
        for pokemon in pokemons:
            treinador.capturar(pokemon)
        return treinador

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador.

        Se a equipa já tem TAMANHO_MAXIMO_DA_EQUIPA Pokémon, não junta nada e
        lança EquipaCheia.
        """
        # A verificação vem antes do append: com a equipa cheia, o raise para o
        # método aqui, e o Pokémon recusado nunca entra na equipa.
        if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
            raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
        self.equipa.append(pokemon)

    def escolher_pokemon(self):
        """Devolve o primeiro Pokémon da equipa que ainda pode lutar, ou None."""
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                return pokemon
        return None


class Lider(Treinador):
    """Um Lider É UM Treinador que escolhe sempre o Pokémon com mais vida."""

    def escolher_pokemon(self):
        """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
        escolhido = None
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                if escolhido is None or pokemon.vida > escolhido.vida:
                    escolhido = pokemon
        return escolhido


@dataclass
class Combate:
    """Um combate do histórico. Só o ginásio cria combates (composição).

    É uma dataclass: guarda os nomes do desafiante, do seu Pokémon e do
    vencedor, e o @dataclass escreve sozinho o construtor, a forma de o
    mostrar com print e a comparação com ==.
    """

    desafiante: str
    pokemon_desafiante: str
    vencedor: str

    def resumo(self):
        """Devolve uma linha de texto que descreve o combate."""
        return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"


class Ginasio:
    """Um ginásio tem um líder e recebe desafiantes (agregação)
    e guarda o histórico dos seus combates (composição)."""

    def __init__(self, cidade, lider):
        """Cria um ginásio com a cidade e o líder, e as duas listas vazias."""
        self.cidade = cidade
        self.lider = lider              # AGREGAÇÃO: Treinador criado fora
        self.desafiantes = []           # AGREGAÇÃO: existem sem o ginásio
        self.combates = []              # COMPOSIÇÃO: só o ginásio os cria

    def combater(self, desafiante):
        """Um combate entre o Pokémon escolhido por cada treinador.

        Se um dos dois não tem Pokémon com vida, não há combate: lança
        SemPokemonComVida, e o ginásio fica como estava.
        """
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            # O aviso vem antes do raise: depois dele, o método já parou.
            logger.warning(f"Combate recusado em {self.cidade}: {desafiante.nome} contra {self.lider.nome}, sem Pokémon com vida.")
            raise SemPokemonComVida(f"Não há combate em {self.cidade}: um dos treinadores não tem Pokémon com vida.")
        # O desafiante só entra na lista depois da verificação: um combate
        # recusado deixa o ginásio como estava.
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
        # O combate entra no histórico, que só o ginásio guarda (composição).
        self.combates.append(Combate(desafiante.nome, atacante.nome, vencedor.nome))
        logger.info(f"Fim do combate em {self.cidade}: venceu {vencedor.nome}.")

    def mostrar_historico(self):
        """Mostra o resumo de todos os combates deste ginásio."""
        print(f"\nHistórico do ginásio de {self.cidade}:")
        for combate in self.combates:
            print(" -", combate.resumo())

    def anunciar_combates(self, anunciador):
        """Entrega cada combate ao anunciador, para ele o anunciar.

        O anunciador pode ser um objeto de qualquer classe, desde que tenha o
        método anunciar(combate). O ginásio não quer saber de que classe é.
        """
        for combate in self.combates:
            anunciador.anunciar(combate)


if __name__ == "__main__":
    misty = Treinador("Misty")
    misty.capturar(PokemonAgua("Starmie", 120, 35))
    ash = Treinador("Ash")
    ash.capturar(PokemonFogo("Charmander", 90, 40))
    ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
    cerulean = Ginasio("Cerulean", misty)
    cerulean.combater(ash)
    cerulean.combater(ash)
    cerulean.mostrar_historico()
    # Apagar o ginásio apaga o histórico dos combates, que só ele guardava.
    # Os treinadores e os seus Pokémon continuam a existir.
    del cerulean
    print(f"\n{ash.nome} continua com {len(ash.equipa)} Pokémon; {misty.nome} continua com {len(misty.equipa)}.")
```

As quatro mensagens do registo estão todas no `combater`, à volta do combate e da recusa. O resto do ficheiro é o da paragem 3, com o texto do início novo e o histórico no lugar do registo dos combates.

Pensa antes de continuares: para ver a mensagem de `DEBUG`, mudaste uma palavra no `registo.py` e nenhuma no `ginasio.py`. Que vantagem tem isto sobre acrescentar e apagar `print` no ginásio? A resposta: as mensagens ficam no código, e a configuração decide o que se vê. Não é preciso escrever `print` para investigar, apagá-los depois, nem lembrar onde estavam quando o erro volta.

## Fase 7: O registo num ficheiro

O registo passa do ecrã para o ficheiro `ginasio.log`, com a data e a hora de cada mensagem. Rever: [O registo num ficheiro](../04-excecoes-depuracao-e-logging.md#o-registo-num-ficheiro).

1. No `registo.py`, substitui a linha do `basicConfig`, e o comentário por cima dela, por estas:

   ```python
   # O filename manda o registo para um ficheiro, e o %(asctime)s põe a data e a
   # hora à frente de cada mensagem. Sem o encoding="utf-8", no Windows, os
   # acentos do ficheiro ficam estragados.
   logging.basicConfig(filename="ginasio.log", encoding="utf-8", level=logging.INFO,
                       format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
   ```

2. Corre `python3 registo.py` duas vezes seguidas. O que deves ver no terminal, de cada vez:

   ```text

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
   Recusado: Não há combate em Celadon: um dos treinadores não tem Pokémon com vida.
   ```

   Ficaram só as linhas dos `print`: as do registo foram para o ficheiro.

3. Na pasta apareceu o ficheiro `ginasio.log`. Antes de o abrires, prevê quantas linhas tem. Abre-o no VS Code, com um clique no painel Explorer. O que deves ver: seis linhas, com a data e a hora do teu computador. As três primeiras são parecidas com estas:

   ```text
   2026-11-12 09:23:04,291 [INFO] ginasio: Combate em Celadon: Misty com Psyduck contra Erika com Tangela.
   2026-11-12 09:23:04,291 [INFO] ginasio: Fim do combate em Celadon: venceu Erika.
   2026-11-12 09:23:04,291 [WARNING] ginasio: Combate recusado em Celadon: Misty contra Erika, sem Pokémon com vida.
   ```

   Cada execução acrescentou as suas três linhas ao fim do ficheiro, sem apagar as anteriores. Se o `ginasio.log` não aparecer na pasta, vê [O `ginasio.log` não aparece](#o-ginasiolog-não-aparece).

### Paragem 7

O registo do ginásio vai para o `ginasio.log`, com a hora de cada mensagem, e o terminal mostra só o jogo.

Pensa antes de terminares: se mudares o nível do `basicConfig` para `logging.WARNING` e correres o `registo.py` mais uma vez, quantas linhas ganha o `ginasio.log`? A resposta: uma, a do aviso do combate recusado. As duas de `INFO` ficam abaixo do nível mínimo, e o ficheiro passa de seis para sete linhas.

## Se alguma coisa falhar

1. Estás na pasta certa? Escreve `pwd` no terminal, ou `cd` na linha de comandos clássica do Windows: o caminho tem de acabar em `ginasio-com-erros`.
2. Guardaste o ficheiro? O Python corre o que está guardado no disco, e não o que vês no editor.
3. Os ficheiros estão todos na mesma pasta, com os nomes certos, em minúsculas e sem acentos?
4. A saída é diferente da do texto? Compara o teu `ginasio.py` com o da [paragem 3](#paragem-3) ou o da [paragem 6](#paragem-6), linha a linha.
5. Faltaste a uma aula, ou perdeste-te a meio? Faz [Preparar o projeto](#preparar-o-projeto) e cria o `erros.py` do passo 1 da fase 1. Para continuares na fase 3, faz também os passos 1 e 2 da fase 2. Para continuares na fase 4, 5 ou 6, copia o `ginasio.py` da paragem 3. Para continuares na fase 7, copia o da paragem 6 e cria o `registo.py` do passo 3 da fase 6.

### `can't open file '...': [Errno 2] No such file or directory`

O Python procurou o ficheiro na pasta onde o terminal está, e o caminho da mensagem mostra que é outra. Abre a pasta `ginasio-com-erros` no VS Code e abre lá um terminal novo.

### `ModuleNotFoundError: No module named 'erros'`

A linha do `import` pede um ficheiro que não está na pasta. Confirma que o `erros.py` está na mesma pasta que o programa que corres, com esse nome exato. A mesma mensagem com `'pokemon'` ou `'ginasio'` tem a mesma causa.

### `ImportError: cannot import name 'EquipaCheia' from 'erros'`

O ficheiro foi encontrado, mas não tem uma classe com esse nome. Confirma a grafia, com as maiúsculas, no `erros.py` e na linha do `import`. Nas versões recentes do Python, a mensagem acaba com o nome parecido que encontrou, depois de `Did you mean`.

### `TypeError: EquipaCheia() takes no arguments`

A classe não tem a classe-mãe entre parênteses, e por isso é uma classe normal, sem construtor, e não uma exceção. A `ErroDoGinasio` tem de ser filha de `Exception`, e as outras duas de `ErroDoGinasio`. Dentro de um `try`, a mesma causa acrescenta uma segunda mensagem, `catching classes that do not inherit from BaseException is not allowed`.

### `NameError: name 'EquipaCheia' is not defined`

O `ginasio.py` usa a exceção, mas não a importou. Confirma a linha `from erros import EquipaCheia, SemPokemonComVida` no início do ficheiro. O erro só aparece quando o `raise` corre, e por isso o ginásio parece estar bem até à primeira recusa. A mesma mensagem com `SemPokemonComVida` aparece na fase 3, quando falta juntá-la à importação.

### A recusa aparece sem a cidade

O `combates.py` escreve "Não há combate: um dos treinadores não tem Pokémon com vida." porque o `combater` ainda tem o `print` e o `return` do tema 03. Substitui as linhas desde o `def combater` até ao `return` pelo bloco do passo 2 da fase 3.

### A linha dos desafiantes diz 2 depois do Brock

O `if desafiante not in self.desafiantes:` e o `append` estão antes da verificação, e o Brock entrou na lista antes de ser recusado. Passa essas duas linhas para depois do `raise`.

### O depurador não para no ponto de paragem

Correste sem o depurador, com o triângulo do canto de cima ou no terminal, ou carregaste em F5 com outro ficheiro à frente. Volta ao separador do `investigar.py` e carrega em F5. Confirma também que o ponto vermelho está na linha 14, que corre sempre.

### O F5 não mostra o depurador de Python

A extensão Python da Microsoft não está instalada, ou está desativada. Instala-a no painel Extensions e carrega outra vez em F5.

### O traceback tem outros números de linha

O teu `ginasio.py` é diferente do da paragem 3, com linhas a mais ou a menos. Os andares e a última linha são os mesmos, e o resto da fase funciona. Para teres os números do texto, copia o `ginasio.py` da [paragem 3](#paragem-3).

### As linhas do registo não aparecem

O `registo.py` não tem o `basicConfig`, ou tem o `basicConfig` depois dos combates. Sem configuração, aparece só o aviso, sem o nível nem o nome à frente. A chamada ao `basicConfig` fica antes de tudo o que regista.

### `--- Logging error ---`, com `not all arguments converted during string formatting`

Uma mensagem do registo foi escrita como num `print`, com vírgulas: `logger.info("Fim do combate:", vencedor.nome)`. O logger recebe uma só mensagem. Escreve-a numa f-string, como as do passo 2 da fase 6.

### O `ginasio.log` não aparece

O ficheiro é criado na pasta onde o terminal está quando corres o programa, que pode não ser a do projeto. Confirma com `pwd` e corre o `registo.py` a partir da pasta `ginasio-com-erros`.

## Desafios

Os desafios partem do `erros.py` e do `ginasio.py` do fim da fase 6.

1. Um Pokémon capturado duas vezes. Hoje, o mesmo objeto Pokémon pode entrar duas vezes na equipa do mesmo treinador. Acrescenta ao `erros.py` a exceção `PokemonRepetido`, filha de `ErroDoGinasio`. O `capturar` recusa esse caso: regista um aviso, com o nível `WARNING`, e lança a `PokemonRepetido`, sem juntar nada à equipa. As mensagens são as do teste, com o nome do treinador e o do Pokémon. Testa com o `repetido.py`, na mesma pasta:

   ```python
   # repetido.py: testa a exceção PokemonRepetido, do desafio 1.
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

   Pista: o terceiro `capturar` junta um Charmander novo, com os mesmos valores do primeiro, e tem de ser aceite. A tua verificação pergunta se é o mesmo objeto ou se tem os mesmos valores? E, com a equipa cheia e um Pokémon repetido, qual das duas exceções diz mais a quem chamou?

2. A `EquipaCheia` com dados. Hoje, a `EquipaCheia` só tem a docstring, e a mensagem é escrita no `raise` do `capturar`. Dá-lhe um construtor que recebe o treinador e o Pokémon que ficou de fora e os guarda nos atributos `treinador` e `pokemon`. A própria exceção escreve a mensagem, com o mesmo texto de hoje. No `capturar`, o `raise` passa só o treinador e o Pokémon. Rever: [Uma exceção com dados](../04-excecoes-depuracao-e-logging.md#uma-exceção-com-dados). Testa com o `fora_da_equipa.py`:

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

   O `capturas.py` da fase 2 tem de mostrar o mesmo que antes, porque a mensagem não mudou.

   Pista: o 6 da mensagem vinha da constante do `ginasio.py`, e o `ginasio.py` já importa o `erros.py`. O que te diz a equipa do treinador, no momento da recusa? E, no teste, a variável `ash` nunca chega a existir: por onde chega o programa ao treinador?

## Antes de terminares

- [ ] O `erros.py` tem as três exceções, e o `teste_erros.py` mostra `True True`, `True` e a mensagem.
- [ ] O `capturas.py` mostra seis capturas, duas recusas e o 6, e o `combates.py` mostra o estado do ginásio depois de cada um dos três desafios.
- [ ] O `investigar.py` está corrigido e acaba com o comentário com o caso, a hipótese, a verificação e o que mudou.
- [ ] O `pilha.py` está corrigido e faz os dois combates.
- [ ] O `ginasio.py` tem as quatro mensagens do registo, e o `ginasio.log` tem as linhas das execuções do `registo.py`.
- [ ] Entregaste ao professor o `investigar.py` e o `ginasio.log`, conforme ele indicar.

![Rodapé](../../imagens/rodape.png)
