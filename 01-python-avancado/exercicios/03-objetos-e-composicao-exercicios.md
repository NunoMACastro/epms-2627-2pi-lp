![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento

Praticas as classes, as propriedades, a herança, a agregação e a composição, os três tipos de método, o duck typing, as dataclasses e a arroba dos decoradores. Os exercícios 1 a 20 são obrigatórios. Cada exercício fica num ficheiro com o número dele no nome, na pasta da ficha. As respostas que um exercício pedir por escrito ficam em comentários. Quando descobres, sem executar, o que um programa mostra, explica num comentário cada linha em que falhaste. Para rever: o [guia do tema](../03-objetos-e-composicao.md) e o [laboratório](../laboratorios/03-objetos-e-composicao-laboratorio.md).

## O cenário

Os exercícios usam os Pokémon das aulas e uma classe nova, a `Baga`: nos jogos, as bagas são frutos que curam os Pokémon. Cria uma pasta para a ficha e copia para lá o [pokemon.py](../../exemplos/python-avancado/pokemon/03-objetos-e-composicao/pokemon.py) e o [ginasio.py](../../exemplos/python-avancado/pokemon/03-objetos-e-composicao/ginasio.py) dos exemplos. Os exercícios que começam por `from pokemon import` ou `from ginasio import` só correm nessa pasta. Os exercícios 17 a 19 usam só funções.

## Classes e objetos

### Exercício 1: Uma baga que se descreve

Escreve a classe `Baga`. Uma baga tem um nome e uma cura, que recebe quando é criada. O método `descricao()` devolve o texto que descreve a baga, como `Baga Oran (cura 10)`.

Linhas de teste, no fim do ficheiro:

```python
oran = Baga("Baga Oran", 10)
sitrus = Baga("Baga Sitrus", 30)
sitrus.cura = sitrus.cura + oran.cura
print(oran.descricao())
print(sitrus.descricao())
```

O teste deve mostrar:

```text
Baga Oran (cura 10)
Baga Sitrus (cura 40)
```

Rever: [O construtor dá a cada objeto o estado inicial](../03-objetos-e-composicao.md#o-construtor-dá-a-cada-objeto-o-estado-inicial) e [Um método é uma função que pertence à classe](../03-objetos-e-composicao.md#um-método-é-uma-função-que-pertence-à-classe).

<details>
<summary>Pista</summary>

Se aparece uma linha `None` a seguir a cada descrição, olha para o que o teu método devolve.

</details>

### Exercício 2: Um método que recebe um Pokémon

Copia a classe `Baga` do exercício 1 para um ficheiro novo, com a importação `from pokemon import Pokemon` no início. Acrescenta-lhe o método `dar_a(pokemon)`: o Pokémon come a baga, e a vida dele sobe tanto quanto a cura.

Linhas de teste, no fim do ficheiro:

```python
pikachu = Pokemon("Pikachu", "Elétrico", 100, 30)
oran = Baga("Baga Oran", 10)
sitrus = Baga("Baga Sitrus", 30)
oran.dar_a(pikachu)
pikachu.vida = 145
sitrus.dar_a(pikachu)
```

O teste deve mostrar:

```text
Pikachu come a Baga Oran.
Pikachu tem 110/150 de vida.
Pikachu come a Baga Sitrus.
Pikachu tem 150/150 de vida.
```

Rever: [Um método que recebe outro objeto](../03-objetos-e-composicao.md#um-método-que-recebe-outro-objeto).

<details>
<summary>Pista</summary>

Compara com o `atacar`: quem muda é o objeto que chega por parâmetro.

</details>

### Exercício 3: Estático ou do objeto

A classe `Baga` do exercício 1 vai ter mais três métodos:

- `cura_valida(valor)` recebe um número e devolve `True` se ele pode ser a cura de uma baga, de 1 a 50, incluindo os dois, e `False` se não pode;
- `cura_mais_do_que(outra)` recebe outra baga e devolve `True` se esta baga cura mais do que a outra;
- `e_forte()` devolve `True` se esta baga cura 30 ou mais.

Escreve os três numa cópia da classe, num ficheiro novo. Ao lado de cada `def`, um comentário diz se é um método estático ou um método do objeto, e porquê.

Linhas de teste, no fim do ficheiro:

```python
oran = Baga("Baga Oran", 10)
pecha = Baga("Baga Pecha", 10)
sitrus = Baga("Baga Sitrus", 30)
print(Baga.cura_valida(1), Baga.cura_valida(0), Baga.cura_valida(50), Baga.cura_valida(51))
print(sitrus.cura_mais_do_que(oran), oran.cura_mais_do_que(sitrus), oran.cura_mais_do_que(pecha))
print(oran.e_forte(), sitrus.e_forte())
```

O teste deve mostrar:

```text
True False True False
True False False
False True
```

Rever: [Métodos estáticos: funções que vivem na classe](../03-objetos-e-composicao.md#métodos-estáticos-funções-que-vivem-na-classe).

<details>
<summary>Pista</summary>

Escreve primeiro o corpo de cada método e vê se ele usa o `self`.

</details>

## Proteger o estado

### Exercício 4: O que os dois sublinhados não impedem

Nesta versão da `Baga`, a cura tem dois sublinhados à frente:

```python
class Baga:
    def __init__(self, nome, cura):
        self.nome = nome
        self.__cura = cura

    def descricao(self):
        return f"{self.nome} (cura {self.__cura})"


oran = Baga("Baga Oran", 10)
print(oran.descricao())
print(oran.__cura)
```

A última linha dá erro. Um colega diz que, com os dois sublinhados, ninguém consegue mudar a cura de uma baga a partir de fora da classe. Mostra-lhe que não tem razão. Troca a última linha por linhas tuas que mudem a cura da `oran` para 99, sem mexeres na classe, e que mostrem a mudança com o `descricao`. O programa passa a mostrar:

```text
Baga Oran (cura 10)
Baga Oran (cura 99)
```

Rever: [Público e privado em Python](../03-objetos-e-composicao.md#público-e-privado-em-python).

<details>
<summary>Pista</summary>

Fora da classe, `oran.__cura` é um atributo novo, que não tem nada a ver com o que a classe guardou. Que nome lhe deu o Python lá dentro?

</details>

### Exercício 5: Uma propriedade para um texto

Na classe `Baga` do exercício 1, o nome não pode ficar vazio. Transforma o atributo `nome` numa propriedade, com get e set. Se alguém der à baga o texto vazio, `""`, ela fica com o nome `"Baga sem nome"`, também quando é criada. Qualquer outro texto é guardado tal como vem.

Linhas de teste, no fim do ficheiro:

```python
misteriosa = Baga("", 20)
print(misteriosa.nome)
oran = Baga("Baga Oran", 10)
print(oran.nome)
oran.nome = ""
print(oran.nome)
oran.nome = "Baga Pecha"
print(oran.nome)
```

O teste deve mostrar:

```text
Baga sem nome
Baga Oran
Baga sem nome
Baga Pecha
```

Rever: [Propriedades: o get e o set com cara de atributo](../03-objetos-e-composicao.md#propriedades-o-get-e-o-set-com-cara-de-atributo) e [Onde se escreve `vida` e onde se escreve `_vida`](../03-objetos-e-composicao.md#onde-se-escreve-vida-e-onde-se-escreve-_vida).

<details>
<summary>Pista</summary>

Segue o molde da vida do `Pokemon`. O valor não pode ficar guardado no próprio `nome`, porque esse é o nome da propriedade.

</details>

## Herança

### Exercício 6: Um Pokémon elétrico

Escreve a classe `PokemonEletrico`, filha de `Pokemon`. Um `PokemonEletrico` é sempre do tipo `"Elétrico"`, e por isso o construtor pede só o nome, a vida e o ataque. Reescreve o método `calcular_dano(alvo)`, que devolve o dano, com estas regras:

- contra um Pokémon do tipo `"Água"`, o dano é o dobro do dano base, e antes do ataque aparece "É super eficaz!";
- contra um Pokémon do tipo `"Planta"`, o dano é metade do dano base, arredondada para baixo, e antes do ataque aparece "Não é muito eficaz...";
- contra os outros tipos, o dano é o dano base.

O dano base é o que a classe-mãe calcula. No início do ficheiro, importa as classes de que precisas:

```python
from pokemon import Pokemon, PokemonAgua, PokemonFogo, PokemonPlanta
```

Linhas de teste, no fim do ficheiro:

```python
pikachu = PokemonEletrico("Pikachu", 100, 25)
squirtle = PokemonAgua("Squirtle", 100, 20)
bulbasaur = PokemonPlanta("Bulbasaur", 100, 20, 10)
charmander = PokemonFogo("Charmander", 100, 30)
pikachu.atacar(squirtle)
pikachu.atacar(bulbasaur)
pikachu.atacar(charmander)
```

O teste deve mostrar:

```text
É super eficaz!
Pikachu ataca Squirtle e tira 50 de vida.
Squirtle tem 50/150 de vida.
Não é muito eficaz...
Pikachu ataca Bulbasaur e tira 12 de vida.
Bulbasaur tem 88/150 de vida.
Pikachu ataca Charmander e tira 25 de vida.
Charmander tem 75/150 de vida.
```

Rever: [O construtor da filha chama o da mãe](../03-objetos-e-composicao.md#o-construtor-da-filha-chama-o-da-mãe) e [Reescrever um método](../03-objetos-e-composicao.md#reescrever-um-método).

<details>
<summary>Pista</summary>

Começa pelo dano que a mãe calcula, e só depois aplica a regra do tipo do alvo. Para a metade arredondada para baixo, há um operador do 10.º ano.

</details>

## Composição e agregação

### Exercício 7: Herança, agregação ou composição

Para cada uma das quatro relações da tabela, decide se é herança, agregação ou composição, num ficheiro só com comentários. Justifica cada uma com a frase "é um" ou "tem". Nas relações "tem", responde às duas perguntas do guia e diz de que lado fica o losango do diagrama de classes, e se é vazio ou cheio.

| | Relação |
| --- | --- |
| a) | Uma personagem de um jogo e o inventário com que ela nasce |
| b) | Uma equipa de um torneio de jogos online e os jogadores inscritos nela |
| c) | A classe `PokemonEletrico`, do exercício 6, e a classe `Pokemon` |
| d) | Uma liga e os ginásios que fazem parte dela. Os ginásios já existiam antes de a liga ser criada, e continuam abertos se a liga acabar |

Rever: [As perguntas que decidem](../03-objetos-e-composicao.md#as-perguntas-que-decidem), [O diagrama de classes: losango vazio e losango cheio](../03-objetos-e-composicao.md#o-diagrama-de-classes-losango-vazio-e-losango-cheio) e [É um ou tem um: herança, agregação ou composição](../03-objetos-e-composicao.md#é-um-ou-tem-um-herança-agregação-ou-composição).

<details>
<summary>Pista</summary>

Experimenta cada relação com as duas frases, "é um" e "tem", e fica com a que é verdadeira. Só depois escolhes o losango.

</details>

### Exercício 8: Encontrar a agregação e a composição num programa

Num Centro Pokémon, os treinadores deixam os Pokémon feridos para serem tratados, e o centro guarda uma ficha de cada tratamento:

```python
from pokemon import PokemonFogo, PokemonPlanta, VIDA_MAXIMA


class Ficha:
    """Registo de um tratamento feito num Centro Pokémon."""

    def __init__(self, nome_pokemon, vida_antes):
        self.nome_pokemon = nome_pokemon
        self.vida_antes = vida_antes

    def resumo(self):
        return f"{self.nome_pokemon} entrou com {self.vida_antes} de vida"


class CentroPokemon:
    """Centro onde os Pokémon são tratados."""

    def __init__(self, cidade):
        self.cidade = cidade
        self.pacientes = []
        self.fichas = []

    def receber(self, pokemon):
        self.pacientes.append(pokemon)

    def tratar_todos(self):
        for pokemon in self.pacientes:
            self.fichas.append(Ficha(pokemon.nome, pokemon.vida))
            pokemon.vida = VIDA_MAXIMA
        self.pacientes = []


charmander = PokemonFogo("Charmander", 20, 40)
bulbasaur = PokemonPlanta("Bulbasaur", 0, 25, 20)
centro = CentroPokemon("Viridian")
centro.receber(charmander)
centro.receber(bulbasaur)
centro.tratar_todos()
for ficha in centro.fichas:
    print(ficha.resumo())
print(len(centro.pacientes))
del centro
charmander.verificar_vida()
bulbasaur.verificar_vida()
```

Dos atributos `pacientes` e `fichas`, um é uma agregação e o outro uma composição. Diz qual é qual num comentário, com a linha do código que o mostra.

Rever: [Agregação: o todo reúne partes que existem por si](../03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si) e [Composição: o todo cria e guarda as suas partes](../03-objetos-e-composicao.md#composição-o-todo-cria-e-guarda-as-suas-partes).

<details>
<summary>Pista</summary>

Procura em cada método o sítio onde o objeto é criado e o sítio onde fica guardado.

</details>

### Exercício 9: Uma parte criada no construtor

Cada treinador tem uma Pokédex, onde fica o nome de cada Pokémon diferente que ele capturou. A Pokédex de um treinador é só dele: nasce com o treinador, e mais ninguém a usa. Esta é a classe `Pokedex`, já pronta:

```python
class Pokedex:
    """Lista dos nomes dos Pokémon que um treinador já registou."""

    def __init__(self):
        """Cria uma Pokédex vazia."""
        self.registados = []

    def registar(self, pokemon):
        """Regista o nome do Pokémon, se ainda não estiver registado."""
        if pokemon.nome not in self.registados:
            self.registados.append(pokemon.nome)

    def total(self):
        """Devolve quantos Pokémon diferentes estão registados."""
        return len(self.registados)
```

Num ficheiro novo, com a importação `from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta` no início, escreve a classe `Pokedex` e uma cópia da classe `Treinador` da secção [Um objeto que guarda outros objetos](../03-objetos-e-composicao.md#um-objeto-que-guarda-outros-objetos) do guia.

**a)** Muda o `Treinador` de forma que cada treinador crie a sua Pokédex, num atributo `pokedex`, e que o `capturar` registe nela cada Pokémon que junta à equipa. Linhas de teste, no fim do ficheiro:

```python
ash = Treinador("Ash")
misty = Treinador("Misty")
ash.capturar(PokemonFogo("Charmander", 90, 40))
ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
misty.capturar(PokemonAgua("Starmie", 120, 35))
print(ash.nome, ash.pokedex.total())
print(misty.nome, misty.pokedex.total())
print(ash.pokedex is misty.pokedex)
```

O teste deve mostrar:

```text
Ash 2
Misty 1
False
```

**b)** Explica num comentário porque é que a Pokédex é criada dentro do `Treinador`, e não recebida por parâmetro como os Pokémon do `capturar`, e que relação isso faz dela.

Rever: [Composição: o todo cria e guarda as suas partes](../03-objetos-e-composicao.md#composição-o-todo-cria-e-guarda-as-suas-partes).

<details>
<summary>Pista</summary>

Compara com a linha do `combater` que cria um `Combate`.

</details>

### Exercício 10: Tirar um Pokémon da equipa

Num ficheiro novo, com a importação `from pokemon import PokemonFogo, PokemonPlanta` no início, copia outra vez a classe `Treinador` do guia, sem a Pokédex do exercício 9. Acrescenta-lhe o método `libertar(pokemon)`. Se o Pokémon estiver na equipa, o método tira-o de lá e escreve "Ash liberta Charmander.", com o nome do treinador e o do Pokémon. Se não estiver, não tira nada e escreve "Charmander não está na equipa de Ash.".

Linhas de teste, no fim do ficheiro:

```python
charmander = PokemonFogo("Charmander", 90, 40)
bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
ash = Treinador("Ash")
ash.capturar(charmander)
ash.capturar(bulbasaur)
ash.libertar(charmander)
ash.libertar(charmander)
print(len(ash.equipa))
charmander.verificar_vida()
```

O teste deve mostrar:

```text
Ash liberta Charmander.
Charmander não está na equipa de Ash.
1
Charmander tem 90/150 de vida.
```

Rever: [Agregação: o todo reúne partes que existem por si](../03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si).

<details>
<summary>Pista</summary>

O que faz o `remove` a um valor que não está na lista?

</details>

## Métodos de classe

### Exercício 11: Seguir o cls

A classe `Baga` tem agora duas formas de criar bagas conhecidas, uma de classe e outra estática. A `BagaRara` é uma filha que se descreve de outra maneira:

```python
class Baga:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    @classmethod
    def oran(cls):
        return cls("Baga Oran", 10)

    @staticmethod
    def sitrus():
        return Baga("Baga Sitrus", 30)

    def descricao(self):
        return f"{self.nome} (cura {self.cura})"


class BagaRara(Baga):
    def descricao(self):
        return f"{self.nome} rara (cura {self.cura * 2})"


print(Baga.oran().descricao())
print(BagaRara.oran().descricao())
print(BagaRara.sitrus().descricao())
print(type(BagaRara.oran()).__name__, type(BagaRara.sitrus()).__name__)
```

Descobre, sem executar, as quatro linhas que o programa mostra, e confirma executando.

Rever: [Primeira tentativa: um método estático](../03-objetos-e-composicao.md#primeira-tentativa-um-método-estático) e [O método de classe recebe a classe](../03-objetos-e-composicao.md#o-método-de-classe-recebe-a-classe).

<details>
<summary>Pista</summary>

Procura, no `oran` e no `sitrus`, a linha que cria a baga. De que classe é o objeto que cada uma cria, quando o método é chamado por `BagaRara`?

</details>

### Exercício 12: Uma baga feita de duas

Copia as classes `Baga` e `BagaRara` do exercício 11 para um ficheiro novo, sem os métodos `oran` e `sitrus`. Acrescenta à `Baga` o método de classe `mistura(primeira, segunda)`, que recebe duas bagas e devolve uma baga nova, da classe por onde foi chamado. O nome da baga nova é "Mistura de", seguido dos nomes das duas, ligados por "e", e a cura é a soma das duas curas. As duas bagas recebidas não mudam.

Linhas de teste, no fim do ficheiro:

```python
oran = Baga("Baga Oran", 10)
sitrus = Baga("Baga Sitrus", 30)
mistura = Baga.mistura(oran, sitrus)
print(mistura.descricao())
rara = BagaRara.mistura(oran, sitrus)
print(rara.descricao())
print(type(rara).__name__)
print(oran.descricao(), sitrus.descricao())
```

O teste deve mostrar:

```text
Mistura de Baga Oran e Baga Sitrus (cura 40)
Mistura de Baga Oran e Baga Sitrus rara (cura 80)
BagaRara
Baga Oran (cura 10) Baga Sitrus (cura 30)
```

Rever: [O método de classe recebe a classe](../03-objetos-e-composicao.md#o-método-de-classe-recebe-a-classe) e [Escolher o tipo de método](../03-objetos-e-composicao.md#escolher-o-tipo-de-método).

<details>
<summary>Pista</summary>

Volta ao `oran` do exercício 11: o que faz a baga nova sair da classe por onde o método foi chamado?

</details>

## Duck typing

### Exercício 13: Tudo o que se pode usar num Pokémon

A função `tratar` recebe um Pokémon e uma lista de coisas, e usa cada coisa no Pokémon. As três classes não têm nenhuma classe-mãe em comum:

```python
from pokemon import Pokemon


class Baga:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    def usar_em(self, pokemon):
        print(f"{pokemon.nome} come a {self.nome}.")
        pokemon.vida = pokemon.vida + self.cura


class Pocao:
    def usar_em(self, pokemon):
        print(f"{pokemon.nome} bebe uma poção.")
        pokemon.vida = pokemon.vida + 50


class Pedra:
    def usar(self, pokemon):
        print(f"{pokemon.nome} olha para a pedra.")


def tratar(pokemon, itens):
    for item in itens:
        item.usar_em(pokemon)
    pokemon.verificar_vida()


pikachu = Pokemon("Pikachu", "Elétrico", 40, 30)
tratar(pikachu, [Baga("Baga Oran", 10), Pocao()])
tratar(pikachu, [])
tratar(pikachu, [Pedra(), Baga("Baga Oran", 10)])
```

**a)** O programa para com um erro. Descobre, sem executar, tudo o que ele mostra até lá, e a última linha da mensagem de erro. Depois, confirma executando.

**b)** Muda a `Pedra`, sem mexeres na função `tratar`, de forma que a terceira chamada funcione até ao fim. A pedra não cura nada. As três últimas linhas passam a ser:

```text
Pikachu olha para a pedra.
Pikachu come a Baga Oran.
Pikachu tem 110/150 de vida.
```

Rever: [Duck typing: o que conta é o comportamento](../03-objetos-e-composicao.md#duck-typing-o-que-conta-é-o-comportamento) e [Quando o objeto não tem o que é preciso](../03-objetos-e-composicao.md#quando-o-objeto-não-tem-o-que-é-preciso).

<details>
<summary>Pista</summary>

Segue as três chamadas pela ordem, item a item. Em que momento é que o Python procura o método `usar_em` de cada item?

</details>

### Exercício 14: Um líder que não é um treinador

O ginásio de Pallet não tem líder: tem uma máquina de treino. A máquina não é um treinador, e a classe dela não herda de `Treinador`. O nome dela, que aparece no combate, é "Máquina de treino". Tem sempre um só Pokémon, que ela própria cria quando é criada: um `PokemonAgua` chamado "Robô de água", com 60 de vida e 20 de ataque. Quando o Robô de água já não tiver vida, a máquina não tem Pokémon para lutar.

Num ficheiro novo, escreve a classe `MaquinaDeTreino`, só com o que o `combater` do `ginasio.py` usa do líder. No início do ficheiro, um comentário diz o que é isso: que atributos o `combater` lê do líder e que métodos lhe chama. As importações são estas:

```python
from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Treinador
```

Linhas de teste, no fim do ficheiro:

```python
maquina = MaquinaDeTreino()
treino = Ginasio("Pallet", maquina)
ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])
treino.combater(ash)
treino.combater(ash)
treino.mostrar_historico()
```

O teste deve mostrar:

```text

=== Ash desafia Máquina de treino no ginásio de Pallet ===
É super eficaz!
Bulbasaur ataca Robô de água e tira 50 de vida.
Robô de água tem 10/150 de vida.
Robô de água ataca Bulbasaur e tira 20 de vida.
Bulbasaur tem 90/150 de vida.
É super eficaz!
Bulbasaur ataca Robô de água e tira 50 de vida.
Robô de água está KO (0/150).
Não há combate: um dos treinadores não tem Pokémon com vida.

Histórico do ginásio de Pallet:
 - Ash com Bulbasaur: venceu Ash
```

Rever: [Duck typing ou herança](../03-objetos-e-composicao.md#duck-typing-ou-herança) e [O ginásio organiza um combate](../03-objetos-e-composicao.md#o-ginásio-organiza-um-combate).

<details>
<summary>Pista</summary>

O que devolve o `escolher_pokemon` de um `Treinador` quando não há Pokémon com vida?

</details>

## Dataclasses

### Exercício 15: A ficha do Centro Pokémon como dataclass

A `Ficha` do exercício 8 guardava o nome do Pokémon e a vida com que ele entrou no Centro Pokémon. O centro quer guardar também a vida com que o Pokémon saiu, e saber quanta vida ele recuperou. Num ficheiro novo, escreve a `Ficha` como dataclass, com os dois campos do exercício 8 e um terceiro, `vida_depois`. Tem também o método `recuperou`, que devolve quanta vida o Pokémon recuperou no centro.

Linhas de teste, no fim do ficheiro:

```python
primeira = Ficha("Charmander", 20, 150)
segunda = Ficha("Charmander", 20, 150)
terceira = Ficha("Bulbasaur", 0, 150)
print(primeira)
print(primeira.recuperou(), terceira.recuperou())
print(primeira == segunda, primeira == terceira)
```

O teste deve mostrar:

```text
Ficha(nome_pokemon='Charmander', vida_antes=20, vida_depois=150)
130 150
True False
```

Rever: [Uma dataclass escreve o construtor por ti](../03-objetos-e-composicao.md#uma-dataclass-escreve-o-construtor-por-ti) e [Uma dataclass continua a ser uma classe](../03-objetos-e-composicao.md#uma-dataclass-continua-a-ser-uma-classe).

<details>
<summary>Pista</summary>

O `recuperou` é um método como os das classes normais: faz uma conta com dois campos do próprio objeto, lidos com o `self`.

</details>

### Exercício 16: Dataclass ou classe normal

Para cada uma destas quatro classes, decide se faria sentido escrevê-la como dataclass. Justifica cada resposta num comentário, com o que a classe guarda e com as regras que tem.

| | Classe |
| --- | --- |
| a) | A `Baga` do exercício 1, que guarda um nome e uma cura e tem o método `descricao` |
| b) | A `Baga` do exercício 5, em que o nome é uma propriedade e nunca pode ficar vazio |
| c) | A `Pokedex` do exercício 9, com a lista dos nomes registados, que começa vazia, e o método `registar`, que não repete nomes |
| d) | Uma `Medalha`, que só guarda a cidade do ginásio que a deu |

Rever: [Quando uma dataclass não serve](../03-objetos-e-composicao.md#quando-uma-dataclass-não-serve).

<details>
<summary>Pista</summary>

Para cada classe, pergunta-te se só guarda dados ou se também tem regras.

</details>

## Decoradores

### Exercício 17: Uma tabela de conversões

Um dicionário também pode guardar funções:

```python
def km_para_metros(valor):
    return valor * 1000


def horas_para_minutos(valor):
    return valor * 60


conversoes = {"km": km_para_metros, "horas": horas_para_minutos}

print(conversoes["km"](3))
print(conversoes["horas"](2))
```

Escreve a função `euros_para_centimos` e junta-a ao dicionário, com a chave `"euros"`. Acrescenta uma linha que mostre, através do dicionário, quantos cêntimos são 2,5 euros, que em Python se escreve `2.5`. A saída passa a ser:

```text
3000
120
250.0
```

Explica num comentário de onde vem o `.0` da última linha.

Rever: [Uma função é um valor](../03-objetos-e-composicao.md#uma-função-é-um-valor).

<details>
<summary>Pista</summary>

O que dá `conversoes["km"]` sozinho, sem o `(3)`?

</details>

### Exercício 18: O momento em que o decorador corre

```python
def avisar(funcao):
    print(f"Li a função {funcao.__name__}.")
    return funcao


print("Início")


@avisar
def saltar():
    print("A personagem salta.")


print("Meio")


@avisar
def agachar():
    print("A personagem agacha-se.")


print("Fim")
agachar()
saltar()
```

Descobre, sem executar, todas as linhas que o programa mostra, pela ordem certa, e confirma executando.

Rever: [Um decorador corre uma vez, quando o def é lido](../03-objetos-e-composicao.md#um-decorador-corre-uma-vez-quando-o-def-é-lido).

<details>
<summary>Pista</summary>

O Python lê o ficheiro de cima para baixo. Em que momento corre o corpo do `avisar`, e em que momento corre o corpo de cada função decorada?

</details>

### Exercício 19: O teu primeiro decorador

Uma personagem de um jogo tem três comandos:

```python
def saltar():
    print("A personagem salta.")


def agachar():
    print("A personagem agacha-se.")


def atacar():
    print("A personagem ataca.")
```

Escreve um decorador, `comando`, que guarda cada função numa lista, `comandos`, e põe-no por cima dos três `def`. O programa mostra um menu numerado com o nome de cada comando, que se obtém com `.__name__`, pede o número de um comando e executa-o. Só tens de aceitar os números do menu. Uma execução, com a resposta 2:

```text
1 - saltar
2 - agachar
3 - atacar
Comando: 2
A personagem agacha-se.
```

Rever: [O que faz a arroba](../03-objetos-e-composicao.md#o-que-faz-a-arroba) e [Um decorador corre uma vez, quando o def é lido](../03-objetos-e-composicao.md#um-decorador-corre-uma-vez-quando-o-def-é-lido).

<details>
<summary>Pista</summary>

Um decorador recebe uma função. O que tem de devolver, para a função continuar a existir com o mesmo nome? No menu, os números começam em 1, e as posições da lista começam em 0.

</details>

### Exercício 20: Uma classe sem arrobas

Esta versão da `Baga` usa três decoradores:

```python
class Baga:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    @staticmethod
    def cura_valida(valor):
        return valor >= 1 and valor <= 50

    @classmethod
    def oran(cls):
        return cls("Baga Oran", 10)

    @property
    def descricao(self):
        return f"{self.nome} (cura {self.cura})"


print(Baga.cura_valida(30), Baga.cura_valida(80))
print(Baga.oran().descricao)
```

O programa mostra:

```text
True False
Baga Oran (cura 10)
```

Um colega reescreveu a classe sem nenhuma linha começada por arroba. O programa dele tem um erro, e para logo:

```python
class Baga:
    cura_valida = staticmethod(cura_valida)
    oran = classmethod(oran)
    descricao = property(descricao)

    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    def cura_valida(valor):
        return valor >= 1 and valor <= 50

    def oran(cls):
        return cls("Baga Oran", 10)

    def descricao(self):
        return f"{self.nome} (cura {self.cura})"


print(Baga.cura_valida(30), Baga.cura_valida(80))
print(Baga.oran().descricao)
```

**a)** Encontra o erro e corrige-o, sem voltares a pôr arrobas. As duas linhas de teste têm de mostrar o mesmo que a versão com arrobas.

**b)** Na tua versão corrigida, tira a linha que substitui o `@property`. O que mostra agora a última linha do teste? Experimenta, explica num comentário o que viste e volta a pôr a linha.

Rever: [O que faz a arroba](../03-objetos-e-composicao.md#o-que-faz-a-arroba).

<details>
<summary>Pista</summary>

Lê a mensagem: que nome é que o Python ainda não conhecia quando chegou a essa linha? Na alínea b), pensa no que fica no nome `descricao` quando ele não é uma propriedade.

</details>

## Desafios

### Desafio 1: O mesmo Pokémon em duas equipas

Na agregação, a mesma parte pode estar em mais do que um todo. Com a classe `Treinador` do `ginasio.py`, nada impede que dois treinadores capturem o mesmo Pokémon:

```python
from pokemon import PokemonAgua
from ginasio import Treinador

starmie = PokemonAgua("Starmie", 120, 35)
misty = Treinador("Misty")
brock = Treinador("Brock")
misty.capturar(starmie)
brock.capturar(starmie)
print(misty.equipa[0] is brock.equipa[0])
misty.equipa[0].vida = 0
print(brock.escolher_pokemon())
```

```text
True
None
```

O Starmie está nas duas equipas ao mesmo tempo. Quando fica KO num combate da Misty, o Brock fica sem Pokémon para lutar, sem ter combatido.

Muda as classes de forma que um Pokémon que já pertence a um treinador não possa ser capturado por outro. Quando alguém tenta, o `capturar` não junta o Pokémon à equipa e escreve "Starmie já pertence a Misty.". Um Pokémon libertado com o `libertar` do exercício 10 fica sem treinador e pode voltar a ser capturado. Tens de decidir em que objeto fica a informação de quem é o treinador de cada Pokémon, e em que métodos ela muda. Podes mudar a tua cópia do `pokemon.py`.

Testa com estas linhas, num ficheiro com as tuas classes:

```python
starmie = PokemonAgua("Starmie", 120, 35)
misty = Treinador("Misty")
brock = Treinador("Brock")
misty.capturar(starmie)
brock.capturar(starmie)
print(len(misty.equipa), len(brock.equipa))
misty.libertar(starmie)
brock.capturar(starmie)
print(len(misty.equipa), len(brock.equipa))
misty.capturar(starmie)
```

O teste deve mostrar:

```text
Starmie já pertence a Misty.
1 0
Misty liberta Starmie.
0 1
Starmie já pertence a Brock.
```

<details>
<summary>Pista</summary>

Enquanto o Pokémon não for capturado, que valor deve ter a informação de quem é o treinador?

</details>

### Desafio 2: Um histórico que se deixa estragar

Um colega acrescentou ao ginásio um método para saber qual foi o último combate:

```python
class Ginasio:
    # O construtor, o combater e o mostrar_historico ficam como estão.

    def ultimo_combate(self):
        """Devolve o registo do último combate."""
        return self.combates[-1]
```

Numa cópia do `ginasio.py`, com o nome `historico.py`, acrescenta este método à classe `Ginasio` e troca o programa principal por este:

```python
if __name__ == "__main__":
    misty = Treinador("Misty")
    misty.capturar(PokemonAgua("Starmie", 120, 35))
    ash = Treinador("Ash")
    ash.capturar(PokemonFogo("Charmander", 90, 40))
    cerulean = Ginasio("Cerulean", misty)
    cerulean.combater(ash)
    cerulean.mostrar_historico()
    registo = cerulean.ultimo_combate()
    registo.vencedor = "Ash"
    cerulean.mostrar_historico()
```

Ao correres o `historico.py`, os dois históricos do fim da saída são diferentes:

```text
Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Misty

Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Ash
```

**a)** Explica num comentário porque é que o histórico mudou, se o programa principal nunca mexeu na lista `combates`, e que característica da composição deixou de ser verdade.

**b)** Muda o `ultimo_combate` de forma que quem o chama fique a saber o resultado do último combate, sem conseguir estragar o histórico do ginásio. Está certo quando, com o mesmo programa principal, a linha `registo.vencedor = "Ash"` já não muda o histórico: o segundo histórico, se o programa chegar a escrevê-lo, fica igual ao primeiro.

<details>
<summary>Pista</summary>

Depois de o `ultimo_combate` devolver o registo, quantos caminhos levam a esse objeto? Na alínea b), pensa em devolver outra coisa que não seja o objeto da lista.

</details>

### Desafio 3: Uma função que recebe outra função

Estas duas funções fazem contas com um número:

```python
def dobro(numero):
    return numero * 2


def triplo(numero):
    return numero * 3
```

Escreve a função `aplicar(funcao, valores)`, que recebe uma função e uma lista de números e devolve uma lista nova, com o resultado da função para cada número. A lista recebida não muda.

Linhas de teste, no fim do ficheiro:

```python
print(aplicar(dobro, [1, 2, 3]))
print(aplicar(triplo, [10]))
print(aplicar(dobro, []))
operacao = triplo
print(aplicar(operacao, [1, 2]))
numeros = [4, 5]
print(aplicar(dobro, numeros), numeros)
```

O teste deve mostrar:

```text
[2, 4, 6]
[30]
[]
[3, 6]
[8, 10] [4, 5]
```

<details>
<summary>Pista</summary>

Compara com o `para_todos` do guia: o que é que o `aplicar` tem de fazer de diferente com o que a função devolve?

</details>

## Critérios de conclusão

- Os exercícios 1, 2, 3, 4, 5, 6, 9, 10, 12, 13, 14, 15, 17, 19 e 20 correm e mostram exatamente o que o enunciado diz.
- As escolhas dos exercícios 3, 7 e 16, e as explicações dos exercícios 8, 9, 14, 17 e 20, estão em comentários, no ficheiro de cada exercício.
- Nos exercícios 11, 13 e 18, cada linha que falhaste tem um comentário com a razão.

![Rodapé](../../imagens/rodape.png)
