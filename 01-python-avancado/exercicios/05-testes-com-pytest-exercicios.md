![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Testes de comportamento com pytest

Praticas os testes com o pytest: escolher os casos que apanham os erros, testar as recusas, usar uma fixture e testar um erro antes de o corrigir. Os exercícios 1 a 7 são obrigatórios e fazem-se pela ordem, porque o 5 e o 7 continuam os testes que escreves no 2, no 3 e no 4. Os ficheiros ficam numa pasta nova, `treino-com-testes`, fora da pasta do repositório dos alunos, como a do guia. As explicações que um exercício pedir ficam num comentário, no ficheiro de testes dele. Precisas do pytest: se o computador ainda não o tiver, instala-o como no passo 4 de [Preparar o projeto](../laboratorios/05-testes-com-pytest-laboratorio.md#preparar-o-projeto), no laboratório. Para rever: o [guia do tema](../05-testes-com-pytest.md) e o [laboratório](../laboratorios/05-testes-com-pytest-laboratorio.md).

## O cenário

Um Pokémon em treino sobe de nível com a experiência: cada 100 pontos sobem um nível, até ao nível 100. Os exercícios testam a classe `PokemonEmTreino`, do ficheiro `treino.py`. Cria-o na pasta da ficha, com este conteúdo:

```python
"""O treino de um Pokémon, para a ficha de exercícios do tema 05.

Cada 100 pontos de experiência sobem um nível, até ao nível 100. Os pontos
que sobram ficam guardados para o nível seguinte. Um doce raro sobe um nível
de uma vez, sem mexer na experiência.
"""

NIVEL_MAXIMO = 100
PONTOS_POR_NIVEL = 100


class PokemonEmTreino:
    """Um Pokémon que ganha experiência e sobe de nível, até ao nível 100."""

    def __init__(self, nome, nivel=1):
        """Cria o Pokémon no nível indicado, com a experiência a zero."""
        self.nome = nome
        self.nivel = nivel
        self.experiencia = 0

    def ganhar_experiencia(self, pontos):
        """Junta os pontos à experiência e sobe um nível por cada 100.

        Os pontos têm de ser mais do que zero: se não forem, lança ValueError
        e não muda nada. No nível 100, a experiência deixa de contar e fica a 0.
        """
        if pontos <= 0:
            raise ValueError(f"{self.nome} só pode ganhar pontos positivos, e recebeu {pontos}.")
        self.experiencia = self.experiencia + pontos
        # Um while, e não um if: uma só chamada pode subir mais do que um nível.
        while self.experiencia >= PONTOS_POR_NIVEL and self.nivel < NIVEL_MAXIMO:
            self.experiencia = self.experiencia - PONTOS_POR_NIVEL
            self.nivel = self.nivel + 1
        if self.nivel == NIVEL_MAXIMO:
            self.experiencia = 0

    def usar_doce_raro(self):
        """Sobe um nível de uma vez, sem mexer na experiência.

        No nível 100 já não há para onde subir: lança ValueError e não muda nada.
        """
        if self.nivel > NIVEL_MAXIMO:
            raise ValueError(f"{self.nome} já está no nível {NIVEL_MAXIMO}.")
        self.nivel = self.nivel + 1
```

`PokemonEmTreino("Eevee")` cria um Eevee no nível 1, e `PokemonEmTreino("Pikachu", 99)` cria um Pikachu no nível 99, os dois com a experiência a zero. As regras do treino são as das docstrings, e é delas que tiras os resultados esperados dos teus testes. O `usar_doce_raro` tem um erro que fica para o exercício 7: não o corrijas antes.

## Escrever e correr testes

### Exercício 1: Prever o resultado do pytest

Três colegas juntaram os testes deles no ficheiro `test_previsao.py`:

```python
# test_previsao.py: três testes de colegas diferentes.
from treino import PokemonEmTreino


def test_cem_pontos_sobem_um_nivel():
    """Cem pontos sobem exatamente um nível."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(100)
    assert eevee.nivel == 2


def test_cento_e_vinte_pontos_deixam_vinte():
    """Cento e vinte pontos sobem um nível e deixam vinte guardados."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(120)
    assert eevee.experiencia == 20


def test_ao_subir_de_nivel_a_experiencia_volta_a_zero():
    """Quando sobe de nível, o Pokémon começa o nível novo sem experiência."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(150)
    assert eevee.experiencia == 0
```

Descobre, sem executar, que testes passam e que testes falham, a última linha que o pytest mostra e, em cada teste que falha, a linha `E`, com os dois valores. Confirma com `python3 -m pytest test_previsao.py`, e explica num comentário cada previsão em que te enganaste. Em cada teste que falha, decide se o erro está no teste ou no código, e corrige-o. Justifica a decisão com a regra do treino, num comentário junto do teste. No fim, os três testes passam.

Rever: [Um teste que falha](../05-testes-com-pytest.md#um-teste-que-falha) e, para a segunda linha `E`, [Um teste antes da correção](../05-testes-com-pytest.md#um-teste-antes-da-correção).

<details>
<summary>Pista</summary>

Faz a conta de cada teste com a regra: o nível e a experiência antes, e depois. Num teste que falha, compara os dois valores da linha `E` com o que dizem as docstrings do `treino.py`.

</details>

### Exercício 2: Os primeiros testes do treino

Cria o ficheiro `test_treino.py`, com dois testes do `ganhar_experiencia`, um para cada caso:

- um Vulpix no nível 5 ganha 40 pontos;
- um Eevee no nível 10 ganha 130 pontos.

Cada teste tem as três partes, um nome que diz o comportamento e uma docstring. Os resultados esperados tiras tu da regra do treino, e decides tu o que cada teste confirma. No fim, `python3 -m pytest test_treino.py` mostra os dois testes a passar.

Rever: [Preparar, fazer, confirmar](../05-testes-com-pytest.md#preparar-fazer-confirmar).

<details>
<summary>Pista</summary>

Antes de escreveres os `assert`, pensa em tudo o que o `ganhar_experiencia` pode mudar num Pokémon.

</details>

### Exercício 3: As fronteiras do treino

O treino tem duas regras com fronteiras: um nível sobe aos 100 pontos, e o nível não passa de 100. Acrescenta ao `test_treino.py` pelo menos quatro testes de fronteira do `ganhar_experiencia`, dois para cada regra, e diz na docstring de cada um que fronteira ele testa. Todos passam com o código do cenário.

Rever: [Os casos de fronteira: o KO e os limites da vida](../05-testes-com-pytest.md#os-casos-de-fronteira-o-ko-e-os-limites-da-vida).

<details>
<summary>Pista</summary>

Numa fronteira, testa o último valor que ainda não muda nada e o primeiro que já muda. Na regra do nível máximo, pergunta-te o que a faz mudar: os pontos, o nível de partida, ou os dois.

</details>

### Exercício 4: Uma recusa, e o que fica depois dela

O `ganhar_experiencia` só aceita pontos mais do que zero, e recusa os outros com `ValueError`, sem mudar nada. Acrescenta ao `test_treino.py` dois testes de recusa, um com 0 pontos e outro com -10, que confirmam a exceção e que o nível e a experiência ficaram como estavam. No fim, os testes do ficheiro passam todos.

Os dois testes têm também de falhar com um `ganhar_experiencia` que, ao recusar, apague os pontos guardados. Para o confirmares, troca as duas linhas a seguir à docstring do método por estas três:

```python
        if pontos <= 0:
            self.experiencia = 0
            raise ValueError(f"{self.nome} só pode ganhar pontos positivos, e recebeu {pontos}.")
```

Corre os testes e, depois, repõe o `treino.py` como estava.

Rever: [Testar uma recusa: pytest.raises](../05-testes-com-pytest.md#testar-uma-recusa-pytestraises) e [Depois da recusa, o estado](../05-testes-com-pytest.md#depois-da-recusa-o-estado).

<details>
<summary>Pista</summary>

Se o Pokémon começa com 0 pontos, o teu `assert` distingue "ficou como estava" de "voltou a zero"?

</details>

## Escolher e organizar os testes

### Exercício 5: Três versões erradas

Três colegas escreveram o `ganhar_experiencia` de outra forma, e cada um enganou-se numa coisa. Esta é a parte do método que muda em cada versão, do `while` até ao fim.

Versão A:

```python
        while self.experiencia > PONTOS_POR_NIVEL and self.nivel < NIVEL_MAXIMO:
            self.experiencia = self.experiencia - PONTOS_POR_NIVEL
            self.nivel = self.nivel + 1
        if self.nivel == NIVEL_MAXIMO:
            self.experiencia = 0
```

Versão B:

```python
        while self.experiencia >= PONTOS_POR_NIVEL and self.nivel < NIVEL_MAXIMO:
            self.experiencia = 0
            self.nivel = self.nivel + 1
        if self.nivel == NIVEL_MAXIMO:
            self.experiencia = 0
```

Versão C:

```python
        while self.experiencia >= PONTOS_POR_NIVEL:
            self.experiencia = self.experiencia - PONTOS_POR_NIVEL
            self.nivel = self.nivel + 1
        if self.nivel == NIVEL_MAXIMO:
            self.experiencia = 0
```

O teu `test_treino.py` tem de apanhar as três versões: com cada uma no `treino.py`, no lugar das linhas do `while` em diante, pelo menos um teste falha com `python3 -m pytest test_treino.py`. Se alguma versão passar em todos os teus testes, acrescenta o teste que a apanha, que falha com ela e passa com o código do cenário. No fim do `test_treino.py`, um comentário diz, para cada versão, o que ela faz de errado, comparada com a regra do treino, e que testes a apanharam. Depois, repõe o `treino.py` como estava.

Rever: [Um teste tem de distinguir o certo do errado](../05-testes-com-pytest.md#um-teste-tem-de-distinguir-o-certo-do-errado) e [Mudanças que partem o código](../05-testes-com-pytest.md#mudanças-que-partem-o-código).

<details>
<summary>Pista</summary>

Para cada versão, procura um nível de partida e uns pontos em que ela e a do cenário dão resultados diferentes. Começa pelas fronteiras das duas regras.

</details>

### Exercício 6: Uma fixture, ou não

Guarda este ficheiro, `test_fixture.py`, na pasta da ficha:

```python
# test_fixture.py: quatro testes do Pidgey.
from treino import PokemonEmTreino


def test_mais_30_pontos_ficam_guardados():
    """Um Pidgey no nível 20, com 50 pontos, fica com 80 se ganhar mais 30."""
    pidgey = PokemonEmTreino("Pidgey", 20)
    pidgey.ganhar_experiencia(50)

    pidgey.ganhar_experiencia(30)

    assert pidgey.experiencia == 80


def test_mais_10_pontos_nao_sobem_de_nivel():
    """Um Pidgey no nível 20, com 50 pontos, continua no nível 20 se ganhar mais 10."""
    pidgey = PokemonEmTreino("Pidgey", 20)
    pidgey.ganhar_experiencia(50)

    pidgey.ganhar_experiencia(10)

    assert pidgey.nivel == 20


def test_mais_70_pontos_sobem_um_nivel():
    """Um Pidgey no nível 20, com 50 pontos, sobe ao nível 21 se ganhar mais 70."""
    pidgey = PokemonEmTreino("Pidgey", 20)
    pidgey.ganhar_experiencia(50)

    pidgey.ganhar_experiencia(70)

    assert pidgey.nivel == 21


def test_pidgey_acabado_de_criar_nao_tem_experiencia():
    """Um Pidgey acabado de criar no nível 20 tem a experiência a zero."""
    pidgey = PokemonEmTreino("Pidgey", 20)

    assert pidgey.experiencia == 0
```

Reescreve o `test_fixture.py` com uma fixture para a preparação que se repete. Decide que testes a pedem e que nome lhe dás. Os quatro testes continuam a confirmar exatamente o mesmo, e passam com `python3 -m pytest test_fixture.py`, antes e depois da mudança. Num comentário junto da fixture, explica a tua escolha dos testes que a pedem.

Rever: [Uma fixture prepara o que vários testes repetem](../05-testes-com-pytest.md#uma-fixture-prepara-o-que-vários-testes-repetem).

<details>
<summary>Pista</summary>

Compara a preparação dos quatro testes, linha a linha. Um teste que pede a fixture recebe tudo o que ela prepara.

</details>

### Exercício 7: O teste antes da correção

Chegou um relato: "Um Pikachu no nível 100 comeu um doce raro e ficou no nível 101." Acrescenta ao `test_treino.py` o teste que reproduz o relato, e só depois corrige a causa no `usar_doce_raro`. O teste confirma a recusa e o nível depois dela, como no exercício 4. Com o erro, o teste falha; depois da correção, os testes do `test_treino.py` passam todos. Num comentário junto do teste, escreve a mensagem com que ele falhou, e explica porque é que essa mensagem mostra que o teste reproduz o relato.

Rever: [Um teste antes da correção](../05-testes-com-pytest.md#um-teste-antes-da-correção) e [Testar uma recusa: pytest.raises](../05-testes-com-pytest.md#testar-uma-recusa-pytestraises).

<details>
<summary>Pista</summary>

Para encontrares a causa, faz a conta da condição do `if` do `usar_doce_raro` com o nível do Pikachu do relato. Dá `True` ou `False`?

</details>

## Desafios

### Desafio 1: O doce raro longe do nível 100

Acrescenta ao `test_treino.py` um teste do `usar_doce_raro` com um caso normal, longe do nível 100, que confirme as duas coisas que a docstring do método promete. O teste tem de falhar com um `usar_doce_raro` que comece o nível novo sem experiência. Para o confirmares, acrescenta esta linha ao fim do método:

```python
        self.experiencia = 0
```

Confirma e, depois, repõe o `treino.py` como estava.

Rever: [Um teste tem de distinguir o certo do errado](../05-testes-com-pytest.md#um-teste-tem-de-distinguir-o-certo-do-errado).

### Desafio 2: Os seis testes do colega

Um colega diz que os testes dele são ótimos, porque são seis e passam todos. Guarda-os no ficheiro `test_colega.py`:

```python
# test_colega.py: os seis testes do colega.
from treino import PokemonEmTreino


def test_dez_pontos():
    """Dez pontos ficam guardados."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(10)
    assert eevee.experiencia == 10


def test_vinte_pontos():
    """Vinte pontos ficam guardados."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(20)
    assert eevee.experiencia == 20


def test_trinta_pontos():
    """Trinta pontos ficam guardados."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(30)
    assert eevee.experiencia == 30


def test_quarenta_pontos():
    """Quarenta pontos ficam guardados."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(40)
    assert eevee.experiencia == 40


def test_cinquenta_pontos_nao_sobem():
    """Cinquenta pontos não sobem de nível."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(50)
    assert eevee.nivel == 1


def test_sessenta_pontos_nao_sobem():
    """Sessenta pontos não sobem de nível."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(60)
    assert eevee.nivel == 1
```

Mostra-lhe que seis testes a passar não querem dizer que o código está certo. Escreve uma versão errada do `ganhar_experiencia`, diferente das versões desta ficha, que passe nos seis testes do colega e não cumpra a regra do treino. Os testes do colega nunca fazem correr o `while`, a linha do nível 100 nem a recusa. Escreve os testes que faltam para fazer correr essas linhas, com o menor número de testes que conseguires. Esses testes têm também de apanhar a tua versão errada. Explica a escolha num comentário junto deles. Depois, repõe o `treino.py` como estava.

Rever: [Um teste tem de distinguir o certo do errado](../05-testes-com-pytest.md#um-teste-tem-de-distinguir-o-certo-do-errado).

<details>
<summary>Pista</summary>

Um só teste pode fazer correr mais do que uma dessas linhas. Escolhe o nível de partida e os pontos de cada teste a pensar nas linhas que ele faz correr e na tua versão errada.

</details>

### Desafio 3: A soma antes da verificação

Um colega mudou a ordem do `ganhar_experiencia`: soma os pontos à experiência e só depois verifica se são positivos. As três linhas a seguir à docstring ficam assim, e o resto não muda:

```python
        self.experiencia = self.experiencia + pontos
        if pontos <= 0:
            raise ValueError(f"{self.nome} só pode ganhar pontos positivos, e recebeu {pontos}.")
```

Descobre, sem executar, que testes do `test_treino.py` falham com esta versão. Confirma, e explica num comentário cada previsão em que te enganaste. Num comentário no fim do `test_treino.py`, explica também porque é que o exercício 4 pede os dois casos de recusa, o 0 e o -10, e não só um. Depois, repõe o `treino.py` como estava.

Rever: [Depois da recusa, o estado](../05-testes-com-pytest.md#depois-da-recusa-o-estado).

<details>
<summary>Pista</summary>

O 0 e o -10 passam pela mesma linha do `if`. Que engano nessa linha só o 0 apanhava?

</details>

### Desafio 4: Os testes antes do método

Até aqui, escreveste os testes para código que já existia. O `PokemonEmTreino` vai ter um método novo, `pontos_para_o_proximo_nivel`, sem parâmetros, com esta docstring: "Devolve quantos pontos faltam para o próximo nível. No nível 100, não há próximo nível, e devolve 0."

Num ficheiro novo, `test_proximo_nivel.py`, escreve os testes do método a partir da docstring: um caso normal e as fronteiras. Os testes vêm antes do método, e por isso começam por falhar. Num comentário no `test_proximo_nivel.py`, escreve a mensagem com que falham, e explica-a. Depois escreve o método no `treino.py`, até os testes passarem, sem partir os do `test_treino.py`.

Rever: [Um teste antes da correção](../05-testes-com-pytest.md#um-teste-antes-da-correção).

<details>
<summary>Pista</summary>

Um método que só faz uma conta passa em todos os teus testes? Pensa num Pokémon que já não tem próximo nível.

</details>

## Critérios de conclusão

- O `test_previsao.py` passa, e cada teste que falhava tem junto a decisão de onde estava o erro, justificada com a regra do treino.
- O `test_treino.py` tem os testes dos exercícios 2 a 5 e 7, com as três partes, nomes que dizem o comportamento e docstrings, e passam todos com o `usar_doce_raro` corrigido.
- Os dois testes de recusa falham com o `ganhar_experiencia` que apaga os pontos guardados.
- Cada versão do exercício 5 faz falhar pelo menos um teste, e o comentário sobre as versões diz o que cada uma faz de errado e que testes a apanharam.
- O `test_fixture.py` usa uma fixture nos testes que repetiam a preparação, os quatro testes passam, e um comentário explica a escolha.
- O teste do exercício 7 tem num comentário a mensagem com que falhou antes da correção.

![Rodapé](../../imagens/rodape.png)
