![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: construir o ginásio Pokémon

## O que vais fazer

Vais construir no computador, uma classe de cada vez, o ginásio Pokémon da parte 4 do [guia](03-objetos-e-composicao.md): o treinador com a sua equipa, o registo de um combate e o ginásio que organiza os combates. Depois de cada classe, vais executar um pequeno teste, e antes de cada teste vais escrever o que achas que ele vai mostrar.

Além de pores o programa a funcionar, vais ver com os teus olhos, no computador, as ideias da parte 4: que a equipa de um treinador guarda os mesmos Pokémon que existem fora dele, que o mesmo treinador pode desafiar dois ginásios, e o que sobrevive e o que desaparece quando um ginásio deixa de existir. No fim há uma parte autónoma, em que acrescentas ao ginásio um método teu.

Este laboratório não repete a teoria. Tem o guia aberto ao lado: é de lá que vais tirar o código de cada classe, e é lá que está explicado o porquê de cada linha. Cada parte diz a secção do guia de que precisas.

## O que precisas de saber antes

Do guia, precisas das partes 1 a 3 e das secções da parte 4 até ao exemplo guiado. Não precisas de as saber de cor, mas precisas de as ter lido, porque os testes deste laboratório só fazem sentido para quem sabe o que é uma referência, uma agregação e uma composição.

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

## O que entregar

O ficheiro `ginasio.py`, na versão final: com as classes `Treinador`, `Combate` e `Ginasio`, com o método `vitorias_de`, e com o programa principal da parte 7 e as duas linhas de teste da parte autónoma. Entrega também as tuas previsões e as respostas às perguntas das partes 3, 6 e 7, escritas por ti, em papel ou num ficheiro de texto, conforme o professor indicar.

![Rodapé](../imagens/rodape.png)
