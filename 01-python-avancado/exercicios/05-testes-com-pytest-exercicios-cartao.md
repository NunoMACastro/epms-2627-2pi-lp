![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Testes de comportamento com pytest num cartão de transportes

Praticas, num programa pequeno e fora dos Pokémon, as exceções próprias e os testes com o pytest. Os exercícios 1 a 5 são obrigatórios: o primeiro cria o cartão, e cada um dos seguintes acrescenta-lhe uma regra. Trabalhas numa pasta nova, `cartao-de-transportes`, fora da pasta do repositório dos alunos, com dois ficheiros, `cartao.py` e `test_cartao.py`. Se fizeres a ficha num computador sem o pytest, como o de casa, instala-o primeiro, como no passo 4 de [Preparar o projeto](../laboratorios/05-testes-com-pytest-laboratorio.md#preparar-o-projeto), no laboratório. Para rever: o [guia do tema](../05-testes-com-pytest.md) e o [laboratório](../laboratorios/05-testes-com-pytest-laboratorio.md).

## O cenário

Um cartão de transportes, como o cartão do autocarro, é carregado com viagens. Cada cartão tem um número, como 1234, e as viagens que ainda tem, e começa sem viagens. Carregar junta viagens ao cartão, e validar, ao entrar no autocarro, gasta uma. Um cartão nunca fica com mais de 50 viagens.

## Exercício 1: O cartão e os primeiros testes

No `cartao.py`, escreve a classe `Cartao`, criada com o número do cartão, como `Cartao(1234)`, com os métodos `carregar(viagens)` e `validar()`, ainda sem recusas. No `test_cartao.py`, escreve um teste para cada caso:

- um cartão novo tem 0 viagens;
- carregar 10 e depois 5 deixa o cartão com 15;
- carregar 10 e validar uma vez deixa o cartão com 9.

Rever: [Um teste é uma função](../05-testes-com-pytest.md#um-teste-é-uma-função) e [Preparar, fazer, confirmar](../05-testes-com-pytest.md#preparar-fazer-confirmar).

<details>
<summary>Pista</summary>

No teste de carregar 10 e depois 5, o carregamento de 10 é a preparação, e o de 5 é a ação cujo resultado confirmas.

</details>

## Exercício 2: A primeira exceção própria

Um carregamento de 0 viagens ou menos é recusado com a exceção `CarregamentoInvalido`, uma classe tua, e o cartão fica com as viagens que tinha. A mensagem diz as viagens pedidas, como "Não se carregam -5 viagens.". Acrescenta ao `test_cartao.py` dois testes:

- num cartão com 4 viagens, carregar 0 é recusado, e ficam 4;
- num cartão com 4 viagens, carregar -5 é recusado, e ficam 4.

Rever: [Uma exceção própria herda de Exception](../04-excecoes-depuracao-e-logging.md#uma-exceção-própria-herda-de-exception), [Testar uma recusa: pytest.raises](../05-testes-com-pytest.md#testar-uma-recusa-pytestraises) e [Depois da recusa, o estado](../05-testes-com-pytest.md#depois-da-recusa-o-estado).

<details>
<summary>Pista</summary>

Onde tem de ficar a verificação: antes ou depois da linha que muda as viagens? Com a verificação depois da soma, qual dos dois testes falhava, e porquê só esse?

</details>

## Exercício 3: Uma segunda exceção

Validar num cartão sem viagens é recusado com a exceção `SemViagens`, e o cartão continua com 0. Acrescenta dois testes:

- num cartão com 1 viagem, validar ainda passa, e o cartão fica com 0;
- num cartão novo, validar é recusado, e o cartão continua com 0.

Rever: [Os casos de fronteira: o KO e os limites da vida](../05-testes-com-pytest.md#os-casos-de-fronteira-o-ko-e-os-limites-da-vida).

<details>
<summary>Pista</summary>

A última viagem é a fronteira. Que comparação deixa validar com 1 viagem e recusa com 0?

</details>

## Exercício 4: O limite das 50 viagens

Um carregamento que deixaria o cartão com mais de 50 viagens é recusado com a exceção `LimiteUltrapassado`, e nada muda. A mensagem diz quantas viagens ainda cabiam e quantas foram pedidas, como "Só cabem mais 6 viagens; pediste 10.". Acrescenta dois testes:

- num cartão com 45 viagens, carregar 5 é aceite, e o cartão fica com 50;
- num cartão com 45 viagens, carregar 6 é recusado, e ficam 45.

Rever: [Os casos de fronteira: o KO e os limites da vida](../05-testes-com-pytest.md#os-casos-de-fronteira-o-ko-e-os-limites-da-vida) e [Depois da recusa, o estado](../05-testes-com-pytest.md#depois-da-recusa-o-estado).

<details>
<summary>Pista</summary>

O número de viagens que ainda cabem muda de cartão para cartão. De onde vem, para um cartão qualquer?

</details>

## Exercício 5: Uma família de exceções

As três exceções passam a ser filhas de uma mãe, `ErroDoCartao`. Acrescenta um teste com três recusas num cartão novo: validar, carregar 0 e carregar 51. Cada recusa é apanhada por `pytest.raises(ErroDoCartao)`, no seu próprio `with`, com uma só linha lá dentro.

No fim do `cartao.py`, por baixo de `if __name__ == "__main__":`, escreve um programa que tenta carregar 10, 0, 45, 30, 15 e 10 viagens num cartão novo. Tem um só `except` para todas as recusas. Com `python3 cartao.py`, aparece:

```text
Carregadas 10 viagens. Ficam 10.
Recusado: Não se carregam 0 viagens.
Recusado: Só cabem mais 40 viagens; pediste 45.
Carregadas 30 viagens. Ficam 40.
Recusado: Só cabem mais 10 viagens; pediste 15.
Carregadas 10 viagens. Ficam 50.
```

Rever: [Uma família de exceções](../04-excecoes-depuracao-e-logging.md#uma-família-de-exceções) e [Apanhar a recusa: try, except e else](../04-excecoes-depuracao-e-logging.md#apanhar-a-recusa-try-except-e-else).

<details>
<summary>Pista</summary>

Um `except` com a classe-mãe apanha também as filhas. A linha "Carregadas…" só se escreve quando o carregamento não foi recusado.

</details>

## Desafios

### Desafio 1: Uma exceção com dados

A `LimiteUltrapassado` passa a guardar as viagens pedidas, em `pedidas`, e as que ainda cabiam, em `possiveis`, e escreve ela própria a mensagem. Acrescenta um teste: num cartão com 44 viagens, carregar 10 é recusado. A exceção tem `pedidas` igual a 10, `possiveis` igual a 6 e a mensagem "Só cabem mais 6 viagens; pediste 10.". O programa do exercício 5 continua a mostrar a mesma saída.

Para chegares à exceção no teste, escreve `with pytest.raises(LimiteUltrapassado) as erro:`. Depois do bloco, a exceção está em `erro.value`, e o texto da mensagem é `str(erro.value)`. Aqui o teste confirma a mensagem, porque é a própria exceção que a escreve.

Rever: [Uma exceção com dados](../04-excecoes-depuracao-e-logging.md#uma-exceção-com-dados).

### Desafio 2: Ver os testes a apanhar um erro

No `carregar`, põe a soma das viagens antes das duas verificações, e confirma que os teus testes apanham o erro: pelo menos um falha. Escreve num comentário, no fim do `test_cartao.py`, que testes falharam e porquê. Depois, repõe a ordem certa, e os testes voltam a passar.

## Critérios de conclusão

- Os testes dos exercícios 1 a 5 estão no `test_cartao.py`, e `python3 -m pytest` passa sem falhas.
- Cada recusa tem a sua classe de exceção, e as três são filhas da `ErroDoCartao`.
- Os testes das recusas confirmam também as viagens que ficam no cartão.
- `python3 cartao.py` mostra exatamente a saída do exercício 5.

![Rodapé](../../imagens/rodape.png)
