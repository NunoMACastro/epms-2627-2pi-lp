![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: exceções, depuração e registo no ginásio

## O que vais fazer

Vais pegar no ginásio Pokémon do tema 03 e dar-lhe três coisas novas, uma de cada vez: exceções próprias para as recusas, a investigação de dois erros com o depurador do VS Code, e um registo do que o ginásio faz. No fim, o teu ginásio fica igual à versão 04 do exemplo, e numa parte autónoma acrescentas-lhe uma exceção tua.

Como nos laboratórios anteriores, antes de cada teste vais escrever o que achas que ele vai mostrar, e só depois executar.

Este laboratório não repete a teoria. Tem o [guia](04-excecoes-depuracao-e-logging.md) aberto ao lado: cada parte diz a secção de que precisas.

## O que precisas de saber antes

Do guia, precisas da parte 1 para as partes 2 a 4 deste laboratório, da parte 2 para as partes 5 e 6, e da parte 3 para as partes 7 e 8. Do tema 03, precisas do ginásio Pokémon e do `com_equipa`.

## Material

O computador com o Python 3 e o VS Code, com a extensão Python da Microsoft, e o guia aberto ao lado. Uma folha de papel, ou um ficheiro de texto, para as previsões e as respostas.

## Parte 1: Preparar a pasta (5 min)

1. Cria uma pasta nova, chamada `ginasio-com-erros`, e abre-a no VS Code.
2. Copia para ela os três ficheiros da pasta [03-objetos-e-composicao dos exemplos](../exemplos/python-avancado/pokemon/03-objetos-e-composicao/): o `pokemon.py`, o `ginasio.py` e o `anunciadores.py`. Copia os dos exemplos, e não os teus do laboratório anterior, para os testes deste laboratório darem exatamente as saídas indicadas.
3. Executa `python3 ginasio.py`. A última linha tem de ser:

```text
Ash continua com 2 Pokémon; Misty continua com 1.
```

Ao longo do laboratório, vais mudar o `ginasio.py` e criar ficheiros novos nesta pasta. Os testes ficam em ficheiros à parte, e não no programa principal do `ginasio.py`.

## Parte 2: As exceções do ginásio (10 min)

Precisas da secção [As exceções do ginásio](04-excecoes-depuracao-e-logging.md#as-exceções-do-ginásio) do guia.

1. Cria o ficheiro `erros.py`, com as três classes do guia: `ErroDoGinasio`, filha de `Exception`, e `EquipaCheia` e `SemPokemonComVida`, filhas de `ErroDoGinasio`. Escreve-as tu, com as docstrings.
2. Cria o ficheiro `teste_erros.py`, com as linhas abaixo. O `isinstance` está explicado no guia, no início da secção [Uma exceção própria](04-excecoes-depuracao-e-logging.md#uma-exceção-própria): pergunta se um objeto é de uma classe, ou de uma classe-filha dela, e devolve `True` ou `False`.

```python
from erros import EquipaCheia, ErroDoGinasio, SemPokemonComVida

print(isinstance(EquipaCheia("teste"), ErroDoGinasio), isinstance(SemPokemonComVida("teste"), ErroDoGinasio))
print(isinstance(ErroDoGinasio("teste"), Exception))
erro = EquipaCheia("A equipa está cheia.")
print(erro)
```

3. Antes de executar, escreve a tua previsão das três linhas.
4. Executa `python3 teste_erros.py`. A saída deve ser:

```text
True True
True
A equipa está cheia.
```

As duas primeiras linhas confirmam a família: as duas exceções do ginásio são `ErroDoGinasio`, e um `ErroDoGinasio` é uma exceção. A terceira mostra que um `print` de uma exceção escreve a sua mensagem.

## Parte 3: A equipa cheia (15 min)

Precisas das secções [raise: uma recusa que não se pode ignorar](04-excecoes-depuracao-e-logging.md#raise-uma-recusa-que-não-se-pode-ignorar) e [As exceções do ginásio](04-excecoes-depuracao-e-logging.md#as-exceções-do-ginásio).

1. No início do `ginasio.py`, a seguir à importação dos Pokémon, importa as duas exceções e cria a constante do tamanho da equipa:

```python
from erros import EquipaCheia, SemPokemonComVida

TAMANHO_MAXIMO_DA_EQUIPA = 6
```

2. Muda o `capturar` do `Treinador`, como no guia: se a equipa já tem `TAMANHO_MAXIMO_DA_EQUIPA` Pokémon, lança `EquipaCheia`, com a mensagem do guia; se não, junta o Pokémon à equipa. Atualiza também a docstring.
3. Cria o ficheiro `capturas.py`:

```python
from erros import EquipaCheia
from pokemon import Pokemon
from ginasio import Treinador

brock = Treinador("Brock")
nomes = ["Geodude", "Onix", "Vulpix", "Zubat", "Sandshrew", "Rhyhorn", "Kabuto", "Omanyte"]
for nome in nomes:
    try:
        brock.capturar(Pokemon(nome, "Pedra", 50, 20))
    except EquipaCheia as erro:
        print(f"Recusado: {erro}")
    else:
        print(f"{nome} capturado.")
print(len(brock.equipa))
```

4. Antes de executar, escreve quantas linhas "capturado" vão aparecer, quais os Pokémon recusados, e o número da última linha.
5. Executa e compara. A saída deve ser:

```text
Geodude capturado.
Onix capturado.
Vulpix capturado.
Zubat capturado.
Sandshrew capturado.
Rhyhorn capturado.
Recusado: Brock já tem 6 Pokémon e não pode capturar Kabuto.
Recusado: Brock já tem 6 Pokémon e não pode capturar Omanyte.
6
```

Responde por escrito:

- **a)** Porque é que a última linha diz 6, e não 8, se o ciclo tentou oito capturas?
- **b)** Troca, no `capturar`, a ordem do `if` e do `append`, de forma que o `append` venha primeiro e o `if` com o `raise` depois. Antes de executar, prevê o que muda na saída. Executa, compara e volta a pôr a ordem certa. O que mostra esta experiência sobre o sítio do `raise`?

## Parte 4: O combate recusado (15 min)

Precisas da secção [As exceções do ginásio](04-excecoes-depuracao-e-logging.md#as-exceções-do-ginásio) e da secção [finally: o que corre sempre](04-excecoes-depuracao-e-logging.md#finally-o-que-corre-sempre).

1. Muda o início do `combater` do `Ginasio`, como no guia, sem as linhas com `logger`, que ficam para a parte 7. Tira o `print` com "Não há combate" e o `return`, e põe no lugar deles um `raise SemPokemonComVida`, com a mensagem do guia. Põe também a verificação antes da linha que junta o desafiante à lista de desafiantes, como no guia.
2. Cria o ficheiro `combates.py`. O Brock entra com um Geodude que já não tem vida nenhuma:

```python
from erros import ErroDoGinasio
from pokemon import Pokemon, PokemonAgua, PokemonFogo
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
gary = Treinador.com_equipa("Gary", [PokemonFogo("Vulpix", 30, 20)])
brock = Treinador.com_equipa("Brock", [Pokemon("Geodude", "Pedra", 0, 10)])
cerulean = Ginasio("Cerulean", misty)
for desafiante in [gary, brock, gary]:
    try:
        cerulean.combater(desafiante)
    except ErroDoGinasio as erro:
        print(f"{desafiante.nome} recusado: {erro}")
    finally:
        print(f"Desafiantes: {len(cerulean.desafiantes)}, combates: {len(cerulean.combates)}")
```

3. Antes de executar, prevê o que acontece a cada um dos três desafios, e as três linhas com os desafiantes e os combates.
4. Executa e compara. Depois do primeiro combate, que o Gary perde, a saída deve acabar assim:

```text
Desafiantes: 1, combates: 1
Brock recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
Desafiantes: 1, combates: 1
Gary recusado: Não há combate em Cerulean: um dos treinadores não tem Pokémon com vida.
Desafiantes: 1, combates: 1
```

Responde por escrito:

- **a)** O Brock foi recusado e não entrou na lista de desafiantes. Que linha do teu `combater` garante isso?
- **b)** Na versão do tema 03, o desafiante entrava na lista logo no início do `combater`. Com essa ordem, o que diria a linha dos desafiantes depois do Brock? Porque é que isso estaria errado?
- **c)** A linha dos desafiantes e dos combates aparece três vezes, embora só tenha havido um combate. Porquê?

## Parte 5: Investigar um erro de cálculo com o depurador (20 min)

Precisas das secções [O depurador do VS Code](04-excecoes-depuracao-e-logging.md#o-depurador-do-vs-code) e [Exemplo guiado: o dano a dobrar](04-excecoes-depuracao-e-logging.md#exemplo-guiado-o-dano-a-dobrar).

O ficheiro seguinte tem uma cópia da classe `PokemonAgua`, com um erro. Um Squirtle, de água, ataca um Charmander, de fogo, e a água devia tirar o dobro ao fogo.

1. Cria o ficheiro `investigar.py`:

```python
from pokemon import Pokemon, PokemonFogo


class PokemonAgua(Pokemon):
    """Uma cópia da PokemonAgua do pokemon.py, com um erro para investigar."""

    def __init__(self, nome, vida, ataque):
        """Cria um Pokémon de água com nome, vida e ataque."""
        super().__init__(nome, "Água", vida, ataque)

    def calcular_dano(self, alvo):
        """Contra Fogo, a água tira o dobro."""
        dano = super().calcular_dano(alvo)
        if alvo.tipo == "fogo":
            print("É super eficaz!")
            dano = dano * 2
        return dano


squirtle = PokemonAgua("Squirtle", 100, 30)
charmander = PokemonFogo("Charmander", 90, 40)
squirtle.atacar(charmander)
```

2. Executa-o normalmente e regista o sintoma: quanto devia tirar o ataque, quanto tirou, e o que falta na saída.
3. Antes de abrires o depurador, escreve a tua hipótese, como no passo 2 do exemplo guiado: o que achas que está a acontecer, em que linha, e o que esperas ver no depurador se tiveres razão.
4. Põe um ponto de paragem na linha `dano = super().calcular_dano(alvo)`, e executa com o depurador (F5). Quando o programa parar, abre o `alvo` no painel das variáveis e regista o valor do `tipo`.
5. No painel Vigiar, acrescenta duas expressões: `alvo.tipo` e `alvo.tipo == "fogo"`. Regista o que o VS Code mostra para cada uma.
6. Avança com F10, linha a linha, até ao `return`. Regista, para cada passo, a linha marcada a amarelo e o valor do `dano`, numa tabela como a do passo 5 do exemplo guiado.
7. Para a depuração (Shift+F5), corrige a causa, e volta a executar o programa. Quando estiver certo, a saída é:

```text
É super eficaz!
Squirtle ataca Charmander e tira 60 de vida.
Charmander tem 30/150 de vida.
```

Responde por escrito:

- **a)** A tua hipótese do passo 3 estava certa? Se não estava, o que é que o depurador te mostrou que não esperavas?
- **b)** Qual era a causa, e porque é que o Python não deu nenhuma mensagem de erro?

## Parte 6: Um erro que rebenta longe da causa (15 min)

Precisas das secções [Ler um traceback com três andares](04-excecoes-depuracao-e-logging.md#ler-um-traceback-com-três-andares) e [A pilha de chamadas no depurador](04-excecoes-depuracao-e-logging.md#a-pilha-de-chamadas-no-depurador).

1. Cria o ficheiro `pilha.py`:

```python
from pokemon import PokemonAgua, PokemonFogo
from ginasio import Ginasio, Lider, Treinador

misty = Lider.com_equipa("Misty", [PokemonAgua("Starmie", 90, 35)])
ash = Treinador.com_equipa("Ash", [PokemonFogo("Charmander", 30, 40), "Squirtle"])
cerulean = Ginasio("Cerulean", misty)
cerulean.combater(ash)
cerulean.combater(ash)
```

2. Executa-o normalmente. O primeiro combate acontece, o Charmander perde, e o programa para com um traceback que acaba assim:

```text
AttributeError: 'str' object has no attribute 'vida'
```

Os números das linhas do `ginasio.py` no traceback dependem do teu ficheiro.

3. Lê o traceback e responde, antes de abrires o depurador: em que linha do `pilha.py` começou o caminho até ao erro? Por que funções passou? Em que linha do `ginasio.py` rebentou?
4. Executa com o depurador (F5), sem nenhum ponto de paragem. O programa para na linha onde a exceção rebentou. No painel da pilha de chamadas, clica em cada andar, e regista, para o andar do `combater`, o que está na `equipa` do `desafiante`.
5. Encontra a linha onde está a causa e corrige-a: o Ash devia ter um Squirtle a sério, `PokemonAgua("Squirtle", 100, 30)`. Executa outra vez. O segundo combate passa a acontecer, e o Ash ganha-o:

```text
=== Ash desafia Misty no ginásio de Cerulean ===
Squirtle ataca Starmie e tira 30 de vida.
Starmie tem 20/150 de vida.
Starmie ataca Squirtle e tira 35 de vida.
Squirtle tem 65/150 de vida.
Squirtle ataca Starmie e tira 30 de vida.
Starmie está KO (0/150).
```

Responde por escrito:

- **a)** O erro está na linha 5 do `pilha.py`, e o primeiro combate correu bem. Porque é que só rebentou no segundo?
- **b)** Um colega propõe corrigir o `escolher_pokemon` para saltar tudo o que não tenha vida. Porque é que isso esconde o erro, em vez de o corrigir?

## Parte 7: O registo do ginásio (15 min)

Precisas das secções [O registo do ginásio](04-excecoes-depuracao-e-logging.md#o-registo-do-ginásio), [Quem configura é o programa](04-excecoes-depuracao-e-logging.md#quem-configura-é-o-programa) e [Mudar o nível sem mudar o código](04-excecoes-depuracao-e-logging.md#mudar-o-nível-sem-mudar-o-código).

1. No início do `ginasio.py`, importa o `logging` e cria o logger do módulo, como no guia: `import logging` na primeira linha de importações, e `logger = logging.getLogger(__name__)` a seguir à constante do tamanho da equipa.
2. No `combater`, acrescenta as quatro mensagens do guia: o `warning` antes do `raise`, o `info` e o `debug` do início do combate, e o `info` do fim, depois de criar o registo.
3. Cria o ficheiro `registo.py`:

```python
import logging

from erros import ErroDoGinasio
from pokemon import PokemonAgua, PokemonPlanta
from ginasio import Ginasio, Lider, Treinador

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

erika = Lider.com_equipa("Erika", [PokemonPlanta("Tangela", 50, 20, 10)])
misty = Treinador.com_equipa("Misty", [PokemonAgua("Psyduck", 60, 20)])
celadon = Ginasio("Celadon", erika)
for tentativa in range(2):
    try:
        celadon.combater(misty)
    except ErroDoGinasio as erro:
        print(f"Recusado: {erro}")
```

4. Antes de executar, prevê que linhas do registo vão aparecer, com que nível, e onde ficam em relação às linhas do combate.
5. Executa e compara. As linhas do registo devem ser estas três, a primeira antes do combate e as outras duas depois dele:

```text
[INFO] ginasio: Combate em Celadon: Misty com Psyduck contra Erika com Tangela.
[INFO] ginasio: Fim do combate em Celadon: venceu Erika.
[WARNING] ginasio: Combate recusado em Celadon: Misty contra Erika, sem Pokémon com vida.
```

6. Muda o nível para `logging.DEBUG` e executa outra vez. Logo a seguir à primeira linha do registo tem de aparecer:

```text
[DEBUG] ginasio: Vida no início: Psyduck 60, Tangela 50.
```

7. Muda o nível para `logging.WARNING` e executa. Das linhas do registo, só fica a do aviso.

Responde por escrito: para ver as mensagens de `DEBUG`, mudaste uma palavra no `registo.py` e nenhuma no `ginasio.py`. Porque é que isso é uma vantagem em relação a acrescentar e apagar `print`?

## Parte 8: O registo num ficheiro (10 min)

Precisas da secção [Guardar o registo num ficheiro](04-excecoes-depuracao-e-logging.md#guardar-o-registo-num-ficheiro).

1. No `registo.py`, troca a linha do `basicConfig` por esta, que manda o registo para um ficheiro e acrescenta a hora de cada mensagem:

```python
logging.basicConfig(filename="ginasio.log", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
```

2. Executa o `registo.py` duas vezes seguidas.
3. Abre o ficheiro `ginasio.log`, que apareceu na pasta. Antes de o abrires, prevê quantas linhas tem.

Responde por escrito: quantas linhas tem o ficheiro, e porquê? O que aparece no ecrã, e o que deixou de aparecer?

## Parte autónoma: um Pokémon repetido (15 min)

Esta parte fazes sozinho. Não está no guia.

Neste momento, nada impede que o mesmo Pokémon seja capturado duas vezes pelo mesmo treinador: o mesmo objeto fica duas vezes na lista da equipa. Acrescenta ao ginásio uma exceção nova para este caso:

- no `erros.py`, uma classe `PokemonRepetido`, filha de `ErroDoGinasio`;
- no `capturar`, se o Pokémon já está na equipa do treinador, o método regista um aviso, com o nível `WARNING`, e lança `PokemonRepetido`, sem juntar nada à equipa.

A mensagem do aviso é "Ash tentou capturar outra vez o Charmander.", e a da exceção é "Ash já tem este Charmander na equipa.", com o nome do treinador e o do Pokémon.

Para testar, cria o ficheiro `repetido.py`:

```python
import logging

from erros import PokemonRepetido
from pokemon import PokemonFogo
from ginasio import Treinador

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s: %(message)s")

ash = Treinador("Ash")
charmander = PokemonFogo("Charmander", 90, 40)
ash.capturar(charmander)
try:
    ash.capturar(charmander)
except PokemonRepetido as erro:
    print(f"Recusado: {erro}")
ash.capturar(PokemonFogo("Charmander", 90, 40))
print(len(ash.equipa))
```

Quando estiver certo, o teste mostra:

```text
[WARNING] ginasio: Ash tentou capturar outra vez o Charmander.
Recusado: Ash já tem este Charmander na equipa.
2
```

Antes de escreveres o código, decide duas coisas. A primeira: o terceiro `capturar` junta um Charmander criado de novo, com os mesmos valores do primeiro, e tem de ser aceite. Que pergunta faz a verificação, "é o mesmo objeto?" ou "tem os mesmos valores?", e como se escreve? A segunda: um treinador com a equipa cheia tenta capturar um Pokémon que já tem. Qual das duas exceções deve ser lançada, e o que decide isso no teu código?

## Quando alguma coisa corre mal

**`ModuleNotFoundError: No module named 'erros'`.** O ficheiro `erros.py` não está na mesma pasta que o `ginasio.py`, ou tem outro nome. Confirma que se chama exatamente `erros.py`.

**`ImportError: cannot import name 'EquipaCheia' from 'erros'`.** O ficheiro foi encontrado, mas não tem uma classe com esse nome. Confirma a grafia, com as maiúsculas: `EquipaCheia`.

**`NameError: name 'EquipaCheia' is not defined`, quando se captura com a equipa cheia.** O `ginasio.py` usa a exceção, mas não a importou. Confirma a linha `from erros import EquipaCheia, SemPokemonComVida` no início do ficheiro. O erro só aparece quando o `raise` corre, e por isso o ficheiro parece estar bem até a equipa encher.

**`TypeError: exceptions must derive from BaseException`.** Uma das classes do `erros.py` não tem a classe-mãe entre parênteses. A `ErroDoGinasio` tem de ser filha de `Exception`, e as outras de `ErroDoGinasio`.

**O teste da parte 4 escreve "Não há combate: um dos treinadores não tem Pokémon com vida." sem o nome do desafiante.** O `combater` ainda tem o `print` e o `return` da versão anterior. Tira-os e põe o `raise` no lugar deles.

**Na parte 4, a linha dos desafiantes diz 2 depois do Brock.** A linha que junta o desafiante à lista está antes da verificação. Passa-a para depois do `raise`.

**O depurador não para no ponto de paragem.** Ou executaste sem o depurador, com o triângulo ou com Ctrl+F5, ou o ponto está numa linha que não corre. Usa o F5, e confirma que o ponto vermelho está na linha certa do ficheiro que estás a executar.

**O F5 pergunta que depurador usar e não aparece o de Python.** A extensão Python da Microsoft não está instalada, ou está desativada. Instala-a no painel das extensões do VS Code.

**As mensagens do registo não aparecem.** O `registo.py` não tem o `basicConfig`, ou tem o nível acima do das mensagens. Sem configuração, só aparecem as de `WARNING`.

**`--- Logging error ---`, com `not all arguments converted during string formatting`.** Uma mensagem do registo foi escrita como um `print`, com vírgulas. Escreve-a numa f-string.

**O `ginasio.log` não aparece.** O ficheiro é criado na pasta onde o terminal está, que pode não ser a do laboratório. Abre o terminal na pasta `ginasio-com-erros` e executa de lá.

## O que entregar

A pasta `ginasio-com-erros`, com o `erros.py` e o `ginasio.py` na versão final, incluindo a parte autónoma, e os ficheiros de teste: `teste_erros.py`, `capturas.py`, `combates.py`, `investigar.py` já corrigido, `pilha.py` já corrigido, `registo.py` e `repetido.py`. Entrega também as tuas previsões, a hipótese e a tabela da parte 5, e as respostas às perguntas das partes 3 a 8, escritas por ti, em papel ou num ficheiro de texto, conforme o professor indicar.

![Rodapé](../imagens/rodape.png)
