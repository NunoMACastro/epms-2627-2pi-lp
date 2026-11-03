![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Testes de comportamento com pytest

Ficha do tema Testes de comportamento com pytest, do módulo 10794, Programação avançada com Python. Praticas escrever testes com as três partes e escolher casos normais, de fronteira e de erro que distinguem o código certo do errado. Praticas também usar uma fixture quando ela poupa repetição, e escrever o teste de um defeito antes de o corrigir. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](../05-testes-com-pytest.md) e o [laboratório](../laboratorios/05-testes-com-pytest-laboratorio.md). Cada exercício diz, em "Treina", a secção do guia de que precisa.

## Como trabalhar

Os exercícios de 1 a 7 são obrigatórios e estão em dois grupos. Escrever e correr testes são os exercícios 1 a 4. Escolher e organizar os testes são os exercícios 5 a 7. Faz os exercícios pela ordem, porque o exercício 5 usa os testes que escreveste nos exercícios 2 a 4. O desafio opcional e "Para ires mais longe", no fim, são para quem acabar cedo. As pistas estão em "Apoio", depois dos exercícios: tenta cada exercício antes de as ler.

Cada exercício treina uma coisa só, e o enunciado diz qual é. O primeiro exercício de cada grupo é o mais próximo do guia, e os seguintes pedem-te uma decisão pequena que o guia não tomou por ti.

Precisas do computador com o Python 3, o VS Code e o pytest, que o laboratório te ensinou a confirmar e a instalar. Cria uma pasta para esta ficha, `treino-com-testes`, e guarda lá o `treino.py` do cenário e os teus ficheiros de testes. Corre os testes nessa pasta, com `python3 -m pytest`, ou com o nome do ficheiro a seguir, para correr só esse.

As respostas escritas vão para comentários, com `#`, no ficheiro de testes do exercício, junto do teste a que dizem respeito ou no fim do ficheiro. Escreve-as em frases completas, com as tuas palavras. Quando um exercício pedir uma previsão, prevê antes de executar: é a previsão, e não a execução, que mostra o que percebeste. Entrega os ficheiros como o professor indicar.

## O cenário

Um Pokémon em treino sobe de nível com a experiência: cada 100 pontos sobem um nível, até ao nível 100. Os exercícios testam o ficheiro `treino.py`, que tem a classe `PokemonEmTreino`. Cria-o na pasta `treino-com-testes`, com este conteúdo:

```python
"""O treino de um Pokémon, para a ficha de exercícios do tema 05.

Cada 100 pontos de experiência sobem um nível, até ao nível 100. Os pontos
que sobram ficam guardados para o nível seguinte. Um doce raro sobe um nível
de uma vez, sem mexer na experiência.

O método usar_doce_raro tem um defeito de propósito, que o exercício 7 da
ficha pede para encontrar e corrigir.
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

O construtor tem um valor por omissão: `PokemonEmTreino("Eevee")` cria um Eevee no nível 1, e `PokemonEmTreino("Pikachu", 99)` cria um Pikachu no nível 99. As regras do treino são as das docstrings, e é delas que tiras os resultados esperados dos teus testes.

## Escrever e correr testes

### Exercício 1: Prever o resultado do pytest

Treina: ler o que o pytest mostra quando um teste falha (guia, [Um teste que falha](../05-testes-com-pytest.md#um-teste-que-falha)).

Um colega escreveu estes quatro testes, no ficheiro `test_previsao.py`:

```python
# test_previsao.py: quatro testes para prever antes de correr.
from treino import PokemonEmTreino


def test_trinta_pontos_ficam_na_experiencia():
    """Trinta pontos não chegam para subir e ficam guardados."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(30)
    assert eevee.experiencia == 30


def test_trinta_pontos_nao_sobem_de_nivel():
    """Trinta pontos não chegam para subir de nível."""
    eevee = PokemonEmTreino("Eevee")
    eevee.ganhar_experiencia(30)
    assert eevee.nivel == 2


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
```

**a)** Sem executar, prevê que testes passam e que testes falham, e a última linha que o pytest vai mostrar. Para cada teste que falha, prevê também a linha que começa por `E       assert`, com os dois valores. Para confirmares, guarda o ficheiro e corre `python3 -m pytest test_previsao.py`.

**b)** Em cada teste que falha, o erro está no teste ou no código? Justifica com a regra do treino, num comentário junto desse teste.

### Exercício 2: Os primeiros testes do treino

Treina: escrever testes com as três partes, preparar, fazer e confirmar (guia, [Preparar, fazer, confirmar](../05-testes-com-pytest.md#preparar-fazer-confirmar)).

Cria o ficheiro `test_treino.py` e escreve nele dois testes para o `ganhar_experiencia`:

- um Vulpix no nível 5 ganha 40 pontos;
- um Eevee, no nível 1, ganha 250 pontos de uma vez.

Cada teste tem as três partes, um nome que diz o comportamento e uma docstring. Os resultados esperados tiras tu da regra do treino, e não do que o código dá. Decide também o que cada teste tem de confirmar no fim.

No fim, `python3 -m pytest test_treino.py` mostra os dois testes a passar.

### Exercício 3: As fronteiras do treino

Treina: escolher casos de fronteira (guia, [Os casos de fronteira](../05-testes-com-pytest.md#os-casos-de-fronteira-o-ko-e-os-limites-da-vida)).

O treino tem duas regras com fronteiras: um nível sobe aos 100 pontos, e o nível não passa de 100. Acrescenta ao `test_treino.py` pelo menos quatro testes de fronteira do `ganhar_experiencia`, dois para cada regra. Na docstring de cada teste, diz que fronteira ele testa.

No fim, os testes passam todos.

### Exercício 4: Uma recusa, e o que fica depois dela

Treina: confirmar uma exceção com `pytest.raises` e o estado depois da recusa (guia, [Testar uma recusa](../05-testes-com-pytest.md#testar-uma-recusa-pytestraises) e [Depois da recusa, o estado](../05-testes-com-pytest.md#depois-da-recusa-o-estado)).

A docstring do `ganhar_experiencia` diz que os pontos têm de ser mais do que zero, e que o método recusa os outros com `ValueError`, sem mudar nada. Acrescenta ao `test_treino.py` dois testes de erro: um com 0 pontos e outro com -10. Cada teste confirma a exceção e confirma que o nível e a experiência ficaram como estavam.

Decide com que Pokémon preparas cada teste, e explica a escolha na docstring. No fim, os testes passam todos.

## Escolher e organizar os testes

### Exercício 5: Três versões erradas

Treina: confirmar que os testes distinguem o código certo do errado (guia, [Um teste tem de distinguir o certo do errado](../05-testes-com-pytest.md#um-teste-tem-de-distinguir-o-certo-do-errado) e o exemplo guiado).

Três colegas escreveram o `ganhar_experiencia` de outra forma, e cada um enganou-se numa coisa. As três versões têm erros de propósito. Esta é a parte do corpo do método que muda em cada uma, a partir do `while`.

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

**a)** Para cada versão, diz numa frase o que ela faz de errado, comparada com a regra do treino. Responde num comentário no fim do `test_treino.py`.

**b)** Os teus testes dos exercícios 2 a 4 têm de apanhar as três versões. Com cada uma delas no `treino.py`, no lugar das linhas do `while` em diante, pelo menos um teste do `test_treino.py` falha. Antes de experimentares, prevê quais. Se alguma versão passar em todos os teus testes, acrescenta ao `test_treino.py` o teste que a apanha: falha com essa versão e passa com o código do cenário. No comentário da alínea a), junta a cada versão os testes que a apanharam. No fim, o `treino.py` fica como no cenário.

### Exercício 6: Uma fixture, ou não

Treina: usar uma fixture só quando poupa repetição que importa (guia, [Uma fixture prepara o que vários testes repetem](../05-testes-com-pytest.md#uma-fixture-prepara-o-que-vários-testes-repetem)).

Guarda este ficheiro, `test_fixture.py`, na pasta da ficha:

```python
# test_fixture.py: quatro testes, três deles com a mesma preparação.
from treino import PokemonEmTreino


def test_mais_30_pontos_ficam_guardados():
    """Um Pidgey no nível 20, com 50 pontos, fica com 80 se ganhar mais 30."""
    pidgey = PokemonEmTreino("Pidgey", 20)
    pidgey.ganhar_experiencia(50)

    pidgey.ganhar_experiencia(30)

    assert pidgey.experiencia == 80


def test_mais_10_pontos_nao_sobem_de_nivel():
    """O mesmo Pidgey continua no nível 20 se ganhar mais 10."""
    pidgey = PokemonEmTreino("Pidgey", 20)
    pidgey.ganhar_experiencia(50)

    pidgey.ganhar_experiencia(10)

    assert pidgey.nivel == 20


def test_mais_70_pontos_sobem_um_nivel():
    """O mesmo Pidgey sobe ao nível 21 se ganhar mais 70."""
    pidgey = PokemonEmTreino("Pidgey", 20)
    pidgey.ganhar_experiencia(50)

    pidgey.ganhar_experiencia(70)

    assert pidgey.nivel == 21


def test_eevee_comeca_no_nivel_um():
    """Sem nível indicado, um Pokémon começa no nível 1."""
    eevee = PokemonEmTreino("Eevee")

    assert eevee.nivel == 1
```

**a)** Reescreve o ficheiro com uma fixture para a preparação que se repete. Decide que testes a pedem e que nome lhe dás. Os testes têm de continuar a confirmar exatamente o mesmo, e os quatro passam com `python3 -m pytest test_fixture.py`, antes e depois da mudança.

**b)** Num comentário no fim do `test_fixture.py`, explica por que razão um dos testes não pede a fixture. Explica também porque é que os três testes que a pedem não se estragam uns aos outros, embora todos deem pontos ao Pidgey.

### Exercício 7: O teste antes da correção

Treina: escrever o teste de um defeito antes de o corrigir (guia, [Um teste antes da correção](../05-testes-com-pytest.md#um-teste-antes-da-correção)).

Chegou um relato: "Um Pikachu no nível 100 comeu um doce raro e ficou no nível 101." O defeito está no `usar_doce_raro` do `treino.py`.

**a)** Acrescenta ao `test_treino.py` o teste que reproduz o relato, e corrige a causa no `usar_doce_raro`. O resultado esperado tira-se da docstring do `usar_doce_raro`. O teste escreve-se antes da correção: com o defeito, falha, e depois da correção os testes do `test_treino.py` passam todos. Num comentário junto do teste, escreve a mensagem com que ele falhou, e explica porque é que essa mensagem mostra que o teste reproduz o relato.

**b)** O `usar_doce_raro` também tem de funcionar fora do nível 100. Escreve mais um teste, para um caso normal, que confirme as duas coisas que a docstring promete.

## Apoio

- Exercício 1: para cada teste, faz a conta pela regra, com o nível e a experiência antes e depois. Num teste que falha, o pytest mostra o valor que o código deu à esquerda, e o valor que o teste esperava à direita.
- Exercício 2: antes de escreveres os `assert`, pensa em tudo o que o `ganhar_experiencia` pode mudar num Pokémon.
- Exercício 3: numa fronteira, testa o último valor que ainda não muda nada e o primeiro que já muda. Para o nível máximo, pergunta-te o que faz a regra mudar: os pontos, o nível de partida, ou os dois. Ajuda decidir, para cada teste, o nível de partida, os pontos, o nível esperado e a experiência esperada, antes de o escreveres.
- Exercício 4: o `pytest.raises` confirma a exceção. O que fica no Pokémon confirmas tu, com `assert`, depois do bloco. Imagina um erro que mexesse na experiência antes de lançar a exceção: o teu teste dava por ele?
- Exercício 5: para cada versão, procura o nível de partida e os pontos em que a versão errada e a do cenário dão resultados diferentes. Começa pelas fronteiras das duas regras.
- Exercício 6: o nome da fixture diz o que ela prepara, e não como. Para a alínea b), pergunta-te quantas vezes o pytest chama a fixture, se três testes a pedem.
- Exercício 7: a docstring diz duas coisas para o nível 100. Uma confirma-se com `pytest.raises`, e a outra com um `assert`.

## Desafio opcional

Um colega diz que os testes dele são ótimos, porque são seis e passam todos. Guarda-os no ficheiro `test_colega.py`:

```python
# test_colega.py: os seis testes do colega, todos com casos normais.
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

Mostra-lhe que seis testes a passar não querem dizer que o código está certo. Escreve uma versão errada do `ganhar_experiencia`, diferente das três do exercício 5, que passe nos seis testes do colega e não cumpra a regra do treino. Depois escreve os testes que faltam ao colega para a apanhar, com o menor número de testes que conseguires, e explica a escolha num comentário junto deles. No fim, volta a pôr o `treino.py` como estava.

## Para ires mais longe

Até aqui, escreveste os testes para código que já existia. Também se pode fazer ao contrário: primeiro os testes, a partir do que o método deve fazer, e só depois o método.

O `PokemonEmTreino` vai ter um método novo, `pontos_para_o_proximo_nivel`, sem parâmetros, com esta docstring: "Devolve quantos pontos faltam para o próximo nível. No nível 100, não há próximo nível, e devolve 0."

Num ficheiro novo, `test_proximo_nivel.py`, escreve pelo menos três testes para o método, a partir da docstring: um caso normal e as fronteiras. Os testes vêm antes do método, e por isso começam por falhar. Num comentário no `test_proximo_nivel.py`, escreve a mensagem com que falham, e explica-a. Depois escreve o método no `treino.py`, até os testes passarem, sem partir os outros ficheiros de testes.

## Critérios de conclusão

Concluíste a ficha quando:

- o `test_previsao.py` tem, junto de cada teste que falha, a justificação de onde está o erro, no teste ou no código;
- o `test_treino.py` tem os testes dos exercícios 2 a 4, com as três partes, nomes que dizem o comportamento e docstrings, e passam todos com o código do cenário;
- cada uma das três versões do exercício 5 faz falhar pelo menos um dos teus testes;
- o `test_fixture.py` usa uma fixture nos testes que repetiam a preparação, e os quatro testes passam;
- o teste do exercício 7 tem num comentário a mensagem com que falhou antes da correção, passa depois dela, e o `usar_doce_raro` está corrigido no `treino.py`.

## Autoavaliação

1. Em que exercício precisaste de mais tempo, e o que fizeste para o resolver?
2. Consegues explicar, por palavras tuas, porque é que um teste que passa com o código certo e com o código errado não serve para nada?
3. Num programa teu, que comportamento escolhias para escrever o primeiro teste de fronteira, e porquê?

![Rodapé](../../imagens/rodape.png)
