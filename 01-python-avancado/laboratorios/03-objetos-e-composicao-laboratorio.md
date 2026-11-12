![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Objetos, composição e comportamento

## O que vais construir

Vais construir o ginásio Pokémon: treinadores com equipas, um ginásio que organiza combates e guarda o registo de cada um, e duas maneiras de anunciar esses combates. No fim, a pasta do projeto fica assim:

```text
ginasio-pokemon/
├── pokemon.py
├── ginasio.py
├── anunciadores.py
└── anunciar.py
```

1. [Fase 1: Um objeto que guarda outros objetos](#fase-1-um-objeto-que-guarda-outros-objetos)
2. [Fase 2: Uma variável guarda uma referência, não uma cópia](#fase-2-uma-variável-guarda-uma-referência-não-uma-cópia)
3. [Fase 3: Um registo guarda nomes, e não objetos](#fase-3-um-registo-guarda-nomes-e-não-objetos)
4. [Fase 4: Agregação: o todo reúne partes que existem por si](#fase-4-agregação-o-todo-reúne-partes-que-existem-por-si)
5. [Fase 5: Composição: o todo cria e guarda as suas partes](#fase-5-composição-o-todo-cria-e-guarda-as-suas-partes)
6. [Fase 6: O que sobrevive quando o ginásio desaparece](#fase-6-o-que-sobrevive-quando-o-ginásio-desaparece)
7. [Fase 7: O método de classe recebe a classe](#fase-7-o-método-de-classe-recebe-a-classe)
8. [Fase 8: O contrato de um método fica na docstring](#fase-8-o-contrato-de-um-método-fica-na-docstring)
9. [Fase 9: Uma dataclass escreve o construtor por ti](#fase-9-uma-dataclass-escreve-o-construtor-por-ti)

## O que precisas

- O Python 3.9 ou mais recente. Confirma com `python3 --version`: deve aparecer `Python 3.9.6` ou uma versão maior. No Windows, o comando pode ser `python` ou `py`, e onde o texto diz `python3` usas o teu.
- O VS Code, para escreveres os ficheiros e abrires o terminal.
- O `pokemon.py` dos exemplos, com as classes dos Pokémon. O laboratório começa numa pasta vazia, e copias o ficheiro para lá em [Preparar o projeto](#preparar-o-projeto).

## Preparar o projeto

1. Cria uma pasta nova, `ginasio-pokemon`, onde guardas os trabalhos da disciplina, e abre-a no VS Code, com a opção `Open Folder...` do menu File. Abre o terminal no menu Terminal, com a opção New Terminal, e escreve `pwd`. O que deves ver: o caminho da pasta, a acabar em `ginasio-pokemon`. Isto quer dizer que o terminal está a trabalhar na pasta do projeto.

2. O teu `ginasio.py` vai importar as classes dos Pokémon do `pokemon.py`, e por isso os dois ficheiros ficam na mesma pasta. Abre o [`pokemon.py` dos exemplos](../../exemplos/python-avancado/pokemon/03-objetos-e-composicao/pokemon.py) e copia o conteúdo todo. No painel Explorer do VS Code, cria um ficheiro novo, com o nome `pokemon.py`, cola o conteúdo e guarda com Ctrl+S (Cmd+S no Mac).

3. Corre o ficheiro, para confirmares que funciona:

   ```bash
   python3 pokemon.py
   ```

   O que deves ver no início da saída:

   ```text
   Bulbasaur: vida 150, ataque 25
   Squirtle: vida 100, ataque 50
   ```

   Isto quer dizer que o `pokemon.py` está na pasta e funciona; o resto da saída é a demonstração do fim do ficheiro. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

## Fase 1: Um objeto que guarda outros objetos

Crias o `ginasio.py` com a classe `Treinador`, que guarda a sua equipa de Pokémon numa lista. O treinador é o todo, e cada Pokémon da equipa é uma parte. Rever: [Um objeto que guarda outros objetos](../03-objetos-e-composicao.md#um-objeto-que-guarda-outros-objetos).

1. Cria o ficheiro `ginasio.py`, na mesma pasta, com esta primeira versão. Escreve-a à mão, em vez de a colares: ao escrever, dás pelo `self` de cada método e pela indentação.

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

2. No fim do ficheiro, encostadas à margem, acrescenta estas linhas de teste. Ficam depois da classe, porque o Python lê o ficheiro de cima para baixo, e uma linha que use o `Treinador` antes da classe dá erro.

   ```python
   ash = Treinador("Ash")
   ash.capturar(PokemonFogo("Charmander", 90, 40))
   ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
   print(ash.nome, "tem", len(ash.equipa), "Pokémon")
   print("Primeiro a lutar:", ash.escolher_pokemon().nome)
   ```

3. Antes de correres, prevê as duas linhas que o teste vai escrever. Depois corre:

   ```bash
   python3 ginasio.py
   ```

   O que deves ver:

   ```text
   Ash tem 2 Pokémon
   Primeiro a lutar: Charmander
   ```

   Isto quer dizer que a equipa guardou os dois Pokémon e que o Charmander, o primeiro a ser capturado, é o primeiro com vida. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

O `ginasio.py` tem um treinador com uma equipa, e o `escolher_pokemon` devolve o primeiro Pokémon com vida.

Pensa antes de continuares: quem criou o Charmander, o treinador ou as linhas de teste? A resposta: as linhas de teste, com `PokemonFogo("Charmander", 90, 40)`. O `capturar` só recebe o Pokémon, já criado, e junta-o à lista.

## Fase 2: Uma variável guarda uma referência, não uma cópia

Entregas ao Ash um Pokémon guardado numa variável e mudas-lhe a vida pela variável. A variável e a lista da equipa guardam referências para o mesmo objeto, e o operador `is` confirma-o. Rever: [Uma variável guarda uma referência, não uma cópia](../03-objetos-e-composicao.md#uma-variável-guarda-uma-referência-não-uma-cópia).

1. No fim do `ginasio.py`, substitui as linhas de teste da fase 1 por estas:

   ```python
   charmander = PokemonFogo("Charmander", 90, 40)
   ash = Treinador("Ash")
   ash.capturar(charmander)
   print(ash.equipa[0] is charmander)
   charmander.vida = 0
   print(ash.escolher_pokemon())
   ```

2. Antes de correres, prevê o que o `escolher_pokemon` devolve depois de `charmander.vida = 0`. Corre `python3 ginasio.py`. O que deves ver:

   ```text
   True
   None
   ```

   O `True` quer dizer que há um só Charmander, com duas referências para ele: a vida mudou pela variável, e o Ash ficou sem nenhum Pokémon com vida.

### Paragem 2

A equipa do Ash guarda o mesmo Charmander que a variável `charmander`, e não uma cópia.

Pensa antes de continuares: se a linha `charmander.vida = 0` fosse `ash.equipa[0].vida = 0`, o que escrevia `print(charmander.vida)`? A resposta: `0`. A vida mudava por outra referência, mas o Charmander era o mesmo.

## Fase 3: Um registo guarda nomes, e não objetos

Escreves a classe `Combate`, que guarda o registo de um combate. O registo guarda os nomes, que são textos, e não os objetos `Treinador` e `Pokemon`. Rever: [Um registo guarda nomes, e não objetos](../03-objetos-e-composicao.md#um-registo-guarda-nomes-e-não-objetos).

1. No `ginasio.py`, a seguir à classe `Treinador` e antes das linhas de teste, acrescenta a classe `Combate`, com duas linhas em branco antes dela:

   ```python
   class Combate:
       """Registo de um combate: quem desafiou, com que Pokémon e quem venceu."""

       def __init__(self, desafiante, pokemon_desafiante, vencedor):
           """Guarda os nomes do desafiante, do seu Pokémon e do vencedor."""
           self.desafiante = desafiante
           self.pokemon_desafiante = pokemon_desafiante
           self.vencedor = vencedor

       def resumo(self):
           """Devolve uma linha de texto que descreve o combate."""
           return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"
   ```

2. Substitui as linhas de teste da fase 2 por estas, que criam um registo à mão, só para experimentar a classe:

   ```python
   registo = Combate("Ash", "Bulbasaur", "Ash")
   print(registo.resumo())
   ```

   Corre `python3 ginasio.py`. O que deves ver:

   ```text
   Ash com Bulbasaur: venceu Ash
   ```

   Isto quer dizer que o `resumo` junta os três nomes numa linha, a que vai aparecer no histórico do ginásio.

### Paragem 3

A classe `Combate` cria um registo e descreve-o numa linha.

Pensa antes de continuares: porque é que o registo guarda o nome do Pokémon, e não o próprio objeto? A resposta: o objeto continua a mudar depois do combate, porque perde vida noutros combates. O nome não muda, e o registo de um combate antigo fica como estava.

## Fase 4: Agregação: o todo reúne partes que existem por si

Escreves a classe `Ginasio`, que recebe no construtor o treinador que é o seu líder. É uma agregação: o líder já existia antes do ginásio, e o ginásio só guarda uma referência para ele. Rever: [Agregação: o todo reúne partes que existem por si](../03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si).

1. A seguir à classe `Combate`, e antes das linhas de teste, acrescenta a classe `Ginasio`, por agora só com o construtor e o `mostrar_historico`:

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

2. Substitui as linhas de teste da fase 3 por estas:

   ```python
   misty = Treinador("Misty")
   misty.capturar(PokemonAgua("Starmie", 120, 35))
   cerulean = Ginasio("Cerulean", misty)
   print(cerulean.lider is misty)
   print(len(cerulean.desafiantes), len(cerulean.combates))
   cerulean.mostrar_historico()
   ```

   Corre `python3 ginasio.py`. O que deves ver, com a linha em branco que o `\n` escreve antes do título:

   ```text
   True
   0 0

   Histórico do ginásio de Cerulean:
   ```

   O `True` diz que o líder do ginásio é a própria Misty, e não uma cópia. As duas listas estão vazias, porque ainda não houve combates.

### Paragem 4

O ginásio existe, com o líder e as duas listas vazias.

Pensa antes de continuares: a Misty já existia antes do ginásio de Cerulean? A resposta: sim. Foi criada nas linhas de teste, com `Treinador("Misty")`, e o ginásio só a recebeu no construtor. É uma parte que existe por si, como os Pokémon da equipa de um treinador.

## Fase 5: Composição: o todo cria e guarda as suas partes

Escreves o método `combater`, que põe a lutar um Pokémon de cada treinador e, no fim, cria o registo do combate. É uma composição: os registos pertencem ao ginásio, que os cria, não os partilha e os leva consigo quando desaparece. Rever: [Composição: o todo cria e guarda as suas partes](../03-objetos-e-composicao.md#composição-o-todo-cria-e-guarda-as-suas-partes).

1. Dentro da classe `Ginasio`, entre o construtor e o `mostrar_historico`, acrescenta o início do método `combater`, que prepara o combate. O `def` tem quatro espaços, como os outros métodos:

   ```python
       def combater(self, desafiante):
           """Um combate entre o primeiro Pokémon com vida de cada treinador."""
           # O not in evita que o mesmo treinador fique duas vezes na lista.
           if desafiante not in self.desafiantes:
               self.desafiantes.append(desafiante)
           # Cada treinador escolhe o seu Pokémon. O do desafiante ataca primeiro.
           atacante = desafiante.escolher_pokemon()
           defensor = self.lider.escolher_pokemon()
           # Sem este if, o ciclo punha o None a atacar e parava com um erro.
           if atacante is None or defensor is None:
               print("Não há combate: um dos treinadores não tem Pokémon com vida.")
               return
   ```

2. Por baixo do último `if`, ainda dentro do método, acrescenta o ciclo do combate e o registo. A primeira linha fica alinhada com o `if`, com oito espaços:

   ```python
           print(f"\n=== {desafiante.nome} desafia {self.lider.nome} no ginásio de {self.cidade} ===")
           # O while True só acaba num break. Acaba sempre, porque o ataque
           # nunca é menor do que 1, e cada ataque tira vida a um dos dois.
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

3. Substitui as linhas de teste da fase 4 pelo programa principal. Fica debaixo do `if __name__ == "__main__":`, que faz estas linhas correrem só quando corres o próprio `ginasio.py`, e não quando outro programa o importa.

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
   ```

4. Antes de correres, prevê o primeiro combate, ataque a ataque: o dano de cada ataque e a vida com que fica cada Pokémon. O Charmander luta primeiro, por ser o primeiro da equipa, e a água tira o dobro ao fogo. Depois corre `python3 ginasio.py`. O que deves ver, a começar por uma linha em branco:

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
   ```

   O primeiro combate, ataque a ataque:

   | Ataque | Quem ataca | Dano | Vida do Charmander | Vida do Starmie |
   | --- | --- | ---: | ---: | ---: |
   | Antes | ninguém | 0 | 90 | 120 |
   | 1 | Charmander | 40 | 90 | 80 |
   | 2 | Starmie, super eficaz | 70 | 20 | 80 |
   | 3 | Charmander | 40 | 20 | 40 |
   | 4 | Starmie, super eficaz | 70 | 0 | 40 |

   No quarto ataque, o Charmander fica KO, e a Misty vence. Em `80/150`, o 150 é a vida máxima de qualquer Pokémon, e não a vida com que começou. No segundo combate, o Ash luta com o Bulbasaur. O Starmie começa com os 40 de vida com que ficou, porque o ginásio usa os Pokémon das equipas, e não cópias. A planta tira o dobro à água, e o Bulbasaur vence logo no primeiro ataque. O "É super eficaz!" sai antes da linha do ataque, porque o `pokemon.py` o escreve ao calcular o dano.

   Se o programa não parar, ou parar com um `TypeError` sobre o `Ginasio`, vê [O programa não para](#o-programa-não-para) ou [`TypeError: Ginasio() takes no arguments`](#typeerror-ginasio-takes-no-arguments).

### Paragem 5

O ginásio faz combates e guarda o registo de cada um no histórico. O `ginasio.py` completo, como deve estar no fim desta fase:

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
    """Registo de um combate: quem desafiou, com que Pokémon e quem venceu."""

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
        # O not in evita que o mesmo treinador fique duas vezes na lista.
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        # Cada treinador escolhe o seu Pokémon. O do desafiante ataca primeiro.
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        # Sem este if, o ciclo punha o None a atacar e parava com um erro.
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
        print(f"\n=== {desafiante.nome} desafia {self.lider.nome} no ginásio de {self.cidade} ===")
        # O while True só acaba num break. Acaba sempre, porque o ataque
        # nunca é menor do que 1, e cada ataque tira vida a um dos dois.
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
```

O `Ginasio` recebe os treinadores, pede-lhes os Pokémon com o `escolher_pokemon` e cria os objetos `Combate` dentro do `combater`. O programa principal fica no fim, depois de todas as classes.

Pensa antes de continuares: se o programa principal tivesse um terceiro `cerulean.combater(ash)`, logo a seguir aos outros dois, o que escrevia? A resposta: `Não há combate: um dos treinadores não tem Pokémon com vida.`, e o histórico continuava com dois combates. O Starmie é o mesmo objeto que ficou KO no segundo combate, e o `escolher_pokemon` da Misty devolve `None`.

## Fase 6: O que sobrevive quando o ginásio desaparece

O Ash desafia dois ginásios, e depois apagas o de Cerulean com `del`. Vês o que desaparece com o ginásio, os registos dos combates, e o que sobrevive, os treinadores e os Pokémon. Rever: [O que sobrevive quando o ginásio desaparece](../03-objetos-e-composicao.md#o-que-sobrevive-quando-o-ginásio-desaparece).

1. Substitui o programa principal inteiro, da linha `if __name__ == "__main__":` até ao fim do ficheiro, por este. A Erika, líder do ginásio de Celadon, tem uma Tangela, de planta.

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
       # O Ash está nas listas de desafiantes dos dois ginásios, e é o mesmo objeto?
       print(ash in cerulean.desafiantes, ash in celadon.desafiantes)
       print(cerulean.desafiantes[0] is celadon.desafiantes[0])
       # O del apaga a variável cerulean, a única referência para este ginásio.
       del cerulean
       celadon.mostrar_historico()
       print(ash.nome, "continua com", len(ash.equipa), "Pokémon")
   ```

2. Corre `python3 ginasio.py`. Os dois combates de Cerulean são iguais aos da fase 5. A partir do título do combate de Celadon, o que deves ver é isto:

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

   Em Celadon luta o Bulbasaur, com 110 de vida, porque não levou nenhum ataque em Cerulean. O `del cerulean` não mexeu no histórico de Celadon nem na equipa do Ash.

3. Provoca um erro de propósito: no fim do programa principal, com quatro espaços, acrescenta a linha `cerulean.mostrar_historico()`. Antes de correres, prevê o que acontece. Corre outra vez. O que deves ver, depois da saída do passo 2, no fim da mensagem de erro:

   ```text
   NameError: name 'cerulean' is not defined
   ```

   O erro fala da variável, e não do ginásio. Depois do `del`, o programa já não tem nenhuma maneira de chegar ao ginásio de Cerulean, nem de lhe pedir o histórico. Apaga a linha que acrescentaste.

### Paragem 6

O programa mostra o que sobrevive ao `del cerulean`: os treinadores, os Pokémon e o ginásio de Celadon.

Pensa antes de continuares: depois do `del cerulean`, ainda há alguma forma de chegar aos registos dos dois combates de Cerulean? A resposta: não. Só a lista `combates` do ginásio de Cerulean tinha referências para eles, e essa lista desapareceu com o ginásio. Na composição, as partes desaparecem com o todo.

## Fase 7: O método de classe recebe a classe

Acrescentas ao `Treinador` o `com_equipa`, que cria um treinador já com a equipa, e escreves o `Lider`, um treinador que escolhe o Pokémon com mais vida. O `com_equipa` é um método de classe: recebe no `cls` a classe por onde foi chamado. Rever: [O método de classe recebe a classe](../03-objetos-e-composicao.md#o-método-de-classe-recebe-a-classe).

1. Na classe `Treinador`, entre o construtor e o `capturar`, acrescenta o método de classe `com_equipa`. A linha `@classmethod` fica por cima do `def`:

   ```python
       @classmethod
       def com_equipa(cls, nome, pokemons):
           """Cria um treinador da classe cls, já com os Pokémon da lista na equipa.

           É um construtor alternativo. Em Treinador.com_equipa(...), cls é
           Treinador; em Lider.com_equipa(...), cls é Lider, e o objeto criado
           é um Lider.
           """
           treinador = cls(nome)
           for pokemon in pokemons:
               # Usa o capturar, e não equipa.append: se a captura tiver uma
               # regra, como um limite de Pokémon, este método cumpre-a também.
               treinador.capturar(pokemon)
           return treinador
   ```

2. A seguir à classe `Treinador`, e antes da classe `Combate`, acrescenta a classe `Lider`, filha do `Treinador`:

   ```python
   class Lider(Treinador):
       """Um Lider É UM Treinador que escolhe sempre o Pokémon com mais vida.

       Não tem construtor próprio: usa o do Treinador, que só pede o nome.
       """

       def escolher_pokemon(self):
           """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
           # Começa em None, porque ainda não viu nenhum Pokémon.
           escolhido = None
           for pokemon in self.equipa:
               if pokemon.vida > 0:
                   if escolhido is None or pokemon.vida > escolhido.vida:
                       escolhido = pokemon
           return escolhido
   ```

3. Substitui outra vez o programa principal inteiro, agora por este:

   ```python
   if __name__ == "__main__":
       erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10), PokemonPlanta("Gloom", 80, 25, 5)])
       ash = Treinador.com_equipa("Ash", [PokemonAgua("Squirtle", 100, 30), PokemonFogo("Charmander", 90, 40)])
       # O type dá a classe do objeto, e o __name__ dá o nome dessa classe.
       print(type(erika).__name__, len(erika.equipa))
       print(type(ash).__name__, len(ash.equipa))
       print(erika.escolher_pokemon().nome, ash.escolher_pokemon().nome)
       celadon = Ginasio("Celadon", erika)
       celadon.combater(ash)
       celadon.combater(ash)
       celadon.mostrar_historico()
   ```

4. Antes de correres, prevê as três primeiras linhas da saída. Corre `python3 ginasio.py`. O que deves ver:

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

   A Erika é um `Lider` e escolhe o Gloom, que tem mais vida. O Ash é um `Treinador` e escolhe o Squirtle, o primeiro da equipa. No segundo combate, a Erika luta com a Tangela, porque o Gloom ficou com 20 de vida, e ela tem 50.

   Se aparecer um `TypeError` sobre o `com_equipa`, ou se a primeira linha disser `Treinador 2`, vê [o erro do `com_equipa`](#typeerror-treinadorcom_equipa-missing-1-required-positional-argument-pokemons) ou [a primeira linha errada](#a-primeira-linha-da-fase-7-diz-treinador-2-e-não-lider-2).

### Paragem 7

Os treinadores e os líderes criam-se numa só linha, já com a equipa. Confere o teu `ginasio.py` com este, completo:

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
            # Usa o capturar, e não equipa.append: se a captura tiver uma
            # regra, como um limite de Pokémon, este método cumpre-a também.
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
    """Um Lider É UM Treinador que escolhe sempre o Pokémon com mais vida.

    Não tem construtor próprio: usa o do Treinador, que só pede o nome.
    """

    def escolher_pokemon(self):
        """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
        # Começa em None, porque ainda não viu nenhum Pokémon.
        escolhido = None
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                if escolhido is None or pokemon.vida > escolhido.vida:
                    escolhido = pokemon
        return escolhido


class Combate:
    """Registo de um combate: quem desafiou, com que Pokémon e quem venceu."""

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
        # O not in evita que o mesmo treinador fique duas vezes na lista.
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        # Cada treinador escolhe o seu Pokémon. O do desafiante ataca primeiro.
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        # Sem este if, o ciclo punha o None a atacar e parava com um erro.
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
        print(f"\n=== {desafiante.nome} desafia {self.lider.nome} no ginásio de {self.cidade} ===")
        # O while True só acaba num break. Acaba sempre, porque o ataque
        # nunca é menor do que 1, e cada ataque tira vida a um dos dois.
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
    # O type dá a classe do objeto, e o __name__ dá o nome dessa classe.
    print(type(erika).__name__, len(erika.equipa))
    print(type(ash).__name__, len(ash.equipa))
    print(erika.escolher_pokemon().nome, ash.escolher_pokemon().nome)
    celadon = Ginasio("Celadon", erika)
    celadon.combater(ash)
    celadon.combater(ash)
    celadon.mostrar_historico()
```

O `com_equipa` está escrito uma só vez, no `Treinador`, e o `Lider` herda-o, como herda o construtor, e só reescreve o `escolher_pokemon`.

Pensa antes de continuares: o que mudava na saída se o `com_equipa` criasse o treinador com `Treinador(nome)`, em vez de `cls(nome)`? A resposta: a Erika passava a ser uma treinadora normal, e a primeira linha dizia `Treinador 2`. Escolhia a Tangela, a primeira da equipa, e os dois combates acabavam ao contrário, sem nenhuma mensagem de erro.

## Fase 8: O contrato de um método fica na docstring

O ginásio passa a anunciar os seus combates, com dois anunciadores sem nenhuma classe-mãe em comum, o `Narrador` e o `Placard`. Usa-os por duck typing, pelo método `anunciar(combate)` que os dois têm, e esse contrato fica escrito na docstring do método do ginásio. Rever: [O contrato de um método fica na docstring](../03-objetos-e-composicao.md#o-contrato-de-um-método-fica-na-docstring).

1. No fim da classe `Ginasio`, depois do `mostrar_historico` e antes do programa principal, acrescenta o método `anunciar_combates`:

   ```python
       def anunciar_combates(self, anunciador):
           """Entrega cada combate ao anunciador, para ele o anunciar.

           O anunciador pode ser um objeto de qualquer classe, desde que tenha o
           método anunciar(combate). O ginásio não quer saber de que classe é.
           """
           for combate in self.combates:
               anunciador.anunciar(combate)
   ```

2. Cria, na mesma pasta, o ficheiro `anunciadores.py`, com os dois anunciadores:

   ```python
   """anunciadores.py: dois anunciadores de combates para o ginásio do ginasio.py.

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

3. Cria outro ficheiro, `anunciar.py`, com o programa que faz três combates no ginásio de Celadon e os anuncia das duas maneiras:

   ```python
   """anunciar.py: faz três combates no ginásio de Celadon e anuncia-os de duas maneiras."""

   from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
   from ginasio import Ginasio, Lider, Treinador
   # O ginasio.py não importa os anunciadores: é este programa que os junta ao ginásio.
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

4. Corre `python3 anunciar.py`. O que deves ver:

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

   No primeiro combate, a Erika, que é líder, escolhe o Gloom, que tem mais vida, e o Charmander vence-o, porque o fogo tira o dobro à planta. No segundo, com o Gloom KO, a Tangela vence o Psyduck, que não tem vantagem contra a planta. No terceiro, a Tangela só tem 10 de vida, e o Charmander vence outra vez.

   Se o placard parar com um `AttributeError` sobre o `numero`, vê [o que lhe falta](#attributeerror-placard-object-has-no-attribute-numero).

5. Provoca um erro de propósito: no fim do `anunciar.py`, acrescenta a linha `celadon.anunciar_combates(ash)`, que entrega ao ginásio um treinador no lugar de um anunciador. Antes de correres, prevê se o erro aparece antes ou depois do placard e do narrador. Corre outra vez. O que deves ver, no fim da mensagem de erro:

   ```text
   AttributeError: 'Treinador' object has no attribute 'anunciar'
   ```

   O erro aparece depois: os combates, o placard e o narrador saem como antes, porque o Python só falha quando a linha `anunciador.anunciar(combate)` corre com o Ash. O Ash não cumpre o contrato, porque não tem o método `anunciar`. Apaga a linha que acrescentaste.

### Paragem 8

O mesmo `anunciar_combates` anunciou os combates de duas maneiras, conforme o anunciador que recebeu, sem mudar uma linha do ginásio.

Pensa antes de continuares: o `ginasio.py` não tem nenhuma linha com `Narrador` ou `Placard`. Como é que o `anunciar_combates` consegue usar os dois? A resposta: chama `anunciador.anunciar(combate)` sem perguntar a classe do objeto, e os dois objetos, criados no `anunciar.py`, têm esse método. É o duck typing.

## Fase 9: Uma dataclass escreve o construtor por ti

Vês o que o `print` e o `==` fazem com dois registos de combate, e depois escreves o `Combate` como dataclass. Rever: [Uma dataclass escreve o construtor por ti](../03-objetos-e-composicao.md#uma-dataclass-escreve-o-construtor-por-ti).

1. Antes de mexeres no `Combate`, acrescenta estas linhas ao fim do `anunciar.py`:

   ```python
   # O primeiro e o terceiro combates têm os mesmos três nomes: Ash, Charmander e Ash.
   print()
   print(celadon.combates[0])
   print(celadon.combates[0] == celadon.combates[2])
   print(celadon.combates[0] is celadon.combates[2])
   ```

   Corre `python3 anunciar.py`. As três últimas linhas devem ser parecidas com estas, com outro número depois de `at`:

   ```text
   <ginasio.Combate object at 0x100cc0590>
   False
   False
   ```

   O `print` só mostra a classe e o sítio da memória, e o `==` pergunta o mesmo que o `is`: se os dois registos são o mesmo objeto.

2. No início do `ginasio.py`, antes da importação dos Pokémon, acrescenta a importação do `dataclass`, com uma linha em branco entre as duas:

   ```python
   from dataclasses import dataclass

   from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
   ```

3. Substitui a classe `Combate` inteira por esta, com o `@dataclass` por cima e os três campos no lugar do construtor:

   ```python
   @dataclass
   class Combate:
       """Registo de um combate: quem desafiou, com que Pokémon e quem venceu.

       É uma dataclass: o @dataclass escreve sozinho o construtor, a forma de o
       mostrar com print e a comparação com ==. Só o ginásio cria registos
       (composição).
       """

       # Cada campo é um nome, dois pontos e o tipo, pela ordem em que o combater dá os valores.
       desafiante: str
       pokemon_desafiante: str
       vencedor: str

       def resumo(self):
           """Devolve uma linha de texto que descreve o combate."""
           return f"{self.desafiante} com {self.pokemon_desafiante}: venceu {self.vencedor}"
   ```

4. Antes de correres, prevê o que passam a escrever as três últimas linhas. Corre `python3 anunciar.py`. Os combates e os anúncios ficam iguais, e as três últimas linhas passam a ser estas:

   ```text
   Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Ash')
   True
   False
   ```

   O `print` mostra os três campos, o `==` compara-os e diz que os registos são iguais, e o `is` continua a dizer que são dois objetos.

   Se o programa parar com um `TypeError` sobre o `Combate`, vê [`Combate() takes no arguments`](#typeerror-combate-takes-no-arguments) ou [`__init__() takes 3 positional arguments`](#typeerror-combate__init__-takes-3-positional-arguments-but-4-were-given).

### Paragem 9

O ginásio funciona como antes, e o registo escreve-se em menos linhas, com um `print` que se lê e um `==` que compara os dados. O `ginasio.py` completo, no fim do laboratório:

```python
"""ginasio.py: o ginásio Pokémon, construído passo a passo no laboratório.

O treinador guarda uma equipa de Pokémon, e o ginásio recebe treinadores e guarda
o registo de cada combate. As classes de Pokémon vêm do ficheiro pokemon.py, que
tem de estar na mesma pasta que este.
"""

from dataclasses import dataclass

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
            # Usa o capturar, e não equipa.append: se a captura tiver uma
            # regra, como um limite de Pokémon, este método cumpre-a também.
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
    """Um Lider É UM Treinador que escolhe sempre o Pokémon com mais vida.

    Não tem construtor próprio: usa o do Treinador, que só pede o nome.
    """

    def escolher_pokemon(self):
        """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
        # Começa em None, porque ainda não viu nenhum Pokémon.
        escolhido = None
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                if escolhido is None or pokemon.vida > escolhido.vida:
                    escolhido = pokemon
        return escolhido


@dataclass
class Combate:
    """Registo de um combate: quem desafiou, com que Pokémon e quem venceu.

    É uma dataclass: o @dataclass escreve sozinho o construtor, a forma de o
    mostrar com print e a comparação com ==. Só o ginásio cria registos
    (composição).
    """

    # Cada campo é um nome, dois pontos e o tipo, pela ordem em que o combater dá os valores.
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
        """Um combate entre o primeiro Pokémon com vida de cada treinador."""
        # O not in evita que o mesmo treinador fique duas vezes na lista.
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
        # Cada treinador escolhe o seu Pokémon. O do desafiante ataca primeiro.
        atacante = desafiante.escolher_pokemon()
        defensor = self.lider.escolher_pokemon()
        # Sem este if, o ciclo punha o None a atacar e parava com um erro.
        if atacante is None or defensor is None:
            print("Não há combate: um dos treinadores não tem Pokémon com vida.")
            return
        print(f"\n=== {desafiante.nome} desafia {self.lider.nome} no ginásio de {self.cidade} ===")
        # O while True só acaba num break. Acaba sempre, porque o ataque
        # nunca é menor do que 1, e cada ataque tira vida a um dos dois.
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
    erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10), PokemonPlanta("Gloom", 80, 25, 5)])
    ash = Treinador.com_equipa("Ash", [PokemonAgua("Squirtle", 100, 30), PokemonFogo("Charmander", 90, 40)])
    # O type dá a classe do objeto, e o __name__ dá o nome dessa classe.
    print(type(erika).__name__, len(erika.equipa))
    print(type(ash).__name__, len(ash.equipa))
    print(erika.escolher_pokemon().nome, ash.escolher_pokemon().nome)
    celadon = Ginasio("Celadon", erika)
    celadon.combater(ash)
    celadon.combater(ash)
    celadon.mostrar_historico()
```

O `Ginasio` cria os registos `Combate` no `combater`, guarda-os na lista `combates` e entrega-os, um a um, ao anunciador no `anunciar_combates`. O programa principal continua o da fase 7, e o `anunciar.py` importa as classes sem o correr.

Pensa antes de continuares: o primeiro e o terceiro combates aconteceram em alturas diferentes, e a Erika lutou com Pokémon diferentes. Porque é que o `==` diz que os registos são iguais? A resposta: o registo só guarda três nomes, e são os mesmos nos dois. Não guarda quando foi o combate nem com que Pokémon lutou o líder, e por isso não os distingue.

## Se alguma coisa falhar

1. Estás na pasta certa? Escreve `pwd` no terminal: o caminho tem de acabar em `ginasio-pokemon`. No Windows, na linha de comandos clássica, o comando é `cd`. Para mudar de pasta, abre a pasta no VS Code e abre lá um terminal novo.
2. Guardaste o ficheiro? O Python corre o que está guardado no disco, e não o que vês no ecrã.
3. Os ficheiros estão todos na mesma pasta, com os nomes certos? São `pokemon.py`, `ginasio.py`, `anunciadores.py` e `anunciar.py`, em minúsculas e sem acentos.
4. A saída é diferente da do texto? Compara o teu `ginasio.py` com o ficheiro completo da paragem seguinte, a [5](#paragem-5), a [7](#paragem-7) ou a [9](#paragem-9), linha a linha, a começar pela indentação e pelos `\n`. Se te perderes antes da paragem 5, copia o ficheiro dela e continua na fase 6. Entre as paragens 5 e 7, copia o da paragem 7 e continua na fase 8.
5. No Python 3.9, as mensagens de `TypeError` mostram só o nome do método, sem a classe: `capturar()` em vez de `Treinador.capturar()`.

### `can't open file '...ginasio.py': [Errno 2] No such file or directory`

O terminal está noutra pasta, e o Python não encontrou o ficheiro. A mensagem mostra o caminho onde o procurou. Muda para a pasta `ginasio-pokemon`, como diz a primeira verificação.

### `ModuleNotFoundError: No module named 'pokemon'`

O Python não encontrou o ficheiro que a linha do `import` pede. Confirma que o `pokemon.py` está na mesma pasta que o ficheiro que corres, com o nome exato. A mesma mensagem com `'ginasio'` ou `'anunciadores'` tem a mesma causa.

### `ImportError: cannot import name 'PokemonAgau' from 'pokemon'`

O ficheiro foi encontrado, mas não tem uma classe com o nome escrito na importação: aqui, `PokemonAgau` está mal escrito. Nas versões recentes do Python, a mensagem acaba com o nome certo, depois de `Did you mean`.

### `NameError: name 'Treinador' is not defined`

Há uma linha a usar a classe antes de ela estar definida. As linhas de teste e o programa principal ficam no fim do ficheiro, depois de todas as classes.

### `IndentationError` ou `AttributeError: 'Treinador' object has no attribute 'capturar'`

Um método saiu da classe, ou tem espaços a mais ou a menos. Os métodos têm quatro espaços em relação à linha `class`, e as linhas dentro deles têm oito. Quando saem da classe um método e todos os que estão por baixo dele, o Python não dá `IndentationError`: o erro só aparece quando o programa chama um deles.

### `TypeError: Treinador.capturar() takes 1 positional argument but 2 were given`

Falta o `self` na definição do método: `def capturar(pokemon):` em vez de `def capturar(self, pokemon):`.

### `AttributeError: 'Treinador' object has no attribute 'equipa'`

No construtor, a linha da equipa ficou sem `self.`. Com `equipa = []`, a lista desaparece quando o construtor acaba, e tem de ser `self.equipa = []`.

### `TypeError: Ginasio() takes no arguments`

O ficheiro tem duas linhas `class Ginasio:`, e a segunda classe, sem construtor, substitui a primeira. Procura as linhas que começam por `class`, deixa uma para cada classe e põe os métodos dentro dela, com quatro espaços. Na fase 7, o mesmo engano com o `Treinador` dá `Lider() takes no arguments`.

### O programa não para

Carrega em Ctrl+C no terminal, para o interromper. Um combate sem fim vem do `while True` do `combater`: confirma os dois `break` e as condições `defensor.vida == 0` e `atacante.vida == 0`.

### `TypeError: Treinador.com_equipa() missing 1 required positional argument: 'pokemons'`

Falta o `@classmethod` por cima do `def com_equipa`. Sem ele, o Python não passa a classe ao método: o nome vai para o `cls`, a lista vai para o `nome`, e o `pokemons` fica sem valor.

### A primeira linha da fase 7 diz `Treinador 2`, e não `Lider 2`

No `com_equipa`, o treinador está a ser criado com `Treinador(nome)`. Tem de ser `cls(nome)`, para criar um objeto da classe por onde o método foi chamado.

### `AttributeError: 'Placard' object has no attribute 'numero'`

O `Placard` ficou sem o construtor, ou a linha `self.numero = 0` ficou sem o `self.`.

### `TypeError: Combate() takes no arguments`

A classe `Combate` tem os campos, mas falta o `@dataclass` por cima dela, e ninguém escreveu o construtor.

### `NameError: name 'dataclass' is not defined`

Falta a linha `from dataclasses import dataclass` no início do `ginasio.py`.

### `TypeError: Combate.__init__() takes 3 positional arguments but 4 were given`

Um dos campos ficou sem o tipo, como `vencedor = ""` em vez de `vencedor: str`. Sem o tipo, a linha não é um campo, e o construtor só recebe os outros dois.

## Desafios

Os desafios partem do `ginasio.py`, do `anunciadores.py` e do `anunciar.py` do fim da fase 9.

1. Conta as vitórias de um treinador. Acrescenta à classe `Ginasio` um método `vitorias_de(treinador)`, que devolve quantos combates desse ginásio o treinador venceu, sem escrever nada no ecrã. Para o testares, cria o `desafio_vitorias.py`, na mesma pasta, com este programa:

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

   Pista: o que é que um registo guarda sobre o vencedor? A resposta decide como comparas cada registo com o treinador que o método recebe.

2. Um anunciador que conta vitórias. No `anunciadores.py`, escreve a classe `Contador`, com um método `anunciar(combate)`, como o `Narrador` e o `Placard`. Esse método não escreve nada: conta quantos combates ganharam os desafiantes e quantos ganhou o líder. Tem também um método `mostrar()`, que escreve as duas contagens numa linha. Para o testares, junta o `Contador` à importação dos anunciadores no `anunciar.py` e acrescenta estas linhas ao fim do ficheiro:

   ```python
   contador = Contador()
   celadon.anunciar_combates(contador)
   contador.mostrar()
   ```

   Quando a classe estiver certa, a última linha da saída é:

   ```text
   Desafiantes: 2 | Líder: 1
   ```

   Pista: o `Contador` só recebe os combates, e não sabe quem é o líder. Como é que, só com os três atributos de um registo, se sabe se ganhou o desafiante ou o líder?

## Antes de terminares

- [ ] O `ginasio.py` tem as classes `Treinador`, `Lider`, `Combate` e `Ginasio`, com o `Combate` escrito como dataclass, e `python3 ginasio.py` mostra os combates de Celadon e o histórico.
- [ ] `python3 anunciar.py` mostra os três combates, o placard, o narrador e, no fim, o registo `Combate(...)`, `True` e `False`.
- [ ] Entregaste ao professor o `ginasio.py`, o `anunciadores.py` e o `anunciar.py`, conforme ele indicar.

![Rodapé](../../imagens/rodape.png)
