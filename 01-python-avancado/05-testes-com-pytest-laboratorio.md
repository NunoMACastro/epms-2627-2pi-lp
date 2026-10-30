![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: Testes de comportamento com pytest

Laboratório do tema Testes de comportamento com pytest, do módulo 10794, Programação avançada com Python. Vais escrever, fase a fase, os testes do ginásio Pokémon do tema 04, e usá-los para encontrar um defeito e para ver que mudanças partem o código. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas em casa ou na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](05-testes-com-pytest.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

No fim, o teu ginásio tem uma bateria de treze testes, em dois ficheiros, que corres com um só comando. Os testes confirmam as vantagens de tipo, os limites do ataque e da vida, as recusas do ginásio e o registo dos combates. Pelo caminho, escreves um teste antes de corrigir um defeito relatado, e vês que testes apanham cada mudança errada no código. O ginásio em si não muda: no fim, os quatro ficheiros dele estão como no início.

A pasta de trabalho acaba assim:

```text
ginasio-com-testes/
├── anunciadores.py
├── erros.py
├── ginasio.py
├── pokemon.py
├── test_ginasio.py
└── test_pokemon.py
```

Ao correres os programas e os testes, aparecem também duas pastas. A `__pycache__` é criada pelo Python, com os teus ficheiros já traduzidos para correrem mais depressa. A `.pytest_cache` é criada pelo pytest, que lá guarda o resultado da última execução. Não lhes mexas.

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | O `test_pokemon.py` | Um teste, que o pytest encontra e corre |
| 2 | O `test_pokemon.py` | Um teste que falha, lido e corrigido |
| 3 | O `test_pokemon.py` | Quatro testes das vantagens de tipo, com as três partes |
| 4 | O `test_pokemon.py` | Um teste que distingue um erro, e os casos de fronteira |
| 5 | O `test_ginasio.py` | As recusas do ginásio, confirmadas com `pytest.raises` |
| 6 | O `test_ginasio.py` | Uma fixture que prepara o ginásio para vários testes |
| 7 | O `ginasio.py` e o `test_ginasio.py` | Um defeito encontrado com um teste escrito antes da correção |
| 8 | O `ginasio.py`, o `pokemon.py` e o `test_pokemon.py` | Três mudanças erradas, e o teste que faltava |

Em todas as fases trabalhas da mesma maneira. Antes de executares, escreves no papel, ou num ficheiro de texto, o que esperas ver. Depois executas e comparas. Quando o resultado é diferente do que previste, explica a diferença antes de continuares: é essa explicação que mais te ensina.

As saídas mostradas são as do Python 3.14, com o pytest 9.1. No Python 3.9, com o pytest 8.4, são iguais, menos onde o texto diz. A primeira vez que corres o pytest, o laboratório mostra a saída inteira, com o caminho da pasta encurtado. Nas outras, mostra-a a partir da linha `collected`, porque as linhas de cima dizem o sistema, as versões e a pasta, e no teu computador são outras. O tempo da última linha, como `in 0.01s`, muda de execução para execução. Quando aparece um objeto, como `<ginasio.Ginasio object at 0x10ae4b390>`, o número depois de `at` também muda.

## Palavras que vais usar

- Teste: um pedaço de código que executa uma parte do programa e compara o resultado com o resultado esperado. Para saber mais, vê a secção "Testar a olhar para o ecrã" do [guia](05-testes-com-pytest.md).
- `assert`: a instrução que confirma que uma condição é verdadeira. Se for falsa, lança a exceção `AssertionError`.
- Função de teste: uma função cujo nome começa por `test_`, num ficheiro cujo nome também começa por `test_`.
- pytest: o programa que encontra as funções de teste, corre-as uma a uma e diz quais passaram e quais falharam, com os valores verdadeiros.
- Preparar, fazer, confirmar: as três partes de um teste. Prepara-se o que é preciso, faz-se a ação que se quer testar, uma só, e confirma-se o resultado. Em inglês, Arrange, Act, Assert.
- Caso de fronteira: um valor onde uma regra muda, ou o valor logo a seguir, como 50 e 51 para o ataque máximo. Um caso normal é um valor no meio da regra. Um caso de erro é um pedido que o código tem de recusar.
- `pytest.raises`: usado com `with`, confirma que a linha dentro do bloco lança uma certa exceção.
- Fixture: uma função com o decorador `@pytest.fixture`, que prepara um objeto. O pytest chama-a e entrega o objeto a cada teste que tenha o nome dela como parâmetro.
- Regressão: um defeito que volta, ou uma coisa que funcionava e deixou de funcionar depois de uma mudança. Um teste de regressão fica a guardar o sítio onde um defeito já apareceu.
- Exceção própria: uma classe que herda de `Exception`, diretamente ou através de outra classe, como a `EquipaCheia` e a `SemPokemonComVida` do `erros.py`, do tema 04.
- Dataclass: uma classe escrita com `@dataclass`, como o `Combate` do ginásio, em que o `==` compara os campos um a um, do tema 03.

## O que precisas

- O Python 3, para executar os programas. Confirma que o tens com o comando `python3 --version`. Deve aparecer `Python 3.` seguido de dois números, o que quer dizer que o Python está instalado. No Windows, se `python3` não funcionar, usa `python --version` ou `py --version`.
- O VS Code, para escrever os ficheiros e abrir o terminal.
- O pytest. A preparação do projeto confirma se o tens, e diz como o instalar se não o tiveres.
- Os ficheiros `pokemon.py`, `erros.py`, `anunciadores.py` e `ginasio.py` da [pasta 04 dos exemplos](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/), que o laboratório copia na preparação. São o ginásio no fim do tema 04, e o [README do exemplo](../exemplos/python-avancado/pokemon/README.md) explica o que tem cada pasta.
- Papel, ou um ficheiro de texto, para as previsões e as respostas.

## Se alguma coisa falhar

1. Estás na pasta certa? Todos os comandos correm na pasta `ginasio-com-testes`. Para confirmar, escreve `pwd` (na linha de comandos clássica do Windows, `cd`) e vê se o caminho acaba em `ginasio-com-testes`.
2. Guardaste o ficheiro antes de correr os testes? O pytest lê o que está guardado no disco. Guarda e corre outra vez.
3. Os ficheiros de testes estão na mesma pasta que o `pokemon.py` e o `ginasio.py`? Os testes importam deles, e só os encontram na mesma pasta.
4. Apareceu uma mensagem que não esperavas? Procura-a em [Problemas frequentes](#problemas-frequentes).
5. Mudaste o `pokemon.py` ou o `ginasio.py` numa experiência e não o voltaste a pôr como estava? As fases 2, 4, 7 e 8 mudam o código de propósito e mandam desfazer a mudança. Se te perderes, copia outra vez o ficheiro da pasta 04 dos exemplos.

## Preparar o projeto

1. Cria uma pasta nova no teu computador, com o nome `ginasio-com-testes`, e abre-a no VS Code, com o menu File, Open Folder (Ficheiro, Abrir Pasta, em português).
2. Copia para essa pasta os quatro ficheiros da [pasta 04 dos exemplos](../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/): o `pokemon.py`, o `erros.py`, o `anunciadores.py` e o `ginasio.py`. Copia os dos exemplos, e não os teus do tema 04, para os testes deste laboratório darem exatamente os resultados indicados.
3. Abre o terminal do VS Code, com o menu Terminal, New Terminal (Terminal, Novo Terminal), e executa a demonstração do ginásio, para confirmares que os ficheiros estão no sítio certo:

```bash
python3 ginasio.py
```

O que deves ver: a demonstração do tema 04, com os combates, o registo e o histórico, e uma última linha igual a esta:

```text
Ash continua com 2 Pokémon; Misty continua com 1.
```

Isto quer dizer que o ponto de partida funciona. Se aparecer outra coisa, vê as [verificações rápidas](#se-alguma-coisa-falhar).

4. Confirma se o pytest está instalado. O `-m pytest` pede ao Python que corra o pytest, com o mesmo Python que usas para os programas:

```bash
python3 -m pytest --version
```

No Windows, o comando é `py -m pytest --version`.

O que deves ver: uma linha como `pytest 9.1.1`, com a versão instalada. No Python 3.9, a versão começa por 8. Se aparecer `No module named pytest`, o pytest não está instalado. Instala-o com o comando seguinte, que o descarrega da internet e o junta ao teu Python (no Windows, `py -m pip install pytest`):

```bash
python3 -m pip install pytest
```

Depois de instalar, corre outra vez `python3 -m pytest --version`, para confirmares. Se a instalação for recusada, por exemplo com `externally-managed-environment` ou com um erro de permissões, fala com o professor antes de continuares.

## Fase 1: O primeiro teste

Até aqui, para saber se o ginásio funcionava, executavas a demonstração e comparavas a saída com o que esperavas. Um teste faz essa comparação por ti. É uma função, com um nome que começa por `test_`, que prepara uns objetos, chama um método e confirma o resultado com `assert`. O `assert` é seguido de uma condição: se for verdadeira, não acontece nada; se for falsa, o `assert` lança um erro. Quem chama as funções de teste é o pytest. Para saber mais, lê as secções "Uma função de teste" e "Correr os testes com o pytest" do [guia](05-testes-com-pytest.md).

1. Cria o ficheiro `test_pokemon.py`, na pasta `ginasio-com-testes`. O primeiro teste confirma uma vantagem de tipo: a água tira o dobro ao fogo. O ficheiro é novo, e fica completo com este conteúdo:

```python
# test_pokemon.py: os testes das classes de Pokémon.
from pokemon import PokemonAgua, PokemonFogo


def test_agua_contra_fogo_tira_o_dobro():
    """A água tem vantagem contra o fogo: o dano é o dobro do ataque."""
    squirtle = PokemonAgua("Squirtle", 100, 30)
    charmander = PokemonFogo("Charmander", 90, 40)
    dano = squirtle.calcular_dano(charmander)
    assert dano == 60
```

Leitura guiada: o ficheiro importa as duas classes de que o teste precisa e define uma função. A docstring diz, numa frase, o comportamento que o teste confirma. O corpo cria os dois Pokémon, calcula o dano do Squirtle contra o Charmander e confirma que é 60, o dobro do ataque de 30. A função não recebe nada e não devolve nada.

2. Antes de correres o ficheiro como um programa normal, prevê o que aparece. Depois corre:

```bash
python3 test_pokemon.py
```

O que deves ver: nada. O programa acaba sem escrever uma linha. Isto acontece porque o ficheiro só define uma função, e definir uma função não a executa. Ninguém chama a `test_agua_contra_fogo_tira_o_dobro`, e por isso o corpo dela nunca corre.

3. Agora corre o ficheiro com o pytest. Antes, prevê quantos testes ele vai encontrar.

```bash
python3 -m pytest
```

O que deves ver:

```text
============================= test session starts ==============================
platform darwin -- Python 3.14.8, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/.../ginasio-com-testes
collected 1 item

test_pokemon.py .                                                        [100%]

============================== 1 passed in 0.01s ===============================
```

Isto quer dizer que o pytest encontrou um teste e que o teste passou. A linha `platform` diz o sistema e as versões, e a `rootdir` diz a pasta onde o pytest procurou. Em `collected 1 item`, "collected" quer dizer recolhidos: o pytest encontrou um teste. A linha do ficheiro tem um ponto por cada teste que passou. A última linha, `1 passed`, diz que um passou, e no terminal do VS Code aparece a verde.

4. Provoca um erro de propósito, para veres como o pytest encontra os testes. No `test_pokemon.py`, tira o `test_` do início do nome da função, para ficar `def agua_contra_fogo_tira_o_dobro():`. Guarda, e antes de correres `python3 -m pytest` outra vez, prevê o que muda.

O que deves ver, a partir da linha `collected`:

```text
collected 0 items

============================ no tests ran in 0.01s =============================
```

`no tests ran` quer dizer que nenhum teste correu. O pytest procura os ficheiros cujo nome começa por `test_`, e dentro deles as funções cujo nome começa por `test_`. Sem o `test_`, a função é ignorada. Volta a pôr o nome `test_agua_contra_fogo_tira_o_dobro`, guarda, e confirma que o pytest volta a dizer `1 passed`.

### Paragem 1

O `test_pokemon.py` tem um teste, e `python3 -m pytest` diz `1 passed`.

Pensa antes de continuares: porque é que é o pytest que corre os testes, e não uma linha no fim do ficheiro a chamar a função? A resposta: com uma chamada por teste, o primeiro `assert` falso parava o programa, e os testes seguintes já não corriam. O pytest chama cada teste à parte, continua quando um falha, e no fim diz quais falharam e porquê.

## Fase 2: Um teste que falha

Um teste falha quando o resultado do código e o resultado esperado não são iguais. Quando isso acontece, o pytest mostra a linha do `assert` e os dois valores. Mas não diz qual dos dois está errado, o teste ou o código. Quem decide são as regras do jogo. Para saber mais, lê a secção "Um teste que falha" do [guia](05-testes-com-pytest.md).

1. Acrescenta um segundo teste, escrito por um colega, para a vantagem da planta contra a água. No `test_pokemon.py`, substitui a linha do `import` por esta, que traz também a `PokemonPlanta`:

```python
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
```

E acrescenta ao fim do ficheiro:

```python


def test_planta_contra_agua_tira_o_dobro():
    """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    squirtle = PokemonAgua("Squirtle", 100, 30)
    dano = bulbasaur.calcular_dano(squirtle)
    assert dano == 25
```

Leitura guiada: as duas linhas em branco no início do bloco separam o teste novo do anterior, como entre duas funções de um programa. O teste tem a mesma forma do primeiro: cria a planta e o alvo, calcula o dano e confirma-o.

2. Antes de correres `python3 -m pytest`, prevê qual dos dois testes falha e que valores o pytest vai mostrar.

O que deves ver, a partir da linha `collected`:

```text
collected 2 items

test_pokemon.py .F                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_planta_contra_agua_tira_o_dobro _____________________

    def test_planta_contra_agua_tira_o_dobro():
        """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
        bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
        squirtle = PokemonAgua("Squirtle", 100, 30)
        dano = bulbasaur.calcular_dano(squirtle)
>       assert dano == 25
E       assert 50 == 25

test_pokemon.py:18: AssertionError
----------------------------- Captured stdout call -----------------------------
É super eficaz!
=========================== short test summary info ============================
FAILED test_pokemon.py::test_planta_contra_agua_tira_o_dobro - assert 50 == 25
========================= 1 failed, 1 passed in 0.02s ==========================
```

Lê de baixo para cima, como um traceback. A última linha diz que um falhou e um passou, e aparece a vermelho. A linha `FAILED` diz qual foi o teste. Na secção `FAILURES`, o `>` aponta a linha onde o teste parou, e a linha `E` mostra a comparação com os valores verdadeiros: `assert 50 == 25`. O valor da esquerda é o que o código deu, e o da direita é o que o teste esperava. A secção `Captured stdout call` mostra o que o teste escreveu com `print`: o "É super eficaz!" do `calcular_dano`. "stdout" é o nome técnico da saída normal de um programa, o ecrã. O pytest guarda o que os testes escrevem e só o mostra quando um teste falha.

3. Decide quem está errado, o teste ou o código, e escreve a tua resposta antes de leres a seguinte.

A resposta: o teste. As regras do jogo dizem que a planta tem vantagem contra a água, e uma vantagem dobra o dano. O dano certo é 50, e foi o que o código deu. O valor esperado tira-se das regras, e não do código. Se mudasses o teste só para ele passar, sem confirmar a regra, o teste deixava de confirmar o que quer que fosse.

4. Corrige o teste: a última linha passa a ser `assert dano == 50`. Corre outra vez `python3 -m pytest`.

O que deves ver, a partir da linha `collected`:

```text
collected 2 items

test_pokemon.py ..                                                       [100%]

============================== 2 passed in 0.01s ===============================
```

5. Agora o contrário: um teste certo e o código errado. No `pokemon.py`, no `calcular_dano` da `PokemonPlanta`, tira o acento da palavra "Água", para a linha ficar `if alvo.tipo == "Agua":`. É um engano de escrita, que não dá nenhum erro do Python. Antes de correres os testes, prevê o resultado.

O que deves ver, a partir da linha `collected`:

```text
collected 2 items

test_pokemon.py .F                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_planta_contra_agua_tira_o_dobro _____________________

    def test_planta_contra_agua_tira_o_dobro():
        """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
        bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
        squirtle = PokemonAgua("Squirtle", 100, 30)
        dano = bulbasaur.calcular_dano(squirtle)
>       assert dano == 50
E       assert 25 == 50

test_pokemon.py:18: AssertionError
=========================== short test summary info ============================
FAILED test_pokemon.py::test_planta_contra_agua_tira_o_dobro - assert 25 == 50
========================= 1 failed, 1 passed in 0.02s ==========================
```

Isto quer dizer que a planta deixou de ter vantagem: o tipo do Squirtle é `"Água"`, com acento, e a comparação com `"Agua"` dá falso. Desta vez o teste está certo e o código está errado. Repara também que já não há a secção `Captured stdout call`: sem a vantagem, o "É super eficaz!" não foi escrito. Volta a pôr o acento no `pokemon.py`, guarda, e confirma que o pytest diz `2 passed`.

### Paragem 2

O `test_pokemon.py` tem dois testes, e os dois passam. O `pokemon.py` está como na pasta 04.

Pensa antes de continuares: nos dois erros desta fase, o pytest mostrou a mesma forma de mensagem. O que te disse que, da primeira vez, o erro estava no teste, e da segunda estava no código? A resposta: as regras do jogo. O pytest só diz que o teste e o código não concordam. Para decidir quem está certo, comparas os dois valores com o que as regras pedem.

## Fase 3: Preparar, fazer, confirmar

Os dois testes têm a mesma forma, em três partes. Primeiro preparam o que é preciso, os dois Pokémon. Depois fazem a ação que se quer testar, uma só: calculam o dano. Por fim confirmam o resultado com um `assert`. Com as três partes à vista, um teste lê-se como uma frase, e quando falha sabes logo que ação falhou. O nome do teste diz o comportamento que se confirma, porque é o nome que o pytest mostra quando ele falha. Para saber mais, lê a secção "Preparar, fazer, confirmar" do [guia](05-testes-com-pytest.md).

1. Substitui o conteúdo do `test_pokemon.py` por esta versão. Tem os dois testes que já tinhas, com as três partes marcadas no primeiro. Tem também mais dois: o fogo contra a planta, com vantagem, e o fogo contra a água, sem vantagem.

```python
# test_pokemon.py: os testes das classes de Pokémon, com as três partes de cada teste.
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


def test_agua_contra_fogo_tira_o_dobro():
    """A água tem vantagem contra o fogo: o dano é o dobro do ataque."""
    # Preparar: o atacante e o alvo.
    squirtle = PokemonAgua("Squirtle", 100, 30)
    charmander = PokemonFogo("Charmander", 90, 40)
    # Fazer: uma só ação, a que se está a testar.
    dano = squirtle.calcular_dano(charmander)
    # Confirmar: o valor que as regras do jogo pedem.
    assert dano == 60


def test_planta_contra_agua_tira_o_dobro():
    """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
    bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    dano = bulbasaur.calcular_dano(squirtle)

    assert dano == 50


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

    assert dano == 40
```

Leitura guiada: lê primeiro o teste de cima, com um comentário em cada parte. Nos outros três, as partes estão separadas por uma linha em branco, sem comentários, porque a forma já é conhecida. Em todos, só mudam os Pokémon e o valor esperado. O último é o único sem vantagem: o fogo não tem vantagem contra a água, e o dano é o próprio ataque do Charmander.

2. Corre os testes com a opção `-v`, de "verbose", que quer dizer detalhado. Com ela, o pytest mostra o nome de cada teste. Antes, prevê o resultado dos dois testes novos.

```bash
python3 -m pytest -v
```

O que deves ver, a partir da linha `collected`:

```text
collecting ... collected 4 items

test_pokemon.py::test_agua_contra_fogo_tira_o_dobro PASSED               [ 25%]
test_pokemon.py::test_planta_contra_agua_tira_o_dobro PASSED             [ 50%]
test_pokemon.py::test_fogo_contra_planta_tira_o_dobro PASSED             [ 75%]
test_pokemon.py::test_fogo_contra_agua_tira_so_o_ataque PASSED           [100%]

============================== 4 passed in 0.01s ===============================
```

Isto quer dizer que os quatro passam. Cada linha tem o ficheiro, dois pontos duas vezes e o nome do teste, e `PASSED` quer dizer que passou. Os testes correm pela ordem em que estão no ficheiro.

### Paragem 3

O `test_pokemon.py` tem quatro testes, todos com as três partes, e os quatro passam.

Pensa antes de continuares: um colega juntou os quatro testes num só, com os quatro cálculos e os quatro `assert` seguidos. Porque é que é pior? A resposta: se o segundo `assert` falhar, o teste para aí, e não sabes se o terceiro e o quarto passavam. E o nome do teste já não diz qual das quatro vantagens se partiu.

## Fase 4: Casos que distinguem o certo do errado

Um teste só vale alguma coisa se der um resultado diferente com o código certo e com o código errado. Se as duas versões dão o mesmo resultado, o teste passa nas duas, e não distingue nada. Os erros escondem-se sobretudo nas fronteiras das regras, onde um número ou uma comparação errados só se veem no próprio limite. Um caso de fronteira é um valor onde a regra muda, ou o valor logo a seguir. Para saber mais, lê as secções "Um teste tem de distinguir o certo do errado" e "Os casos de fronteira" do [guia](05-testes-com-pytest.md).

1. Põe um erro de propósito no `pokemon.py`. No `calcular_dano` da `PokemonFogo`, tira quatro espaços à linha `dano = dano * 2`, para ela sair do `if`. O método fica assim:

```python
    def calcular_dano(self, alvo):
        """Contra Planta, o fogo tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "Planta":
            print("É super eficaz!")
        dano = dano * 2
        return dano
```

Com a multiplicação fora do `if`, o fogo tira o dobro a qualquer alvo. Antes de correres `python3 -m pytest`, prevê qual dos quatro testes falha.

O que deves ver, a partir da linha `collected`:

```text
collected 4 items

test_pokemon.py ...F                                                     [100%]

=================================== FAILURES ===================================
____________________ test_fogo_contra_agua_tira_so_o_ataque ____________________

    def test_fogo_contra_agua_tira_so_o_ataque():
        """Sem vantagem, o dano é o próprio ataque."""
        charmander = PokemonFogo("Charmander", 90, 40)
        squirtle = PokemonAgua("Squirtle", 100, 30)
    
        dano = charmander.calcular_dano(squirtle)
    
>       assert dano == 40
E       assert 80 == 40

test_pokemon.py:43: AssertionError
=========================== short test summary info ============================
FAILED test_pokemon.py::test_fogo_contra_agua_tira_so_o_ataque - assert 80 == 40
========================= 1 failed, 3 passed in 0.02s ==========================
```

Só o teste do fogo contra a água apanhou o erro.

2. Responde por escrito: porque é que o teste do fogo contra a planta passou, se o `calcular_dano` do fogo está errado?

A resposta: contra a planta, o fogo tem vantagem, e o dobro está certo. A versão certa dá 80, e a versão errada também dá 80. Esse teste não distingue as duas. Só um alvo sem vantagem, como a água, dá resultados diferentes: 40 com o código certo, 80 com o errado. Sem o teste do fogo contra a água, este erro passava despercebido com quatro testes a passar.

3. Volta a indentar a linha `dano = dano * 2` da `PokemonFogo`, para ficar dentro do `if`, por baixo do `print`. Guarda, e confirma que o pytest diz `4 passed`.

4. Agora os casos de fronteira. O ataque vai de 1 a 50: o set da propriedade `ataque` corrige um valor abaixo de 1 para 1, e um acima de 50 para 50. A vida não passa de 150, e um Pokémon KO, com 0 de vida, não ataca nem recupera. Acrescenta estes quatro testes ao fim do `test_pokemon.py`:

```python


def test_ataque_abaixo_do_minimo_fica_no_minimo():
    """O ataque vai de 1 a 50: 0 passa a 1."""
    charmander = PokemonFogo("Charmander", 90, 0)

    assert charmander.ataque == 1


def test_ataque_acima_do_maximo_fica_no_maximo():
    """O ataque vai de 1 a 50: 51 passa a 50."""
    charmander = PokemonFogo("Charmander", 90, 51)

    assert charmander.ataque == 50


def test_pokemon_ko_nao_ataca():
    """Um Pokémon KO não tira vida a ninguém."""
    charmander = PokemonFogo("Charmander", 0, 40)
    squirtle = PokemonAgua("Squirtle", 100, 30)

    charmander.atacar(squirtle)

    assert squirtle.vida == 100


def test_planta_recupera_ate_ao_maximo():
    """A recuperação passa pelo set da vida, que não a deixa passar de 150."""
    bulbasaur = PokemonPlanta("Bulbasaur", 140, 25, 20)

    bulbasaur.recuperar()

    assert bulbasaur.vida == 150
```

Leitura guiada: nos dois primeiros testes, a ação é criar o Pokémon, porque é o construtor que passa o ataque pelo set. Por isso a preparação e a ação são a mesma linha. Os valores são os primeiros fora dos limites, 0 e 51, e não um valor qualquer como 200. O terceiro teste prepara um Charmander com 0 de vida, que é a fronteira do KO, e confirma que o ataque não mexeu na vida do Squirtle. O quarto prepara uma planta com 140 de vida e 20 de regeneração: a soma, 160, passa do limite, e o set tem de a deixar em 150.

5. Antes de correres `python3 -m pytest`, prevê se os oito testes passam.

O que deves ver, a partir da linha `collected`:

```text
collected 8 items

test_pokemon.py ........                                                 [100%]

============================== 8 passed in 0.01s ===============================
```

Isto quer dizer que o ginásio respeita as fronteiras do ataque, do KO e da recuperação.

### Paragem 4

O `test_pokemon.py` tem oito testes, todos a passar, e o `pokemon.py` está como na pasta 04.

Pensa antes de continuares: para testar o limite de 50 do ataque, porque é que 51 é melhor do que 200? A resposta: o set do ataque é parecido com o da vida, e é fácil copiar um para o outro. Imagina que a comparação ficava com o limite da vida, `elif valor > VIDA_MAXIMA:`, e a linha de baixo continuava a pôr 50. Um ataque de 200 dava 50, e o teste com 200 passava. Um ataque de 51 ficava 51, e só o teste com 51 dava pelo erro. O primeiro valor acima do limite é o que separa o limite certo de um limite errado.

## Fase 5: As recusas, com pytest.raises

O ginásio recusa pedidos com exceções próprias: a `EquipaCheia` à sétima captura, e a `SemPokemonComVida` quando um treinador não tem Pokémon com vida para combater. Se um teste chamasse o método e a exceção fosse lançada, o teste parava, e o pytest dava-o como falhado. O `pytest.raises` diz o contrário: esta linha tem de lançar esta exceção. Usa-se com um `with`, como o `with open(...)` do 10.º ano. Se a linha dentro do bloco lançar a exceção indicada, o teste continua depois do bloco; se não lançar, o teste falha. Uma recusa tem também uma segunda metade: o objeto fica como estava. Essa confirma-se com `assert` depois do bloco. Para saber mais, lê as secções "Testar uma recusa: pytest.raises", "Depois da recusa, o estado" e "A equipa vazia" do [guia](05-testes-com-pytest.md).

1. Cria o ficheiro `test_ginasio.py`, com este conteúdo. O `import pytest`, no início, é o que dá acesso ao `pytest.raises`.

```python
# test_ginasio.py: os testes do treinador e do ginásio.
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

Leitura guiada: no primeiro teste, as seis capturas ficam fora do `with`, e por isso têm de correr sem exceção. Se a sexta fosse recusada, o teste falhava logo ali. A sétima captura é a única linha dentro do `with`. Depois do bloco, o `assert` confirma que a equipa continua com seis. No segundo teste, o Ash é criado sem Pokémon, e por isso o `escolher_pokemon` dele devolve `None`. O combate é a linha dentro do `with`, e os dois `assert` do fim confirmam que o ginásio não registou nem o desafiante nem o combate. A lista vazia escreve-se `[]`.

2. Antes de correres `python3 -m pytest`, prevê quantos testes o pytest encontra, e em que ficheiros.

O que deves ver, a partir da linha `collected`:

```text
collected 10 items

test_ginasio.py ..                                                       [ 20%]
test_pokemon.py ........                                                 [100%]

============================== 10 passed in 0.02s ==============================
```

Isto quer dizer que o pytest encontrou os dois ficheiros e correu os dez testes. Os do `test_ginasio.py` vêm primeiro, pela ordem do nome dos ficheiros.

3. Provoca um erro de propósito, no teste. No primeiro teste do `test_ginasio.py`, troca a exceção do `pytest.raises` pela errada, para ficar `with pytest.raises(SemPokemonComVida):`. Antes de correres `python3 -m pytest test_ginasio.py`, que corre só os testes desse ficheiro, prevê o que acontece.

O que deves ver, a partir da linha `collected`:

```text
collected 2 items

test_ginasio.py F.                                                       [100%]

=================================== FAILURES ===================================
__________ test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis ___________

    def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
        """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
        brock = Treinador("Brock")
        for numero in range(6):
            brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
    
        with pytest.raises(SemPokemonComVida):
>           brock.capturar(Pokemon("Onix", "Pedra", 50, 20))

test_ginasio.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ginasio.Treinador object at 0x106f68440>
pokemon = <pokemon.Pokemon object at 0x106f745a0>

    def capturar(self, pokemon):
        """Junta à equipa um Pokémon que foi criado fora do treinador.
    
        Se a equipa já tem TAMANHO_MAXIMO_DA_EQUIPA Pokémon, não junta nada e
        lança EquipaCheia.
        """
        if len(self.equipa) >= TAMANHO_MAXIMO_DA_EQUIPA:
>           raise EquipaCheia(f"{self.nome} já tem {TAMANHO_MAXIMO_DA_EQUIPA} Pokémon e não pode capturar {pokemon.nome}.")
E           erros.EquipaCheia: Brock já tem 6 Pokémon e não pode capturar Onix.

ginasio.py:81: EquipaCheia
=========================== short test summary info ============================
FAILED test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis
========================= 1 failed, 1 passed in 0.02s ==========================
```

Isto quer dizer que o `pytest.raises(SemPokemonComVida)` só apanha essa exceção, e as filhas dela. A `EquipaCheia` que o `capturar` lançou não é uma delas, e passou pelo bloco como se ele não existisse. A saída tem dois andares, como um traceback, separados pela linha de traços e espaços: o teste, em cima, e o `capturar`, em baixo, com a linha do `raise`. Volta a pôr `pytest.raises(EquipaCheia)`, guarda, e confirma com `python3 -m pytest` que os dez testes passam.

### Paragem 5

Há dois ficheiros de testes, com dez testes no total, e todos passam.

Pensa antes de continuares: o primeiro teste tem o `pytest.raises` e um `assert` depois dele. O que é que o `assert` apanha que o `pytest.raises` não apanha? A resposta: um `capturar` que lançasse a exceção depois de juntar o Pokémon à equipa. O `pytest.raises` ficava satisfeito, porque a exceção era lançada, mas a equipa ficava com sete, e o `assert` falhava. A recusa tem duas metades, e cada uma tem a sua confirmação.

## Fase 6: Uma fixture para o ginásio

O teste do combate recusado cria a Misty e o ginásio. Os testes seguintes dos combates precisam do mesmo ginásio, e cada um ia repetir as mesmas linhas. Criar o ginásio uma só vez, no início do ficheiro, não resolve: os testes partilhavam o mesmo objeto, e os combates de um apareciam no outro. Uma fixture resolve as duas coisas. É uma função com o decorador `@pytest.fixture`, que cria o ginásio e o devolve. Um teste que precisa do ginásio tem um parâmetro com o nome da fixture, e o pytest chama a fixture antes desse teste e entrega-lhe o que ela devolveu. Como a chama de novo para cada teste, cada um recebe um ginásio acabado de criar. Para saber mais, lê as secções "Cada teste começa do zero" e "Uma fixture prepara o que vários testes repetem" do [guia](05-testes-com-pytest.md).

1. Substitui o conteúdo do `test_ginasio.py` por esta versão. Tem a fixture `cerulean`, o teste da equipa cheia como estava, o teste do combate recusado a usar a fixture, e um teste novo: um combate que o desafiante ganha.

```python
# test_ginasio.py: os testes do treinador e do ginásio, com uma fixture.
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
```

Leitura guiada: começa pela fixture. O `@pytest.fixture` é um decorador, como o `@property` do tema 03. Escrever a arroba por cima do `def` é o mesmo que escrever, logo a seguir à função, `cerulean = pytest.fixture(cerulean)`, e o nome `cerulean` passa a ser uma fixture. A função cria a Misty e o ginásio e devolve o ginásio. A docstring diz o que ela prepara, para quem lê os testes saber que a Starmie tem 90 de vida e 35 de ataque. O teste do combate recusado perdeu as duas linhas que criavam a Misty e o ginásio, e ganhou o parâmetro `cerulean`. O teste novo faz um combate e confirma a lista dos combates. O `Combate` é uma dataclass, e por isso o `==` compara os três campos, e duas listas são iguais quando têm os mesmos elementos, pela mesma ordem. O primeiro teste não pede a fixture, porque usa um Brock com seis Pokémon de pedra, que só ele usa. A importação do `PokemonFogo` já fica para a fase 7.

2. Antes de correres os testes, responde a duas perguntas. Quantas vezes é chamada a função `cerulean`? Quem ganha o combate do teste novo? Depois corre só os testes do ginásio, com o nome de cada um:

```bash
python3 -m pytest -v test_ginasio.py
```

O que deves ver, a partir da linha `collected`:

```text
collecting ... collected 3 items

test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis PASSED [ 33%]
test_ginasio.py::test_combate_sem_pokemon_com_vida_e_recusado PASSED     [ 66%]
test_ginasio.py::test_o_desafiante_que_vence_fica_registado PASSED       [100%]

============================== 3 passed in 0.01s ===============================
```

As respostas: a fixture é chamada duas vezes, uma por cada teste que tem `cerulean` como parâmetro. O Ash ganha. O Bulbasaur tira 50 à Starmie, o dobro de 25, e deixa-a com 40. A Starmie tira 35 ao Bulbasaur, e o Bulbasaur tira mais 50: a Starmie fica KO.

### Paragem 6

O `test_ginasio.py` tem três testes, dois deles com a fixture, e os três passam.

Pensa antes de continuares: se o teste do combate recusado corresse depois do teste do combate ganho, a lista dos combates estaria vazia? A resposta: sim. Cada teste recebe um ginásio novo, criado pela fixture só para ele, e o combate de um teste não aparece no ginásio do outro. A ordem por que os testes correm deixa de importar.

## Fase 7: Um defeito relatado: o teste primeiro

Quando aparece um defeito, a rotina de cinco passos do tema 04 começa por o observar e reproduzir. Com testes, reproduzir o defeito quer dizer escrever um teste que falha por causa dele, antes de mexer no código. Depois corriges, e o mesmo teste a passar prova que a correção resolveu o defeito. O teste fica no ficheiro: é um teste de regressão, que apanha o defeito se ele voltar. Para saber mais, lê a secção "Um teste antes da correção" do [guia](05-testes-com-pytest.md).

1. Imagina que um colega mudou o `combater` do `Ginasio`. Para seguires esta fase, faz tu a mesma mudança. No `ginasio.py`, no `combater`, a linha `vencedor = self.lider` passa a ser:

```python
                vencedor = defensor
```

2. Executa a demonstração do ginásio, como um utilizador o faria:

```bash
python3 ginasio.py
```

O que deves ver, no histórico, no fim da saída:

```text
Histórico do ginásio de Cerulean:
 - Ash com Charmander: venceu Starmie
 - Ash com Bulbasaur: venceu Ash
```

Este é o sintoma, e é o relato que chega: "Quando a Misty ganha, o histórico diz que venceu a Starmie, e não a Misty." Um combate é entre treinadores, e o histórico diz o nome do Pokémon. O `defensor` é o Pokémon da Misty, e o `vencedor` tem de ser o treinador.

3. Antes de corrigires, escreve o teste que reproduz o relato. Acrescenta ao fim do `test_ginasio.py`:

```python


def test_o_lider_que_vence_fica_registado(cerulean):
    """Quando o líder ganha, o registo do combate diz o nome do líder."""
    ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])

    cerulean.combater(ash)

    assert cerulean.combates == [Combate("Ash", "Charmander", "Misty")]
```

Leitura guiada: o teste usa a fixture, e o Ash vem com um Charmander. O Charmander tira 40 à Starmie, e a Starmie tira 70 ao Charmander, o dobro de 35, porque a água tem vantagem contra o fogo. Ao segundo ataque da Starmie, o Charmander fica KO, e quem ganha é a Misty. O `assert` diz o que as regras pedem: o registo tem o nome da Misty como vencedora.

4. Antes de correres `python3 -m pytest`, com o código do colega ainda no `ginasio.py`, prevê se o teste novo passa.

O que deves ver, a partir da linha `collected`:

```text
collected 12 items

test_ginasio.py ...F                                                     [ 33%]
test_pokemon.py ........                                                 [100%]

=================================== FAILURES ===================================
____________________ test_o_lider_que_vence_fica_registado _____________________

cerulean = <ginasio.Ginasio object at 0x10ae4b390>

    def test_o_lider_que_vence_fica_registado(cerulean):
        """Quando o líder ganha, o registo do combate diz o nome do líder."""
        ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])
    
        cerulean.combater(ash)
    
>       assert cerulean.combates == [Combate("Ash", "Charmander", "Misty")]
E       AssertionError: assert [Combate(desa...or='Starmie')] == [Combate(desa...edor='Misty')]
E         
E         At index 0 diff: Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Starmie') != Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Misty')
E         Use -v to get more diff

test_ginasio.py:54: AssertionError
----------------------------- Captured stdout call -----------------------------

=== Ash desafia Misty no ginásio de Cerulean ===
Charmander ataca Starmie e tira 40 de vida.
Starmie tem 50/150 de vida.
É super eficaz!
Starmie ataca Charmander e tira 70 de vida.
Charmander tem 20/150 de vida.
Charmander ataca Starmie e tira 40 de vida.
Starmie tem 10/150 de vida.
É super eficaz!
Starmie ataca Charmander e tira 70 de vida.
Charmander está KO (0/150).
=========================== short test summary info ============================
FAILED test_ginasio.py::test_o_lider_que_vence_fica_registado - AssertionErro...
========================= 1 failed, 11 passed in 0.03s =========================
```

Isto quer dizer que o teste reproduz o relato. A linha `At index 0 diff` diz que as duas listas diferem na posição 0, e mostra os dois registos, com o `!=`, que quer dizer "diferente de". Só o campo `vencedor` é diferente: `'Starmie'` em vez de `'Misty'`. A linha `cerulean = <ginasio.Ginasio object at 0x...>`, no início, mostra o que a fixture entregou ao teste. A secção `Captured stdout call` mostra o combate, escrito pelo `print` do ginásio, e confirma que a Misty ganhou.

5. Corrige a causa: no `ginasio.py`, volta a pôr `vencedor = self.lider`. Depois volta a testar tudo, com `python3 -m pytest`.

O que deves ver, a partir da linha `collected`:

```text
collected 12 items

test_ginasio.py ....                                                     [ 33%]
test_pokemon.py ........                                                 [100%]

============================== 12 passed in 0.02s ==============================
```

Isto quer dizer que a correção resolveu o defeito e não partiu mais nada: os outros onze testes continuam a passar.

### Paragem 7

O `ginasio.py` está como na pasta 04, e os doze testes passam. O teste `test_o_lider_que_vence_fica_registado` fica no ficheiro.

Pensa antes de continuares: porque é que o teste se escreveu antes da correção, e não depois? A resposta: antes da correção, vê-lo falhar confirma que ele reproduz o defeito. Depois, vê-lo passar prova que a correção o resolveu. Um teste escrito só depois da correção passa logo, e não sabes se teria apanhado o defeito.

## Fase 8: Mudanças que partem o código

Os testes servem para dar por uma mudança que parte o código, mesmo quando quem a fez não deu por nada. Nesta fase fazes três mudanças erradas, uma de cada vez. Antes de correres os testes, dizes qual deles vai falhar. Se nenhum falhar, encontraste um sítio do código que nenhum teste guarda, e escreves o teste que falta.

1. Primeira mudança. No `ginasio.py`, no `capturar` do `Treinador`, troca o `>=` da condição por `>`, para a linha ficar `if len(self.equipa) > TAMANHO_MAXIMO_DA_EQUIPA:`. Antes de correres `python3 -m pytest`, prevê que teste falha e porquê.

O que deves ver, a partir da linha `FAILURES`:

```text
=================================== FAILURES ===================================
__________ test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis ___________

    def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
        """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
        brock = Treinador("Brock")
        for numero in range(6):
            brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
    
>       with pytest.raises(EquipaCheia):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE EquipaCheia

test_ginasio.py:22: Failed
=========================== short test summary info ============================
FAILED test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis
========================= 1 failed, 11 passed in 0.03s =========================
```

Isto quer dizer que, com o `>`, a sétima captura foi aceite: a equipa tinha seis, e 6 não é maior do que 6. `DID NOT RAISE EquipaCheia` quer dizer "não lançou `EquipaCheia`". No Python 3.9, com o pytest 8, a mensagem é `DID NOT RAISE <class 'erros.EquipaCheia'>`, e o `>` aponta a linha da captura, a 23. Também não aparece a linha com os acentos circunflexos. Volta a pôr o `>=`.

2. Segunda mudança. No `ginasio.py`, no `combater` do `Ginasio`, o desafiante passa a entrar na lista dos desafiantes logo no início, antes de se saber se há combate. Antes da linha `atacante = desafiante.escolher_pokemon()`, acrescenta estas duas, com a mesma indentação dela:

```python
        if desafiante not in self.desafiantes:
            self.desafiantes.append(desafiante)
```

Antes de correres `python3 -m pytest`, prevê que teste falha.

O que deves ver, a partir da linha `FAILURES`:

```text
=================================== FAILURES ===================================
_________________ test_combate_sem_pokemon_com_vida_e_recusado _________________

cerulean = <ginasio.Ginasio object at 0x106a2c830>

    def test_combate_sem_pokemon_com_vida_e_recusado(cerulean):
        """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
        ash = Treinador("Ash")
    
        with pytest.raises(SemPokemonComVida):
            cerulean.combater(ash)
    
>       assert cerulean.desafiantes == []
E       assert [<ginasio.Tre... 0x106a765d0>] == []
E         
E         Left contains one more item: <ginasio.Treinador object at 0x106a765d0>
E         Use -v to get more diff

test_ginasio.py:35: AssertionError
------------------------------ Captured log call -------------------------------
WARNING  ginasio:ginasio.py:145 Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
=========================== short test summary info ============================
FAILED test_ginasio.py::test_combate_sem_pokemon_com_vida_e_recusado - assert...
========================= 1 failed, 11 passed in 0.03s =========================
```

Isto quer dizer que o combate foi recusado, mas o Ash ficou na lista dos desafiantes. `Left contains one more item` quer dizer que a lista da esquerda tem um elemento a mais, o treinador Ash. O `pytest.raises` passou, porque a exceção foi lançada, e foi o `assert` depois do bloco que apanhou o erro. A secção `Captured log call` mostra o aviso que o ginásio escreveu com o logging do tema 04. Tira as duas linhas que acrescentaste.

3. Terceira mudança. No `pokemon.py`, no `recuperar` da `PokemonPlanta`, apaga as três linhas que impedem um Pokémon KO de recuperar:

```python
        if self.vida == 0:
            print(f"{self.nome} está KO e não pode recuperar.")
            return
```

Antes de correres `python3 -m pytest`, prevê que teste falha.

O que deves ver, a partir da linha `collected`:

```text
collected 12 items

test_ginasio.py ....                                                     [ 33%]
test_pokemon.py ........                                                 [100%]

============================== 12 passed in 0.02s ==============================
```

Passam todos. Uma planta KO passou a recuperar, o que as regras não deixam, e nenhum dos teus testes deu por isso. O teste da recuperação usa uma planta com 140 de vida, longe da fronteira do KO.

4. Escreve o teste que falta, com o código errado ainda no `pokemon.py`. Acrescenta ao fim do `test_pokemon.py`:

```python


def test_planta_ko_nao_recupera():
    """Uma planta KO não recupera: fica com 0 de vida."""
    bulbasaur = PokemonPlanta("Bulbasaur", 0, 25, 20)

    bulbasaur.recuperar()

    assert bulbasaur.vida == 0
```

Corre `python3 -m pytest`. O que deves ver, a partir da linha `FAILURES`:

```text
=================================== FAILURES ===================================
_________________________ test_planta_ko_nao_recupera __________________________

    def test_planta_ko_nao_recupera():
        """Uma planta KO não recupera: fica com 0 de vida."""
        bulbasaur = PokemonPlanta("Bulbasaur", 0, 25, 20)
    
        bulbasaur.recuperar()
    
>       assert bulbasaur.vida == 0
E       assert 20 == 0
E        +  where 20 = <pokemon.PokemonPlanta object at 0x108e67820>.vida

test_pokemon.py:85: AssertionError
----------------------------- Captured stdout call -----------------------------
Bulbasaur recupera vida.
Bulbasaur tem 20/150 de vida.
=========================== short test summary info ============================
FAILED test_pokemon.py::test_planta_ko_nao_recupera - assert 20 == 0
========================= 1 failed, 12 passed in 0.03s =========================
```

Isto quer dizer que o teste novo apanha a mudança errada. A linha `where 20 = <pokemon.PokemonPlanta object at 0x...>.vida` explica de onde veio o 20: é o `.vida` do Bulbasaur.

5. Volta a pôr no `recuperar` as três linhas que apagaste, no mesmo sítio, logo a seguir à docstring. Corre `python3 -m pytest`.

O que deves ver, a partir da linha `collected`:

```text
collected 13 items

test_ginasio.py ....                                                     [ 30%]
test_pokemon.py .........                                                [100%]

============================== 13 passed in 0.02s ==============================
```

### Paragem 8

O `pokemon.py` e o `ginasio.py` estão como na pasta 04, e os treze testes passam. A tua bateria de testes guarda agora também o KO na recuperação.

Pensa antes de terminares: a terceira mudança passou por doze testes sem que nenhum falhasse. O que é que isso diz sobre contar testes? A resposta: o número de testes não diz se eles guardam o que interessa. Doze testes não apanharam a mudança, e um teste a mais, escolhido na fronteira certa, apanhou-a. O que conta é cada teste distinguir o código certo de uma forma provável de o errar.

## Problemas frequentes

### `No module named pytest`

O pytest não está instalado no Python que estás a usar. Instala-o com `python3 -m pip install pytest`, como no passo 4 da preparação. Se o instalaste e a mensagem continua, confirma que usas `python3 -m` nos dois comandos, para ser o mesmo Python.

### `error: externally-managed-environment`, ao instalar

Em alguns computadores, o Python do sistema não deixa instalar nada com o `pip`. Não tentes contornar a mensagem: fala com o professor, que te diz como fazer nesse computador.

### `collected 0 items` e `no tests ran`

O pytest não encontrou testes. O nome do ficheiro tem de começar por `test_`, e o nome de cada função de teste também. Confirma também que estás na pasta `ginasio-com-testes`.

### `ModuleNotFoundError: No module named 'pokemon'`

O ficheiro de testes não está na mesma pasta que o `pokemon.py`. Os dois ficheiros de testes ficam ao lado dos quatro ficheiros do ginásio.

### `NameError: name 'pytest' is not defined`

Falta a linha `import pytest` no início do `test_ginasio.py`. Sem ela, o `pytest.raises` e o `@pytest.fixture` não existem nesse ficheiro.

### `fixture 'ginasio' not found`

O parâmetro do teste tem um nome diferente do da fixture. O nome do parâmetro tem de ser exatamente o nome da função da fixture, aqui `cerulean`.

### O número de testes é menor do que o do laboratório

Provavelmente tens dois testes com o mesmo nome. Quando duas funções têm o mesmo nome, a segunda substitui a primeira, e o pytest só encontra uma. Acontece muito ao copiar um teste para escrever o seguinte. Confirma os nomes com `python3 -m pytest -v`.

### Um teste que devia falhar passa

Confirma que o teste tem `assert` antes da comparação. Uma linha como `dano == 40`, sem `assert`, compara e deita o resultado fora, e o teste passa sempre. Confirma também que guardaste o ficheiro com a mudança errada antes de correres os testes.

### A linha do resumo aparece cortada

Se o terminal for estreito, a linha `FAILED` acaba em reticências, como `- assert 50 ...`. A mensagem completa está mais acima, na secção `FAILURES`, na linha `E`.

## Desafios

1. O `anunciar_combates` do `Ginasio` entrega cada combate registado a um anunciador, chamando o método `anunciar(combate)` dele. Os anunciadores do `anunciadores.py` escrevem no ecrã, e um teste não lê o ecrã. Escreve um teste para o `anunciar_combates`, no `test_ginasio.py`. O ginásio faz dois combates, com dois desafiantes diferentes, e o teste confirma que o anunciador recebeu os dois registos, pela ordem em que aconteceram. O teste não pode usar o `Narrador` nem o `Placard`.

Pista: lembra-te do duck typing do tema 03. O ginásio não quer saber de que classe é o anunciador, só que tenha o método `anunciar`. O que é que um anunciador feito só para o teste podia fazer com cada combate que recebe, em vez de o escrever?

2. Os três `calcular_dano` da `PokemonFogo`, da `PokemonAgua` e da `PokemonPlanta` repetem as mesmas linhas: comparam o tipo do alvo com um tipo, escrevem "É super eficaz!" e dobram o dano. Só muda o tipo com que comparam. Reescreve as quatro classes do `pokemon.py` para essas linhas ficarem escritas num só sítio, sem mudares o comportamento.

A regra deste desafio é não mudares nenhum teste. Antes de começares, corre `python3 -m pytest` e confirma que os treze passam. Depois de cada mudança, corre-os outra vez. Quando acabares, os treze têm de passar, e a demonstração do ginásio tem de mostrar exatamente o que mostrava.

Pista: a classe-mãe pode fazer a comparação, se cada classe-filha lhe disser qual é o tipo contra o qual tem vantagem. Pensa em como um método reescrito na classe-filha pode dar esse tipo à classe-mãe, e no que a `Pokemon` devolve quando não tem vantagem contra nenhum.

## Antes de terminares

- [ ] A pasta `ginasio-com-testes` tem os quatro ficheiros do ginásio, iguais aos da pasta 04, e os dois ficheiros de testes.
- [ ] `python3 -m pytest` diz `13 passed`.
- [ ] Tens as previsões e as respostas das fases 1 a 8, escritas por ti, em papel ou num ficheiro de texto, conforme o professor indicar.
- [ ] Se fizeste o desafio 1, o teste do anunciador passa, e não usa o `Narrador` nem o `Placard`.
- [ ] Se fizeste o desafio 2, o comportamento do ginásio não mudou: os treze testes passam sem terem sido mudados, e a demonstração mostra o mesmo.
- [ ] Consegues explicar, por palavras tuas, porque é que um teste só vale alguma coisa se falhar com o código errado. Consegues explicar também porque é que se escreve o teste de um defeito antes de o corrigir.

![Rodapé](../imagens/rodape.png)
