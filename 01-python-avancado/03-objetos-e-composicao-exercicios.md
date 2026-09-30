![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento

## Objetivos e organização

Esta ficha serve para praticares sem ajuda o que o [guia](03-objetos-e-composicao.md) explica. Está dividida em quatro grupos, um por cada parte do guia, e cada grupo só precisa da parte do guia que lhe corresponde, indicada na tabela. Podes fazer os grupos em alturas diferentes.

Cada exercício treina uma coisa só, e o enunciado diz qual é. O primeiro exercício de cada grupo é o mais próximo do guia, e os seguintes pedem-te uma decisão pequena que o guia não tomou por ti. O desafio e a secção "Para ires mais longe", no fim, são opcionais, e é lá que estão os casos que enganam.

| Grupo | Parte do guia | Exercícios | Tempo |
| --- | --- | --- | ---: |
| Classes e objetos | Parte 1 | 1, 2 e 3 | 35 min |
| Proteger o estado | Parte 2 | 4 e 5 | 25 min |
| Herança | Parte 3 | 6 | 20 min |
| Composição e agregação | Parte 4 | 7, 8, 9 e 10 | 55 min |
| Desafio opcional | Partes 1 a 4 | | 30 min |
| Para ires mais longe, opcional | Parte 4 | | 15 min |

Os tempos são para quem leu a parte do guia antes de começar o grupo.

## Antes de começar

Material: o computador com o Python 3 e o VS Code, e o guia aberto ao lado.

Cria uma pasta para esta ficha e copia para lá o ficheiro [pokemon.py dos exemplos](../exemplos/python-avancado/ginasio-pokemon/pokemon.py), da mesma forma que no início do [laboratório](03-objetos-e-composicao-laboratorio.md). Vários exercícios usam as classes de Pokémon desse ficheiro, com uma linha como `from pokemon import Pokemon`, e por isso cada exercício deve ser feito num ficheiro dentro desta pasta. Os exercícios 9 e 10 pedem também a classe `Treinador`, que copias do teu `ginasio.py` do laboratório ou do [ginasio.py dos exemplos](../exemplos/python-avancado/ginasio-pokemon/ginasio.py). O desafio e a secção "Para ires mais longe" usam o `ginasio.py` inteiro, e por isso, para esses dois, copia-o também para a pasta da ficha.

Duas regras para toda a ficha. A primeira: quando um exercício te pedir para prever o que um programa escreve, escreve a previsão antes de executar. Se só a escreveres depois, concorda sempre com o computador e não te ensina nada. A segunda: quando um exercício te pedir para explicar, responde em frases completas, com as tuas palavras, como se estivesses a explicar a um colega que faltou à aula.

## Classes e objetos

### Exercício 1: Prever o que um programa escreve (10 min)

Treina: ler uma classe e seguir o `self` (guia, [self: o objeto que está a ser usado](03-objetos-e-composicao.md#self-o-objeto-que-está-a-ser-usado)).

Nos jogos, as bagas são frutos que curam os Pokémon. Esta classe representa uma baga:

```python
class Baga:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    def descricao(self):
        return f"{self.nome} (cura {self.cura})"


oran = Baga("Baga Oran", 10)
sitrus = Baga("Baga Sitrus", 30)
sitrus.cura = sitrus.cura + oran.cura
print(oran.descricao())
print(sitrus.descricao())
```

**a)** Sem executar, escreve as duas linhas que o programa mostra.

**b)** Na segunda chamada ao método `descricao`, que objeto está no `self`? Como é que o Python sabe?

**c)** Executa o programa e compara com a tua previsão. Se falhaste alguma linha, diz em que linha do código o teu raciocínio se afastou do programa.

### Exercício 2: Um método que recebe um Pokémon (15 min)

Treina: escrever um método que usa outro objeto, além do `self` (guia, [Um método que recebe outro objeto](03-objetos-e-composicao.md#um-método-que-recebe-outro-objeto)).

Copia a classe `Baga` do exercício 1 para um ficheiro novo, e acrescenta-lhe um método `dar_a(pokemon)`. Quando se dá uma baga a um Pokémon, o método escreve a frase "Pikachu come a Baga Oran.", com o nome do Pokémon e o da baga, depois soma a cura da baga à vida do Pokémon, e no fim chama o método `verificar_vida` do Pokémon.

No início do ficheiro, antes da classe, importa a classe `Pokemon`:

```python
from pokemon import Pokemon
```

No fim do ficheiro, depois da classe, escreve estas linhas de teste:

```python
pikachu = Pokemon("Pikachu", "Elétrico", 100, 30)
oran = Baga("Baga Oran", 10)
sitrus = Baga("Baga Sitrus", 30)
oran.dar_a(pikachu)
pikachu.vida = 145
sitrus.dar_a(pikachu)
```

Quando o método estiver certo, o teste mostra:

```text
Pikachu come a Baga Oran.
Pikachu tem 110/150 de vida.
Pikachu come a Baga Sitrus.
Pikachu tem 150/150 de vida.
```

Depois de o teste funcionar, responde: o Pikachu tinha 145 de vida e comeu uma baga que cura 30. Porque é que ficou com 150, e não com 175, se o teu método não tem nenhum `if`?

### Exercício 3: Estático ou do objeto (10 min)

Treina: decidir se um método precisa do objeto (guia, [Métodos estáticos: funções que vivem na classe](03-objetos-e-composicao.md#métodos-estáticos-funções-que-vivem-na-classe)).

Queremos acrescentar três métodos à classe `Baga`:

- `cura_valida(valor)`, que recebe um número e devolve `True` se esse número pode ser a cura de uma baga, ou seja, se está entre 1 e 50, incluindo os dois, e `False` se não pode;
- `cura_mais_do_que(outra)`, que recebe outra baga e devolve `True` se esta baga cura mais do que a outra;
- `e_forte()`, que devolve `True` se esta baga cura 30 ou mais.

**a)** Para cada um dos três, diz se deve ser um método estático ou um método normal, com `self`. Justifica cada resposta com a pergunta do guia: este método precisa de saber qual é o objeto?

**b)** Escreve só a primeira linha de cada um dos três métodos, com o decorador por cima, se for preciso.

**c)** Escreve o método `cura_valida` completo, dentro da classe, e testa-o com `print(Baga.cura_valida(10))` e o mesmo para 0, 50 e 51. Os quatro resultados têm de ser `True`, `False`, `True` e `False`.

## Proteger o estado

### Exercício 4: Uma propriedade para um texto (15 min)

Treina: escrever uma propriedade com uma regra (guia, [Propriedades: o get e o set com cara de atributo](03-objetos-e-composicao.md#propriedades-o-get-e-o-set-com-cara-de-atributo)).

Na classe `Baga`, o nome não pode ficar vazio. Transforma o atributo `nome` numa propriedade, com get e set, que aplica esta regra: se alguém tentar dar à baga o texto vazio, `""`, a baga fica com o nome `"Baga sem nome"`. Qualquer outro texto é guardado tal como vem.

A regra tem de se aplicar também quando a baga é criada. Pensa também em onde fica guardado o valor: não pode ser no próprio `nome`.

Testa com estas linhas, no fim do ficheiro:

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

Quando a propriedade estiver certa, o teste mostra:

```text
Baga sem nome
Baga Oran
Baga sem nome
Baga Pecha
```

### Exercício 5: O que o privado deixa e não deixa fazer (10 min)

Treina: prever o efeito dos dois sublinhados (guia, [Público e privado em Python](03-objetos-e-composicao.md#público-e-privado-em-python)).

```python
class Baga:
    def __init__(self, nome, cura):
        self.nome = nome
        self.__cura = cura

    def descricao(self):
        return f"{self.nome} (cura {self.__cura})"


oran = Baga("Baga Oran", 10)
print(oran.descricao())
print(oran.nome)
print(oran._Baga__cura)
print(oran.__cura)
```

**a)** Sem executar, diz, para cada uma das quatro linhas com `print`, se funciona ou dá erro. Para as que funcionam, escreve o que mostram.

**b)** O método `descricao` usa `self.__cura` e funciona. A última linha usa `oran.__cura` e não funciona. Explica a diferença.

**c)** Executa e confirma. O que mostra a terceira linha sobre a proteção que os dois sublinhados dão?

## Herança

### Exercício 6: Um Pokémon elétrico (20 min)

Treina: escrever uma classe-filha que reescreve um método com `super()` (guia, [Reescrever um método](03-objetos-e-composicao.md#reescrever-um-método) e [super() dentro de um método reescrito](03-objetos-e-composicao.md#super-dentro-de-um-método-reescrito)).

Escreve a classe `PokemonEletrico`, filha de `Pokemon`. Um `PokemonEletrico` é sempre do tipo `"Elétrico"`, e por isso o construtor pede só o nome, a vida e o ataque. O dano segue estas regras:

- contra um Pokémon do tipo `"Água"`, tira o dobro do dano base, e antes do ataque escreve "É super eficaz!";
- contra um Pokémon do tipo `"Planta"`, tira metade do dano base, arredondada para baixo, e antes do ataque escreve "Não é muito eficaz...";
- contra os outros tipos, tira o dano base.

O dano base é o que a classe-mãe calcula. Metade de 25, arredondada para baixo, é 12: o operador da divisão inteira, que usaste no 10.º, faz esta conta.

No início do ficheiro, importa as classes de que precisas:

```python
from pokemon import Pokemon, PokemonAgua, PokemonFogo, PokemonPlanta
```

Testa com estas linhas, no fim do ficheiro:

```python
pikachu = PokemonEletrico("Pikachu", 100, 25)
squirtle = PokemonAgua("Squirtle", 100, 20)
bulbasaur = PokemonPlanta("Bulbasaur", 100, 20, 10)
charmander = PokemonFogo("Charmander", 100, 30)
pikachu.atacar(squirtle)
pikachu.atacar(bulbasaur)
pikachu.atacar(charmander)
```

Quando a classe estiver certa, o teste mostra:

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

A tua classe não tem nenhum método `atacar`, e mesmo assim o `pikachu.atacar(...)` funciona e usa a tua regra do dano. Explica numa frase porquê.

## Composição e agregação

### Exercício 7: Herança, agregação ou composição (10 min)

Treina: classificar uma relação com as perguntas do guia (guia, [As perguntas que decidem](03-objetos-e-composicao.md#as-perguntas-que-decidem) e [É um ou tem um: herança, agregação ou composição](03-objetos-e-composicao.md#é-um-ou-tem-um-herança-agregação-ou-composição)).

Para cada uma das cinco relações, decide se é herança, agregação ou composição. Na justificação, usa a frase "é um" ou "tem", e, nas relações "tem", responde às duas perguntas: a parte faz sentido sem o todo? Quem cria a parte? Nas que forem agregação ou composição, diz também como é o losango em UML e de que lado fica.

| | Relação |
| --- | --- |
| a) | Uma Pokédex e os registos que ela própria cria, cada vez que o treinador vê um Pokémon novo. Os registos só existem dentro daquela Pokédex |
| b) | Uma liga e os ginásios que fazem parte dela. Os ginásios já existiam antes de a liga ser criada, e continuam abertos se a liga acabar |
| c) | A classe `PokemonEletrico`, do exercício 6, e a classe `Pokemon` |
| d) | Uma encomenda de uma loja online e as linhas da encomenda. Cada linha diz que produto se comprou e em que quantidade, é criada pela própria encomenda quando o cliente junta um produto ao carrinho, e não faz sentido fora daquela encomenda |
| e) | A mesma encomenda e os produtos do catálogo da loja. O mesmo produto aparece em muitas encomendas, e continua no catálogo quando uma encomenda é apagada |

### Exercício 8: Encontrar a agregação e a composição num programa (15 min)

Treina: reconhecer no código a agregação e a composição (guia, [No código, as duas parecem iguais](03-objetos-e-composicao.md#no-código-as-duas-parecem-iguais)).

Num Centro Pokémon, os treinadores deixam os Pokémon feridos para serem tratados. O centro guarda uma ficha de cada tratamento. Lê o programa com atenção:

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

**a)** Dos dois atributos `pacientes` e `fichas`, qual é uma agregação e qual é uma composição? Para cada um, aponta a linha do código que o mostra e explica porquê.

**b)** Escreve o que prevês que o programa mostra, e só depois executa e compara.

**c)** Depois de `del centro`, que objetos continuam a existir, e que objetos deixaram de poder ser usados? Explica com as palavras agregação e composição.

### Exercício 9: Uma parte criada no construtor (15 min)

Treina: escrever uma composição em que o todo cria a parte no construtor (guia, [Composição: o todo cria e guarda as suas partes](03-objetos-e-composicao.md#composição-o-todo-cria-e-guarda-as-suas-partes)).

Cada treinador tem uma Pokédex, onde fica registado o nome de cada Pokémon diferente que ele capturou. A Pokédex de um treinador é só dele: é criada quando o treinador é criado, e mais ninguém a usa. Esta é a classe `Pokedex`, já pronta:

```python
class Pokedex:
    """Lista dos nomes dos Pokémon que um treinador já registou."""

    def __init__(self):
        self.registados = []

    def registar(self, pokemon):
        if pokemon.nome not in self.registados:
            self.registados.append(pokemon.nome)

    def total(self):
        return len(self.registados)
```

Num ficheiro novo, com a importação `from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta` no início, escreve a classe `Pokedex` e uma cópia da classe `Treinador`.

**a)** Altera a classe `Treinador` de forma que cada treinador crie a sua própria Pokédex, num atributo chamado `pokedex`, e que o método `capturar`, além de juntar o Pokémon à equipa, o registe na Pokédex do treinador.

**b)** Testa com estas linhas, no fim do ficheiro:

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

Quando a alteração estiver certa, o teste mostra:

```text
Ash 2
Misty 1
False
```

**c)** No ginásio do guia, os registos de combate eram criados num método, o `combater`. Aqui, a Pokédex é criada no construtor. Explica porque é que, neste caso, o construtor é o sítio certo, e porque é que a Pokédex não deve chegar ao treinador por parâmetro.

### Exercício 10: Tirar um Pokémon da equipa (15 min)

Treina: alterar uma agregação sem destruir a parte (guia, [Agregação: o todo reúne partes que existem por si](03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si)).

Num ficheiro novo, com a importação `from pokemon import PokemonFogo, PokemonPlanta` no início, escreve uma cópia da classe `Treinador` e acrescenta-lhe um método `libertar(pokemon)`. Se o Pokémon estiver na equipa, o método tira-o da equipa e escreve "Ash liberta Charmander.", com o nome do treinador e o do Pokémon. Se não estiver, não tira nada e escreve "Charmander não está na equipa de Ash.".

Testa com estas linhas, no fim do ficheiro:

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

Quando o método estiver certo, o teste mostra:

```text
Ash liberta Charmander.
Charmander não está na equipa de Ash.
1
Charmander tem 90/150 de vida.
```

Depois de o teste funcionar, responde: o Charmander deixou de estar na equipa, mas a última linha ainda o consegue usar. Porquê? Relaciona a tua resposta com a agregação.

## Desafio opcional: o mesmo Pokémon em duas equipas (30 min)

Na agregação, a mesma parte pode estar em mais do que um todo. No mundo dos Pokémon, isso cria um problema: com a classe `Treinador` do guia, nada impede que dois treinadores capturem o mesmo Pokémon.

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

Altera as classes de forma que um Pokémon que já pertence a um treinador não possa ser capturado por outro. Quando alguém tenta, o `capturar` não junta o Pokémon à equipa e escreve "Starmie já pertence a Misty.". Um Pokémon libertado com o `libertar` do exercício 10 fica sem treinador, e pode voltar a ser capturado.

Antes de escreveres código, decide em que objeto deve ficar guardada a informação de quem é o treinador de cada Pokémon, e em que métodos essa informação tem de ser atualizada. Podes alterar a tua cópia do `pokemon.py`.

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
print(starmie.treinador.nome)
```

Quando as classes estiverem certas, o teste mostra:

```text
Starmie já pertence a Misty.
1 0
0 1
Brock
```

## Para ires mais longe: um histórico que se deixa estragar (15 min)

Um colega acrescentou ao ginásio um método para saber qual foi o último combate:

```python
class Ginasio:
    # O construtor, o combater e o mostrar_historico ficam como estão.

    def ultimo_combate(self):
        """Devolve o registo do último combate."""
        return self.combates[-1]
```

Numa cópia do `ginasio.py`, acrescenta este método à classe `Ginasio` e substitui o programa principal por este:

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

Executa. Os dois históricos, no fim da saída, são diferentes:

```text
Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Misty

Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Ash
```

**a)** Explica porque é que o histórico do ginásio mudou, se o programa principal nunca mexeu na lista `combates`.

**b)** Que característica da composição deixou de ser verdade quando o método `ultimo_combate` foi acrescentado?

**c)** Muda o método `ultimo_combate` de forma que quem o chama fique a saber o resultado do último combate, mas não consiga estragar o histórico do ginásio.

## Critérios de conclusão

Concluíste a ficha quando:

- os testes dos exercícios 2, 3, 4, 6, 9 e 10 mostram exatamente as linhas indicadas no enunciado;
- as tuas previsões dos exercícios 1, 5 e 8 foram escritas antes de executares, e, onde falhaste, sabes dizer em que linha o teu raciocínio se afastou do programa;
- as tuas justificações dos exercícios 3, 7 e 8 usam as perguntas do guia, e não só a resposta final;
- consegues explicar a um colega, sem ler, a diferença entre agregação e composição com o exemplo do ginásio.

![Rodapé](../imagens/rodape.png)
