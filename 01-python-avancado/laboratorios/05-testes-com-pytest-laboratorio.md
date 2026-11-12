![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Testes de comportamento com pytest

## O que vais construir

Vais escrever treze testes para o ginásio Pokémon do tema 04, em dois ficheiros, e usá-los para encontrar um erro e para ver que mudanças partem o código. O ginásio não muda: no fim, os quatro ficheiros dele estão como no início. A pasta acaba com estes ficheiros, além das pastas que o Python e o pytest criam sozinhos:

```text
ginasio-com-testes/
├── anunciadores.py
├── erros.py
├── ginasio.py
├── pokemon.py
├── test_ginasio.py
└── test_pokemon.py
```

1. [Fase 1: Correr os testes com o pytest](#fase-1-correr-os-testes-com-o-pytest)
2. [Fase 2: Um teste que falha](#fase-2-um-teste-que-falha)
3. [Fase 3: Preparar, fazer, confirmar](#fase-3-preparar-fazer-confirmar)
4. [Fase 4: Um teste tem de distinguir o certo do errado](#fase-4-um-teste-tem-de-distinguir-o-certo-do-errado)
5. [Fase 5: Testar uma recusa: pytest.raises](#fase-5-testar-uma-recusa-pytestraises)
6. [Fase 6: Uma fixture prepara o que vários testes repetem](#fase-6-uma-fixture-prepara-o-que-vários-testes-repetem)
7. [Fase 7: Um teste antes da correção](#fase-7-um-teste-antes-da-correção)
8. [Fase 8: Mudanças que partem o código](#fase-8-mudanças-que-partem-o-código)

## O que precisas

- O Python, a partir do 3.9: o `python3 --version` tem de mostrar `Python 3.9.6` ou uma versão mais recente. No Windows, se o `python3` não funcionar, escreve `py` no lugar dele em todos os comandos.
- O VS Code, para os ficheiros e para o terminal.
- O pytest, que confirmas, e instalas se faltar, em [Preparar o projeto](#preparar-o-projeto).
- Os quatro ficheiros do ginásio da [pasta 04 dos exemplos](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/), que também copias na preparação.

## Preparar o projeto

1. Cria uma pasta nova, `ginasio-com-testes`, onde guardas os trabalhos da disciplina. Não a cries dentro da pasta do repositório dos alunos, se a tiveres no computador: os exemplos de lá têm ficheiros de testes com os mesmos nomes dos teus. Abre-a no VS Code, com a opção `Open Folder...` do menu File. Abre um terminal no menu Terminal, com a opção New Terminal, e escreve `pwd`. O que deves ver: o caminho da tua pasta, a acabar em `ginasio-com-testes`.

2. Copia para a pasta o [`pokemon.py`](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/pokemon.py), o [`erros.py`](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/erros.py), o [`anunciadores.py`](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/anunciadores.py) e o [`ginasio.py`](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/ginasio.py) dos exemplos. Para cada um: abre-o, copia tudo, cria no painel Explorer um ficheiro com o mesmo nome, cola e guarda. Usa os dos exemplos, e não os teus do tema 04, porque são eles que dão as saídas deste laboratório.

3. Corre a demonstração do ginásio, para confirmares o ponto de partida:

   ```bash
   python3 ginasio.py
   ```

   O que deves ver: os combates, as linhas do registo e o histórico, e na última linha `Ash continua com 2 Pokémon; Misty continua com 1.` Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Confirma se o pytest está instalado. O `-m pytest` pede ao Python que corra o pytest, e assim é o mesmo Python dos teus programas:

   ```bash
   python3 -m pytest --version
   ```

   No Windows, se o `python3` não funcionar, o comando é `py -m pytest --version`.

   O que deves ver: uma linha como `pytest 9.1.1`, com a versão que tens. Se aparecer `No module named pytest`, instala-o com o comando seguinte, que o descarrega da internet e o junta ao teu Python:

   ```bash
   python3 -m pip install pytest
   ```

   No Windows, com o `py`, o comando é `py -m pip install pytest`. Depois, corre outra vez `python3 -m pytest --version`. Se o `pip` recusar a instalação ou escrever um aviso, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

## Fase 1: Correr os testes com o pytest

Escreves o primeiro teste do ginásio e corre-lo com o pytest, que encontra sozinho as funções cujo nome começa por `test_`. Rever: [Correr os testes com o pytest](../05-testes-com-pytest.md#correr-os-testes-com-o-pytest).

1. Cria o ficheiro `test_pokemon.py`, na pasta do projeto, com este conteúdo. Rever: [Um teste é uma função](../05-testes-com-pytest.md#um-teste-é-uma-função).

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

2. Corre o ficheiro como um programa:

   ```bash
   python3 test_pokemon.py
   ```

   O que deves ver: nada. O ficheiro só define a função, e ninguém a chama.

3. Corre agora o pytest, que procura os testes na pasta onde o terminal está:

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

   O pytest encontrou um teste no `test_pokemon.py`, e o ponto quer dizer que passou. No teu computador, as linhas `platform` e `rootdir` são outras, e o tempo do fim muda de vez para vez. Daqui em diante, o laboratório mostra a saída a partir da linha `collected`. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Tira, de propósito, o `test_` do nome da função, para a linha ficar `def agua_contra_fogo_tira_o_dobro():`, e guarda. Antes de correres outra vez `python3 -m pytest`, prevê quantos testes o pytest vai encontrar. O que deves ver:

   ```text
   collected 0 items

   ============================ no tests ran in 0.01s =============================
   ```

   Nenhum: sem o `test_` no início do nome, a função não conta como teste, e `no tests ran` quer dizer que nenhum teste correu. Rever: [O que o pytest procura e o que guarda](../05-testes-com-pytest.md#o-que-o-pytest-procura-e-o-que-guarda). Volta a pôr o nome `test_agua_contra_fogo_tira_o_dobro`, guarda e corre outra vez: a última linha volta a dizer `1 passed`.

### Paragem 1

O `test_pokemon.py` tem um teste, e `python3 -m pytest` diz `1 passed`.

Pensa antes de continuares: porque é que é o pytest a chamar o teste, e não uma linha no fim do ficheiro? A resposta: com uma chamada por teste, o primeiro `assert` falso parava o programa, e os testes seguintes já não corriam. O pytest chama cada teste à parte, continua quando um falha e, no fim, diz quais falharam e porquê.

## Fase 2: Um teste que falha

Pões dois testes a falhar de propósito, um de cada vez, e decides pelas regras do jogo se o erro está no teste ou no código. Rever: [Um teste que falha](../05-testes-com-pytest.md#um-teste-que-falha).

1. Um colega escreveu um teste para a planta contra a água. No `test_pokemon.py`, substitui a linha do `import` por esta, que traz também a `PokemonPlanta`:

   ```python
   from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta
   ```

   No fim do ficheiro, deixa duas linhas em branco, como entre duas funções, e acrescenta o teste do colega, como ele o escreveu:

   ```python
   def test_planta_contra_agua_tira_o_dobro():
       """A planta tem vantagem contra a água: o dano é o dobro do ataque."""
       bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
       squirtle = PokemonAgua("Squirtle", 100, 30)
       dano = bulbasaur.calcular_dano(squirtle)
       assert dano == 25
   ```

2. Antes de correres `python3 -m pytest`, prevê qual dos dois testes falha, que valor o código dá e que valor o teste espera. O que deves ver:

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

   Falhou o teste do colega. Na linha `E`, o 50 é o que o código deu, e o 25 é o que o teste esperava. A secção `Captured stdout call` mostra o "É super eficaz!" do `calcular_dano`: o pytest guarda o que os testes escrevem e só o mostra quando um falha. Se aparecer um `NameError`, vê [`name 'PokemonPlanta' is not defined`](#nameerror-name-pokemonplanta-is-not-defined).

3. Decide quem está errado, o teste ou o código. A resposta: o teste. A planta tem vantagem contra a água, e a vantagem dobra o ataque de 25, por isso as regras pedem 50, o que o código deu. Corrige o teste: a última linha passa a `assert dano == 50`. Corre outra vez `python3 -m pytest`. O que deves ver:

   ```text
   collected 2 items

   test_pokemon.py ..                                                       [100%]

   ============================== 2 passed in 0.01s ===============================
   ```

4. Agora, o teste certo e o código errado. No `pokemon.py`, no `calcular_dano` da `PokemonPlanta`, tira o acento a "Água", para a linha ficar `if alvo.tipo == "Agua":`, e guarda. Corre `python3 -m pytest`. O que deves ver:

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

   A mensagem tem a mesma forma, e desta vez o erro está no código: o teste espera os 50 que as regras pedem. O tipo do Squirtle é `"Água"`, com acento, e a comparação com `"Agua"` dá `False`. Por isso, o "É super eficaz!" não foi escrito, e a secção `Captured stdout call` desapareceu. Volta a pôr o acento no `pokemon.py`, guarda e corre outra vez: `2 passed`.

### Paragem 2

O `test_pokemon.py` tem dois testes, e os dois passam. O `pokemon.py` está como na pasta 04.

Pensa antes de continuares: nos dois erros desta fase, o pytest mostrou a mesma forma de mensagem. O que te disse que, da primeira vez, o erro estava no teste e, da segunda, no código? A resposta: as regras do jogo. O pytest só diz que o teste e o código não concordam, e quem está certo é quem concorda com as regras.

## Fase 3: Preparar, fazer, confirmar

Marcas as três partes nos testes que já tens, preparar, fazer e confirmar, e escreves mais dois com a mesma forma. Cada teste faz uma só ação, e o nome dele diz o que confirma. Rever: [Preparar, fazer, confirmar](../05-testes-com-pytest.md#preparar-fazer-confirmar).

1. No `test_pokemon.py`, substitui as quatro linhas do primeiro teste que estão por baixo da docstring por estas, com um comentário em cada parte:

   ```python
       # Preparar: o atacante e o alvo.
       squirtle = PokemonAgua("Squirtle", 100, 30)
       charmander = PokemonFogo("Charmander", 90, 40)
       # Fazer: só a ação que se está a testar.
       dano = squirtle.calcular_dano(charmander)
       # Confirmar: o valor que as regras do jogo pedem.
       assert dano == 60
   ```

   No segundo teste, separa as três partes com uma linha em branco, sem comentários. As linhas por baixo da docstring ficam assim:

   ```python
       bulbasaur = PokemonPlanta("Bulbasaur", 110, 25, 20)
       squirtle = PokemonAgua("Squirtle", 100, 30)

       dano = bulbasaur.calcular_dano(squirtle)

       assert dano == 50
   ```

2. No fim do ficheiro, acrescenta dois testes do fogo, contra a planta, com vantagem, e contra a água, sem vantagem:

   ```python
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

3. Corre os testes com a opção `-v`, de "verbose", detalhado, que mostra o nome de cada teste:

   ```bash
   python3 -m pytest -v
   ```

   O que deves ver:

   ```text
   collecting ... collected 4 items

   test_pokemon.py::test_agua_contra_fogo_tira_o_dobro PASSED               [ 25%]
   test_pokemon.py::test_planta_contra_agua_tira_o_dobro PASSED             [ 50%]
   test_pokemon.py::test_fogo_contra_planta_tira_o_dobro PASSED             [ 75%]
   test_pokemon.py::test_fogo_contra_agua_tira_so_o_ataque PASSED           [100%]

   ============================== 4 passed in 0.01s ===============================
   ```

   Os quatro passam, pela ordem em que estão no ficheiro. Se o pytest encontrar menos de quatro, vê [O pytest encontra menos testes do que devia](#o-pytest-encontra-menos-testes-do-que-devia).

4. Um colega acha que o fogo devia tirar o triplo à planta. Faz a mudança dele: no `pokemon.py`, no `calcular_dano` da `PokemonFogo`, a linha `dano = dano * 2` passa a `dano = dano * 3`. Antes de correres outra vez `python3 -m pytest -v`, prevê quantos dos quatro testes falham. O que deves ver, nas linhas dos testes:

   ```text
   test_pokemon.py::test_agua_contra_fogo_tira_o_dobro PASSED               [ 25%]
   test_pokemon.py::test_planta_contra_agua_tira_o_dobro PASSED             [ 50%]
   test_pokemon.py::test_fogo_contra_planta_tira_o_dobro FAILED             [ 75%]
   test_pokemon.py::test_fogo_contra_agua_tira_so_o_ataque PASSED           [100%]
   ```

   Falha só um, e mais abaixo a linha `E` diz `assert 120 == 80`. O nome do teste diz logo que regra se partiu: o fogo contra a planta já não tira o dobro. O do fogo contra a água passa, porque contra a água o `if` da multiplicação não corre. Volta a pôr o `* 2` no `pokemon.py` e corre `python3 -m pytest`: `4 passed`.

### Paragem 3

O `test_pokemon.py` tem quatro testes, todos com as três partes, e os quatro passam. O ficheiro completo, como deve estar agora:

```python
# test_pokemon.py: os testes das classes de Pokémon.
from pokemon import PokemonAgua, PokemonFogo, PokemonPlanta


def test_agua_contra_fogo_tira_o_dobro():
    """A água tem vantagem contra o fogo: o dano é o dobro do ataque."""
    # Preparar: o atacante e o alvo.
    squirtle = PokemonAgua("Squirtle", 100, 30)
    charmander = PokemonFogo("Charmander", 90, 40)
    # Fazer: só a ação que se está a testar.
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

O primeiro teste marca as três partes com comentários, e os outros separam-nas com linhas em branco. Todos criam os seus Pokémon, fazem um só cálculo do dano e acabam num `assert`.

Pensa antes de continuares: um colega juntou os quatro testes num só, com os quatro cálculos e os quatro `assert` seguidos. Porque é que é pior? A resposta: se o segundo `assert` falhar, o teste para aí, e não sabes se o terceiro e o quarto passavam. E o nome do teste já não diz qual das vantagens se partiu.

## Fase 4: Um teste tem de distinguir o certo do errado

Pões de propósito um erro no `pokemon.py` e vês quais dos quatro testes dão por ele. Depois, escreves quatro testes nas fronteiras das regras. Rever: [Um teste tem de distinguir o certo do errado](../05-testes-com-pytest.md#um-teste-tem-de-distinguir-o-certo-do-errado).

1. No `pokemon.py`, no `calcular_dano` da `PokemonFogo`, tira quatro espaços à linha `dano = dano * 2`, para ela sair do `if`. O método fica assim:

   ```python
       def calcular_dano(self, alvo):
           """Contra Planta, o fogo tira o dobro."""
           dano = super().calcular_dano(alvo)
           if alvo.tipo == "Planta":
               print("É super eficaz!")
           dano = dano * 2
           return dano
   ```

   Com a multiplicação fora do `if`, o fogo tira o dobro a qualquer alvo. Antes de correres `python3 -m pytest`, prevê quais dos quatro testes falham. O que deves ver:

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

   Só o do fogo contra a água. O do fogo contra a planta passou porque, contra a planta, o dobro está certo: o código certo dá 80, e o errado também. Só um alvo sem vantagem dá resultados diferentes, 40 com o código certo e 80 com o errado. Se aparecer `ERROR collecting`, vê [o `IndentationError`](#error-collecting-com-um-indentationerror).

2. Volta a indentar a linha `dano = dano * 2`, para ficar dentro do `if`, por baixo do `print`, e corre `python3 -m pytest`: `4 passed`.

3. Agora, as fronteiras das regras: o ataque vai de 1 a 50, a vida não passa de 150, e um Pokémon com 0 de vida está KO. No fim do `test_pokemon.py`, acrescenta estes quatro testes. Rever: [Os casos de fronteira: o KO e os limites da vida](../05-testes-com-pytest.md#os-casos-de-fronteira-o-ko-e-os-limites-da-vida).

   ```python
   def test_ataque_abaixo_do_minimo_fica_no_minimo():
       """O ataque vai de 1 a 50: 0 passa a 1."""
       # Preparar e fazer numa só linha: é o construtor que passa o ataque pelo set.
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

4. Corre `python3 -m pytest`. O que deves ver:

   ```text
   collected 8 items

   test_pokemon.py ........                                                 [100%]

   ============================== 8 passed in 0.02s ===============================
   ```

   Os Pokémon respeitam as regras também nas fronteiras: o ataque, o KO e a recuperação.

5. Provoca um erro de propósito no set do ataque: no `pokemon.py`, a linha `elif valor > ATAQUE_MAXIMO:` passa a `elif valor > VIDA_MAXIMA:`, o limite da vida, e a linha de baixo continua a pôr 50. Corre `python3 -m pytest`. O que deves ver, na secção `FAILURES`:

   ```text
   __________________ test_ataque_acima_do_maximo_fica_no_maximo __________________

       def test_ataque_acima_do_maximo_fica_no_maximo():
           """O ataque vai de 1 a 50: 51 passa a 50."""
           charmander = PokemonFogo("Charmander", 90, 51)
       
   >       assert charmander.ataque == 50
   E       assert 51 == 50
   E        +  where 51 = <pokemon.PokemonFogo object at 0x10ad6a650>.ataque
   ```

   Um ataque de 51 não passa de 150, e o set deixou-o ficar 51. Um teste com 200 não dava pelo erro, porque 200 passa de 150 e o set punha 50 na mesma. Só o primeiro valor acima do limite separa o limite certo do errado. Volta a pôr `ATAQUE_MAXIMO` e corre outra vez: `8 passed`.

### Paragem 4

O `test_pokemon.py` tem oito testes, todos a passar, e o `pokemon.py` está como na pasta 04.

Pensa antes de continuares: porque é que o teste da recuperação usa uma planta com 140 de vida, e não com 90? A resposta: com 90, a recuperação dava 110, longe do limite, e o set da vida não tinha nada para corrigir. Um `recuperar` que somasse a vida sem passar pelo set também dava 110, e o teste não distinguia as duas versões. Com 140, a soma dá 160, e só o código certo deixa a vida em 150.

## Fase 5: Testar uma recusa: pytest.raises

Crias o `test_ginasio.py`, com os testes das duas recusas do ginásio. O `pytest.raises` confirma que a linha de dentro do `with` lança a exceção indicada. Rever: [Testar uma recusa: pytest.raises](../05-testes-com-pytest.md#testar-uma-recusa-pytestraises).

1. Cria o ficheiro `test_ginasio.py` com o teste da equipa cheia. O `import pytest` é o que dá acesso ao `pytest.raises`.

   ```python
   # test_ginasio.py: os testes do treinador e do ginásio.
   import pytest

   from erros import EquipaCheia
   from ginasio import Treinador
   from pokemon import Pokemon


   def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
       """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
       # Preparar: seis capturas, que têm de correr sem exceção.
       brock = Treinador("Brock")
       for numero in range(6):
           brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
       # Fazer e confirmar: a sétima captura tem de lançar EquipaCheia.
       with pytest.raises(EquipaCheia):
           brock.capturar(Pokemon("Onix", "Pedra", 50, 20))
       # Confirmar: a recusa não mexeu na equipa.
       assert len(brock.equipa) == 6
   ```

2. Corre `python3 -m pytest`. O que deves ver:

   ```text
   collected 9 items

   test_ginasio.py .                                                        [ 11%]
   test_pokemon.py ........                                                 [100%]

   ============================== 9 passed in 0.02s ===============================
   ```

   O pytest encontrou os dois ficheiros de testes e correu os nove testes, os do `test_ginasio.py` primeiro, pela ordem alfabética dos ficheiros. Se aparecer `NameError: name 'pytest' is not defined`, vê [o `import pytest`](#nameerror-name-pytest-is-not-defined).

3. Acrescenta o teste do combate sem Pokémon com vida. No `test_ginasio.py`, substitui as três linhas que começam por `from` por estas:

   ```python
   from erros import EquipaCheia, SemPokemonComVida
   from ginasio import Ginasio, Lider, Treinador
   from pokemon import Pokemon, PokemonAgua
   ```

   No fim do ficheiro, acrescenta o teste. Rever: [Depois da recusa, o estado](../05-testes-com-pytest.md#depois-da-recusa-o-estado).

   ```python
   def test_combate_sem_pokemon_com_vida_e_recusado():
       """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
       misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
       cerulean = Ginasio("Cerulean", misty)
       # Um treinador acabado de criar tem a equipa vazia.
       ash = Treinador("Ash")

       with pytest.raises(SemPokemonComVida):
           cerulean.combater(ash)

       # Uma lista compara-se com ==, e [] é a lista vazia.
       assert cerulean.desafiantes == []
       assert cerulean.combates == []
   ```

   Corre `python3 -m pytest`. O que deves ver, na última linha: `10 passed`.

4. Troca, de propósito, a exceção do primeiro teste: a linha do `with` passa a `with pytest.raises(SemPokemonComVida):`. A sétima captura continua a ser recusada. Antes de correres só os testes deste ficheiro, com `python3 -m pytest test_ginasio.py`, prevê se o teste passa. O que deves ver:

   ```text
   collected 2 items

   test_ginasio.py F.                                                       [100%]

   =================================== FAILURES ===================================
   __________ test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis ___________

       def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
           """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
           # Preparar: seis capturas, que têm de correr sem exceção.
           brock = Treinador("Brock")
           for numero in range(6):
               brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
           # Fazer e confirmar: a sétima captura tem de lançar EquipaCheia.
           with pytest.raises(SemPokemonComVida):
   >           brock.capturar(Pokemon("Onix", "Pedra", 50, 20))

   test_ginasio.py:17: 
   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

   self = <ginasio.Treinador object at 0x107074ec0>
   pokemon = <pokemon.Pokemon object at 0x107036250>

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
   ========================= 1 failed, 1 passed in 0.03s ==========================
   ```

   Não passa. O `pytest.raises(SemPokemonComVida)` só apanha essa exceção e as que descendem dela, e a `EquipaCheia` atravessou o bloco como se ele não existisse. A saída tem dois andares, separados pela linha de traços baixos, `_ _ _`: o teste, em cima, e o `capturar`, em baixo, com o `raise`. Os números depois de `at` mudam de vez para vez. Volta a pôr `pytest.raises(EquipaCheia)` e corre `python3 -m pytest`: `10 passed`.

### Paragem 5

O `test_ginasio.py` tem os testes das duas recusas, e `python3 -m pytest` diz `10 passed`.

Pensa antes de continuares: o primeiro teste tem o `pytest.raises` e um `assert` depois dele. O que é que o `assert` apanha que o `pytest.raises` não apanha? A resposta: um `capturar` que juntasse o Pokémon à equipa antes de lançar a exceção. O `pytest.raises` ficava satisfeito, porque a exceção era lançada, mas a equipa ficava com sete, e o `assert` falhava.

## Fase 6: Uma fixture prepara o que vários testes repetem

Passas a preparação do ginásio para a fixture `cerulean`, que o pytest chama de novo para cada teste que a pede, e escreves um teste novo que a usa. Rever: [Uma fixture prepara o que vários testes repetem](../05-testes-com-pytest.md#uma-fixture-prepara-o-que-vários-testes-repetem).

1. No `test_ginasio.py`, entre as linhas `from` e o primeiro teste, acrescenta a fixture, com duas linhas em branco antes e depois:

   ```python
   # O @pytest.fixture faz desta função uma fixture, que os testes pedem pelo nome.
   @pytest.fixture
   def cerulean():
       """Devolve um ginásio novo em Cerulean, com a Misty como líder e só a Starmie."""
       misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
       return Ginasio("Cerulean", misty)
   ```

2. Substitui o teste do combate recusado por esta versão, que já não cria a Misty nem o ginásio, e os recebe da fixture:

   ```python
   def test_combate_sem_pokemon_com_vida_e_recusado(cerulean):
       """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
       # O parâmetro cerulean recebe o ginásio que a fixture devolveu.
       ash = Treinador("Ash")

       with pytest.raises(SemPokemonComVida):
           cerulean.combater(ash)

       assert cerulean.desafiantes == []
       assert cerulean.combates == []
   ```

   Corre só os testes do ginásio, com o nome de cada um:

   ```bash
   python3 -m pytest -v test_ginasio.py
   ```

   O que deves ver:

   ```text
   collecting ... collected 2 items

   test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis PASSED [ 50%]
   test_ginasio.py::test_combate_sem_pokemon_com_vida_e_recusado PASSED     [100%]

   ============================== 2 passed in 0.01s ===============================
   ```

3. Muda, de propósito, o nome do parâmetro desse teste de `cerulean` para `ginasio`, e corre `python3 -m pytest test_ginasio.py`. O que deves ver no início:

   ```text
   collected 2 items

   test_ginasio.py .E                                                       [100%]

   ==================================== ERRORS ====================================
   ________ ERROR at setup of test_combate_sem_pokemon_com_vida_e_recusado ________
   ```

   Mais abaixo, a linha que começa por `E` diz `fixture 'ginasio' not found`, e a última linha diz `1 passed, 1 error`. O pytest procura uma fixture com o nome do parâmetro, e não há nenhuma chamada `ginasio`. Na linha `available fixtures`, entre os nomes do próprio pytest, está o nome certo, `cerulean`. O `E` da linha do ficheiro e o `ERROR at setup` querem dizer que o teste nem chegou a correr: o pytest não o conseguiu preparar. Volta a pôr `cerulean` e corre outra vez: `2 passed`.

4. Acrescenta um teste em que o Ash ganha o combate. Substitui as linhas `from ginasio` e `from pokemon` por estas, que trazem o `Combate` e a `PokemonPlanta`:

   ```python
   from ginasio import Combate, Ginasio, Lider, Treinador
   from pokemon import Pokemon, PokemonAgua, PokemonPlanta
   ```

   No fim do ficheiro, acrescenta:

   ```python
   def test_o_desafiante_que_vence_fica_no_historico(cerulean):
       """Quando o desafiante ganha, o combate fica no histórico com ele como vencedor."""
       ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])

       cerulean.combater(ash)

       # Combate é uma dataclass: o == compara os três campos dos dois combates.
       assert cerulean.combates == [Combate("Ash", "Bulbasaur", "Ash")]
   ```

5. A opção `--setup-show` mostra cada vez que o pytest prepara uma fixture. Antes de correres, prevê quantas vezes ele vai chamar a `cerulean` para os três testes do ficheiro. Depois, corre:

   ```bash
   python3 -m pytest --setup-show test_ginasio.py
   ```

   O que deves ver:

   ```text
   collected 3 items

   test_ginasio.py 
           test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis .
           SETUP    F cerulean
           test_ginasio.py::test_combate_sem_pokemon_com_vida_e_recusado (fixtures used: cerulean) .
           TEARDOWN F cerulean
           SETUP    F cerulean
           test_ginasio.py::test_o_desafiante_que_vence_fica_no_historico (fixtures used: cerulean) .
           TEARDOWN F cerulean

   ============================== 3 passed in 0.01s ===============================
   ```

   Duas vezes: há um `SETUP` antes de cada teste que tem o parâmetro `cerulean`. O `F` aqui não é o de falhou. O teste da equipa cheia não pede a fixture e não recebe ginásio. No pytest 8, o ponto do fim de cada teste vem colado ao nome. Um `NameError` quer dizer que falta uma classe nas linhas do `import`: vê [como se corrige](#nameerror-name-pokemonplanta-is-not-defined).

### Paragem 6

O `test_ginasio.py` tem três testes, dois deles com a fixture, e `python3 -m pytest` diz `11 passed`. O ficheiro completo, como deve estar agora:

```python
# test_ginasio.py: os testes do treinador e do ginásio.
import pytest

from erros import EquipaCheia, SemPokemonComVida
from ginasio import Combate, Ginasio, Lider, Treinador
from pokemon import Pokemon, PokemonAgua, PokemonPlanta


# O @pytest.fixture faz desta função uma fixture, que os testes pedem pelo nome.
@pytest.fixture
def cerulean():
    """Devolve um ginásio novo em Cerulean, com a Misty como líder e só a Starmie."""
    misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
    return Ginasio("Cerulean", misty)


def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
    """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
    # Preparar: seis capturas, que têm de correr sem exceção.
    brock = Treinador("Brock")
    for numero in range(6):
        brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
    # Fazer e confirmar: a sétima captura tem de lançar EquipaCheia.
    with pytest.raises(EquipaCheia):
        brock.capturar(Pokemon("Onix", "Pedra", 50, 20))
    # Confirmar: a recusa não mexeu na equipa.
    assert len(brock.equipa) == 6


def test_combate_sem_pokemon_com_vida_e_recusado(cerulean):
    """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
    # O parâmetro cerulean recebe o ginásio que a fixture devolveu.
    ash = Treinador("Ash")

    with pytest.raises(SemPokemonComVida):
        cerulean.combater(ash)

    assert cerulean.desafiantes == []
    assert cerulean.combates == []


def test_o_desafiante_que_vence_fica_no_historico(cerulean):
    """Quando o desafiante ganha, o combate fica no histórico com ele como vencedor."""
    ash = Treinador.com_equipa("Ash", [PokemonPlanta("Bulbasaur", 110, 25, 20)])

    cerulean.combater(ash)

    # Combate é uma dataclass: o == compara os três campos dos dois combates.
    assert cerulean.combates == [Combate("Ash", "Bulbasaur", "Ash")]
```

A fixture fica entre as importações e os testes. Os dois testes do ginásio recebem-na pelo parâmetro `cerulean`, e nenhum repete as linhas que criam a Misty e o ginásio.

Pensa antes de continuares: se o teste do combate ganho estivesse antes do teste do combate recusado, este último continuava a passar, com o `assert cerulean.combates == []`? A resposta: sim. Cada um recebe um ginásio acabado de criar pela fixture, e o combate de um não aparece no ginásio do outro. Rever: [Cada teste começa do zero](../05-testes-com-pytest.md#cada-teste-começa-do-zero).

## Fase 7: Um teste antes da correção

Recebes o relato de um erro e escreves o teste que o reproduz antes de corrigires o código. Depois da correção, o teste fica no ficheiro, como teste de regressão. Rever: [Um teste antes da correção](../05-testes-com-pytest.md#um-teste-antes-da-correção).

1. Um colega mudou o `combater` do `Ginasio`. Faz tu a mesma mudança, para teres o erro dele: no `ginasio.py`, a linha `vencedor = self.lider` passa a `vencedor = defensor`.

2. Corre a demonstração, como quem usa o ginásio:

   ```bash
   python3 ginasio.py
   ```

   O que deves ver, no histórico, no fim:

   ```text
   Histórico do ginásio de Cerulean:
    - Ash com Charmander: venceu Starmie
    - Ash com Bulbasaur: venceu Ash
   ```

   É o sintoma, e chega o relato: "Quando a Misty ganha, o histórico diz que venceu a Starmie, e não a Misty."

3. Antes de corrigires, escreve o teste que reproduz o relato. No `test_ginasio.py`, substitui a linha `from pokemon` por esta, que traz também o `PokemonFogo`:

   ```python
   from pokemon import Pokemon, PokemonAgua, PokemonFogo, PokemonPlanta
   ```

   No fim do ficheiro, acrescenta o teste. A Starmie tem vantagem contra o fogo, e o Charmander perde:

   ```python
   def test_o_lider_que_vence_fica_no_historico(cerulean):
       """Quando o líder ganha, o combate fica no histórico com o líder como vencedor."""
       ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])

       cerulean.combater(ash)

       assert cerulean.combates == [Combate("Ash", "Charmander", "Misty")]
   ```

4. Com a mudança do colega ainda no `ginasio.py`, prevê se o teste novo passa. Depois, corre `python3 -m pytest`. O que deves ver:

   ```text
   collected 12 items

   test_ginasio.py ...F                                                     [ 33%]
   test_pokemon.py ........                                                 [100%]

   =================================== FAILURES ===================================
   ___________________ test_o_lider_que_vence_fica_no_historico ___________________

   cerulean = <ginasio.Ginasio object at 0x109150410>

       def test_o_lider_que_vence_fica_no_historico(cerulean):
           """Quando o líder ganha, o combate fica no histórico com o líder como vencedor."""
           ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 90, 40)])
       
           cerulean.combater(ash)
       
   >       assert cerulean.combates == [Combate("Ash", "Charmander", "Misty")]
   E       AssertionError: assert [Combate(desa...or='Starmie')] == [Combate(desa...edor='Misty')]
   E         
   E         At index 0 diff: Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Starmie') != Combate(desafiante='Ash', pokemon_desafiante='Charmander', vencedor='Misty')
   E         Use -v to get more diff

   test_ginasio.py:58: AssertionError
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
   FAILED test_ginasio.py::test_o_lider_que_vence_fica_no_historico - AssertionE...
   ========================= 1 failed, 11 passed in 0.03s =========================
   ```

   O teste falha, como o relato. A linha `At index 0 diff` diz que as duas listas diferem na posição 0: só o `vencedor` muda, `'Starmie'` em vez de `'Misty'`. A linha `cerulean = <ginasio.Ginasio object at 0x...>` mostra o ginásio que a fixture entregou ao teste. Se o teste falhar com um `NameError`, falta o `PokemonFogo` na linha `from pokemon`: vê [o `NameError`](#nameerror-name-pokemonplanta-is-not-defined).

5. Corrige a causa: o `defensor` é o Pokémon da Misty, e o vencedor de um combate é um treinador. No `ginasio.py`, volta a pôr `vencedor = self.lider`, e corre outra vez todos os testes, com `python3 -m pytest`. O que deves ver:

   ```text
   collected 12 items

   test_ginasio.py ....                                                     [ 33%]
   test_pokemon.py ........                                                 [100%]

   ============================== 12 passed in 0.02s ==============================
   ```

   O teste do relato passa, e os outros onze continuam a passar: a correção não partiu nada.

### Paragem 7

O `ginasio.py` está como na pasta 04, os doze testes passam, e o `test_o_lider_que_vence_fica_no_historico` fica no ficheiro.

Pensa antes de continuares: porque é que o teste se escreveu antes da correção, e não depois? A resposta: vê-lo falhar antes da correção confirma que ele reproduz o relato, e vê-lo passar depois prova que a correção o resolveu. Um teste escrito só depois da correção passa logo, e não sabes se teria apanhado o erro.

## Fase 8: Mudanças que partem o código

Fazes três mudanças erradas no ginásio, uma de cada vez, e vês que teste apanha cada uma. A que nenhum teste apanha pede um teste novo. Rever: [Mudanças que partem o código](../05-testes-com-pytest.md#mudanças-que-partem-o-código).

1. Primeira mudança: no `ginasio.py`, no `capturar` do `Treinador`, troca o `>=` da condição por `>`, para a linha ficar `if len(self.equipa) > TAMANHO_MAXIMO_DA_EQUIPA:`. Corre `python3 -m pytest`. O que deves ver, a partir da linha `FAILURES`:

   ```text
   =================================== FAILURES ===================================
   __________ test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis ___________

       def test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis():
           """A equipa aceita seis Pokémon, recusa o sétimo e fica como estava."""
           # Preparar: seis capturas, que têm de correr sem exceção.
           brock = Treinador("Brock")
           for numero in range(6):
               brock.capturar(Pokemon(f"Geodude {numero + 1}", "Pedra", 50, 20))
           # Fazer e confirmar: a sétima captura tem de lançar EquipaCheia.
   >       with pytest.raises(EquipaCheia):
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
   E       Failed: DID NOT RAISE EquipaCheia

   test_ginasio.py:24: Failed
   =========================== short test summary info ============================
   FAILED test_ginasio.py::test_a_setima_captura_e_recusada_e_a_equipa_fica_com_seis
   ========================= 1 failed, 11 passed in 0.03s =========================
   ```

   Com o `>`, a sétima captura foi aceite, porque 6 não é maior do que 6. `DID NOT RAISE EquipaCheia` quer dizer "não lançou `EquipaCheia`". No Python 3.9, com o pytest 8, a mensagem é `DID NOT RAISE <class 'erros.EquipaCheia'>`, o `>` aponta a linha da captura, a 25, e não há a linha com `^`. Se nenhum teste falhar, vê [Um teste que devia falhar passa](#um-teste-que-devia-falhar-passa). Volta a pôr o `>=`.

2. Segunda mudança: no `combater` do `Ginasio`, passa para o início do método, logo a seguir à docstring, as duas linhas que juntam o desafiante à lista. São o `if desafiante not in self.desafiantes:` e o `append` por baixo dele. Corre `python3 -m pytest`. O que deves ver, na secção das falhas:

   ```text
   _________________ test_combate_sem_pokemon_com_vida_e_recusado _________________

   cerulean = <ginasio.Ginasio object at 0x10b0d52b0>

       def test_combate_sem_pokemon_com_vida_e_recusado(cerulean):
           """Um desafiante com a equipa vazia não combate, e o ginásio fica como estava."""
           # O parâmetro cerulean recebe o ginásio que a fixture devolveu.
           ash = Treinador("Ash")
       
           with pytest.raises(SemPokemonComVida):
               cerulean.combater(ash)
       
   >       assert cerulean.desafiantes == []
   E       assert [<ginasio.Tre... 0x10b07b750>] == []
   E         
   E         Left contains one more item: <ginasio.Treinador object at 0x10b07b750>
   E         Use -v to get more diff

   test_ginasio.py:38: AssertionError
   ------------------------------ Captured log call -------------------------------
   WARNING  ginasio:ginasio.py:145 Combate recusado em Cerulean: Ash contra Misty, sem Pokémon com vida.
   ```

   O combate foi recusado, e o `pytest.raises` ficou satisfeito, mas o Ash ficou na lista dos desafiantes. Foi o `assert` depois do bloco que deu pelo erro: `Left contains one more item` quer dizer que a lista da esquerda tem um elemento a mais. A secção `Captured log call` mostra o aviso que o ginásio escreveu no registo. Volta a pôr as duas linhas onde estavam: a seguir ao `raise`, com o `if` alinhado com o `if atacante is None`, com oito espaços, antes da linha `logger.info(f"Combate em`. Corre outra vez: `12 passed`.

3. Terceira mudança: no `pokemon.py`, no `recuperar` da `PokemonPlanta`, apaga as três linhas que impedem um Pokémon KO de recuperar:

   ```python
           if self.vida == 0:
               print(f"{self.nome} está KO e não pode recuperar.")
               return
   ```

   Antes de correres `python3 -m pytest`, prevê se algum dos doze testes falha. O que deves ver:

   ```text
   collected 12 items

   test_ginasio.py ....                                                     [ 33%]
   test_pokemon.py ........                                                 [100%]

   ============================== 12 passed in 0.02s ==============================
   ```

   Nenhum. Uma planta KO passou a recuperar, o que as regras não deixam, e os doze testes não deram por isso. O teste da recuperação usa uma planta com 140 de vida, longe da fronteira do KO.

4. Escreve o teste que falta, com a mudança ainda no `pokemon.py`. No fim do `test_pokemon.py`, acrescenta:

   ```python
   def test_planta_ko_nao_recupera():
       """Uma planta KO não recupera: fica com 0 de vida."""
       bulbasaur = PokemonPlanta("Bulbasaur", 0, 25, 20)

       bulbasaur.recuperar()

       assert bulbasaur.vida == 0
   ```

   Corre `python3 -m pytest`. O que deves ver, depois das duas linhas dos ficheiros:

   ```text
   =================================== FAILURES ===================================
   _________________________ test_planta_ko_nao_recupera __________________________

       def test_planta_ko_nao_recupera():
           """Uma planta KO não recupera: fica com 0 de vida."""
           bulbasaur = PokemonPlanta("Bulbasaur", 0, 25, 20)
       
           bulbasaur.recuperar()
       
   >       assert bulbasaur.vida == 0
   E       assert 20 == 0
   E        +  where 20 = <pokemon.PokemonPlanta object at 0x10abb3230>.vida

   test_pokemon.py:86: AssertionError
   ----------------------------- Captured stdout call -----------------------------
   Bulbasaur recupera vida.
   Bulbasaur tem 20/150 de vida.
   =========================== short test summary info ============================
   FAILED test_pokemon.py::test_planta_ko_nao_recupera - assert 20 == 0
   ========================= 1 failed, 12 passed in 0.03s =========================
   ```

   O teste novo apanha a mudança. A linha `where 20 = ...` diz de onde veio o 20: é a `vida` do Bulbasaur.

5. Volta a pôr as três linhas no `recuperar`, logo a seguir à docstring, e corre `python3 -m pytest`. O que deves ver:

   ```text
   collected 13 items

   test_ginasio.py ....                                                     [ 30%]
   test_pokemon.py .........                                                [100%]

   ============================== 13 passed in 0.02s ==============================
   ```

### Paragem 8

O `pokemon.py` e o `ginasio.py` estão como na pasta 04, e os treze testes passam. Os testes guardam agora também o KO na recuperação.

Pensa antes de terminares: a terceira mudança passou por doze testes sem que nenhum falhasse. O que é que isso diz sobre contar testes? A resposta: o número de testes não diz se eles guardam o que interessa. Doze testes não apanharam a mudança, e um teste a mais, na fronteira certa, apanhou-a.

## Se alguma coisa falhar

1. Estás na pasta certa? Escreve `pwd` no terminal, ou `cd` na linha de comandos clássica do Windows, e confirma que o caminho acaba em `ginasio-com-testes`. Se não acabar, abre essa pasta com `Open Folder...` e abre lá um terminal novo.
2. Guardaste o ficheiro antes de correres? O pytest lê os ficheiros como estão no disco.
3. Os dois ficheiros de testes estão na mesma pasta que o `pokemon.py` e o `ginasio.py`?
4. Mudaste o `pokemon.py` ou o `ginasio.py` numa experiência e não o puseste como estava? Copia-o outra vez da [pasta 04 dos exemplos](../../exemplos/python-avancado/pokemon/04-excecoes-depuracao-e-logging/).
5. Os números das linhas, como em `test_pokemon.py:18`, são outros, e o resto da saída é igual? Tens linhas em branco a mais ou a menos no ficheiro de testes, e está tudo bem.
6. Faltaste a uma aula, ou queres recomeçar a meio? Faz [Preparar o projeto](#preparar-o-projeto) e, conforme a fase em que continuas:
   - fase 2: o passo 1 da fase 1;
   - fase 3: o passo 1 da fase 1 e os passos 1 e 3 da fase 2;
   - fase 4: copia o `test_pokemon.py` da [paragem 3](#paragem-3);
   - fase 5: copia o `test_pokemon.py` da paragem 3 e acrescenta-lhe os quatro testes do passo 3 da fase 4;
   - fase 6: o mesmo que para a fase 5, e os passos 1 e 3 da fase 5;
   - fase 7: o mesmo que para a fase 5, e copia o `test_ginasio.py` da [paragem 6](#paragem-6);
   - fase 8: o mesmo que para a fase 7, e o passo 3 da fase 7.

### `No module named pytest`

O pytest não está instalado no Python que estás a usar. Instala-o como no passo 4 de [Preparar o projeto](#preparar-o-projeto). Se já o instalaste e a mensagem continua, foi noutro Python: usa `python3 -m` nos dois comandos.

### `error: externally-managed-environment`, ao instalar

Neste computador, o Python do sistema não deixa o `pip` instalar nada. Não tentes contornar a mensagem: fala com o professor, que te diz como fazer nesse computador.

### `Defaulting to user installation because normal site-packages is not writeable`, ao instalar

Não é um erro. A conta com que entraste não pode instalar para todas as contas do computador, e o `pip` instalou o pytest só para a tua. Confirma com `python3 -m pytest --version` e continua.

### Um aviso que acaba em `not on PATH`, ao instalar

Também não é um erro. O comando `pytest`, escrito sozinho, ficou numa pasta onde o terminal não procura comandos. O laboratório usa sempre `python3 -m pytest`, que chama o pytest através do Python e não precisa dessa pasta. Não mudes nada no computador.

### `collected 0 items` e `no tests ran`

O pytest não encontrou testes. O nome do ficheiro tem de começar por `test_`, e o de cada função de teste também. Confirma também a pasta, como na primeira verificação.

### `ERROR: file or directory not found: test_ginasio.py`

Pediste um ficheiro de testes pelo nome, e ele não está na pasta onde o terminal está: ou o terminal está noutra pasta, ou o ficheiro tem outro nome. Confirma a pasta, como na primeira verificação, e o nome do ficheiro no painel Explorer.

### `import file mismatch`

O terminal está numa pasta que tem lá dentro outros ficheiros de testes com os nomes dos teus, como os dos exemplos do repositório dos alunos. O pytest apanhou os dois. A pasta do projeto fica fora da pasta do repositório: abre a `ginasio-com-testes` com `Open Folder...` e corre o pytest num terminal aberto nela.

### `ModuleNotFoundError: No module named 'pokemon'`

O Python não encontrou o `pokemon.py` na pasta do ficheiro de testes. Os dois ficheiros de testes ficam ao lado dos quatro ficheiros do ginásio, e o pytest corre-se nessa pasta. A mesma mensagem com `'ginasio'` ou `'erros'` tem a mesma causa.

### `NameError: name 'PokemonPlanta' is not defined`

O teste usa uma classe que a linha do `import` não traz. Acontece quando um passo manda substituir as linhas do `import` e elas ficam como estavam. Confirma a linha `from pokemon` com a do passo onde estás. A mesma mensagem com `Combate`, `PokemonFogo` ou `SemPokemonComVida` tem a mesma causa.

### `NameError: name 'pytest' is not defined`

Falta a linha `import pytest` no início do `test_ginasio.py`. Sem ela, o `pytest.raises` e o `@pytest.fixture` não existem nesse ficheiro. Com a fixture, o erro aparece logo ao recolher os testes, com `ERROR collecting test_ginasio.py`, e nenhum teste do ficheiro corre.

### `ERROR collecting`, com um `IndentationError`

O pytest não conseguiu ler um ficheiro: uma linha tem espaços a mais ou a menos. Acontece quase sempre depois de mudares uma linha de sítio no `pokemon.py` ou no `ginasio.py`. Lê o fim da secção `ERRORS`: diz o ficheiro, o número da linha e a linha. As linhas de um bloco têm todas os mesmos espaços, quatro mais do que o `if` ou o `def` de cima.

### `fixture '...' not found`

O nome do parâmetro do teste não é igual ao da fixture, como no passo 3 da fase 6. O parâmetro tem de se chamar exatamente `cerulean`.

### O pytest encontra menos testes do que devia

Provavelmente tens dois testes com o mesmo nome, e a segunda função substituiu a primeira. Acontece ao copiar um teste para escrever o seguinte. Com a opção `-v`, o pytest mostra o nome de cada teste, e encontras logo o repetido.

### Um teste que devia falhar passa

Confirma que guardaste o ficheiro com a mudança errada antes de correres os testes. Confirma também que o teste tem o `assert`: uma linha como `dano == 40`, sem ele, compara e deita o resultado fora, e o teste passa sempre.

### A linha `FAILED` aparece cortada

Num terminal estreito, a linha `FAILED` do resumo acaba em reticências, como `- AssertionE...`. A mensagem completa está mais acima, na secção `FAILURES`, nas linhas que começam por `E`.

## Desafios

Copia a pasta `ginasio-com-testes` inteira para uma pasta nova, `ginasio-desafios`, ao lado dela, e abre essa no VS Code. A `ginasio-com-testes` fica como no fim da fase 8, e é dela que entregas os testes.

1. Um anunciador de teste. O `anunciar_combates` do `Ginasio` entrega cada combate do histórico a um anunciador, chamando o método `anunciar(combate)` dele. Os anunciadores do `anunciadores.py` escrevem no ecrã, e um teste não lê o ecrã. Escreve, no `test_ginasio.py`, um teste para o `anunciar_combates`. O ginásio faz dois combates, com dois desafiantes diferentes, e o teste confirma que o anunciador recebeu os dois, pela ordem em que aconteceram. O teste não pode usar o `Narrador` nem o `Placard`.

   Pista: lembra-te do duck typing do tema 03. O ginásio não quer saber de que classe é o anunciador, só que tenha o método `anunciar`. O que é que um anunciador feito só para o teste podia fazer com cada combate que recebe, em vez de o escrever? E lembra-te de que a Starmie da fixture fica com a vida que o primeiro combate lhe deixou.

2. Mudar o código com a rede dos testes. Os três `calcular_dano` da `PokemonFogo`, da `PokemonAgua` e da `PokemonPlanta` repetem as mesmas linhas: comparam o tipo do alvo, escrevem "É super eficaz!" e dobram o dano. Só muda o tipo com que comparam. Reescreve as quatro classes do `pokemon.py` para essas linhas ficarem num só sítio, sem mudares o comportamento. A regra é não mudares nenhum teste: corre `python3 -m pytest` antes de começares e depois de cada mudança. No fim, todos os testes passam, sem nenhum ter mudado, e a demonstração do ginásio mostra exatamente o que mostrava.

   Pista: a classe-mãe pode fazer a comparação, se cada classe-filha lhe disser qual é o tipo contra o qual tem vantagem. Pensa em como um método reescrito na classe-filha pode dar esse tipo à classe-mãe, e no que a `Pokemon` devolve quando não tem vantagem contra nenhum.

## Antes de terminares

- [ ] A pasta `ginasio-com-testes` tem os quatro ficheiros do ginásio, iguais aos da pasta 04, e os dois ficheiros de testes. Se não tens a certeza, copia-os outra vez da pasta 04 e confirma que o pytest diz `13 passed`.
- [ ] `python3 -m pytest` diz `13 passed`.
- [ ] O `test_ginasio.py` tem o teste do líder que vence, da fase 7, e o `test_pokemon.py` tem o da planta KO, da fase 8.
- [ ] Entregaste ao professor o `test_pokemon.py` e o `test_ginasio.py`, conforme ele indicar.

![Rodapé](../../imagens/rodape.png)
