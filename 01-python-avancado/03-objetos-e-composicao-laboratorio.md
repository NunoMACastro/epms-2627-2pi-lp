![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Objetos, composição e comportamento

Laboratório do tema Objetos, composição e comportamento, do módulo 10794, Programação avançada com Python. Vais construir o ginásio Pokémon, uma classe de cada vez, e depois acrescentar-lhe um líder, os anunciadores dos combates e o registo de cada combate como dataclass. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](03-objetos-e-composicao.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, tens três ficheiros novos ao lado do `pokemon.py`, que já existe. O `ginasio.py` tem o treinador, o líder, o registo de um combate e o ginásio. O `anunciadores.py` tem duas maneiras de anunciar um combate. O `anunciar.py` junta tudo num programa.

```text
ginasio-pokemon/
├── pokemon.py
├── ginasio.py
├── anunciadores.py
└── anunciar.py
```

Pelo caminho, vês no computador ideias que são difíceis só de ler. A equipa de um treinador guarda os mesmos Pokémon que existem fora dele, e não cópias. O mesmo treinador pode desafiar dois ginásios. Quando um ginásio deixa de existir, uns objetos sobrevivem e outros desaparecem. No fim, sabes decidir se uma relação entre objetos é agregação ou composição. Sabes escrever um método de classe que cria objetos e usar objetos de classes diferentes por duck typing. E sabes escrever uma classe de dados com `@dataclass`.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | `ginasio.py`: a classe `Treinador` | Um treinador com uma equipa de Pokémon |
| 2 | `ginasio.py`: só as linhas de teste | A equipa guarda o mesmo Pokémon que existe fora dela |
| 3 | `ginasio.py`: a classe `Combate` | Um registo de combate que se descreve numa linha |
| 4 | `ginasio.py`: a classe `Ginasio`, com o construtor e o histórico | Um ginásio com líder e com as duas listas vazias |
| 5 | `ginasio.py`: o método `combater` e o programa principal | Dois combates a sério, registados no histórico |
| 6 | `ginasio.py`: só o programa principal | O mesmo treinador em dois ginásios, e o que sobrevive a um `del` |
| 7 | `ginasio.py`: o método `com_equipa` e a classe `Lider` | Treinadores criados já com a equipa, e um líder que escolhe de outra maneira |
| 8 | `ginasio.py`: o método `anunciar_combates`; ficheiros novos `anunciadores.py` e `anunciar.py` | Os mesmos combates anunciados de duas maneiras |
| 9 | `ginasio.py`: o `Combate` passa a dataclass | O mesmo ginásio, com o registo escrito em menos linhas |

Escrever os teus próprios decoradores e usar funções como valores não tem fase neste laboratório: praticam-se na ficha de exercícios.

Em todas as fases trabalhas da mesma maneira. Antes de executares, escreves no papel, ou num ficheiro de texto, o que esperas ver. Depois executas e comparas. Quando a saída é diferente da tua previsão, explica a diferença antes de continuares. Uma previsão escrita depois de veres o resultado concorda sempre contigo e não te ensina nada.

As previsões e as perguntas têm a resposta logo a seguir. Responde primeiro, por escrito, e só depois lê a resposta.

## Palavras que vais usar

- Classe: a descrição de um tipo de coisa, que diz que dados tem e o que sabe fazer. `Treinador` e `Ginasio` são classes.
- Objeto: uma coisa concreta criada a partir de uma classe, com os seus próprios valores.
- Atributo: uma variável que pertence a um objeto, como o `nome` ou a `equipa` de um treinador.
- Método: uma função definida dentro de uma classe, que recebe o objeto no `self`.
- Construtor: o método `__init__`, que o Python chama ao criar um objeto, para lhe dar o estado inicial.
- `self`: dentro de um método, o objeto que está a ser usado.
- Propriedade: um atributo cuja leitura chama um método, o get, e cuja alteração chama outro, o set, feitos com `@property`. O `Pokemon` usa-as para manter a vida entre 0 e 150.
- Herança: a relação "é um" entre uma classe-filha e uma classe-mãe, em que a filha recebe tudo o que a mãe tem. Um `Lider` é um `Treinador`.
- `None`: o valor que quer dizer "não há nenhum".
- KO: o estado de um Pokémon com a vida a 0, que já não pode lutar.
- Importar: trazer para um ficheiro uma classe escrita noutro ficheiro da mesma pasta, com uma linha como `from pokemon import PokemonAgua`.
- Todo e parte: numa relação "tem", o objeto que guarda e o objeto guardado. O treinador é o todo, e os Pokémon da equipa são as partes.
- Referência: o que uma variável, uma lista ou um atributo guarda quando guarda um objeto. É um caminho para o objeto, e não uma cópia. Para saber mais, vê a secção "Uma variável guarda uma referência, não uma cópia" do [guia](03-objetos-e-composicao.md#uma-variável-guarda-uma-referência-não-uma-cópia).
- `is`: o operador que pergunta se dois caminhos levam ao mesmo objeto.
- `del`: a instrução que apaga um nome, e não o objeto. O objeto só desaparece quando já nenhum caminho leva a ele.
- Agregação: a relação em que as partes existem por si, são criadas fora do todo, podem estar em vários todos e sobrevivem ao todo. Para saber mais, vê a secção "Agregação: o todo reúne partes que existem por si" do [guia](03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si).
- Composição: a relação em que as partes pertencem ao todo, são criadas por ele, não são partilhadas e desaparecem com ele. Para saber mais, vê a secção "Composição: o todo cria e guarda as suas partes" do [guia](03-objetos-e-composicao.md#composição-o-todo-cria-e-guarda-as-suas-partes).
- Decorador: uma marca com `@` por cima de um `def` ou de uma `class`, que muda a forma como o que está por baixo funciona. `@classmethod` e `@dataclass` são decoradores.
- Método de classe: um método marcado com `@classmethod`, que recebe a classe por onde foi chamado, em vez de um objeto.
- `cls`: num método de classe, o nome do parâmetro que recebe a classe, como o `self` recebe o objeto.
- Construtor alternativo: um método de classe que cria e devolve um objeto de outra forma, além do `__init__`.
- Duck typing: usar um objeto pelo que ele sabe fazer, os seus atributos e métodos, e não pela classe a que pertence.
- Contrato de um método: o que a docstring diz que o objeto recebido tem de ter e de fazer. Em duck typing, é o único sítio onde isso está escrito.
- Dataclass: uma classe que serve sobretudo para guardar dados, marcada com `@dataclass`. O Python escreve o construtor, a forma de mostrar o objeto com `print` e a comparação com `==`.
- Campo: numa dataclass, cada dado que os objetos guardam, escrito com o nome, dois pontos e o tipo.
- Anotação de tipo: a indicação do tipo de valor esperado, depois de dois pontos, como em `vencedor: str`. O Python não a verifica.

## O que precisas

- O Python 3, a partir da versão 3.9, para executar os programas. Confirma que o tens com `python3 --version`. Deve aparecer um número como `Python 3.9.6` ou `Python 3.14.8`, que quer dizer que o Python está instalado e qual é a versão. No Windows, se `python3` não funcionar, experimenta `python --version` ou `py --version`. O laboratório foi ensaiado em Python 3.9 e em Python 3.14, com a mesma saída, e diz onde uma mensagem de erro muda de versão para versão.
- O VS Code, para escreveres os ficheiros e abrires o terminal. Do 10.º ano, já sabes criar uma pasta e um ficheiro nele e abrir o terminal do VS Code na pasta.
- O ficheiro `pokemon.py` dos exemplos, com as classes de Pokémon já escritas. A secção "Preparar o projeto" diz como o copiar e como confirmar que funciona.
- Papel, ou um ficheiro de texto, para escreveres as previsões e as respostas às perguntas.

O laboratório usa o que já sabes do 10.º ano: as variáveis, as listas, o ciclo `for`, as funções com `return`, as f-strings e a docstring. Das listas, usa `append`, `len`, `in` e `not in`. Usa também o que já viste sobre classes: construtor, `self`, métodos, propriedades e herança. O resto explica-se aqui, quando aparece.

O laboratório começa de uma pasta vazia. Não precisas de nenhum ficheiro de outro laboratório.

## Se alguma coisa falhar

1. Estás na pasta certa? O terminal tem de estar na pasta `ginasio-pokemon`. Escreve `pwd` para ver onde estás (no Windows, na linha de comandos clássica, o comando é `cd`). Para mudar de pasta, abre a pasta no VS Code e abre aí um terminal novo, que já começa nela.
2. Guardaste os ficheiros antes de executar? O Python executa o que está guardado no disco, e não o que vês no ecrã. Guarda e executa outra vez.
3. Os ficheiros estão todos na mesma pasta, com o nome exato? Os nomes são `pokemon.py`, `ginasio.py`, `anunciadores.py` e `anunciar.py`, em minúsculas, sem acentos e sem espaços.
4. Apareceu uma mensagem de erro? Lê a última linha. Diz o tipo de erro e o que aconteceu. Procura-a em [Problemas frequentes](#problemas-frequentes).
5. A saída é diferente da que deves ver? Compara o teu ficheiro com o ficheiro completo da paragem mais próxima, linha a linha, a começar pelas indentações. Se te perderes, copia esse ficheiro e recomeça dessa fase.

## Preparar o projeto

As classes de Pokémon já estão feitas e estão no ficheiro `pokemon.py` dos exemplos. O teu `ginasio.py` vai importá-las dele, e por isso os dois ficheiros têm de estar na mesma pasta.

1. Cria uma pasta nova, chamada `ginasio-pokemon`, no sítio onde guardas os trabalhos desta disciplina, e abre-a no VS Code. Abre o terminal do VS Code e escreve `pwd`. Deve aparecer o caminho da pasta `ginasio-pokemon`, o que quer dizer que o terminal está no sítio certo.
2. Abre o ficheiro [pokemon.py dos exemplos](../exemplos/python-avancado/pokemon/03-objetos-e-composicao/pokemon.py). Se tens este repositório no teu computador, copia o ficheiro para a tua pasta. Se o estás a ler no GitHub, usa o botão de copiar o conteúdo do ficheiro, que está por cima do código. Cria na tua pasta um ficheiro novo chamado `pokemon.py`, cola o conteúdo e guarda. Também podes usar o botão de descarregar o ficheiro, ao lado do de copiar, e depois mover o ficheiro descarregado para a tua pasta.
3. Confirma o nome do ficheiro. Tem de ser exatamente `pokemon.py`, tudo em minúsculas e sem acento. Se o descarregaste, o browser pode tê-lo guardado com outro nome, como `pokemon (1).py`, e nesse caso muda-lhe o nome.
4. No terminal, executa o ficheiro, para confirmares que funciona:

```bash
python3 pokemon.py
```

No Windows, se `python3` não funcionar, experimenta `python pokemon.py` ou `py pokemon.py`.

As duas primeiras linhas que deves ver são estas:

```text
Bulbasaur: vida 150, ataque 25
Squirtle: vida 100, ataque 50
```

Se as vês, o ficheiro está no sítio certo e funciona. O resto da saída é uma demonstração que está no fim do `pokemon.py`, com ataques entre três Pokémon.

Essa demonstração está debaixo da linha `if __name__ == "__main__":`. O código debaixo desta linha só corre quando executas esse ficheiro diretamente. Quando outro ficheiro o importa, não corre. É por isso que, nas fases seguintes, o teu `ginasio.py` importa o `pokemon.py` sem fazer aparecer a demonstração.

O que o `pokemon.py` já tem, e que vais usar:

- A classe `Pokemon`, com nome, tipo, vida e ataque. A vida fica sempre entre 0 e 150 e o ataque entre 1 e 50, porque o valor passa por uma propriedade que o corrige.
- Três classes-filhas, `PokemonFogo`, `PokemonAgua` e `PokemonPlanta`. Criam-se só com o nome, a vida e o ataque. A planta pede ainda a regeneração.
- Dois métodos que todos os Pokémon têm. O `atacar(alvo)` ataca outro Pokémon e escreve o que aconteceu. O `verificar_vida()` escreve a vida do Pokémon, ou diz que está KO.
- A vantagem de tipo. O fogo tira o dobro ao tipo planta, a água tira o dobro ao fogo e a planta tira o dobro à água. Nos outros casos, o dano é o valor do ataque, e o programa escreve "É super eficaz!" quando há vantagem.

## Fase 1: Um objeto que guarda outros objetos

Até aqui, os atributos de um objeto guardavam números e textos, como o nome e a vida de um Pokémon. Um atributo também pode guardar outro objeto, ou uma lista de objetos. Um treinador tem uma equipa de Pokémon, e por isso a classe `Treinador` vai ter um atributo `equipa`, que é uma lista de Pokémon.

O treinador não cria os Pokémon. Recebe-os, já criados, com o método `capturar`. Quando um objeto, o todo, guarda outros objetos, as partes, que existem por si e foram criadas fora dele, a relação chama-se agregação. Aqui, o treinador é o todo e os Pokémon da equipa são as partes. Para saber mais, lê a secção "O Treinador e a sua equipa" do [guia](03-objetos-e-composicao.md#o-treinador-e-a-sua-equipa).

1. Cria, na mesma pasta, um ficheiro novo chamado `ginasio.py`. É nele que vais construir o ginásio. Escreve o conteúdo à mão, em vez de o copiares e colares. Ao escrever, reparas em pormenores que a leitura deixa escapar, como o `self` em todos os métodos e a indentação de cada linha. Este é o ficheiro completo, por agora:

```python
"""ginasio.py: o ginásio Pokémon, construído passo a passo no laboratório.

O treinador guarda uma equipa de Pokémon, e o ginásio recebe treinadores e guarda
o registo de cada combate. As classes de Pokémon vêm do ficheiro pokemon.py, que
tem de estar na mesma pasta que este.
"""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


class Treinador:
    """Um treinador tem uma equipa de Pokémon (agregação)."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        # AGREGAÇÃO: a equipa começa vazia e recebe Pokémon que já existiam.
        self.equipa = []

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador."""
        self.equipa.append(pokemon)

    def escolher_pokemon(self):
        """Devolve o primeiro Pokémon da equipa que ainda pode lutar, ou None."""
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                return pokemon
        return None
```

Leitura guiada: começa pela docstring do ficheiro e pela linha `from pokemon import ...`. Ela traz para este ficheiro as três classes de Pokémon do `pokemon.py`. A de água só é usada mais à frente. Depois lê a classe de cima para baixo. O construtor dá ao treinador um `nome` e uma `equipa` vazia. O `capturar` recebe um Pokémon e junta-o à lista, sem o criar. O `escolher_pokemon` percorre a equipa pela ordem em que os Pokémon foram capturados e devolve o primeiro que tem vida. Se chegar ao fim sem encontrar nenhum, devolve `None`.

2. No fim do ficheiro, depois da classe e sem nenhuma indentação, acrescenta estas linhas de teste:

```python
ash = Treinador("Ash")
ash.capturar(PokemonFogo("Charmander", 90, 40))
ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
print(ash.nome, "tem", len(ash.equipa), "Pokémon")
print("Primeiro a lutar:", ash.escolher_pokemon().nome)
```

Leitura guiada: o teste cria o Ash e entrega-lhe dois Pokémon, criados ali mesmo, fora do treinador. Depois escreve quantos Pokémon a equipa tem e o nome do primeiro que vai lutar. As linhas de teste ficam sempre depois das classes. O Python lê o ficheiro de cima para baixo, e uma linha que use `Treinador` antes de a classe ser definida dá erro.

3. Antes de executares, escreve a tua previsão das duas linhas que o teste vai mostrar.

4. Executa o ficheiro no terminal:

```bash
python3 ginasio.py
```

No Windows, se `python3` não funcionar, experimenta `python ginasio.py` ou `py ginasio.py`.

O que deves ver:

```text
Ash tem 2 Pokémon
Primeiro a lutar: Charmander
```

Isto quer dizer que o treinador guardou os dois Pokémon e escolheu o primeiro da equipa, o Charmander, porque tem vida. Se aparecer outra coisa, vê os [problemas frequentes](#problemas-frequentes).

### Paragem 1

Tens um treinador com uma equipa a funcionar. O `capturar` junta Pokémon à equipa, e o `escolher_pokemon` devolve o primeiro que tem vida.

Pensa antes de continuares: o treinador criou o Charmander? A resposta: não. O `PokemonFogo("Charmander", 90, 40)` está escrito nas linhas de teste, fora da classe, e o `capturar` só o recebe. É isso que faz da equipa uma agregação.

## Fase 2: Uma variável guarda uma referência, não uma cópia

Quando escreves `charmander = PokemonFogo("Charmander", 90, 40)`, o Python cria o objeto e a variável `charmander` fica a apontar para ele. A variável não contém o objeto. Ao que ela guarda chama-se uma referência: um caminho para o objeto. Quando entregas `charmander` ao `capturar`, o que entra na lista é outra referência para o mesmo objeto, e não uma cópia. Passam a existir dois caminhos para um só Charmander: a variável e o primeiro lugar da lista.

Há três ferramentas para ver isto. O operador `is` pergunta se dois caminhos levam ao mesmo objeto. A instrução `del` apaga um nome, e não o objeto, que só desaparece quando já nenhum caminho leva a ele. E o valor `None` é o que o `escolher_pokemon` devolve quando não encontra ninguém. Numa agregação, as partes sobrevivem ao todo, e é isso que vais ver. Para saber mais, lê a secção "Uma variável guarda uma referência, não uma cópia" do [guia](03-objetos-e-composicao.md#uma-variável-guarda-uma-referência-não-uma-cópia).

1. Apaga as linhas de teste da fase 1, no fim do `ginasio.py`, e escreve estas no lugar delas:

```python
charmander = PokemonFogo("Charmander", 90, 40)
ash = Treinador("Ash")
ash.capturar(charmander)
print(ash.equipa[0] is charmander)
charmander.vida = 0
print(ash.escolher_pokemon())
del ash
charmander.verificar_vida()
```

Leitura guiada: o teste cria o Charmander numa variável e entrega-o ao Ash. A primeira linha com `print` pergunta se o primeiro lugar da equipa e a variável são o mesmo objeto. Depois muda a vida pela variável e pede ao Ash que escolha um Pokémon. Por fim apaga o nome `ash` e usa o Charmander.

2. Antes de executares, escreve a tua previsão das três linhas que o teste vai mostrar. A segunda é a mais difícil: pensa no que o `escolher_pokemon` devolve quando nenhum Pokémon da equipa tem vida.

3. Executa `python3 ginasio.py` e compara. O que deves ver:

```text
True
None
Charmander está KO (0/150).
```

A primeira linha confirma que há um só Charmander, com dois caminhos. A segunda mostra a consequência: a vida mudou por um caminho e o outro viu-a, por isso o Ash ficou sem Pokémon com vida. A terceira mostra que o Charmander sobreviveu ao `del ash`.

4. Responde por escrito a estas três perguntas.

- **a)** A linha `charmander.vida = 0` mudou a vida através da variável `charmander`, e não através da equipa. Porque é que o `escolher_pokemon` do Ash deixou de encontrar um Pokémon com vida?
- **b)** Depois de `del ash`, porque é que a última linha ainda consegue usar o Charmander?
- **c)** Que característica da agregação mostra a resposta à pergunta b)?

As respostas:

- **a)** Porque há um só Charmander. A lista `equipa` guarda uma referência para o mesmo objeto da variável, e não uma cópia. Mudar a vida pela variável mudou o único Charmander que existe. O `escolher_pokemon` encontrou-o com a vida a 0 e, como não havia mais nenhum na equipa, devolveu `None`.
- **b)** O `del ash` apagou a variável `ash`, o único caminho para o treinador, e o Python libertou o treinador com a sua lista. O Charmander não foi com ele, porque a variável `charmander` ainda aponta para ele.
- **c)** As partes existem por si e continuam a existir quando o todo desaparece. O Charmander foi criado fora do treinador, e por isso há um caminho de fora até ele.

### Paragem 2

A equipa guarda o mesmo objeto que existe fora dela, e apagar o treinador não apaga os Pokémon. Se a tua saída for diferente, confirma que a primeira linha de teste cria o Charmander numa variável, e que o `capturar` recebe essa variável.

## Fase 3: O registo de um combate

O ginásio vai guardar o histórico dos combates. Cada combate fica registado numa linha: quem desafiou, com que Pokémon e quem venceu. Para isso precisas de uma classe pequena, a `Combate`.

O registo guarda nomes, que são textos, e não os objetos `Treinador` e `Pokemon`. Um registo é uma fotografia do que aconteceu. O Pokémon pode perder ou recuperar vida num combate seguinte, e a fotografia de um combate antigo não deve mudar por isso.

Há outra coisa a saber desde já. Este registo vai ser criado só pelo ginásio, e só o ginásio o vai guardar. Quando o todo cria as partes e elas não existem sem ele, a relação chama-se composição. A fase 4 usa esta palavra. Para saber mais, lê o [passo 4 do exemplo guiado](03-objetos-e-composicao.md#passo-4-o-combate) do guia.

1. Escreve a classe `Combate` no `ginasio.py`, a seguir à classe `Treinador` e antes das linhas de teste. Deixa duas linhas em branco entre as classes.

```python
class Combate:
    """Registo de um combate. Só o ginásio cria registos (composição)."""

    def __init__(self, desafiante, pokemon_desafiante, vencedor):
        """Guarda os nomes do desafiante, do seu Pokémon e do vencedor."""
        self.desafiante = desafiante
        self.pokemon_desafiante = pokemon_desafiante
        self.vencedor = vencedor

    def resumo(self):
        """Devolve uma linha de texto que descreve o combate."""
        return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"
```

Leitura guiada: o construtor recebe três textos e guarda cada um num atributo. O `resumo` junta os três numa frase, pronta para escrever no histórico.

2. Apaga as linhas de teste da fase 2 e escreve estas no lugar delas:

```python
registo = Combate("Ash", "Bulbasaur", "Ash")
print(registo.resumo())
```

3. Antes de executares, prevê a linha que o teste vai mostrar. Depois executa `python3 ginasio.py`. O que deves ver:

```text
Ash com Bulbasaur: venceu Ash
```

Isto quer dizer que a classe está bem escrita. O teste criou um registo fora do ginásio, só para confirmares isso. No programa final, os registos são criados apenas pelo ginásio, porque são uma composição. É por isso que apagas estas linhas no início da fase seguinte.

### Paragem 3

A classe `Combate` cria um registo e descreve-o numa linha. Ainda não há ginásio, por isso ainda ninguém guarda registos.

## Fase 4: O ginásio guarda um líder e duas listas

Um ginásio tem um líder, recebe treinadores que o vêm desafiar e guarda o registo dos combates. O líder e os desafiantes são treinadores que já existem fora do ginásio. O ginásio recebe-os e guarda uma referência para cada um, tal como o treinador faz com os Pokémon. É agregação.

Os registos dos combates são diferentes. É o próprio ginásio que os cria, e só ele os guarda. É composição. No código, as duas relações escrevem-se da mesma maneira, com um atributo que guarda objetos, e só os comentários dizem qual é qual. A diferença está em quem cria a parte e em quem a guarda, e vês isso no combate, na fase 5. Para saber mais, lê o [passo 5 do exemplo guiado](03-objetos-e-composicao.md#passo-5-o-ginasio-o-construtor-e-o-histórico) do guia.

1. Escreve a classe `Ginasio` a seguir à classe `Combate`, só com o construtor e com o método `mostrar_historico`. O método `combater` entra na fase seguinte.

```python
class Ginasio:
    """Um ginásio tem um líder e recebe desafiantes (agregação)
    e guarda o registo dos seus combates (composição)."""

    def __init__(self, cidade, lider):
        """Cria um ginásio com a cidade e o líder, e as duas listas vazias."""
        self.cidade = cidade
        self.lider = lider              # AGREGAÇÃO: Treinador criado fora
        self.desafiantes = []           # AGREGAÇÃO: existem sem o ginásio
        self.combates = []              # COMPOSIÇÃO: só o ginásio os cria

    def mostrar_historico(self):
        """Mostra o resumo de todos os combates deste ginásio."""
        print(f"\nHistórico do ginásio de {self.cidade}:")
        for combate in self.combates:
            print(" -", combate.resumo())
```

Leitura guiada: o construtor recebe a cidade e o líder, e cria as duas listas vazias. O líder chega por parâmetro, criado fora do ginásio. A lista dos desafiantes vai receber treinadores que vêm de fora. A lista dos combates vai receber registos que o próprio ginásio cria. O `mostrar_historico` escreve um título e percorre a lista de registos, escrevendo o resumo de cada um. O `\n` no início do título escreve uma linha em branco antes dele.

2. Apaga as linhas de teste da fase 3 e escreve estas no lugar delas:

```python
misty = Treinador("Misty")
misty.capturar(PokemonAgua("Starmie", 120, 35))
cerulean = Ginasio("Cerulean", misty)
print(cerulean.lider is misty)
print(len(cerulean.desafiantes), len(cerulean.combates))
cerulean.mostrar_historico()
```

3. Antes de executares, escreve a tua previsão. Repara que o `mostrar_historico` começa com um `\n`. Depois executa `python3 ginasio.py` e compara. A saída deve ser esta, com uma linha em branco antes do título do histórico:

```text
True
0 0

Histórico do ginásio de Cerulean:
```

O `True` mostra que o líder do ginásio e a variável `misty` são o mesmo objeto. O ginásio recebeu a treinadora por parâmetro e guardou uma referência para ela, e não uma cópia. As duas listas estão vazias, porque ainda não houve combates, e por isso o histórico só tem o título.

### Paragem 4

O ginásio existe, com o líder e as duas listas. Falta o método que faz um combate.

## Fase 5: O ginásio organiza um combate

Falta o método `combater`. Cada classe faz o trabalho que lhe pertence. O ginásio não percorre a equipa de ninguém à procura de um Pokémon com vida: pede a cada treinador que escolha, com o `escolher_pokemon`.

O combate é um ciclo que se repete até um Pokémon ficar KO. Vais usar um `while True`, um ciclo que só acaba quando o programa chega a um `break`. Em cada volta, o Pokémon do desafiante ataca primeiro. Se o defensor ficou KO, o desafiante vence e o ciclo acaba. Senão, o defensor ataca, e o mesmo teste é feito ao atacante.

Um `while True` só é seguro se houver a certeza de que um `break` acaba por acontecer. Aqui há, porque o ataque de um Pokémon nunca é menor do que 1, e cada ataque tira pelo menos 1 de vida. No fim, o ginásio cria o registo e guarda-o na lista `combates`. É a composição. Para saber mais, lê o [passo 6 do exemplo guiado](03-objetos-e-composicao.md#passo-6-o-método-combater) do guia.

1. Escreve o método `combater` dentro da classe `Ginasio`, entre o construtor e o `mostrar_historico`. Cuidado com a indentação: o método tem quatro espaços, as linhas dentro dele têm oito, e as linhas dentro do `while` e dos `if` têm doze ou dezasseis. A linha `class Ginasio:` e o comentário do bloco só mostram onde o método fica: escreve só o `def` e o que está debaixo dele, dentro da classe que já tens. Se escreveres também a linha `class`, crias uma segunda classe `Ginasio`, que apaga a primeira.

```python
class Ginasio:
    # O construtor fica por cima deste método, e o mostrar_historico por baixo.

    def combater(self, desafiante):
        """Um combate entre o primeiro Pokémon com vida de cada treinador."""
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
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
```

Leitura guiada: as duas primeiras linhas juntam o desafiante à lista de desafiantes, se ainda lá não estiver. O `not in` evita que o mesmo treinador apareça duas vezes. Depois o método pede a cada treinador o seu Pokémon. Ao do desafiante chama `atacante`, porque ataca primeiro, e ao do líder chama `defensor`. Se um dos treinadores não tem Pokémon com vida, o `escolher_pokemon` devolveu `None`. O `if` seguinte escreve uma mensagem e sai com `return`, sem fazer combate nem registo. Sem este `if`, o ciclo tentava pôr o `None` a atacar e dava erro. O resto é o ciclo do combate. A última linha é a composição: o registo nasce dentro do ginásio e fica no ginásio.

2. Apaga as linhas de teste da fase 4 e escreve, no fim do ficheiro, o programa principal. Fica debaixo de `if __name__ == "__main__":`, para só correr quando executas o `ginasio.py` diretamente. Na fase 8, outros ficheiros vão importar o `ginasio.py`, e não queremos que o combate corra de cada vez que isso acontece.

```python
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

Leitura guiada: o programa cria a Misty com um Starmie e o Ash com um Charmander e um Bulbasaur. Depois cria o ginásio de Cerulean e o Ash desafia-o duas vezes. Mostra o histórico, apaga o ginásio com `del` e escreve quantos Pokémon cada treinador ainda tem. Os dois comentários dizem o que o `del` faz aos registos.

3. Antes de executares, faz no papel a tabela do primeiro combate, com uma linha por ataque, com o dano e a vida dos dois Pokémon depois de cada ataque. Os dados são estes. A Misty tem um Starmie, de água, com 120 de vida e 35 de ataque. O Ash tem um Charmander, de fogo, com 90 de vida e 40 de ataque. Tem também um Bulbasaur, de planta, com 110 de vida, 25 de ataque e 20 de regeneração. O Charmander luta primeiro, porque é o primeiro da equipa. A água tem vantagem contra o fogo. Escreve também quem achas que ganha o segundo combate, e porquê.

4. Executa `python3 ginasio.py` e compara com a tua tabela. A saída é esta. A primeira linha está em branco, por causa do `\n` do título do combate:

```text

=== Ash desafia Misty no ginásio de Cerulean ===
Charmander ataca Starmie e tira 40 de vida.
Starmie tem 80/150 de vida.
É super eficaz!
Starmie ataca Charmander e tira 70 de vida.
Charmander tem 20/150 de vida.
Charmander ataca Starmie e tira 40 de vida.
Starmie tem 40/150 de vida.
É super eficaz!
Starmie ataca Charmander e tira 70 de vida.
Charmander está KO (0/150).

=== Ash desafia Misty no ginásio de Cerulean ===
É super eficaz!
Bulbasaur ataca Starmie e tira 50 de vida.
Starmie está KO (0/150).

Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Misty
 - Ash com Bulbasaur: venceu Ash

Ash continua com 2 Pokémon; Misty continua com 1.
```

A tua tabela do primeiro combate devia ser esta:

| Ataque | Quem ataca | Dano | Vida do Charmander | Vida do Starmie |
| --- | --- | ---: | ---: | ---: |
| Antes | | | 90 | 120 |
| 1 | Charmander | 40 | 90 | 80 |
| 2 | Starmie, super eficaz | 70 | 20 | 80 |
| 3 | Charmander | 40 | 20 | 40 |
| 4 | Starmie, super eficaz | 70 | 0 | 40 |

No quarto ataque, o Charmander fica KO, e a Misty vence. No segundo combate, o `escolher_pokemon` do Ash salta o Charmander, que tem 0 de vida, e escolhe o Bulbasaur. O da Misty escolhe o Starmie, que continua com os 40 de vida com que ficou. Ninguém o curou, porque o ginásio trabalha com os Pokémon verdadeiros das equipas, e não com cópias. O Bulbasaur, de planta, tem vantagem contra a água e tira 50, e o Starmie fica KO logo no primeiro ataque. O Ash vence. O "É super eficaz!" aparece antes da linha do ataque, porque é escrito dentro do cálculo do dano, que o `atacar` faz antes de escrever a sua linha.

5. Responde por escrito: se o programa principal tivesse um terceiro `cerulean.combater(ash)`, logo a seguir aos outros dois, o que escrevia esse terceiro combate? Porquê? Que relação entre classes explica isto?

A resposta: não há terceiro combate. O método escreve "Não há combate: um dos treinadores não tem Pokémon com vida." e sai sem criar registo. O `escolher_pokemon` do Ash devolve o Bulbasaur, mas o da Misty devolve `None`. O Starmie é o mesmo objeto que ficou KO no segundo combate e continua com a vida a 0. É a agregação: a equipa da Misty guarda o Starmie que foi criado fora, e o ginásio guarda uma referência à Misty, e não cópias. Para confirmares, acrescenta a linha, executa e volta a apagá-la. O histórico continua com os dois combates.

### Paragem 5

Tens o ginásio completo, com dois combates e o histórico. O ficheiro `ginasio.py` completo, como deve estar agora:

```python
"""ginasio.py: o ginásio Pokémon, construído passo a passo no laboratório.

O treinador guarda uma equipa de Pokémon, e o ginásio recebe treinadores e guarda
o registo de cada combate. As classes de Pokémon vêm do ficheiro pokemon.py, que
tem de estar na mesma pasta que este.
"""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


class Treinador:
    """Um treinador tem uma equipa de Pokémon (agregação)."""

    def __init__(self, nome):
        """Cria um treinador com um nome e a equipa vazia."""
        self.nome = nome
        # AGREGAÇÃO: a equipa começa vazia e recebe Pokémon que já existiam.
        self.equipa = []

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador."""
        self.equipa.append(pokemon)

    def escolher_pokemon(self):
        """Devolve o primeiro Pokémon da equipa que ainda pode lutar, ou None."""
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                return pokemon
        return None


class Combate:
    """Registo de um combate. Só o ginásio cria registos (composição)."""

    def __init__(self, desafiante, pokemon_desafiante, vencedor):
        """Guarda os nomes do desafiante, do seu Pokémon e do vencedor."""
        self.desafiante = desafiante
        self.pokemon_desafiante = pokemon_desafiante
        self.vencedor = vencedor

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
        """Um combate entre o primeiro Pokémon com vida de cada treinador."""
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
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

## Fase 6: Duas experiências com as relações

Na agregação, a mesma parte pode estar em mais do que um todo. Na composição, as partes desaparecem com o todo. Vais ver as duas coisas no computador.

O Ash vai desafiar dois ginásios: o de Cerulean, da Misty, e o de Celadon, da Erika. A Erika tem uma Tangela, de planta, com 50 de vida, 20 de ataque e 10 de regeneração. Depois, o ginásio de Cerulean vai ser apagado com `del`, e vais ver o que sobrevive. Para saber mais, lê o [passo 8 do exemplo guiado](03-objetos-e-composicao.md#passo-8-o-que-sobrevive-quando-o-ginásio-desaparece) do guia.

1. Substitui todo o programa principal, desde a linha `if __name__ == "__main__":` até ao fim do ficheiro, por este:

```python
if __name__ == "__main__":
    misty = Treinador("Misty")
    misty.capturar(PokemonAgua("Starmie", 120, 35))
    erika = Treinador("Erika")
    erika.capturar(PokemonPlanta("Tangela", 50, 20, 10))
    ash = Treinador("Ash")
    ash.capturar(PokemonFogo("Charmander", 90, 40))
    ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
    cerulean = Ginasio("Cerulean", misty)
    celadon = Ginasio("Celadon", erika)
    cerulean.combater(ash)
    cerulean.combater(ash)
    celadon.combater(ash)
    print()
    print(ash in cerulean.desafiantes, ash in celadon.desafiantes)
    print(cerulean.desafiantes[0] is celadon.desafiantes[0])
    del cerulean
    celadon.mostrar_historico()
    print(ash.nome, "continua com", len(ash.equipa), "Pokémon")
```

Leitura guiada: o programa cria os três treinadores e os dois ginásios. O Ash desafia Cerulean duas vezes e Celadon uma vez. O `print()` sozinho escreve uma linha em branco. A linha com `in` pergunta se o Ash está na lista de desafiantes de cada ginásio. A linha com `is` pergunta se o treinador da lista de Cerulean e o da lista de Celadon são o mesmo objeto. O `del cerulean` apaga o ginásio, e as duas últimas linhas mostram o que ficou.

2. Antes de executares, escreve as tuas previsões. Que Pokémon do Ash luta em Celadon, e com quanta vida começa? Quem ganha? O que escrevem as duas linhas com `in` e com `is`? O que mostra o histórico de Celadon depois de `del cerulean`?

3. Executa `python3 ginasio.py` e compara. Os dois combates de Cerulean são iguais aos da fase 5. A partir do combate de Celadon, a saída é esta:

```text
=== Ash desafia Erika no ginásio de Celadon ===
Bulbasaur ataca Tangela e tira 25 de vida.
Tangela tem 25/150 de vida.
Tangela ataca Bulbasaur e tira 20 de vida.
Bulbasaur tem 90/150 de vida.
Bulbasaur ataca Tangela e tira 25 de vida.
Tangela está KO (0/150).

True True
True

Histórico do ginásio de Celadon:
 - Ash com Bulbasaur: venceu Ash
Ash continua com 2 Pokémon
```

Em Celadon luta o Bulbasaur, com 110 de vida: o Charmander ficou KO no primeiro combate de Cerulean, e o Bulbasaur não levou nenhum ataque no segundo. O Ash ganha em dois ataques do Bulbasaur, com a Tangela a atacar uma vez pelo meio. Não há "É super eficaz!" em Celadon: o Bulbasaur e a Tangela são os dois de planta, e nenhum tem vantagem sobre o outro.

4. Responde por escrito.

- **a)** A linha com `is` escreveu `True`. O que quer isto dizer sobre o treinador que está na lista de desafiantes de Cerulean e o que está na de Celadon? Que característica da agregação mostra?
- **b)** Depois de `del cerulean`, o histórico de Celadon continua completo, e o Ash continua com os dois Pokémon. E os registos dos dois combates de Cerulean: ainda há alguma forma de lhes chegar? Que característica da composição mostra a tua resposta?

As respostas:

- **a)** O `True` quer dizer que o treinador da lista de Cerulean e o da lista de Celadon são o mesmo objeto, o Ash. A mesma parte está em dois todos ao mesmo tempo. A agregação permite isso, e a composição não.
- **b)** Não há forma de chegar aos registos de Cerulean. Só a lista `combates` do ginásio de Cerulean apontava para eles, e essa lista desapareceu com o ginásio quando o `del cerulean` apagou o último caminho para ele. Na composição, as partes desaparecem com o todo. O `del` só apagou o nome `cerulean`. Os registos deixaram de existir porque ficaram sem caminho. O histórico de Celadon não foi afetado, porque os seus registos são de outro todo.

### Paragem 6

O mesmo treinador desafiou dois ginásios, e apagar um deles apagou os seus registos mas não os treinadores nem os Pokémon. Tens agora a base das fases seguintes.

## Fase 7: O líder e o construtor alternativo

Criar um treinador com uma equipa leva uma linha para o treinador e uma linha por cada Pokémon. Dava jeito criar o treinador numa só linha, já com a equipa. Uma segunda maneira de criar objetos, ao lado do construtor, chama-se construtor alternativo. Em Python, escreve-se com um método de classe.

Um método de classe leva por cima a linha `@classmethod`. Essa marca chama-se decorador e muda a forma como o método funciona. O Python passa-lhe a classe por onde foi chamado, num primeiro parâmetro que se chama `cls`, por convenção, como o do objeto se chama `self`. Em `Treinador.com_equipa(...)`, o `cls` é `Treinador`. Em `Lider.com_equipa(...)`, o `cls` é `Lider`.

É por isso que o método cria o objeto com `cls(nome)` e não com `Treinador(nome)`: assim, cria um objeto da classe que o chamou. Um método estático, que não recebe a classe, criaria sempre um `Treinador`, mesmo quando chamado pelo `Lider`.

Um `Lider` é um treinador, e por isso herda da classe `Treinador`. Escolhe de outra maneira: um treinador escolhe o primeiro Pokémon da equipa com vida, e um líder escolhe o que tem mais vida. Para saber mais, lê as secções [O método de classe recebe a classe](03-objetos-e-composicao.md#o-método-de-classe-recebe-a-classe) e [O líder, um treinador que escolhe de outra maneira](03-objetos-e-composicao.md#o-líder-um-treinador-que-escolhe-de-outra-maneira) do guia.

1. Na classe `Treinador` do teu `ginasio.py`, acrescenta o método de classe `com_equipa`, entre o construtor e o `capturar`. Não te esqueças da linha `@classmethod` por cima do `def`. A linha `class Treinador:` e o comentário do bloco só mostram onde o método fica. Escreve só o `@classmethod` e o `def`, com o que está debaixo dele, dentro da classe que já tens. Se escreveres também a linha `class`, crias uma segunda classe `Treinador`, que apaga a primeira.

```python
class Treinador:
    # O construtor fica por cima deste método, e o capturar por baixo.

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
```

Leitura guiada: o método recebe a classe em `cls`, o nome e uma lista de Pokémon. Cria o treinador com `cls(nome)`, captura cada Pokémon da lista e devolve o treinador pronto. Usa o `capturar` do próprio treinador, e não `treinador.equipa.append`: se um dia a captura tiver uma regra, o construtor alternativo passa a cumpri-la sem ninguém lhe mexer.

2. A seguir à classe `Treinador`, e antes da classe `Combate`, escreve a classe `Lider`, com o seu `escolher_pokemon`:

```python
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
```

Leitura guiada: o `Lider` não tem construtor próprio, e herda o do `Treinador`, que só pede o nome. É isso que permite ao `com_equipa`, escrito na classe-mãe, servir também à filha: `cls(nome)` funciona nas duas. O método percorre a equipa e vai guardando em `escolhido` o melhor Pokémon encontrado até ali. Começa em `None`, porque ainda não viu nenhum. No fim, devolve o escolhido, que continua `None` se nenhum Pokémon tinha vida.

3. Substitui todo o programa principal, desde a linha `if __name__ == "__main__":` até ao fim do ficheiro, por este:

```python
if __name__ == "__main__":
    erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10), PokemonPlanta("Gloom", 80, 25, 5)])
    ash = Treinador.com_equipa("Ash", [PokemonAgua("Squirtle", 100, 30), PokemonFogo("Charmander", 90, 40)])
    print(type(erika).__name__, len(erika.equipa))
    print(type(ash).__name__, len(ash.equipa))
    print(erika.escolher_pokemon().nome, ash.escolher_pokemon().nome)
    celadon = Ginasio("Celadon", erika)
    celadon.combater(ash)
    celadon.combater(ash)
    celadon.mostrar_historico()
```

Leitura guiada: o programa cria a Erika como `Lider` e o Ash como `Treinador`, cada um com a equipa dada numa só linha. A função `type` devolve a classe de um objeto, e o `.__name__` dá o nome dessa classe. As três linhas com `print` mostram a classe e o tamanho da equipa de cada um e o Pokémon que cada um escolhe. Depois, o Ash desafia o ginásio de Celadon duas vezes.

4. Antes de executares, escreve a tua previsão das três primeiras linhas. Não precisas de prever os combates ataque a ataque.

5. Executa `python3 ginasio.py` e compara. A saída é esta:

```text
Lider 2
Treinador 2
Gloom Squirtle

=== Ash desafia Erika no ginásio de Celadon ===
Squirtle ataca Gloom e tira 30 de vida.
Gloom tem 50/150 de vida.
É super eficaz!
Gloom ataca Squirtle e tira 50 de vida.
Squirtle tem 50/150 de vida.
Squirtle ataca Gloom e tira 30 de vida.
Gloom tem 20/150 de vida.
É super eficaz!
Gloom ataca Squirtle e tira 50 de vida.
Squirtle está KO (0/150).

=== Ash desafia Erika no ginásio de Celadon ===
É super eficaz!
Charmander ataca Tangela e tira 80 de vida.
Tangela está KO (0/150).

Histórico do ginásio de Celadon:
 - Ash com Squirtle: venceu Erika
 - Ash com Charmander: venceu Ash
```

As três primeiras linhas dizem que a Erika é um `Lider` com dois Pokémon e que o Ash é um `Treinador` com dois. Dizem também que a Erika escolhe o Gloom e que o Ash escolhe o Squirtle. A Erika escolhe o Gloom porque, como líder, escolhe o Pokémon com mais vida: 80, contra os 50 da Tangela. O Ash escolhe o Squirtle porque é o primeiro da equipa com vida.

6. Responde por escrito.

- **a)** No `com_equipa` não há nenhuma linha com a palavra `Lider`. Que linha faz com que a Erika saia um `Lider`?
- **b)** No primeiro combate, a Erika lutou com o Gloom. No segundo, lutou com a Tangela. Porque é que mudou de Pokémon? Procura, na saída do primeiro combate, a vida com que o Gloom acabou.
- **c)** Muda, só por um momento, a primeira linha do programa principal para `erika = Treinador.com_equipa(...)`, com a mesma equipa. Antes de executar, prevê que Pokémon escolhe a Erika no primeiro combate e quem ganha cada um dos dois combates. Executa, compara e volta a pôr `Lider`.

As respostas:

- **a)** A linha `treinador = cls(nome)`. Em `Lider.com_equipa(...)`, o `cls` é `Lider`, e chamar `cls(nome)` é chamar o construtor do `Lider`, que é o herdado do `Treinador`.
- **b)** O Gloom acabou o primeiro combate com 20 de vida, e a Tangela continua com 50. O líder escolhe sempre o Pokémon com mais vida, que no segundo combate é a Tangela. O Squirtle tirou 30 de cada vez ao Gloom. O Gloom tirou 50 ao Squirtle, o dobro do seu ataque, porque a planta tem vantagem contra a água.
- **c)** Com `Treinador.com_equipa`, a Erika escolhe o primeiro Pokémon da equipa com vida, a Tangela. No primeiro combate, o Squirtle tira 30 de cada vez à Tangela, que tem 50, e ganha no segundo ataque, ficando com 60 de vida. No segundo combate, o Squirtle, com 60, enfrenta o Gloom, com 80, e perde. O histórico fica `Ash com Squirtle: venceu Ash` e `Ash com Squirtle: venceu Erika`, e o Charmander nunca chega a lutar. Os resultados trocam: a forma como o líder escolhe muda o desfecho dos combates. Com um método estático que escrevesse `Treinador(nome)`, a Erika seria sempre uma treinadora normal, e era este o resultado, sem nenhuma mensagem de erro.

### Paragem 7

Os treinadores criam-se com a equipa numa só linha, e a Erika é um `Lider`. O ficheiro `ginasio.py` completo, como deve estar agora:

```python
"""ginasio.py: o ginásio Pokémon, construído passo a passo no laboratório.

O treinador guarda uma equipa de Pokémon, e o ginásio recebe treinadores e guarda
o registo de cada combate. As classes de Pokémon vêm do ficheiro pokemon.py, que
tem de estar na mesma pasta que este.
"""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


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
        """Junta à equipa um Pokémon que foi criado fora do treinador."""
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


class Combate:
    """Registo de um combate. Só o ginásio cria registos (composição)."""

    def __init__(self, desafiante, pokemon_desafiante, vencedor):
        """Guarda os nomes do desafiante, do seu Pokémon e do vencedor."""
        self.desafiante = desafiante
        self.pokemon_desafiante = pokemon_desafiante
        self.vencedor = vencedor

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
        """Um combate entre o primeiro Pokémon com vida de cada treinador."""
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
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


if __name__ == "__main__":
    erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10), PokemonPlanta("Gloom", 80, 25, 5)])
    ash = Treinador.com_equipa("Ash", [PokemonAgua("Squirtle", 100, 30), PokemonFogo("Charmander", 90, 40)])
    print(type(erika).__name__, len(erika.equipa))
    print(type(ash).__name__, len(ash.equipa))
    print(erika.escolher_pokemon().nome, ash.escolher_pokemon().nome)
    celadon = Ginasio("Celadon", erika)
    celadon.combater(ash)
    celadon.combater(ash)
    celadon.mostrar_historico()
```

## Fase 8: Anunciar os combates, sem herança

O ginásio quer anunciar os combates de mais do que uma maneira. Para o público, um narrador que conta cada combate com entusiasmo. Para a parede do ginásio, um placard que mostra cada combate numa linha curta e numerada. E amanhã pode querer outra maneira, sem ter de mudar o ginásio.

Basta que o ginásio peça uma só coisa a quem anuncia: um método `anunciar`, que recebe um combate. As classes que anunciam não precisam de ser parentes umas das outras. Só precisam de ter esse método. A isto chama-se duck typing: em Python, usa-se um objeto pelo que ele sabe fazer, e não pela classe a que pertence.

O Python só verifica se o método existe quando a linha que o chama corre. Como nada confirma o que o ginásio espera, esse contrato escreve-se na docstring do método. Para saber mais, lê a secção [Duck typing: o que conta é o comportamento](03-objetos-e-composicao.md#duck-typing-o-que-conta-é-o-comportamento) do guia.

1. Acrescenta à classe `Ginasio` o método `anunciar_combates`, no fim da classe, depois do `mostrar_historico`. A linha `class Ginasio:` e o comentário do bloco só mostram onde o método fica: escreve só o `def` e o que está debaixo dele, dentro da classe que já tens. Se escreveres também a linha `class`, crias uma segunda classe `Ginasio`, que apaga a primeira.

```python
class Ginasio:
    # O construtor, o combater e o mostrar_historico ficam por cima deste método.

    def anunciar_combates(self, anunciador):
        """Entrega cada combate ao anunciador, para ele o anunciar.

        O anunciador pode ser um objeto de qualquer classe, desde que tenha o
        método anunciar(combate). O ginásio não quer saber de que classe é.
        """
        for combate in self.combates:
            anunciador.anunciar(combate)
```

Leitura guiada: o método recebe um anunciador e chama `anunciador.anunciar(combate)` para cada combate da lista. Não diz de que classe tem de ser o anunciador, nem verifica nada. A docstring é o contrato: diz o que o anunciador tem de ter.

2. Cria, na mesma pasta, um ficheiro novo chamado `anunciadores.py`, com este conteúdo:

```python
"""Anunciadores de combates: duck typing, o código das aulas de Python avançado.

O Ginasio, no ficheiro ginasio.py, anuncia os combates com
anunciador.anunciar(combate). Estas duas classes não têm nenhuma classe-mãe em
comum, nem com o ginásio: só têm um método com o mesmo nome e os mesmos
parâmetros. Para o ginásio, é quanto basta.
"""


class Narrador:
    """Anuncia cada combate como um locutor, com entusiasmo."""

    def anunciar(self, combate):
        """Escreve o anúncio do combate, numa frase longa."""
        print(f"E atenção! {combate.desafiante} entrou com {combate.pokemon_desafiante}...")
        print(f"... e o vencedor é {combate.vencedor}! Que combate!")


class Placard:
    """Mostra cada combate numa linha curta, como um placard do ginásio."""

    def __init__(self):
        """Cria o placard com o contador de combates a zero."""
        self.numero = 0

    def anunciar(self, combate):
        """Escreve uma linha numerada com o desafiante e o vencedor."""
        self.numero = self.numero + 1
        print(f"[{self.numero}] {combate.desafiante} | vencedor: {combate.vencedor}")
```

Leitura guiada: o `Narrador` escreve duas linhas por combate. O `Placard` escreve uma, com um número que vai contando, e por isso tem um construtor que põe o `numero` a zero. As duas classes são diferentes por dentro e não têm nenhuma classe-mãe em comum. Têm uma só coisa igual: um método `anunciar` que recebe um combate. Os dois usam os atributos do `Combate` da fase 3: `desafiante`, `pokemon_desafiante` e `vencedor`.

3. Cria outro ficheiro novo, `anunciar.py`, com este programa:

```python
"""anunciar.py: faz três combates no ginásio de Celadon e anuncia-os de duas maneiras."""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador
from anunciadores import Narrador, Placard

erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10), PokemonPlanta("Gloom", 80, 25, 5)])
ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])
gary = Treinador.com_equipa("Gary", [PokemonAgua("Psyduck", 60, 20)])
celadon = Ginasio("Celadon", erika)
celadon.combater(ash)
celadon.combater(gary)
celadon.combater(ash)

print("\n--- Placard ---")
celadon.anunciar_combates(Placard())
print("\n--- Narrador ---")
celadon.anunciar_combates(Narrador())
```

Leitura guiada: o programa importa as classes dos três ficheiros. Cria a Erika como líder e dois desafiantes, faz três combates no ginásio de Celadon e anuncia os combates duas vezes, uma com cada anunciador. O programa fica num ficheiro à parte, de propósito: o `ginasio.py` não importa os anunciadores nem precisa de os conhecer. Quem junta o ginásio aos anunciadores é o `anunciar.py`.

4. Antes de executares, prevê quem vence cada um dos três combates. Uma pista: a Erika é líder, e um líder escolhe sempre o Pokémon com mais vida. Depois, prevê as três linhas do placard.

5. Executa `python3 anunciar.py` e compara. A saída é esta:

```text

=== Ash desafia Erika no ginásio de Celadon ===
É super eficaz!
Charmander ataca Gloom e tira 80 de vida.
Gloom está KO (0/150).

=== Gary desafia Erika no ginásio de Celadon ===
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

=== Ash desafia Erika no ginásio de Celadon ===
É super eficaz!
Charmander ataca Tangela e tira 80 de vida.
Tangela está KO (0/150).

--- Placard ---
[1] Ash | vencedor: Ash
[2] Gary | vencedor: Erika
[3] Ash | vencedor: Ash

--- Narrador ---
E atenção! Ash entrou com Charmander...
... e o vencedor é Ash! Que combate!
E atenção! Gary entrou com Psyduck...
... e o vencedor é Erika! Que combate!
E atenção! Ash entrou com Charmander...
... e o vencedor é Ash! Que combate!
```

No primeiro combate, a Erika escolhe o Gloom, que tem mais vida, e o Charmander ganha logo, porque o fogo tira o dobro à planta. No segundo, o Gloom já está KO, e a Erika escolhe a Tangela. O Psyduck, de água, não tem vantagem contra a planta, e perde. No terceiro, a Tangela só tem 10 de vida, e o Charmander ganha.

6. Responde por escrito.

- **a)** O `ginasio.py` não tem nenhuma linha que fale de `Narrador` ou de `Placard`. Como é que o `anunciar_combates` consegue usar os dois?
- **b)** Acrescenta, no fim do `anunciar.py`, a linha `celadon.anunciar_combates(ash)`, que entrega o treinador Ash ao ginásio como se fosse um anunciador. Antes de executar, prevê o que acontece e em que momento. Executa, compara e apaga a linha.

As respostas:

- **a)** O `anunciar_combates` não precisa de saber de que classe é o anunciador. Só chama `anunciador.anunciar(combate)`. Os objetos `Narrador()` e `Placard()` são criados no `anunciar.py` e entregues ao ginásio como argumento, e o ginásio usa-os pelo que sabem fazer. É o duck typing.
- **b)** Os combates, o placard e o narrador aparecem como antes. Depois, a tentativa de anunciar o primeiro combate com o Ash dá `AttributeError: 'Treinador' object has no attribute 'anunciar'`. O erro só acontece quando a linha `anunciador.anunciar(combate)` corre, e isso é logo no primeiro combate da lista, porque havia combates. O Python entra no método sem verificar nada, e só falha dentro do ciclo. A mensagem é a mesma nas duas versões do Python.

### Paragem 8

O mesmo método, `anunciar_combates`, deu dois resultados diferentes conforme o objeto que recebeu, e o ginásio não mudou uma linha. Para acrescentar uma terceira maneira de anunciar, bastava escrever uma classe nova com um método `anunciar(self, combate)`.

## Fase 9: O registo como dataclass

O construtor do `Combate` obriga a escrever cada nome três vezes: no parâmetro, no atributo e no valor que o atributo recebe. Além disso, o objeto faz duas coisas mal. O `print` de um registo mostra só o sítio da memória onde ele está, e não o que ele guarda. E o `==` entre dois registos com os mesmos dados dá `False`, porque pergunta se são o mesmo objeto.

Uma dataclass é uma classe que serve sobretudo para guardar dados, escrita de forma que o Python faça o trabalho repetitivo. Em vez do construtor, dizes quais são os dados, e o Python escreve o construtor, a forma de mostrar o objeto com `print` e a comparação com `==`. Cada dado é um campo: escreve-se com o nome, dois pontos e o tipo, como em `vencedor: str`. A parte `: str` chama-se anotação de tipo. O Python não verifica o tipo, mas é pela anotação que sabe que aquela linha é um campo.

A marca `@dataclass` por cima da classe é um decorador, como o `@classmethod` da fase 7. A diferença é que este está por cima de uma classe, e muda a classe inteira. O `dataclass` vem de um módulo chamado `dataclasses`, que já vem com o Python. Para saber mais, lê as secções [A mesma classe como dataclass](03-objetos-e-composicao.md#a-mesma-classe-como-dataclass) e [O que a dataclass escreve por ti](03-objetos-e-composicao.md#o-que-a-dataclass-escreve-por-ti) do guia.

1. Antes de mexeres na classe `Combate`, acrescenta estas linhas ao fim do `anunciar.py`:

```python
print()
print(celadon.combates[0])
print(celadon.combates[0] == celadon.combates[2])
print(celadon.combates[0] is celadon.combates[2])
```

Leitura guiada: o primeiro e o terceiro combates de Celadon foram entre o Ash e a Erika, ganhos pelo Ash, com o Charmander. As três linhas mostram um registo, perguntam se os dois são iguais pelos dados e perguntam se são o mesmo objeto.

2. Executa `python3 anunciar.py` e copia para as tuas notas as três últimas linhas da saída. Devem ser parecidas com estas, com outro número depois de `at`:

```text
<ginasio.Combate object at 0x100cc0590>
False
False
```

3. Agora transforma a classe `Combate` do `ginasio.py` numa dataclass. Acrescenta a linha `from dataclasses import dataclass` no início do ficheiro, antes da importação dos Pokémon, com uma linha em branco a separá-las. Põe `@dataclass` por cima da classe, troca o construtor pelos três campos, cada um com o seu tipo, e deixa o `resumo` como está. A classe fica assim:

```python
@dataclass
class Combate:
    """Registo de um combate. Só o ginásio cria registos (composição)."""

    desafiante: str
    pokemon_desafiante: str
    vencedor: str

    def resumo(self):
        """Devolve uma linha de texto que descreve o combate."""
        return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"
```

Leitura guiada: não há construtor. As três linhas com dois pontos são os campos, pela ordem em que o `combater` dá os valores. O `resumo` é um método normal: uma dataclass continua a ser uma classe, e pode ter métodos.

4. Antes de executares outra vez, prevê: os combates e os anúncios mudam? E as três últimas linhas?

5. Executa `python3 anunciar.py` e compara. Tudo o que vem antes das três últimas linhas fica exatamente igual. As três últimas passam a ser estas:

```text
Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Ash')
True
False
```

6. Responde por escrito.

- **a)** O `combater` cria os registos com `Combate(desafiante.nome, atacante.nome, vencedor.nome)`, e não mudaste essa linha. Porque é que continua a funcionar com a dataclass?
- **b)** O primeiro e o terceiro combates aconteceram em alturas diferentes, mas, com a dataclass, o `==` diz que são iguais. O que é que um registo guarda, e o que não guarda, que faz com que os dois sejam iguais? E o `is`, o que continua a dizer?

As respostas:

- **a)** O construtor que a dataclass escreve recebe os valores pela ordem dos campos: `desafiante`, `pokemon_desafiante` e `vencedor`. É a mesma ordem dos parâmetros do construtor antigo, e a linha do `combater` dá os três valores por essa ordem.
- **b)** Um registo guarda três nomes: o desafiante, o Pokémon com que lutou e o vencedor. Não guarda quando o combate aconteceu, nem que número teve, nem com que Pokémon lutou o líder (no primeiro foi o Gloom, e no terceiro a Tangela). O primeiro e o terceiro têm os mesmos três nomes, e por isso o `==` da dataclass diz que são iguais. O `is` continua a dizer `False`: são dois registos, dois objetos. Se fosse preciso distinguir os dois combates, o registo teria de guardar mais um dado, como o número do combate.

### Paragem 9

O ginásio funciona como antes, e o registo de cada combate escreve-se em menos linhas, com um `print` legível e um `==` que compara os dados.

## Problemas frequentes

### `can't open file '...ginasio.py': [Errno 2] No such file or directory`

O Python não encontrou o ficheiro que mandaste executar, porque o terminal está aberto noutra pasta. A mensagem mostra o caminho completo onde o procurou. Abre no VS Code a pasta `ginasio-pokemon` e abre aí um terminal novo, que já começa nessa pasta, ou muda para ela com `cd`.

### `ModuleNotFoundError: No module named 'pokemon'`

O Python não encontrou o ficheiro `pokemon.py`. Confirma que está na mesma pasta que o `ginasio.py` e que o nome é exatamente `pokemon.py`, em minúsculas, sem acento e sem nada a mais, como `pokemon (1).py`.

### `ImportError: cannot import name 'PokemonAgau' from 'pokemon'`

O ficheiro foi encontrado, mas não tem uma classe com o nome escrito na importação. Aqui, `PokemonAgau` está mal escrito. A mensagem continua com o caminho do teu `pokemon.py`, entre parênteses, e nas versões recentes do Python acaba com uma sugestão do nome certo.

### `NameError: name 'Treinador' is not defined`

Há uma linha a usar a classe antes de ela ser definida. As linhas de teste e o programa principal ficam sempre no fim do ficheiro, depois de todas as classes.

### `AttributeError: 'Treinador' object has no attribute 'capturar'`

O método existe no ficheiro, mas não está dentro da classe. Um método tem de estar indentado quatro espaços em relação à linha `class`. Se o `def capturar` começar na margem, é uma função solta, e não um método do treinador. Este erro aparece quando saem da indentação o `def capturar` e todos os métodos a seguir. Aparece também quando o método que saiu é o último da classe, como o `escolher_pokemon`. Se sair só o `def capturar` e os métodos a seguir ficarem onde estavam, o Python não executa nada e dá `IndentationError: unindent does not match any outer indentation level`, apontado à linha do método seguinte.

### `TypeError: Treinador.capturar() takes 1 positional argument but 2 were given`

Falta o `self` na definição do método: escreveste `def capturar(pokemon):` em vez de `def capturar(self, pokemon):`. Nas versões antigas do Python, a mensagem começa só por `capturar()`, sem o nome da classe.

### `AttributeError: 'Treinador' object has no attribute 'equipa'`

No construtor, a linha da equipa ficou sem `self.`: `equipa = []` cria uma variável que desaparece quando o construtor acaba. Tem de ser `self.equipa = []`.

### A demonstração do `pokemon.py` aparece quando executas o `ginasio.py`

Alguém apagou a linha `if __name__ == "__main__":` do `pokemon.py` e tirou a indentação das linhas debaixo dela. Se só uma destas duas coisas foi feita, o que aparece é um erro. É um `NameError` sobre o `PokemonPlanta`, se só se apagou a linha, ou um `IndentationError`, se só se tirou a indentação. Em qualquer dos casos, volta a copiar o ficheiro dos exemplos.

### O programa não para

Carrega em Ctrl+C no terminal para o interromper. Um combate que nunca acaba vem quase sempre do ciclo `while True` do `combater`. Confirma que tens os dois `break`, que as condições são `defensor.vida == 0` e `atacante.vida == 0`, e que não mudaste o ataque mínimo no `pokemon.py`. Com ataque mínimo 1, cada ataque tira pelo menos 1 de vida, e o combate acaba sempre.

### `TypeError: Ginasio() takes no arguments`

A classe ficou sem o construtor, porque o ficheiro tem duas linhas `class Ginasio:`. Escreveste a linha `class` do bloco do método, que só mostrava onde ele fica, e a segunda classe, só com esse método, apaga a primeira, que tinha o construtor. O mesmo acontece com o `Treinador`, na fase 7, e a mensagem pode dizer `Treinador() takes no arguments` ou `Lider() takes no arguments`. Procura no ficheiro as linhas que começam por `class`, deixa uma só para cada classe e põe o método dentro dela, com quatro espaços.

### A saída tem os números certos mas as linhas em branco não coincidem

Confirma os `\n` no início dos títulos do `combater` e do `mostrar_historico`, e o `print()` sozinho do programa principal da fase 6, que escreve uma linha em branco.

### `TypeError: Treinador.com_equipa() missing 1 required positional argument: 'pokemons'`

Falta a linha `@classmethod` por cima do `def com_equipa`. Sem ela, o Python não passa a classe ao método, e os valores que dás ficam desencontrados dos parâmetros. O nome vai para o `cls`, a lista vai para o `nome`, e o `pokemons` fica sem nada. Nas versões antigas do Python, a mensagem começa só por `com_equipa()`.

### Na fase 7, a primeira linha diz `Treinador 2` em vez de `Lider 2`

No `com_equipa`, a linha que cria o treinador está escrita `Treinador(nome)`. Tem de ser `cls(nome)`, para criar um objeto da classe por onde o método foi chamado.

### `ModuleNotFoundError: No module named 'anunciadores'`

O Python não encontrou o ficheiro `anunciadores.py`. Confirma que está na mesma pasta que o `anunciar.py` e o `ginasio.py`, e que o nome está escrito exatamente assim, em minúsculas e sem acentos.

### `AttributeError: 'Placard' object has no attribute 'numero'`

O `Placard` ficou sem o construtor, ou o construtor ficou sem o `self.` na linha `self.numero = 0`. É o mesmo problema da equipa sem `self.`, mais acima.

### `TypeError: Combate() takes no arguments`

A classe `Combate` tem os campos, mas falta a linha `@dataclass` por cima dela. Sem o decorador, ninguém escreve o construtor.

### `NameError: name 'dataclass' is not defined`

Falta a linha `from dataclasses import dataclass` no início do `ginasio.py`.

### `TypeError: Combate.__init__() takes 3 positional arguments but 4 were given`

Um dos três campos ficou sem o tipo, por exemplo `vencedor = ""` em vez de `vencedor: str`. Sem a anotação, a linha não é um campo, e o construtor da dataclass só recebe os outros dois. Nas versões antigas do Python, a mensagem começa só por `__init__()`.

## Desafios

Os desafios são para quem acabou. Consolidam o que o laboratório ensinou e fazem-se sozinhos. Não fazem parte do passo a passo e não levam solução.

1. Conta as vitórias de um treinador. Acrescenta à classe `Ginasio` um método `vitorias_de(treinador)`, que recebe um treinador e devolve quantos combates desse ginásio esse treinador venceu. O método não escreve nada no ecrã: devolve um número. Para o testares, cria um ficheiro novo, `desafio_vitorias.py`, na mesma pasta, com este programa:

```python
"""desafio_vitorias.py: testa o método vitorias_de do ginásio, com dois ginásios e três combates."""

from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
from ginasio import Ginasio, Treinador

misty = Treinador("Misty")
misty.capturar(PokemonAgua("Starmie", 120, 35))
erika = Treinador("Erika")
erika.capturar(PokemonPlanta("Tangela", 50, 20, 10))
ash = Treinador("Ash")
ash.capturar(PokemonFogo("Charmander", 90, 40))
ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
cerulean = Ginasio("Cerulean", misty)
celadon = Ginasio("Celadon", erika)
cerulean.combater(ash)
cerulean.combater(ash)
celadon.combater(ash)
print()
print(cerulean.vitorias_de(ash), cerulean.vitorias_de(misty))
print(celadon.vitorias_de(ash), celadon.vitorias_de(erika), celadon.vitorias_de(misty))
```

Quando o método estiver certo, as duas últimas linhas da saída são:

```text
1 1
1 0 0
```

Pista: olha outra vez para a classe `Combate` e para a linha do `combater` que cria cada registo. O que é que um registo guarda sobre o vencedor? A resposta decide a forma como comparas cada registo com o treinador que o método recebe.

2. Um anunciador que conta vitórias. No `anunciadores.py`, escreve uma classe nova, `Contador`, que serve de anunciador: tem um método `anunciar(combate)`, como o `Narrador` e o `Placard`, mas não escreve nada quando recebe um combate. Em vez disso, conta quantos combates ganharam os desafiantes e quantos ganhou o líder. Tem também um método `mostrar()`, que escreve as duas contagens numa linha, como `Desafiantes: 2 | Líder: 1`. Para o testares, junta o `Contador` à linha que importa os anunciadores no `anunciar.py` e acrescenta estas linhas ao fim do ficheiro:

```python
contador = Contador()
celadon.anunciar_combates(contador)
contador.mostrar()
```

Quando a classe estiver certa, a última linha da saída é:

```text
Desafiantes: 2 | Líder: 1
```

Pista: o `Contador` não sabe quem é o líder do ginásio, porque só recebe os combates, um a um. Olha para os três atributos de um registo. Como é que, só com um registo, se sabe se ganhou o desafiante ou o líder?

## Antes de terminares

- [ ] O `ginasio.py` tem as classes `Treinador`, `Lider`, `Combate` e `Ginasio`, com o `Combate` escrito como dataclass, e corre com `python3 ginasio.py`.
- [ ] O `anunciadores.py` e o `anunciar.py` funcionam: `python3 anunciar.py` mostra o placard e o narrador.
- [ ] Escreveste as previsões antes de executar e, onde falhaste, sabes dizer porquê.
- [ ] Tens por escrito as tuas respostas às perguntas das fases 2, 5, 6, 7, 8 e 9. Entrega-as ao professor, com os ficheiros, conforme ele indicar. Se só fizeste até à fase 6, entrega o `ginasio.py` dessa fase.
- [ ] Se fizeste os desafios, o `ginasio.py` tem o `vitorias_de` e o `anunciadores.py` tem o `Contador`.
- [ ] Consegues explicar porque é que um método de classe cria o objeto com `cls` e não com o nome da classe.
- [ ] Consegues explicar, por palavras tuas, a diferença entre agregação e composição com o exemplo do ginásio.

![Rodapé](../imagens/rodape.png)
