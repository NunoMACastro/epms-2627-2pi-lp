![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: construir o ginásio Pokémon

## O que vais fazer

Vais construir no computador, uma classe de cada vez, o ginásio Pokémon da parte 4 do [guia](03-objetos-e-composicao.md): o treinador com a sua equipa, o registo de um combate e o ginásio que organiza os combates. Depois de cada classe, vais executar um pequeno teste, e antes de cada teste vais escrever o que achas que ele vai mostrar.

Além de pores o programa a funcionar, vais ver com os teus olhos, no computador, as ideias da parte 4: que a equipa de um treinador guarda os mesmos Pokémon que existem fora dele, que o mesmo treinador pode desafiar dois ginásios, e o que sobrevive e o que desaparece quando um ginásio deixa de existir. Depois há uma parte autónoma, em que acrescentas ao ginásio um método teu.

Numa segunda volta, das partes 8 a 10, vais acrescentar ao mesmo ginásio o que as partes 5, 6 e 7 do guia ensinam: o líder, criado por um construtor alternativo; os anunciadores dos combates, por duck typing; e o registo de um combate escrito como dataclass. Esta segunda volta também acaba numa parte autónoma, em que escreves um anunciador teu.

Este laboratório não repete a teoria. Tem o guia aberto ao lado: é de lá que vais tirar o código de cada classe, e é lá que está explicado o porquê de cada linha. Cada parte diz a secção do guia de que precisas.

## O que precisas de saber antes

Do guia, precisas das partes 1 a 3 e das secções da parte 4 até ao exemplo guiado. Não precisas de as saber de cor, mas precisas de as ter lido, porque os testes deste laboratório só fazem sentido para quem sabe o que é uma referência, uma agregação e uma composição. Para a segunda volta, das partes 8 a 10, precisas também das partes 5, 6 e 7 do guia; cada parte do laboratório diz de que secções.

Do 10.º ano, precisas de saber criar uma pasta e um ficheiro no VS Code, abrir o terminal do VS Code nessa pasta e executar um ficheiro com `python3 nome.py`. No Windows, se `python3` não funcionar, experimenta `python` ou `py`.

## Material

O computador com o Python 3 e o VS Code, e o guia aberto ao lado. Uma folha de papel, ou um ficheiro de texto, para escreveres as previsões e as respostas às perguntas.

## Parte 1: Preparar a pasta e o ficheiro pokemon.py (5 min)

As classes de Pokémon já estão feitas: são as das partes 2 e 3 do guia, e estão no ficheiro `pokemon.py` dos exemplos. O teu ficheiro do ginásio vai importá-las desse ficheiro, e por isso os dois têm de estar na mesma pasta.

1. Cria uma pasta nova, chamada `ginasio-pokemon`, no sítio onde guardas os trabalhos desta disciplina, e abre-a no VS Code.
2. Abre o ficheiro [pokemon.py dos exemplos](../exemplos/python-avancado/pokemon/03-objetos-e-composicao/pokemon.py). Se tens este repositório no teu computador, copia o ficheiro para a tua pasta. Se o estás a ler no GitHub, usa o botão de copiar o conteúdo do ficheiro, que está por cima do código, cria na tua pasta um ficheiro novo chamado `pokemon.py`, cola o conteúdo e guarda. Também podes usar o botão de descarregar o ficheiro, ao lado do de copiar, e depois mover o ficheiro descarregado para a tua pasta.
3. Confirma o nome do ficheiro. Tem de ser exatamente `pokemon.py`, tudo em minúsculas e sem acento. Se o descarregaste, o browser pode tê-lo guardado com outro nome, como `pokemon (1).py`, e nesse caso muda-lhe o nome.
4. Abre o terminal do VS Code e executa `python3 pokemon.py`.

As duas primeiras linhas que deves ver são estas:

```text
Bulbasaur: vida 150, ataque 25
Squirtle: vida 100, ataque 50
```

Se as vês, o ficheiro está no sítio certo e funciona. O resto da saída é a demonstração que está no fim do `pokemon.py`, e mostra ataques entre os três Pokémon.

Essa demonstração está debaixo da linha `if __name__ == "__main__":`. É por isso que, nas partes seguintes, quando o teu ficheiro do ginásio importar o `pokemon.py`, a demonstração não vai aparecer: só corre quando executas o `pokemon.py` diretamente.

## Parte 2: O Treinador e a equipa (15 min)

Precisas da secção [O Treinador e a sua equipa](03-objetos-e-composicao.md#o-treinador-e-a-sua-equipa) do guia.

1. Na mesma pasta, cria um ficheiro novo chamado `ginasio.py`.
2. Na primeira linha, escreve a importação das três classes de Pokémon de que o ginásio vai precisar:

```python
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
```

3. Deixa duas linhas em branco e escreve a classe `Treinador`, tal como está no guia. Escreve-a tu, em vez de copiar e colar: ao escrever, vais reparar em pormenores que a leitura deixa escapar, como o `self` em todos os métodos e a indentação de cada linha.
4. No fim do ficheiro, depois da classe e sem indentação nenhuma, escreve estas linhas de teste:

```python
ash = Treinador("Ash")
ash.capturar(PokemonFogo("Charmander", 90, 40))
ash.capturar(PokemonPlanta("Bulbasaur", 110, 25, 20))
print(ash.nome, "tem", len(ash.equipa), "Pokémon")
print("Primeiro a lutar:", ash.escolher_pokemon().nome)
```

5. Antes de executar, escreve a tua previsão das duas linhas que o teste vai mostrar.
6. Executa `python3 ginasio.py` e compara.

A saída deve ser:

```text
Ash tem 2 Pokémon
Primeiro a lutar: Charmander
```

As linhas de teste têm de ficar no fim do ficheiro, depois das classes. O Python lê o ficheiro de cima para baixo, e uma linha que use `Treinador` antes de a classe ter sido definida dá erro.

## Parte 3: A equipa guarda o mesmo objeto (10 min)

Precisas das secções [Uma variável guarda uma referência, não uma cópia](03-objetos-e-composicao.md#uma-variável-guarda-uma-referência-não-uma-cópia) e [Agregação: o todo reúne partes que existem por si](03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si).

1. Apaga as linhas de teste da parte 2 e escreve estas no lugar delas:

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

2. Antes de executar, escreve a tua previsão das três linhas que o teste vai mostrar. A segunda é a mais difícil: pensa no que o `escolher_pokemon` devolve quando nenhum Pokémon da equipa tem vida.
3. Executa e compara.

A saída deve ser:

```text
True
None
Charmander está KO (0/150).
```

Responde por escrito a estas três perguntas:

- **a)** A linha `charmander.vida = 0` mudou a vida através da variável `charmander`, e não através da equipa. Porque é que o `escolher_pokemon` do Ash deixou de encontrar um Pokémon com vida?
- **b)** Depois de `del ash`, porque é que a última linha ainda consegue usar o Charmander?
- **c)** Que característica da agregação mostra a resposta à pergunta b)?

## Parte 4: O registo de um combate (5 min)

Precisas do [passo 4 do exemplo guiado](03-objetos-e-composicao.md#passo-4-o-combate).

1. Escreve a classe `Combate`, tal como está no guia, a seguir à classe `Treinador` e antes das linhas de teste.
2. Apaga as linhas de teste da parte 3 e escreve estas no lugar delas:

```python
registo = Combate("Ash", "Bulbasaur", "Ash")
print(registo.resumo())
```

3. Executa. A saída deve ser:

```text
Ash com Bulbasaur: venceu Ash
```

Estas linhas de teste criam um registo fora do ginásio, só para verificares que a classe está bem escrita. No programa final, os registos vão ser criados apenas pelo ginásio, porque são uma composição. É por isso que as vais apagar no início da parte seguinte.

## Parte 5: O ginásio, sem combates (10 min)

Precisas do [passo 5 do exemplo guiado](03-objetos-e-composicao.md#passo-5-o-ginasio-o-construtor-e-o-histórico).

1. Escreve a classe `Ginasio` a seguir à classe `Combate`, só com o construtor e com o método `mostrar_historico`. O método `combater` fica para a parte 6.
2. Apaga as linhas de teste da parte 4 e escreve estas no lugar delas:

```python
misty = Treinador("Misty")
misty.capturar(PokemonAgua("Starmie", 120, 35))
cerulean = Ginasio("Cerulean", misty)
print(cerulean.lider is misty)
print(len(cerulean.desafiantes), len(cerulean.combates))
cerulean.mostrar_historico()
```

3. Antes de executar, escreve a tua previsão. Repara que o `mostrar_historico` começa com um `\n`.
4. Executa e compara.

A saída deve ser esta, com uma linha em branco antes do título do histórico:

```text
True
0 0

Histórico do ginásio de Cerulean:
```

O `True` mostra que o líder do ginásio e a variável `misty` são o mesmo objeto: o ginásio recebeu a treinadora por parâmetro e guardou uma referência para ela, e não uma cópia. As duas listas estão vazias, porque ainda não houve combates, e por isso o histórico só tem o título.

## Parte 6: O combate (25 min)

Precisas do [passo 6](03-objetos-e-composicao.md#passo-6-o-método-combater) e do [passo 7](03-objetos-e-composicao.md#passo-7-prever-e-executar) do exemplo guiado.

1. Escreve o método `combater` dentro da classe `Ginasio`, entre o construtor e o `mostrar_historico`. Cuidado com a indentação: o método tem quatro espaços, as linhas dentro dele têm oito, e as linhas dentro do `while` e dos `if` têm doze ou dezasseis.
2. Apaga as linhas de teste da parte 5 e escreve no fim do ficheiro o programa principal do passo 7 do guia, que começa em `if __name__ == "__main__":`.
3. Antes de executar, faz no papel a tabela do primeiro combate, com uma linha por ataque, com o dano e a vida dos dois Pokémon depois de cada ataque. Se já leste o passo 7 do guia, tapa a tabela de lá e o parágrafo a seguir a ela, sobre o segundo combate, e faz a tua. Escreve também quem achas que ganha o segundo combate, e porquê.
4. Executa e compara com a tua tabela.

A saída tem de ser exatamente a do passo 7 do guia. As últimas linhas são estas:

```text
Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Misty
 - Ash com Bulbasaur: venceu Ash

Ash continua com 2 Pokémon; Misty continua com 1.
```

Se a tua saída for diferente, compara o teu código com o do guia linha a linha, a começar pelo método `combater`, e vê a secção [Quando alguma coisa corre mal](#quando-alguma-coisa-corre-mal), no fim deste laboratório.

Responde por escrito: se o programa principal tivesse um terceiro `cerulean.combater(ash)`, logo a seguir aos outros dois, o que escrevia esse terceiro combate? Porquê? Que relação entre classes explica isto? Depois de responderes, podes confirmar: acrescenta a linha, executa e volta a apagá-la.

## Parte 7: Duas experiências com as relações (15 min)

Precisas das secções [Agregação: o todo reúne partes que existem por si](03-objetos-e-composicao.md#agregação-o-todo-reúne-partes-que-existem-por-si), [Composição: o todo cria e guarda as suas partes](03-objetos-e-composicao.md#composição-o-todo-cria-e-guarda-as-suas-partes) e do [passo 8](03-objetos-e-composicao.md#passo-8-o-que-sobrevive-quando-o-ginásio-desaparece).

Nesta parte o Ash vai desafiar dois ginásios: o de Cerulean, da Misty, e o de Celadon, da Erika, que tem uma Tangela, de planta, com 50 de vida, 20 de ataque e 10 de regeneração. Depois, o ginásio de Cerulean vai desaparecer.

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

2. Antes de executar, escreve as tuas previsões: que Pokémon do Ash luta em Celadon, e com quanta vida começa? Quem ganha? O que escrevem as duas linhas com `in` e com `is`? O que mostra o histórico de Celadon depois de `del cerulean`?
3. Executa e compara.

Os dois combates de Cerulean são iguais aos da parte 6. A partir do combate de Celadon, a saída é esta:

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

Não há "É super eficaz!" em Celadon: o Bulbasaur e a Tangela são os dois de planta, e nenhum tem vantagem sobre o outro.

Responde por escrito:

- **a)** A linha com `is` escreveu `True`. O que quer isto dizer sobre o treinador que está na lista de desafiantes de Cerulean e o que está na de Celadon? Que característica da agregação mostra?
- **b)** Depois de `del cerulean`, o histórico de Celadon continua completo, e o Ash continua com os dois Pokémon. E os registos dos dois combates de Cerulean: ainda há alguma forma de lhes chegar? Que característica da composição mostra a tua resposta?

## Parte autónoma: contar as vitórias de um treinador (15 min)

Esta parte fazes sozinho. Não está no guia.

Acrescenta à classe `Ginasio` um método `vitorias_de(treinador)`, que recebe um treinador e devolve quantos combates desse ginásio esse treinador venceu. O método não escreve nada no ecrã: devolve um número.

Para o testar, acrescenta ao programa principal da parte 7 as duas linhas com `vitorias_de`, logo antes da linha `del cerulean`, com a mesma indentação das outras. O fim do programa principal fica assim:

```python
if __name__ == "__main__":
    # As linhas de cima ficam iguais às da parte 7, até à linha com is.
    print(cerulean.desafiantes[0] is celadon.desafiantes[0])
    print(cerulean.vitorias_de(ash), cerulean.vitorias_de(misty))
    print(celadon.vitorias_de(ash), celadon.vitorias_de(erika), celadon.vitorias_de(misty))
    del cerulean
    celadon.mostrar_historico()
    print(ash.nome, "continua com", len(ash.equipa), "Pokémon")
```

Quando o método estiver certo, estas duas linhas escrevem:

```text
1 1
1 0 0
```

As duas linhas de teste ficam antes do `del cerulean` porque, depois dele, a variável `cerulean` já não existe.

Antes de escreveres o método, olha outra vez para a classe `Combate` e para a linha do `combater` que cria cada registo: o que é que um registo guarda sobre o vencedor? A resposta decide a forma como comparas cada registo com o treinador que o método recebe.

## Parte 8: O líder e o construtor alternativo (15 min)

Precisas das secções [O método de classe recebe a classe](03-objetos-e-composicao.md#o-método-de-classe-recebe-a-classe) e [O líder, um treinador que escolhe de outra maneira](03-objetos-e-composicao.md#o-líder-um-treinador-que-escolhe-de-outra-maneira), da parte 5 do guia.

1. Na classe `Treinador` do teu `ginasio.py`, acrescenta o método de classe `com_equipa`, entre o construtor e o `capturar`, tal como está no guia. Não te esqueças da linha `@classmethod` por cima do `def`.
2. A seguir à classe `Treinador`, e antes da classe `Combate`, escreve a classe `Lider`, com o seu `escolher_pokemon`.
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

4. Antes de executar, escreve a tua previsão das três primeiras linhas. Não precisas de prever os combates ataque a ataque.
5. Executa e compara.

As três primeiras linhas devem ser estas:

```text
Lider 2
Treinador 2
Gloom Squirtle
```

Depois vêm os dois combates, e a saída acaba com este histórico:

```text
Histórico do ginásio de Celadon:
 - Ash com Squirtle: venceu Erika
 - Ash com Charmander: venceu Ash
```

Responde por escrito:

- **a)** No `com_equipa` não há nenhuma linha com a palavra `Lider`. Que linha faz com que a Erika saia um `Lider`?
- **b)** No primeiro combate, a Erika lutou com o Gloom; no segundo, com a Tangela. Porque é que mudou de Pokémon? Procura, na saída do primeiro combate, a vida com que o Gloom acabou.
- **c)** Muda, só por um momento, a primeira linha do programa principal para `erika = Treinador.com_equipa(...)`, com a mesma equipa. Antes de executar, prevê que Pokémon escolhe a Erika no primeiro combate e quem ganha cada um dos dois combates. Executa, compara e volta a pôr `Lider`.

## Parte 9: Anunciar os combates (15 min)

Precisas do [passo 2](03-objetos-e-composicao.md#passo-2-o-que-o-ginásio-precisa-de-um-anunciador) e do [passo 3](03-objetos-e-composicao.md#passo-3-dois-anunciadores-sem-nada-em-comum) do exemplo guiado da parte 6 do guia.

1. Acrescenta à classe `Ginasio` o método `anunciar_combates`, no fim da classe, depois do `mostrar_historico`.
2. Na mesma pasta, cria um ficheiro novo chamado `anunciadores.py` e escreve nele as classes `Narrador` e `Placard`, tal como estão no passo 3.
3. Cria outro ficheiro novo, `anunciar.py`, com este programa:

```python
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

Este programa fica num ficheiro à parte, e não no programa principal do `ginasio.py`, de propósito. O `ginasio.py` não importa os anunciadores, nem precisa de os conhecer: quem junta o ginásio aos anunciadores é o `anunciar.py`.

4. Antes de executar, prevê quem vence cada um dos três combates. Uma pista: a Erika é líder, e um líder escolhe sempre o Pokémon com mais vida. Depois, prevê as três linhas do placard.
5. Executa `python3 anunciar.py` e compara.

Depois dos três combates, a saída deve acabar assim:

```text
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

Responde por escrito:

- **a)** O `ginasio.py` não tem nenhuma linha que fale de `Narrador` ou de `Placard`. Como é que o `anunciar_combates` consegue usar os dois?
- **b)** Acrescenta, no fim do `anunciar.py`, a linha `celadon.anunciar_combates(ash)`, que entrega o treinador Ash ao ginásio como se fosse um anunciador. Antes de executar, prevê o que acontece e em que momento. Executa, compara e apaga a linha.

## Parte 10: O registo como dataclass (10 min)

Precisas das secções [O que a dataclass escreve por ti](03-objetos-e-composicao.md#o-que-a-dataclass-escreve-por-ti) e [O Combate do ginásio passa a dataclass](03-objetos-e-composicao.md#o-combate-do-ginásio-passa-a-dataclass), da parte 7 do guia.

1. Antes de mexeres na classe `Combate`, acrescenta estas linhas ao fim do `anunciar.py`:

```python
print()
print(celadon.combates[0])
print(celadon.combates[0] == celadon.combates[2])
print(celadon.combates[0] is celadon.combates[2])
```

2. Executa e copia para as tuas notas as três últimas linhas da saída. Devem ser parecidas com estas, com outro número depois de `at`:

```text
<ginasio.Combate object at 0x100cc0590>
False
False
```

3. Agora transforma a classe `Combate` do `ginasio.py` numa dataclass, como no guia. Acrescenta a linha `from dataclasses import dataclass` no início do ficheiro, antes da importação dos Pokémon, com uma linha em branco a separá-las; põe `@dataclass` por cima da classe; troca o construtor pelos três campos, cada um com o seu tipo; e deixa o `resumo` como está.
4. Antes de executar outra vez, prevê: os combates e os anúncios mudam? E as três últimas linhas?
5. Executa e compara.

Tudo o que vem antes das três últimas linhas fica exatamente igual. As três últimas passam a ser estas:

```text
Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Ash')
True
False
```

Responde por escrito:

- **a)** O `combater` cria os registos com `Combate(desafiante.nome, atacante.nome, vencedor.nome)`, e não mudaste essa linha. Porque é que continua a funcionar com a dataclass?
- **b)** O primeiro e o terceiro combates aconteceram em alturas diferentes, mas, com a dataclass, o `==` diz que são iguais. O que é que um registo guarda, e o que não guarda, que faz com que os dois sejam iguais? E o `is`, o que continua a dizer?

## Parte autónoma: um anunciador que conta vitórias (15 min)

Esta parte fazes sozinho. Não está no guia.

No `anunciadores.py`, escreve uma classe nova, `Contador`, que serve de anunciador: tem um método `anunciar(combate)`, como o `Narrador` e o `Placard`, mas não escreve nada quando recebe um combate. Em vez disso, conta quantos combates ganharam os desafiantes e quantos ganhou o líder. Tem também um método `mostrar()`, que escreve as duas contagens numa linha, como `Desafiantes: 2 | Líder: 1`.

Para o testares, junta o `Contador` à linha que importa os anunciadores no `anunciar.py` e acrescenta estas linhas ao fim do ficheiro:

```python
contador = Contador()
celadon.anunciar_combates(contador)
contador.mostrar()
```

Quando a classe estiver certa, a última linha da saída é:

```text
Desafiantes: 2 | Líder: 1
```

Antes de escreveres a classe, repara que o `Contador` não sabe quem é o líder do ginásio: só recebe os combates, um a um. Olha para os três atributos de um registo. Como é que, só com um registo, se sabe se ganhou o desafiante ou o líder?

## Quando alguma coisa corre mal

**`can't open file '...ginasio.py': [Errno 2] No such file or directory`.** O Python não encontrou o ficheiro que mandaste executar, porque o terminal está aberto noutra pasta. A mensagem mostra o caminho completo onde o procurou. Abre no VS Code a pasta `ginasio-pokemon` e abre aí um terminal novo, que já começa nessa pasta, ou muda para ela com `cd`.

**`ModuleNotFoundError: No module named 'pokemon'`.** O Python não encontrou o ficheiro `pokemon.py`. Confirma que está na mesma pasta que o `ginasio.py` e que o nome é exatamente `pokemon.py`, em minúsculas, sem acento e sem nada a mais, como `pokemon (1).py`.

**`ImportError: cannot import name 'PokemonAgau' from 'pokemon'`.** O ficheiro foi encontrado, mas não tem uma classe com o nome escrito na importação. Aqui, `PokemonAgau` está mal escrito. A mensagem continua com o caminho do teu `pokemon.py`, entre parênteses, e nas versões recentes do Python acaba com uma sugestão do nome certo.

**`NameError: name 'Treinador' is not defined`.** Há uma linha a usar a classe antes de ela ser definida. As linhas de teste e o programa principal ficam sempre no fim do ficheiro, depois de todas as classes.

**`AttributeError: 'Treinador' object has no attribute 'capturar'`.** O método existe no ficheiro, mas não está dentro da classe. Um método tem de estar indentado quatro espaços em relação à linha `class`. Se o `def capturar` começar na margem, é uma função solta, e não um método do treinador.

**`TypeError: Treinador.capturar() takes 1 positional argument but 2 were given`.** Falta o `self` na definição do método: escreveste `def capturar(pokemon):` em vez de `def capturar(self, pokemon):`. Nas versões antigas do Python, a mensagem começa só por `capturar()`, sem o nome da classe.

**`AttributeError: 'Treinador' object has no attribute 'equipa'`.** No construtor, a linha da equipa ficou sem `self.`: `equipa = []` cria uma variável que desaparece quando o construtor acaba. Tem de ser `self.equipa = []`.

**A demonstração do `pokemon.py` aparece quando executas o `ginasio.py`.** Alguém apagou a linha `if __name__ == "__main__":` do `pokemon.py` e tirou a indentação das linhas debaixo dela. Se só uma destas duas coisas foi feita, o que aparece é um erro: um `NameError` sobre o `PokemonPlanta`, se só se apagou a linha, ou um `IndentationError`, se só se tirou a indentação. Em qualquer dos casos, volta a copiar o ficheiro dos exemplos.

**O programa não para.** Carrega em Ctrl+C no terminal para o interromper. Um combate que nunca acaba vem quase sempre do ciclo `while True` do `combater`: confirma que tens os dois `break`, que as condições são `defensor.vida == 0` e `atacante.vida == 0`, e que não mudaste o ataque mínimo no `pokemon.py`. Com ataque mínimo 1, cada ataque tira pelo menos 1 de vida, e o combate acaba sempre.

**A saída tem os números certos mas as linhas em branco não coincidem.** Confirma os `\n` no início dos títulos do `combater` e do `mostrar_historico`, e o `print()` sozinho do programa principal da parte 7, que escreve uma linha em branco.

**`TypeError: Treinador.com_equipa() missing 1 required positional argument: 'pokemons'`.** Falta a linha `@classmethod` por cima do `def com_equipa`. Sem ela, o Python não passa a classe ao método, e os valores que dás ficam desencontrados dos parâmetros: o nome vai para o `cls`, a lista vai para o `nome`, e o `pokemons` fica sem nada. Nas versões antigas do Python, a mensagem começa só por `com_equipa()`.

**Na parte 8, a primeira linha diz `Treinador 2` em vez de `Lider 2`.** No `com_equipa`, a linha que cria o treinador está escrita `Treinador(nome)`. Tem de ser `cls(nome)`, para criar um objeto da classe por onde o método foi chamado.

**`ModuleNotFoundError: No module named 'anunciadores'`.** O Python não encontrou o ficheiro `anunciadores.py`. Confirma que está na mesma pasta que o `anunciar.py` e o `ginasio.py`, e que o nome está escrito exatamente assim, em minúsculas e sem acentos.

**`AttributeError: 'Placard' object has no attribute 'numero'`.** O `Placard` ficou sem o construtor, ou o construtor ficou sem o `self.` na linha `self.numero = 0`. É o mesmo problema da equipa sem `self.`, mais acima.

**`TypeError: Combate() takes no arguments`.** A classe `Combate` tem os campos, mas falta a linha `@dataclass` por cima dela. Sem o decorador, ninguém escreve o construtor.

**`NameError: name 'dataclass' is not defined`.** Falta a linha `from dataclasses import dataclass` no início do `ginasio.py`.

**`TypeError: Combate.__init__() takes 3 positional arguments but 4 were given`.** Um dos três campos ficou sem o tipo, por exemplo `vencedor = ""` em vez de `vencedor: str`. Sem a anotação, a linha não é um campo, e o construtor da dataclass só recebe os outros dois. Nas versões antigas do Python, a mensagem começa só por `__init__()`.

## O que entregar

O ficheiro `ginasio.py`, na versão final: com as classes `Treinador`, `Lider`, `Combate` e `Ginasio`, com o método `vitorias_de` e o `anunciar_combates`, o `Combate` já como dataclass, e o programa principal da parte 8. Entrega também o `anunciadores.py`, com o teu `Contador`, e o `anunciar.py`, com as linhas de teste das partes 10 e autónoma. Se fizeste só a primeira volta, entrega o `ginasio.py` com o programa principal da parte 7 e as duas linhas de teste da primeira parte autónoma.

Entrega também as tuas previsões e as respostas às perguntas das partes 3, 6, 7, 8, 9 e 10, escritas por ti, em papel ou num ficheiro de texto, conforme o professor indicar.

![Rodapé](../imagens/rodape.png)
