![Cabeçalho](../imagens/cabecalho.png)

# Testes de comportamento com pytest

Módulo 10794, Programação avançada com Python. Neste guia aprendes a escrever testes: pequenas funções que executam o teu código e confirmam sozinhas que ele faz o que as regras dizem. Lês o guia ao teu ritmo, de preferência em mais do que uma vez, e o que não acabares na aula acabas em casa ou na aula seguinte. Para praticar, há o [laboratório](05-testes-com-pytest-laboratorio.md) e a [ficha de exercícios](05-testes-com-pytest-exercicios.md) deste tema.

Até aqui, para saber se o ginásio Pokémon funcionava, executavas um programa e comparavas a saída com a tua previsão. Funciona com um programa pequeno e com paciência. Deixa de funcionar quando o programa cresce, ou quando mudas uma linha e tens de voltar a confirmar tudo. Também falha quando o erro está num número que passa despercebido no meio de trinta linhas.

Um teste faz essa comparação por ti. Escreves uma vez o que o código deve fazer, e o teste confirma-o sempre que o corres, em menos de um segundo. Neste guia, os testes confirmam o comportamento do ginásio: o dano de cada ataque, a vida depois de um KO, as recusas e o registo dos combates. Por isso se chamam testes de comportamento.

O código completo do exemplo está na pasta [05-testes-com-pytest](../exemplos/python-avancado/pokemon/05-testes-com-pytest/) dos exemplos. Os quatro ficheiros do ginásio, o `pokemon.py`, o `erros.py`, o `anunciadores.py` e o `ginasio.py`, são iguais aos da pasta 04: este tema não muda o ginásio, testa-o. Os ficheiros novos são dois ficheiros de testes, o [test_pokemon.py](../exemplos/python-avancado/pokemon/05-testes-com-pytest/test_pokemon.py) e o [test_ginasio.py](../exemplos/python-avancado/pokemon/05-testes-com-pytest/test_ginasio.py).

Para executares os programas deste guia, cria uma pasta nova no teu computador, com o nome `testes-do-ginasio`. Copia para lá só os quatro ficheiros do ginásio da pasta 05, sem os ficheiros de testes. Os testes escreves tu, à medida que o guia os mostra, e no fim podes compará-los com os da pasta 05, que tem estes e mais alguns. Para executar um programa, abre o terminal do VS Code na pasta e escreve `python3 nome-do-ficheiro.py`. No Windows, se `python3` não funcionar, experimenta `python` ou `py`.

Antes de executares um programa ou um teste, escreve o que achas que vai acontecer, e só depois compara. As saídas mostradas são as do Python 3.14, com o pytest 9.1. No Python 3.9, com o pytest 8.4, são iguais, menos onde o guia diz o contrário.

Nas saídas do pytest, o guia mostra o cabeçalho completo só da primeira vez, com o caminho da pasta encurtado. Nas outras, a saída começa na linha `collected`, porque as linhas de cima dizem o sistema, as versões e a pasta, e no teu computador são outras. O tempo da última linha, como `in 0.01s`, muda de execução para execução. Quando aparece um objeto numa mensagem, como `<pokemon.PokemonPlanta object at 0x10a5e7820>`, o número depois de `at` também muda. Se o terminal for estreito, algumas linhas do resumo final aparecem cortadas, com reticências no fim.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. Testar a olhar para o ecrã
4. O assert: uma confirmação escrita em código
5. Uma função de teste
6. Correr os testes com o pytest
7. Um teste que falha
8. Preparar, fazer, confirmar
9. Um teste tem de distinguir o certo do errado
10. Os casos de fronteira: o KO e os limites da vida
11. Testar uma recusa: pytest.raises
12. Depois da recusa, o estado
13. A equipa vazia
14. Cada teste começa do zero
15. Uma fixture prepara o que vários testes repetem
16. Um teste antes da correção
17. Exemplo guiado: os testes da escolha do líder
18. Erros frequentes
19. Palavras novas deste guia
20. Verificar o que aprendeste
21. O que vem a seguir
22. Para saber mais

## O que vais aprender

No fim deste guia, consegues:

- explicar porque é que um teste escrito em código é melhor do que comparar a saída à mão, sempre que o programa muda;
- escrever uma função de teste com `assert`, com as três partes: preparar, fazer e confirmar;
- correr os testes com `python3 -m pytest` e ler o que o pytest diz quando um teste passa e quando falha;
- escolher casos normais, de fronteira e de erro que distinguem o código certo do código errado;
- confirmar com `pytest.raises` que um método recusa um pedido, e que o objeto fica como estava;
- usar uma fixture quando vários testes preparam o mesmo, e escrever o teste de um defeito antes de o corrigir.

## O que já sabes e vais usar

- Classes, objetos, atributos e métodos, e as propriedades com um set que corrige os valores fora dos limites: explicados nas partes 1 e 2 do guia [Objetos, composição e comportamento](03-objetos-e-composicao.md).
- A herança e os métodos reescritos com `super()`, como o `calcular_dano` de cada tipo de Pokémon: explicados na parte 3 desse guia.
- O ginásio Pokémon, com o `Treinador`, o `Lider`, o `Ginasio` e o método de classe `com_equipa`: explicados nas partes 4 e 5 e no exemplo guiado desse guia.
- O `Combate`, que é uma dataclass, e o `==` entre duas dataclasses, que compara os campos um a um: explicados na parte 7 desse guia.
- O que faz a arroba de um decorador, como o `@property`: explicado na parte 8 desse guia.
- As exceções do `erros.py`, a `EquipaCheia` e a `SemPokemonComVida`, o `raise` antes de mudar o estado, e o `try` com `except`: explicados no guia [Exceções, depuração e logging](04-excecoes-depuracao-e-logging.md).
- O registo do ginásio, feito com o logging, que escreve um aviso quando um combate é recusado: explicado no mesmo guia.
- O tuplo, um conjunto de valores entre parênteses, separados por vírgulas: explicado na secção "Uma pausa: tuplos" do mesmo guia.
- O traceback lido de baixo para cima, o sintoma e a causa de um erro, e a rotina de cinco passos para o encontrar: explicados no mesmo guia. O exemplo guiado desse guia, o dano a dobrar, volta aqui.
- O `with`, que usaste no 10.º ano para abrir ficheiros com `with open(...)`.
- O `assert`, que apareceu no 10.º ano como verificação rápida. Este guia explica-o desde o início, por isso não faz mal se não o usaste.
- Funções com `return`, listas, `len`, ciclos `for` com `range`, ciclos `while`, f-strings, o valor `None` e a pergunta `is None`: do 10.º ano e dos guias 03 e 04.
- Executar um programa no terminal do VS Code: do 10.º ano.

## Testar a olhar para o ecrã

No tema 04 aprendeste a rotina de cinco passos para encontrar a causa de um erro. O último passo é voltar a testar tudo: correr outra vez todos os casos, também os que já passavam, para confirmar que a correção não estragou outra coisa.

Até agora, voltar a testar tudo queria dizer executar o `ginasio.py` e ler a saída linha a linha. A demonstração do ginásio escreve mais de vinte linhas. Para confirmar que estão certas, tens de saber de cabeça quanto devia tirar cada ataque e quem devia ganhar cada combate. Depois de cada mudança, repetes tudo. À terceira vez, já não lês com atenção, e um 50 no lugar de um 25 passa despercebido.

Um **teste** é um pedaço de código que executa uma parte do teu programa e compara o resultado com o resultado esperado. Se forem iguais, o teste passa; se forem diferentes, o teste falha e diz-te onde. O resultado esperado escreves tu uma vez, a partir das regras do jogo, e o teste confirma-o sempre que o corres.

Um teste não lê o ecrã. Confirma valores: o número que um método devolve, o atributo de um objeto depois de uma ação, a exceção que um pedido recusado lança. É isso que o programa faz, o seu comportamento, e é isso que interessa confirmar. A forma como está escrito pode mudar, e o comportamento tem de ficar igual.

## O assert: uma confirmação escrita em código

A instrução `assert` confirma que uma condição é verdadeira. Escreve-se `assert` seguido de uma condição, como as do `if`. Se a condição é verdadeira, o `assert` não faz nada, e o programa continua. Se é falsa, o `assert` lança uma exceção, o `AssertionError`, e o programa para. Em inglês, "assert" quer dizer afirmar: o `assert` afirma que uma coisa é verdade, e o programa para se não for.

Guarda este programa na pasta `testes-do-ginasio`, com o nome `assert_dano.py`. Um Charmander, com 40 de ataque, calcula o dano contra um Bulbasaur. O fogo tem vantagem contra a planta. Antes de executares, prevê o que o programa escreve.

```python
# O assert: uma confirmação escrita em código.
from pokemon import PokemonFogo, PokemonPlanta

charmander = PokemonFogo("Charmander", 90, 40)
bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
dano = charmander.calcular_dano(bulbasaur)
assert dano == 80
print("O primeiro assert passou.")
assert dano == 40
print("O segundo assert passou.")
```

O resultado é este (a mensagem de erro está reduzida à última linha):

```text
É super eficaz!
O primeiro assert passou.
AssertionError
```

A primeira linha vem do próprio `calcular_dano`, que escreve "É super eficaz!" quando há vantagem. O dano é 80, o dobro do ataque. O primeiro `assert` confirma `dano == 80`, que é verdade, e o programa continua. O segundo confirma `dano == 40`, que é falso, e lança o `AssertionError`. O último `print` nunca corre.

Leitura guiada: as três primeiras linhas de código preparam os dois Pokémon e calculam o dano, como nos programas do tema 03. A partir daí, cada `assert` é uma pergunta com resposta obrigatória: se a resposta é "sim", o programa segue; se é "não", para. Os dois `print` só servem para veres até onde o programa chegou.

Repara no que a mensagem não diz. O `AssertionError` diz que uma condição era falsa, mas não diz quanto valia o `dano`. Para saberes, tinhas de acrescentar um `print`. A ferramenta que vais usar a seguir, o pytest, resolve isso.

## Uma função de teste

Um teste escreve-se como uma função, com um nome que começa por `test_` e que diz o que se está a confirmar. Cada função testa uma só coisa. As funções de teste ficam num ficheiro só delas, cujo nome também começa por `test_`, separado do código que testam.

Cria na pasta `testes-do-ginasio` o ficheiro `test_pokemon.py`, com este conteúdo:

```python
# test_pokemon.py: o primeiro teste do ginásio.
from pokemon import PokemonFogo, PokemonPlanta


def test_fogo_contra_planta_tira_o_dobro():
    """O fogo tem vantagem contra a planta: o dano é o dobro do ataque."""
    charmander = PokemonFogo("Charmander", 90, 40)
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    dano = charmander.calcular_dano(bulbasaur)
    assert dano == 80
```

Antes de o executares com `python3 test_pokemon.py`, prevê o que aparece no terminal.

O resultado é que não aparece nada. O programa acaba sem escrever uma linha, nem sequer o "É super eficaz!".

Leitura guiada: o ficheiro importa as duas classes e define uma função. Definir uma função não a executa: o `def` só guarda a função com aquele nome. Como ninguém chama a `test_fogo_contra_planta_tira_o_dobro`, o corpo dela nunca corre. A docstring diz, numa frase, o comportamento que o teste confirma. A função não recebe nada e não devolve nada: prepara, calcula e confirma.

Podias acrescentar no fim do ficheiro uma linha a chamar a função. Com vinte testes, eram vinte chamadas, e o primeiro `assert` que falhasse parava o programa: os testes seguintes já não corriam, e não sabias se também falhavam. Quem chama as funções de teste é outro programa, o pytest.

## Correr os testes com o pytest

O **pytest** é um programa que encontra os teus testes, chama-os um a um e diz quais passaram e quais falharam. Quando um teste falha, continua com os outros, e no fim diz porque falhou cada um, com os valores verdadeiros.

O pytest não vem com o Python: instala-se uma vez em cada computador. Para confirmares se já o tens, corre no terminal:

```bash
python3 -m pytest --version
```

Se aparecer uma linha como `pytest 9.1.1`, está instalado. O número pode ser outro, e no Python 3.9 é um 8. Se aparecer `No module named pytest`, instala-o com o comando seguinte, que descarrega o pytest da internet e o junta ao teu Python:

```bash
python3 -m pip install pytest
```

No Windows, os dois comandos são `py -m pytest --version` e `py -m pip install pytest`. Se a instalação for recusada, fala com o professor: alguns computadores não deixam instalar nada.

O `-m` quer dizer "corre este módulo": `python3 -m pytest` corre o pytest com o mesmo Python que usas para os teus programas. Usa sempre esta forma. Há também um comando `pytest`, sem o `python3 -m`, mas em alguns computadores corre com outro Python, ou nem existe.

Agora, no terminal, na pasta `testes-do-ginasio`, corre os testes. Antes, prevê quantos testes o pytest vai encontrar.

```bash
python3 -m pytest
```

O resultado é este:

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.8, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/.../testes-do-ginasio
collected 1 item

test_pokemon.py .                                                        [100%]

============================== 1 passed in 0.01s ===============================
```

O pytest encontrou um teste e o teste passou.

Leitura guiada: lê a saída de cima para baixo. A linha `platform` diz o sistema, a versão do Python e a do pytest. A linha `rootdir` diz a pasta onde o pytest procurou. A linha `collected 1 item` diz quantos testes encontrou: "collected" quer dizer recolhidos, e "item" é cada teste. Depois vem uma linha por ficheiro de testes, com um ponto por cada teste que passou, e a percentagem dos testes já corridos. A última linha é o resumo: `1 passed`, um passou, e o tempo que levou. No terminal do VS Code, esta linha aparece a verde quando todos passam.

O pytest procura, na pasta onde estás e nas pastas dentro dela, os ficheiros cujo nome começa por `test_`. Dentro deles, corre as funções cujo nome começa por `test_`. Os outros ficheiros e as outras funções são ignorados. É por isso que o `assert_dano.py` não entrou na conta.

Para veres o nome de cada teste, acrescenta a opção `-v`, de "verbose", que quer dizer detalhado:

```bash
python3 -m pytest -v
```

A saída, a partir da linha `collected`, é esta:

```text
collecting ... collected 1 item

test_pokemon.py::test_fogo_contra_planta_tira_o_dobro PASSED             [100%]

============================== 1 passed in 0.01s ===============================
```

Com o `-v`, cada teste tem uma linha com o ficheiro, dois pontos duas vezes e o nome da função. `PASSED` quer dizer que passou.

## Um teste que falha

Acrescenta ao `test_pokemon.py` um segundo teste, que confirma um ataque sem vantagem. Quem o escreveu copiou o primeiro e esqueceu-se de mudar o valor esperado. Para teres exatamente o mesmo ficheiro que o guia, substitui o conteúdo do `test_pokemon.py` por este:

```python
# test_pokemon.py: os testes das vantagens de tipo.
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


def test_fogo_contra_planta_tira_o_dobro():
    """O fogo tem vantagem contra a planta: o dano é o dobro do ataque."""
    charmander = PokemonFogo("Charmander", 90, 40)
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    dano = charmander.calcular_dano(bulbasaur)
    assert dano == 80


def test_fogo_contra_agua_tira_so_o_ataque():
    """Sem vantagem, o dano é o próprio ataque."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 100, 30)
    dano = charmander.calcular_dano(squirtle)
    assert dano == 80
```

Antes de correres `python3 -m pytest`, prevê qual dos dois testes falha e que valores o pytest vai mostrar.

O resultado, a partir da linha `collected`, é este:

```text
collected 2 items

test_pokemon.py .F                                                       [100%]

=================================== FAILURES ===================================
____________________ test_fogo_contra_agua_tira_so_o_ataque ____________________

    def test_fogo_contra_agua_tira_so_o_ataque():
        """Sem vantagem, o dano é o próprio ataque."""
        charmander = PokemonFogo("Charmander", 90, 40)
        squirtle = PokemonAgua("Squirtle", 100, 30)
        dano = charmander.calcular_dano(squirtle)
>       assert dano == 80
E       assert 40 == 80

test_pokemon.py:18: AssertionError
=========================== short test summary info ============================
FAILED test_pokemon.py::test_fogo_contra_agua_tira_so_o_ataque - assert 40 == 80
========================= 1 failed, 1 passed in 0.02s ==========================
```

Leitura guiada: como num traceback, lê de baixo para cima. A última linha conta: um falhou, um passou, e no terminal aparece a vermelho. A linha de cima, `FAILED`, diz qual foi o teste e porquê, em resumo. A secção `FAILURES`, que quer dizer falhas, mostra o código do teste que falhou. O sinal `>` aponta a linha onde o teste parou, e a linha `E`, de erro, mostra a comparação com os valores verdadeiros: `assert 40 == 80`. O pytest trocou o nome `dano` pelo valor que ele tinha, 40. Por baixo vem o ficheiro e o número da linha, `test_pokemon.py:18`. Na linha do progresso, o `F` é o teste que falhou, depois do ponto do que passou.

Na linha `E`, o valor da esquerda é o que o código deu, e o da direita é o que o teste esperava. Foi assim que o teste os escreveu: `dano == 80`, com o resultado do código à esquerda e o esperado à direita. É a diferença em relação ao `AssertionError` sozinho da secção anterior: o pytest mostra os valores sem precisares de um `print`.

Um teste que falha diz que o teste e o código não concordam. Não diz qual dos dois está errado. Quem decide são as regras do jogo, e não o código. O fogo não tem vantagem contra a água, por isso o dano tem de ser o próprio ataque, 40. O código está certo, e o teste é que está errado. Corrige o teste: a última linha passa a ser `assert dano == 40`. Corre outra vez, e os dois passam.

É a mesma regra do primeiro passo da rotina do tema 04. O resultado esperado tira-se do que o programa devia fazer, e não do código que se está a testar. Se mudasses o valor esperado só para o teste passar, sem confirmar a regra, o teste deixava de confirmar o que quer que fosse.

## Preparar, fazer, confirmar

Os dois testes que escreveste têm a mesma forma, em três partes. Primeiro preparam o que é preciso: criam o Charmander e o alvo. Depois fazem a ação que se quer testar, uma só: calculam o dano. Por fim confirmam o resultado com um `assert`. Em inglês, as três partes chamam-se **Arrange, Act, Assert**, e é com esses nomes que as vais encontrar nos livros e na internet. Aqui chamam-se **preparar, fazer e confirmar**.

Com as três partes à vista, um teste lê-se como uma frase: com estes Pokémon, este ataque tem de tirar isto. Fazer uma só ação tem uma razão. Se um teste fizesse duas, e falhasse, não sabias qual das duas tinha falhado.

O nome do teste diz o comportamento que se confirma, como uma frase: `test_fogo_contra_planta_tira_o_dobro`. Quando um teste falha, o nome é a primeira coisa que o pytest mostra, e deve bastar para saberes o que deixou de funcionar.

Substitui o conteúdo do `test_pokemon.py` por esta versão. Tem os dois testes que já tinhas, com o segundo corrigido, e mais dois, com as outras vantagens de tipo. O primeiro teste leva um comentário em cada parte; nos outros, as três partes estão separadas por uma linha em branco.

```python
# test_pokemon.py: os testes das vantagens de tipo, com as três partes de cada teste.
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


def test_fogo_contra_planta_tira_o_dobro():
    """O fogo tem vantagem contra a planta: o dano é o dobro do ataque."""
    # Preparar: os dois Pokémon do combate.
    charmander = PokemonFogo("Charmander", 90, 40)
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    # Fazer: só a ação que se está a testar.
    dano = charmander.calcular_dano(bulbasaur)
    # Confirmar: o resultado que as regras do jogo pedem.
    assert dano == 80


def test_fogo_contra_agua_tira_so_o_ataque():
    """Sem vantagem, o dano é o próprio ataque."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    dano = charmander.calcular_dano(squirtle)

    assert dano == 40


def test_agua_contra_fogo_tira_o_dobro():
    """A água tem vantagem contra o fogo: o dano é o dobro do ataque."""
    squirtle = PokemonAgua("Squirtle", 100, 30)
    charmander = PokemonFogo("Charmander", 90, 40)

    dano = squirtle.calcular_dano(charmander)

    assert dano == 60


def test_planta_contra_agua_tira_o_dobro():
    """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    dano = bulbasaur.calcular_dano(squirtle)

    assert dano == 50
```

Antes de correres `python3 -m pytest -v`, prevê o resultado de cada teste. Para o terceiro e o quarto, faz a conta: o Squirtle tem 30 de ataque, e o Bulbasaur 25.

O resultado, a partir da linha `collected`, é este:

```text
collecting ... collected 4 items

test_pokemon.py::test_fogo_contra_planta_tira_o_dobro PASSED             [ 25%]
test_pokemon.py::test_fogo_contra_agua_tira_so_o_ataque PASSED           [ 50%]
test_pokemon.py::test_agua_contra_fogo_tira_o_dobro PASSED               [ 75%]
test_pokemon.py::test_planta_contra_agua_tira_o_dobro PASSED             [100%]

============================== 4 passed in 0.01s ===============================
```

Os quatro passam. A água tira 60, o dobro de 30, e a planta tira 50, o dobro de 25.

Leitura guiada: todos os testes têm a mesma forma, e só mudam os Pokémon e o valor esperado. O nome diz quem ataca, quem é o alvo e o que tem de acontecer. Os testes correm pela ordem em que estão no ficheiro.

Repara que o "É super eficaz!" não apareceu, embora três dos testes calculem um dano com vantagem. O pytest guarda o que os testes escrevem com `print` e só o mostra quando um teste falha, numa secção própria. Assim, a saída dos testes fica limpa.

## Um teste tem de distinguir o certo do errado

No tema 04, encontraste com o depurador o dano a dobrar: na `PokemonPlanta`, a linha `dano = dano * 2` estava fora do `if`, e a planta tirava o dobro a qualquer alvo. Os teus quatro testes davam por esse erro? Para saber, põe-no de volta, de propósito. No `pokemon.py` da pasta `testes-do-ginasio`, no `calcular_dano` da `PokemonPlanta`, tira quatro espaços à linha da multiplicação, para ficar assim:

```python
    def calcular_dano(self, alvo):
        """Contra Água, a planta tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Água":
            print("É super eficaz!")
        dano = dano * 2
        return dano
```

Antes de correres `python3 -m pytest`, prevê quais dos quatro testes falham.

O resultado, a partir da linha `collected`, é este:

```text
collected 4 items

test_pokemon.py ....                                                     [100%]

============================== 4 passed in 0.01s ===============================
```

Passam os quatro. O código tem um erro, e nenhum teste deu por ele.

Leitura guiada: o único teste que usa a planta a atacar é o `test_planta_contra_agua_tira_o_dobro`. Contra a água, a planta tem vantagem, e o dobro está certo. A versão certa dá 50, e a versão errada também dá 50. Um teste em que o código certo e o código errado dão o mesmo resultado não distingue nada. Os outros três testes nem chamam o `calcular_dano` da planta.

Para apanhar este erro, é preciso um caso em que as duas versões deem resultados diferentes: a planta contra um alvo sem vantagem. Acrescenta este teste ao fim do `test_pokemon.py`:

```python


def test_planta_contra_fogo_tira_so_o_ataque():
    """A planta não tem vantagem contra o fogo: o dano é o próprio ataque."""
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    charmander = PokemonFogo("Charmander", 90, 40)

    dano = bulbasaur.calcular_dano(charmander)

    assert dano == 25
```

Antes de correres outra vez, com o erro ainda no `pokemon.py`, prevê o resultado.

O resultado, a partir da linha `collected`, é este:

```text
collected 5 items

test_pokemon.py ....F                                                    [100%]

=================================== FAILURES ===================================
___________________ test_planta_contra_fogo_tira_so_o_ataque ___________________

    def test_planta_contra_fogo_tira_so_o_ataque():
        """A planta não tem vantagem contra o fogo: o dano é o próprio ataque."""
        bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
        charmander = PokemonFogo("Charmander", 90, 40)
    
        dano = bulbasaur.calcular_dano(charmander)
    
>       assert dano == 25
E       assert 50 == 25

test_pokemon.py:53: AssertionError
=========================== short test summary info ============================
FAILED test_pokemon.py::test_planta_contra_fogo_tira_so_o_ataque - assert 50 ...
========================= 1 failed, 4 passed in 0.02s ==========================
```

O teste novo apanhou o erro: a planta tirou 50 a um alvo contra o qual não tem vantagem. Agora volta a indentar a linha `dano = dano * 2`, para ficar dentro do `if`, e corre outra vez. O resultado é `5 passed`.

Leitura guiada: o teste novo tem a mesma forma dos outros. A diferença está na escolha dos dados: um alvo de fogo, que a planta não vence. Com o código certo, o dano é 25; com o código errado, é 50. É essa diferença que faz o teste valer alguma coisa.

O número de testes não mede a qualidade. Quatro testes não apanharam o erro, e um quinto, bem escolhido, apanhou-o. Quando escolhes os dados de um teste, pergunta: se o código tivesse este erro, o resultado era diferente? Se a resposta é não, o teste não distingue nada, por mais testes que tenhas.

## Os casos de fronteira: o KO e os limites da vida

Os erros escondem-se onde as regras mudam. A vida de um Pokémon vai de 0 a 150. O set da propriedade `vida` corrige qualquer valor acima de 150 para 150, e qualquer valor abaixo de 0 para 0. Uma vida de 90 está no meio, longe dos limites. Uma vida de 150 é o último valor que fica como foi pedido, e 151 é o primeiro que é corrigido.

Um **caso de fronteira**, também chamado caso-limite, é um valor onde a regra muda, ou o valor logo a seguir. Para a vida máxima, as fronteiras são 150 e 151; para a mínima, 0 e -1. Um **caso normal** é um valor no meio da regra, como 90. Um **caso de erro** é um pedido que o código tem de recusar, como a sétima captura numa equipa de seis, que vem na secção seguinte.

Os casos de fronteira apanham os erros que só se veem no próprio limite. Imagina que, no set da vida, a comparação ficou com um número errado, `elif valor > 160:`, e a linha de baixo continua a pôr 150. Uma vida de 200 é corrigida para 150, como devia, e um teste com 200 passa. Uma vida de 151 fica 151, e só o teste com 151 dá pelo erro. Com uma vida de 90, longe do limite, nem se nota. Noutras regras, como a da equipa cheia, o erro do limite é escrever `>` onde devia estar `>=`, e a secção seguinte mostra um.

O KO também é uma fronteira. Um ataque que tira exatamente a vida que resta deixa o Pokémon com 0. Um ataque que tira mais do que isso também o tem de deixar com 0, e não com vida negativa.

Acrescenta estes cinco testes ao fim do `test_pokemon.py`:

```python


def test_ataque_que_tira_a_vida_toda_deixa_ko():
    """Um ataque que tira exatamente a vida que resta deixa o alvo com 0."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 40, 30)

    charmander.atacar(squirtle)

    assert squirtle.vida == 0


def test_ataque_maior_do_que_a_vida_nao_deixa_vida_negativa():
    """Um ataque maior do que a vida que resta deixa o alvo com 0, e não abaixo."""
    charmander = PokemonFogo("Charmander", 90, 40)
    squirtle = PokemonAgua("Squirtle", 25, 30)

    charmander.atacar(squirtle)

    assert squirtle.vida == 0


def test_vida_no_maximo_fica_como_esta():
    """150 é o último valor de vida que fica como foi pedido."""
    charmander = PokemonFogo("Charmander", 150, 40)

    assert charmander.vida == 150


def test_vida_acima_do_maximo_fica_no_maximo():
    """151 é o primeiro valor de vida acima do limite, e passa a 150."""
    charmander = PokemonFogo("Charmander", 151, 40)

    assert charmander.vida == 150


def test_vida_negativa_fica_a_zero():
    """-1 é o primeiro valor de vida abaixo do limite, e passa a 0."""
    charmander = PokemonFogo("Charmander", -1, 40)

    assert charmander.vida == 0
```

Antes de correres `python3 -m pytest`, prevê o resultado de cada um. No segundo, faz a conta: quanto tira o Charmander ao Squirtle, e quanta vida tem o Squirtle?

O resultado, a partir da linha `collected`, é este:

```text
collected 10 items

test_pokemon.py ..........                                               [100%]

============================== 10 passed in 0.01s ==============================
```

Passam todos. No segundo teste, o Charmander tira 40 a um Squirtle com 25 de vida. A conta dá -15, e o set da vida corrige-a para 0.

Leitura guiada: os dois primeiros testes têm as três partes. Preparam o atacante e o alvo, com a vida do alvo escolhida para a fronteira, fazem um ataque e confirmam a vida que ficou. Nos outros três, a ação é criar o Pokémon, porque é o construtor que passa a vida pelo set. Por isso a preparação e a ação são a mesma linha, e só há duas partes. Os três testes da vida usam os valores de fronteira, 150, 151 e -1, e não um valor qualquer acima ou abaixo.

## Testar uma recusa: pytest.raises

O caso de erro do ginásio mais conhecido é a equipa cheia. O `capturar` do `Treinador` aceita seis Pokémon e lança `EquipaCheia` à sétima captura. Como se testa que uma linha lança uma exceção?

Se o teste chamasse simplesmente o `capturar` sete vezes, a exceção da sétima parava o teste. Para o pytest, um teste parado por uma exceção é um teste que falhou. O teste precisa de dizer outra coisa: esta linha tem de lançar esta exceção, e se lançar está tudo bem.

É para isso que serve o `pytest.raises`. Usa-se com um `with`, como o `with open(...)` do 10.º ano: `with pytest.raises(EquipaCheia):` abre um bloco, e a linha dentro do bloco tem de lançar uma `EquipaCheia`. Se lançar, o `pytest.raises` apanha-a, e o teste continua depois do bloco. Se não lançar, o teste falha. O nome vem do inglês "raises", que quer dizer lança, como no `raise` do tema 04. Para o usar, o ficheiro de testes tem de começar por `import pytest`.

Cria na pasta `testes-do-ginasio` o ficheiro `test_ginasio.py`, com este conteúdo:

```python
# test_ginasio.py: os testes das recusas do ginásio.
import pytest

from erros import EquipaCheia
from ginasio import Treinador
from pokemon import Pokemon


def test_a_setima_captura_e_recusada():
    """A equipa aceita seis Pokémon e recusa o sétimo com EquipaCheia."""
    brock = Treinador("Brock")
    for numero in range(6):
        brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))

    with pytest.raises(EquipaCheia):
        brock.capturar(Pokemon("Onix", "Pedra", 50, 20))
```

Antes de correres `python3 -m pytest`, prevê quantos testes o pytest encontra agora, e em que ficheiros.

O resultado, a partir da linha `collected`, é este:

```text
collected 11 items

test_ginasio.py .                                                        [  9%]
test_pokemon.py ..........                                               [100%]

============================== 11 passed in 0.02s ==============================
```

O pytest encontrou os dois ficheiros e correu os onze testes, primeiro os do `test_ginasio.py`, pela ordem do nome dos ficheiros.

Leitura guiada: o teste prepara um treinador com seis Pokémon, capturados num ciclo. As seis capturas estão fora do `with`, e por isso têm de correr sem exceção: se uma delas lançasse a `EquipaCheia`, o teste falhava logo ali. A ação que se testa é a sétima captura, a única linha dentro do `with`. O `pytest.raises` é a confirmação: esta captura tem de ser recusada. O teste confirma as duas fronteiras: a sexta captura é aceite, e a sétima é recusada.

Agora um erro de propósito. No teste, muda o `range(6)` para `range(5)`, para o Brock ter só cinco Pokémon antes do `with`. Antes de correres `python3 -m pytest test_ginasio.py`, que corre só os testes desse ficheiro, prevê o que acontece.

O resultado, a partir da linha `collected`, é este:

```text
collected 1 item

test_ginasio.py F                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_a_setima_captura_e_recusada _______________________

    def test_a_setima_captura_e_recusada():
        """A equipa aceita seis Pokémon e recusa o sétimo com EquipaCheia."""
        brock = Treinador("Brock")
        for numero in range(5):
            brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
    
>       with pytest.raises(EquipaCheia):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE EquipaCheia

test_ginasio.py:15: Failed
=========================== short test summary info ============================
FAILED test_ginasio.py::test_a_setima_captura_e_recusada - Failed: DID NOT RA...
============================== 1 failed in 0.02s ===============================
```

Com cinco Pokémon, a captura dentro do `with` é a sexta, e a equipa aceita-a. Não houve exceção, e o teste falhou com `DID NOT RAISE EquipaCheia`, que quer dizer "não lançou `EquipaCheia`". No Python 3.9, com o pytest 8, a mensagem é `DID NOT RAISE <class 'erros.EquipaCheia'>`. O sinal `>` aponta a linha da captura, e não aparece a linha com os acentos circunflexos. Volta a pôr `range(6)` e confirma que o teste passa.

Dentro do `with` fica só a linha que deve lançar a exceção, como no `try` do tema 04. Uma linha a mais dentro do bloco tem dois problemas. Se essa linha lançar a exceção, o teste passa mesmo que a linha que querias testar esteja errada. E as linhas que vêm depois da que lançou a exceção nunca correm, porque a exceção salta logo para o fim do bloco.

## Depois da recusa, o estado

No tema 04, uma recusa tinha duas metades: o método lança a exceção, e não muda nada no objeto. É por isso que o `raise` vem antes do `append`. O `pytest.raises` confirma a primeira metade. A segunda confirma-se com um `assert` depois do bloco: a equipa tem de continuar com seis.

Este excerto mostra o teste da secção anterior com essa confirmação e com um nome que diz as duas metades. Ainda não é para correr: vai entrar no ficheiro completo da secção seguinte.

```python
def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
    """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
    brock = Treinador("Brock")
    for numero in range(6):
        brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))

    with pytest.raises(EquipaCheia):
        brock.capturar(Pokemon("Onix", "Pedra", 50, 20))

    assert len(brock.equipa) == 6
```

Imagina um `capturar` que junta primeiro o Pokémon à equipa e só depois verifica se ela passou de seis. Com esse código, a sétima captura lança a exceção na mesma, e o `pytest.raises` fica satisfeito. Mas a equipa fica com sete, e o `assert` do fim falha com `assert 7 == 6`. É o `assert` depois do bloco que apanha esse erro.

O teste não confirma o texto da mensagem da exceção. Confirma o que o objeto faz: lança a exceção certa e deixa a equipa como estava. Se amanhã alguém mudar uma vírgula na mensagem, o comportamento continua certo, e o teste continua a passar. É isto que quer dizer testar o comportamento.

## A equipa vazia

O `combater` do `Ginasio` também recusa: se um dos treinadores não tem Pokémon com vida, lança `SemPokemonComVida`, e o ginásio fica como estava. A forma mais simples de não ter Pokémon com vida é não ter Pokémon nenhum. Um treinador acabado de criar tem a equipa vazia, e o `escolher_pokemon` dele devolve `None`.

Substitui o conteúdo do `test_ginasio.py` por esta versão, com o teste da equipa cheia já com o `assert` do fim, e um teste novo para a equipa vazia:

```python
# test_ginasio.py: os testes das recusas do ginásio.
import pytest

from erros import EquipaCheia, SemPokemonComVida
from ginasio import Ginasio, Lider, Treinador
from pokemon import Pokemon, PokemonAgua


def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
    """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
    brock = Treinador("Brock")
    for numero in range(6):
        brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))

    with pytest.raises(EquipaCheia):
        brock.capturar(Pokemon("Onix", "Pedra", 50, 20))

    assert len(brock.equipa) == 6


def test_combate_sem_pokemon_com_vida_e_recusado():
    """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
    cerulean = Ginasio("Cerulean", misty)
    ash = Treinador("Ash")

    with pytest.raises(SemPokemonComVida):
        cerulean.combater(ash)

    assert cerulean.desafiantes == []
    assert cerulean.combates == []
```

Antes de correres `python3 -m pytest`, prevê o resultado do teste novo. O que fica na lista dos desafiantes de Cerulean depois da recusa?

O resultado, a partir da linha `collected`, é este:

```text
collected 12 items

test_ginasio.py ..                                                       [ 16%]
test_pokemon.py ..........                                               [100%]

============================== 12 passed in 0.02s ==============================
```

Passam os doze. A lista dos desafiantes fica vazia, porque o `combater` verifica primeiro se há Pokémon com vida, e só depois junta o desafiante à lista.

Leitura guiada: o teste novo prepara a Misty, o ginásio e um Ash sem Pokémon. A ação é o combate, dentro do `pytest.raises`. Depois do bloco, dois `assert` confirmam que o ginásio ficou como estava: nenhum desafiante e nenhum combate registado. Uma lista compara-se com `==`, e `[]` é a lista vazia. Os dois `assert` confirmam o mesmo comportamento, o ginásio intacto, e por isso ficam no mesmo teste.

O `combater` escreve também um aviso no registo do ginásio, com o logging do tema 04, antes de lançar a exceção. O pytest guarda as mensagens do registo como guarda as do `print`, e só as mostra quando um teste falha.

## Cada teste começa do zero

O teste da equipa vazia criou a sua Misty e o seu ginásio. Parece repetição, e é tentador criar o ginásio uma só vez, no início do ficheiro, para todos os testes o usarem. O programa desta secção faz isso. Guarda-o à parte, num ficheiro `test_partilhado.py`, na mesma pasta:

```python
# test_partilhado.py: dois testes que usam o mesmo ginásio, criado fora deles.
import pytest

from erros import SemPokemonComVida
from ginasio import Combate, Ginasio, Lider, Treinador
from pokemon import PokemonAgua, PokemonPlanta

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
cerulean = Ginasio("Cerulean", misty)


def test_o_desafiante_que_vence_fica_registado():
    """Quando o desafiante ganha, o registo do combate diz o nome dele."""
    ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])

    cerulean.combater(ash)

    assert cerulean.combates == [Combate("Ash", "Bulbasaur", "Ash")]


def test_combate_sem_pokemon_com_vida_e_recusado():
    """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
    ash = Treinador("Ash")

    with pytest.raises(SemPokemonComVida):
        cerulean.combater(ash)

    assert cerulean.combates == []
```

O primeiro teste faz um combate e confirma o registo. O `Combate` é uma dataclass, por isso o `==` compara os três campos, e duas listas são iguais quando têm os mesmos elementos, pela mesma ordem. O segundo teste é o da equipa vazia. Antes de correres `python3 -m pytest test_partilhado.py`, prevê o resultado dos dois.

O resultado, a partir da linha `collected`, é este:

```text
collected 2 items

test_partilhado.py .F                                                    [100%]

=================================== FAILURES ===================================
_________________ test_combate_sem_pokemon_com_vida_e_recusado _________________

    def test_combate_sem_pokemon_com_vida_e_recusado():
        """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
        ash = Treinador("Ash")
    
        with pytest.raises(SemPokemonComVida):
            cerulean.combater(ash)
    
>       assert cerulean.combates == []
E       AssertionError: assert [Combate(desa...ncedor='Ash')] == []
E         
E         Left contains one more item: Combate(desafiante='Ash', pokemon_desafiante='Bulbasaur', vencedor='Ash')
E         Use -v to get more diff

test_partilhado.py:28: AssertionError
------------------------------ Captured log call -------------------------------
WARNING  ginasio:ginasio.py:143 Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
=========================== short test summary info ============================
FAILED test_partilhado.py::test_combate_sem_pokemon_com_vida_e_recusado - Ass...
========================= 1 failed, 1 passed in 0.02s ==========================
```

O segundo teste falhou, e o ginásio não tem erro nenhum. A lista dos combates não está vazia, porque tem o combate do primeiro teste. A linha `Left contains one more item` quer dizer que a lista da esquerda tem um elemento a mais, e mostra-o. A secção `Captured log call` mostra o que o logging do ginásio guardou durante o teste: o aviso do combate recusado, que o pytest só mostra porque o teste falhou.

Agora corre só o segundo teste, e antes prevê se ele passa sozinho. Para correres um só teste, escreves o nome do ficheiro, dois pontos duas vezes e o nome do teste, como o pytest os mostra na linha `FAILED`:

```bash
python3 -m pytest test_partilhado.py::test_combate_sem_pokemon_com_vida_e_recusado
```

O resultado, a partir da linha `collected`, é este:

```text
collected 1 item

test_partilhado.py .                                                     [100%]

============================== 1 passed in 0.01s ===============================
```

Sozinho, o mesmo teste passa.

Leitura guiada: a Misty e o ginásio são criados no início do ficheiro, fora dos testes, e os dois testes usam o mesmo objeto `cerulean`. O primeiro teste corre primeiro e deixa um combate registado. Quando o segundo corre, encontra esse combate na lista. Sozinho, o segundo teste encontra o ginásio acabado de criar, e passa.

Um teste cujo resultado depende dos testes que correram antes é uma armadilha. Passa sozinho e falha com os outros, ou o contrário, e quem o lê não percebe porquê. A regra é cada teste começar do zero: prepara os seus próprios objetos e não depende da ordem por que os testes correm. Apaga o `test_partilhado.py`, para ele não ficar a falhar nas próximas execuções.

## Uma fixture prepara o que vários testes repetem

Cada teste do ginásio precisa de uma Misty e de um ginásio novos. Com um teste, são duas linhas. Com quatro testes, são oito linhas iguais, e se um dia quiseres mudar a Starmie, tens de a mudar em quatro sítios.

Uma **fixture** é uma função que prepara um objeto para os testes. Escreve-se como uma função normal, que cria o objeto e o devolve com `return`, e leva por cima o decorador `@pytest.fixture`. Um teste que precisa desse objeto escreve o nome da fixture como parâmetro. Antes de correr o teste, o pytest chama a fixture e entrega o que ela devolveu nesse parâmetro. Em inglês, "fixture" é o que se prepara e se deixa fixo para um ensaio.

O pytest chama a fixture de novo para cada teste que a pede. Cada teste recebe por isso um ginásio novo, acabado de criar, e nenhum vê os combates dos outros. É a regra da secção anterior, cumprida sem repetir as linhas.

O `@pytest.fixture` é um decorador, como o `@property` do tema 03. Escrever a arroba por cima do `def` é o mesmo que escrever, logo a seguir à função, `cerulean = pytest.fixture(cerulean)`. O nome `cerulean` passa a ser uma fixture, que o pytest reconhece quando procura os testes. Não precisas de saber como o pytest faz isso por dentro, só de saber ler o que a arroba faz.

Substitui o conteúdo do `test_ginasio.py` por esta versão. Tem uma fixture, o teste da equipa cheia e o teste da equipa vazia, já com a fixture. Tem também dois testes novos, que confirmam o registo de um combate ganho por cada um dos lados:

```python
# test_ginasio.py: os testes do ginásio, com uma fixture.
import pytest

from erros import EquipaCheia, SemPokemonComVida
from ginasio import Combate, Ginasio, Lider, Treinador
from pokemon import Pokemon, PokemonAgua, PokemonFogo, PokemonPlanta


@pytest.fixture
def cerulean():
    """Devolve um ginásio novo em Cerulean, com a Misty como líder e só a Starmie."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
    return Ginasio("Cerulean", misty)


def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
    """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
    brock = Treinador("Brock")
    for numero in range(6):
        brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))

    with pytest.raises(EquipaCheia):
        brock.capturar(Pokemon("Onix", "Pedra", 50, 20))

    assert len(brock.equipa) == 6


def test_combate_sem_pokemon_com_vida_e_recusado(cerulean):
    """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
    ash = Treinador("Ash")

    with pytest.raises(SemPokemonComVida):
        cerulean.combater(ash)

    assert cerulean.desafiantes == []
    assert cerulean.combates == []


def test_o_desafiante_que_vence_fica_registado(cerulean):
    """Quando o desafiante ganha, o registo do combate diz o nome dele."""
    ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])

    cerulean.combater(ash)

    assert cerulean.combates == [Combate("Ash", "Bulbasaur", "Ash")]


def test_o_lider_que_vence_fica_registado(cerulean):
    """Quando o líder ganha, o registo do combate diz o nome do líder."""
    ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])

    cerulean.combater(ash)

    assert cerulean.combates == [Combate("Ash", "Charmander", "Misty")]
```

Antes de correres `python3 -m pytest -v test_ginasio.py`, responde a duas perguntas. Quantas vezes é chamada a função `cerulean`? Quem ganha cada um dos dois combates?

O resultado, a partir da linha `collected`, é este:

```text
collecting ... collected 4 items

test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis PASSED [ 25%]
test_ginasio.py::test_combate_sem_pokemon_com_vida_e_recusado PASSED     [ 50%]
test_ginasio.py::test_o_desafiante_que_vence_fica_registado PASSED       [ 75%]
test_ginasio.py::test_o_lider_que_vence_fica_registado PASSED            [100%]

============================== 4 passed in 0.01s ===============================
```

Passam os quatro. A função `cerulean` é chamada três vezes, uma por cada teste que tem `cerulean` como parâmetro. O teste da equipa cheia não a pede, e por isso não a recebe.

Os dois combates fazem-se assim. O Bulbasaur tira 50 à Starmie, o dobro de 25, e deixa-a com 40. A Starmie tira 35 ao Bulbasaur, que fica com 75. O Bulbasaur volta a tirar 50, e a Starmie fica KO: ganha o Ash. No outro combate, o Charmander tira 40, e a Starmie fica com 50. A Starmie tira 70, o dobro de 35, e o Charmander fica com 20. O Charmander tira mais 40, e a Starmie fica com 10. A Starmie tira 70, e o Charmander fica KO: ganha a Misty.

Leitura guiada: começa pela fixture, no topo. É uma função com docstring, que cria a Misty e o ginásio e devolve o ginásio. A docstring diz o que ela prepara, porque quem lê um teste que a usa precisa de saber que a Starmie tem 90 de vida e 35 de ataque. Depois lê os testes que a pedem: o parâmetro `cerulean` tem o nome da fixture, e dentro do teste usa-se como qualquer variável. Os dois testes novos fazem um combate cada e confirmam a lista dos combates, comparada com uma lista com o registo esperado.

Uma fixture vale a pena quando vários testes preparam exatamente o mesmo, e a preparação tem mais do que uma linha ou pode vir a mudar. Não vale a pena para um só teste, nem para testes que precisam de dados diferentes. O teste da equipa cheia usa um Brock com seis Pokémon de pedra, que nenhum outro teste usa, e por isso prepara-os ele próprio. Uma fixture também esconde a preparação. Quem lê o teste tem de ir à fixture ver o que ela faz, e é por isso que não se usa quando não poupa nada.

## Um teste antes da correção

Imagina que um colega mudou o `recuperar` da `PokemonPlanta`. Trocou `self.vida` por `self._vida` na linha que soma a regeneração, "para ser mais direto". Para seguires este exemplo, faz tu a mesma mudança no `pokemon.py` da pasta `testes-do-ginasio`. A linha fica assim:

```python
        self._vida = self.vida + self.regeneracao
```

Dias depois, chega um relato: "Um Bulbasaur com 140 de vida recuperou e ficou com 160." Antes de mexeres no código, segue o primeiro passo da rotina do tema 04: observar e reproduzir o erro. Com testes, reproduzir o erro quer dizer escrever um teste que falha por causa dele. Acrescenta este teste ao fim do `test_pokemon.py`:

```python


def test_planta_recupera_ate_ao_maximo():
    """A recuperação passa pelo set da vida, que não a deixa passar de 150."""
    bulbasaur = PokemonPlanta("Bulbasaur", 140, 25, 20)

    bulbasaur.recuperar()

    assert bulbasaur.vida == 150
```

Antes de correres `python3 -m pytest`, prevê se o teste novo passa com o código do colega, e que valores aparecem na linha `E`.

O resultado, a partir da linha `collected`, é este:

```text
collected 15 items

test_ginasio.py ....                                                     [ 26%]
test_pokemon.py ..........F                                              [100%]

=================================== FAILURES ===================================
______________________ test_planta_recupera_ate_ao_maximo ______________________

    def test_planta_recupera_ate_ao_maximo():
        """A recuperação passa pelo set da vida, que não a deixa passar de 150."""
        bulbasaur = PokemonPlanta("Bulbasaur", 140, 25, 20)
    
        bulbasaur.recuperar()
    
>       assert bulbasaur.vida == 150
E       assert 160 == 150
E        +  where 160 = <pokemon.PokemonPlanta object at 0x10a5e7820>.vida

test_pokemon.py:103: AssertionError
----------------------------- Captured stdout call -----------------------------
Bulbasaur recupera vida.
Bulbasaur tem 160/150 de vida.
=========================== short test summary info ============================
FAILED test_pokemon.py::test_planta_recupera_ate_ao_maximo - assert 160 == 150
========================= 1 failed, 14 passed in 0.03s =========================
```

O teste falha, e falha pela razão certa: a vida ficou em 160, como no relato. O defeito está reproduzido.

Leitura guiada: a linha `E` tem agora uma segunda parte. `where 160 = <pokemon.PokemonPlanta object at 0x...>.vida` quer dizer "onde 160 é o `.vida` deste objeto": o pytest explica de onde veio o 160. A secção `Captured stdout call` mostra o que o teste escreveu com `print` enquanto corria. "stdout" é o nome técnico da saída normal de um programa, o ecrã. São as duas linhas do `recuperar`, e a segunda até mostra a vida acima do máximo.

Agora corrige a causa, o quarto passo da rotina. O `self._vida` guarda o valor diretamente, sem passar pelo set da propriedade, e é o set que não deixa a vida passar de 150. Volta a pôr `self.vida = self.vida + self.regeneracao`, como estava. Depois, o quinto passo, voltar a testar tudo, é só correr `python3 -m pytest` outra vez. O resultado é `15 passed`.

O teste fica no ficheiro para sempre. Se alguém repetir a mudança do colega, daqui a um mês, o teste falha e diz exatamente o que se partiu. Uma **regressão** é um defeito que volta, ou uma coisa que funcionava e deixou de funcionar depois de uma mudança. Um **teste de regressão** é o teste que fica a guardar o sítio onde um defeito já apareceu. O teste da planta contra o fogo, da secção sobre distinguir o certo do errado, é outro: guarda o dano a dobrar do tema 04.

O teste escreve-se antes da correção por duas razões. Primeiro, ao vê-lo falhar, confirmas que percebeste o defeito: o teste reproduz o relato. Segundo, depois de corrigires, o mesmo teste a passar prova que a correção resolveu esse defeito. Um teste escrito só depois da correção passa logo, e não sabes se teria apanhado o defeito.

Com testes, a rotina de cinco passos ganha uma ferramenta. O primeiro passo, reproduzir o erro, fica escrito num teste que falha. O quinto, voltar a testar tudo, é um comando: `python3 -m pytest` corre todos os testes, também os que já passavam.

## Exemplo guiado: os testes da escolha do líder

Este exemplo escreve os testes de um método, do que ele promete até à confirmação de que os testes valem alguma coisa. O método é o `escolher_pokemon` do `Lider`, no `ginasio.py`:

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

### Etapa 1: Ler o que o método promete

A docstring diz duas coisas. O líder escolhe o Pokémon com mais vida. Se estão todos KO, devolve `None`. Há um terceiro caso que a docstring não diz, mas que o ginásio usa: uma equipa vazia. Uma equipa sem Pokémon não tem nenhum Pokémon com vida, e o `combater` conta com o `None` para recusar o combate. Os testes confirmam o que o método promete, e não o que o código faz linha a linha.

### Etapa 2: Escolher os casos

Para cada promessa, um caso, com os dados escolhidos para distinguir o certo do errado.

| Caso | Equipa da Misty | Resultado esperado | Porque estes dados |
| --- | --- | --- | --- |
| Normal | Starmie com 90, Staryu com 120 | A Staryu | O mais forte não é o primeiro da lista. Com o mais forte em primeiro, um método que escolhesse o primeiro com vida, como o do `Treinador`, também passava |
| Fronteira | Psyduck com 0, Goldeen com 0 | `None` | Todos KO: é o limite em que deixa de haver escolha |
| Fronteira | Nenhum Pokémon | `None` | A equipa vazia, o caso que o ginásio usa para recusar |

Repara no primeiro caso. A pergunta para escolher os dados foi a da secção sobre distinguir: se o método estivesse errado de uma forma provável, este caso dava um resultado diferente?

### Etapa 3: Escrever os testes

Cada caso é um teste, com as três partes. Acrescenta estes três ao fim do `test_ginasio.py`. Usam o `Lider` e a `PokemonAgua`, que o ficheiro já importa. Não usam a fixture, porque cada um precisa de uma equipa diferente.

```python


def test_o_lider_escolhe_o_pokemon_com_mais_vida():
    """O líder escolhe o Pokémon com mais vida, mesmo que não seja o primeiro."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35), PokemonAgua("Staryu", 120, 20)])

    escolhido = misty.escolher_pokemon()

    assert escolhido.nome == "Staryu"


def test_o_lider_com_todos_ko_nao_escolhe_nenhum():
    """Com todos os Pokémon KO, o líder não escolhe nenhum: devolve None."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Psyduck", 0, 35), PokemonAgua("Goldeen", 0, 20)])

    escolhido = misty.escolher_pokemon()

    assert escolhido is None


def test_o_lider_com_a_equipa_vazia_nao_escolhe_nenhum():
    """Com a equipa vazia, o líder também devolve None, sem dar erro."""
    misty = Lider("Misty")

    escolhido = misty.escolher_pokemon()

    assert escolhido is None
```

O primeiro teste compara o nome, porque é a forma mais simples de dizer que Pokémon se espera. Os outros dois usam `is None`, a pergunta do 10.º ano para o `None`.

### Etapa 4: Correr os testes

Corre `python3 -m pytest`. O resultado, a partir da linha `collected`, é este:

```text
collected 18 items

test_ginasio.py .......                                                  [ 38%]
test_pokemon.py ...........                                              [100%]

============================== 18 passed in 0.02s ==============================
```

Passam os dezoito: os sete do ginásio e os onze dos Pokémon.

### Etapa 5: Confirmar que os testes distinguem

Os testes passam com o código certo. Falta saber se falham com o código errado. Para isso, imagina três versões erradas do `escolher_pokemon`, que um colega podia escrever. Cada uma tem um erro diferente.

A primeira escolhe o primeiro Pokémon com vida, como o `Treinador`:

```python
        escolhido = None
        for pokemon in self.equipa:
            if pokemon.vida > 0:
                return pokemon
        return escolhido
```

A segunda esquece-se de ver se o Pokémon tem vida:

```python
        escolhido = None
        for pokemon in self.equipa:
            if escolhido is None or pokemon.vida > escolhido.vida:
                escolhido = pokemon
        return escolhido
```

A terceira começa pelo primeiro Pokémon da equipa, em vez de começar por `None`, e só no fim vê se ele está KO:

```python
        escolhido = self.equipa[0]
        for pokemon in self.equipa:
            if pokemon.vida > escolhido.vida:
                escolhido = pokemon
        if escolhido.vida == 0:
            return None
        return escolhido
```

Antes de continuares, prevê, para cada versão, quais dos três testes do líder falham.

Para confirmar, troca no teu `ginasio.py` o corpo do `escolher_pokemon` do `Lider` por cada versão, uma de cada vez, e corre `python3 -m pytest`. No fim, volta a pôr o código certo. Os resultados são estes:

| Versão | Testes que falham |
| --- | --- |
| Primeira: o primeiro com vida | Só o `test_o_lider_escolhe_o_pokemon_com_mais_vida`, com `AssertionError: assert 'Starmie' == 'Staryu'` |
| Segunda: sem ver a vida | Só o `test_o_lider_com_todos_ko_nao_escolhe_nenhum`, com `assert <pokemon.PokemonAgua object at 0x...> is None` |
| Terceira: começa pelo primeiro | Só o `test_o_lider_com_a_equipa_vazia_nao_escolhe_nenhum`, com `IndexError: list index out of range` |

A terceira versão falha de uma forma nova. Com a equipa vazia, o `self.equipa[0]` lança um `IndexError`, uma exceção do Python para uma posição que não existe na lista. A saída, a partir da linha `FAILURES`, é esta:

```text
=================================== FAILURES ===================================
______________ test_o_lider_com_a_equipa_vazia_nao_escolhe_nenhum ______________

    def test_o_lider_com_a_equipa_vazia_nao_escolhe_nenhum():
        """Com a equipa vazia, o líder também devolve None, sem dar erro."""
        misty = Lider("Misty")
    
>       escolhido = misty.escolher_pokemon()
                    ^^^^^^^^^^^^^^^^^^^^^^^^

test_ginasio.py:79: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ginasio.Lider object at 0x108396690>

    def escolher_pokemon(self):
        """Devolve o Pokémon da equipa com mais vida, ou None se estão todos KO."""
>       escolhido = self.equipa[0]
                    ^^^^^^^^^^^^^^
E       IndexError: list index out of range

ginasio.py:97: IndexError
=========================== short test summary info ============================
FAILED test_ginasio.py::test_o_lider_com_a_equipa_vazia_nao_escolhe_nenhum - ...
========================= 1 failed, 17 passed in 0.03s =========================
```

A saída tem dois andares, como um traceback, separados pela linha de traços e espaços. O de cima é o teste, com o `>` na linha que chamou o método. O de baixo é o método, com o `>` na linha onde a exceção rebentou, e a linha `E` com o tipo e a mensagem da exceção. `list index out of range` quer dizer "índice da lista fora do intervalo". Lê-se como no tema 04: de baixo para cima, e a causa está no método, e não no teste. No Python 3.9, as linhas com os acentos circunflexos não aparecem.

### Etapa 6: O que o exemplo mostra

Três testes, três versões erradas, e cada versão é apanhada por um teste diferente. Se tirasses qualquer um dos três testes, uma das versões erradas passava sem ninguém dar por ela. Não é o número de testes que conta. Conta que cada teste distinga uma forma provável de errar.

A pasta [05-testes-com-pytest](../exemplos/python-avancado/pokemon/05-testes-com-pytest/) dos exemplos tem os testes deste guia e mais quatro, que o laboratório escreve contigo. São os dos limites do ataque, o de um Pokémon KO que não ataca e o de uma planta KO que não recupera. Compara-os com os teus.

## Erros frequentes

### O pytest não encontra os testes

A saída diz `collected 0 items` e acaba em `no tests ran`, que quer dizer "nenhum teste correu". Há três causas. O nome do ficheiro não começa por `test_`, como `testes_pokemon.py`. O nome da função não começa por `test_`, como `fogo_contra_planta`. Ou estás noutra pasta, sem ficheiros de testes. Confirma os nomes e a pasta, com `pwd` (na linha de comandos clássica do Windows, `cd`).

### `No module named pytest`

O pytest não está instalado no Python que estás a usar. Instala-o com `python3 -m pip install pytest`, como na secção "Correr os testes com o pytest". Se o instalaste e a mensagem continua, provavelmente instalaste-o noutro Python: usa sempre `python3 -m` nos dois comandos, para ser o mesmo.

### Um teste sem assert

Um teste que acaba em `dano == 40`, sem o `assert`, passa sempre. A comparação é feita, dá `True` ou `False`, e o resultado é deitado fora. O pytest só sabe que um teste falhou quando há um `assert` falso ou uma exceção. Antes de dares um teste por bom, confirma que ele falha quando o código está errado. Muda um valor de propósito, como fizeste com o dano a dobrar.

### Um assert com parênteses

A linha `assert (dano == 40, "o dano devia ser 40")` passa sempre. Os parênteses fazem um tuplo com dois valores. O `assert` não olha para dentro do tuplo: um tuplo que tem valores conta sempre como verdadeiro, mesmo que lá dentro esteja um `False`. O pytest avisa, numa secção `warnings summary`, com a mensagem `assertion is always true, perhaps remove parentheses?`, que quer dizer "a afirmação é sempre verdadeira, talvez devas tirar os parênteses". Escreve o `assert` sem parênteses: `assert dano == 40`.

### Linhas a mais dentro do pytest.raises

Se o bloco do `with pytest.raises(...)` tem várias linhas, o teste passa assim que uma delas lança a exceção, mesmo que não seja a que querias testar. E as linhas depois dela nunca correm. Deixa dentro do bloco só a linha que deve lançar a exceção, e os `assert` do estado depois do bloco.

### Esquecer o import pytest

Sem a linha `import pytest` no início do ficheiro, o `pytest.raises` e o `@pytest.fixture` dão `NameError: name 'pytest' is not defined`, que quer dizer que o nome `pytest` não existe nesse ficheiro. Acrescenta o `import pytest` no início.

### Chamar a fixture como uma função

Um teste que escreve `ginasio = cerulean()` em vez de receber `cerulean` como parâmetro falha com `Fixture "cerulean" called directly. Fixtures are not meant to be called directly`. Quer dizer que as fixtures não se chamam diretamente: o pytest é que as chama, quando um teste as pede como parâmetro.

### O parâmetro com outro nome

Se o teste tiver o parâmetro `ginasio` e a fixture se chamar `cerulean`, o pytest não encontra a fixture. O teste aparece com um `E` na linha do progresso, de erro, e a saída diz `ERROR at setup of`, "erro na preparação de", e `fixture 'ginasio' not found`, "fixture não encontrada". O nome do parâmetro tem de ser exatamente o nome da função da fixture.

## Palavras novas deste guia

- Teste: um pedaço de código que executa uma parte do programa e compara o resultado com o resultado esperado.
- Teste de comportamento: um teste que confirma o que o código faz, como valores, estado e exceções, e não a forma como está escrito.
- `assert`: a instrução que confirma que uma condição é verdadeira, e lança `AssertionError` se não for.
- `AssertionError`: a exceção que o `assert` lança quando a condição é falsa.
- Função de teste: uma função cujo nome começa por `test_`, num ficheiro cujo nome também começa por `test_`, que o pytest encontra e chama.
- pytest: o programa que encontra os testes, corre-os um a um e diz quais passaram e quais falharam, com os valores verdadeiros.
- Preparar, fazer, confirmar: as três partes de um teste. Em inglês, Arrange, Act, Assert.
- Caso normal: um valor no meio da regra, longe dos limites.
- Caso de fronteira, ou caso-limite: um valor onde a regra muda, ou o valor logo a seguir, como 150 e 151 para a vida máxima.
- Caso de erro: um pedido que o código tem de recusar.
- `pytest.raises`: usado com `with`, confirma que a linha dentro do bloco lança uma certa exceção.
- Fixture: uma função com `@pytest.fixture` que prepara um objeto para os testes, entregue a cada teste que tenha o nome dela como parâmetro.
- Regressão: um defeito que volta, ou uma coisa que funcionava e deixou de funcionar depois de uma mudança.
- Teste de regressão: um teste que fica a guardar o sítio onde um defeito já apareceu.

## Verificar o que aprendeste

### Escrever e correr testes

1. Porque é que `python3 test_pokemon.py` não escreve nada? Quem chama as funções de teste?
2. Na linha `E       assert 40 == 80`, de onde vem o 40 e de onde vem o 80?
3. Um teste falha. Como decides se o erro está no teste ou no código?
4. Quais são as três partes de um teste? Porque é que um teste faz uma só ação?

### Escolher os casos

1. Porque é que o teste da planta contra a água não apanha o dano a dobrar?
2. Para a vida máxima de 150, que valores testas, e porquê esses e não 200?
3. Dá um exemplo de um caso normal, de um caso de fronteira e de um caso de erro para o `capturar` do `Treinador`.
4. Um colega diz que os testes dele são melhores porque tem trinta e tu tens dez. Que pergunta lhe fazes?

### Recusas, fixtures e regressões

1. No teste da sétima captura, porque é que as seis primeiras capturas ficam fora do `with`?
2. O que é que o `assert len(brock.equipa) == 6`, depois do bloco, confirma que o `pytest.raises` não confirma?
3. Porque é que o teste do `test_partilhado.py` passava sozinho e falhava com o outro? Como é que uma fixture evita isso?
4. Porque é que o teste do `recuperar` se escreve antes de corrigir o código do colega?
5. No exemplo guiado, porque é que a Staryu, a mais forte, não é a primeira da lista?

## O que vem a seguir

Para praticar este tema, faz o [laboratório](05-testes-com-pytest-laboratorio.md) e depois a [ficha de exercícios](05-testes-com-pytest-exercicios.md). No laboratório, escreves a tua própria bateria de testes para o ginásio, encontras um defeito com um teste escrito antes da correção e vês que testes apanham cada mudança errada. A ficha tem exercícios com outro programa, um Pokémon em treino que sobe de nível, para fazeres sem ajuda.

O tema seguinte é o do Python idiomático. Nele, reescreves partes do ginásio de forma mais curta e mais clara, por exemplo a escolha do Pokémon do líder. Os testes deste tema são a tua rede: depois de cada mudança, `python3 -m pytest` diz-te se o comportamento ficou igual.

## Para saber mais

- [Get Started, da documentação do pytest](https://docs.pytest.org/en/stable/getting-started.html): o primeiro teste, o `pytest.raises` e as fixtures, em inglês.
- [How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html): tudo sobre as fixtures, em inglês, incluindo formas que este guia não usa.

![Rodapé](../imagens/rodape.png)
