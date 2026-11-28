![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: JOIN e agregação introdutórios

Praticas as junções de tabelas, com o `JOIN` e o `LEFT JOIN`, e os resumos, com as funções de agregação, o `GROUP BY` e o `HAVING`. Os exercícios 1 a 6 são obrigatórios. Trabalhas no servidor do laboratório, na base `torneio` das fichas anteriores, e escreves uma consulta para cada pergunta. As consultas ficam no `torneio-relatorios.sql`, na pasta do projeto, cada uma com um comentário com a pergunta. Para rever: o [guia do tema](../04-join-e-agregacao-introdutorios.md) e o [laboratório](../laboratorios/04-join-e-agregacao-introdutorios-laboratorio.md).

## O cenário

O torneio é o da [ficha do tema 03](03-dml-e-consultas-com-contexto-exercicios.md#o-cenário), com o `torneio.sql` e o `torneio-dados.sql` de lá. Inscreveu-se uma equipa nova, as Corujas, que ainda não tem jogadores, e as Raposas ganharam um terceiro jogador. No fim do teu `torneio-dados.sql`, acrescenta estas linhas:

```sql

-- Uma equipa nova, ainda sem jogadores, e mais um jogador nas Raposas.
INSERT INTO equipas (nome) VALUES
    ('Corujas');     -- 5

INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES
    ('fenix', 'Marta Rocha', 1);         -- 9
```

Muda também o comentário do início do `torneio-dados.sql`, que passa a dizer cinco equipas e nove jogadores. Entra na base `torneio` e reconstrói-a, com o `\i torneio.sql` e o `\i torneio-dados.sql`: o segundo acaba em `INSERT 0 1` e `INSERT 0 1`, as linhas novas. O torneio fica com cinco equipas, nove jogadores e sete partidas, três delas por jogar. Os resultados esperados são os desta base acabada de construir.

## Exercício 1: As equipas dos jogadores

Que equipa tem cada jogador? A lista mostra o nome no jogo e o nome da equipa, ordenada pelo nome da equipa e, dentro de cada equipa, pelo nome no jogo.

| Resultado esperado |
| --- |
| 9 linhas, a começar na `nina` e no `sombra`, das Águias, e a acabar no `rexy` e no `ritaxx`, dos Tubarões |

Rever: [O JOIN junta as linhas de duas tabelas](../04-join-e-agregacao-introdutorios.md#o-join-junta-as-linhas-de-duas-tabelas) e [Os nomes das colunas dizem de que tabela vêm](../04-join-e-agregacao-introdutorios.md#os-nomes-das-colunas-dizem-de-que-tabela-vêm).

## Exercício 2: Os jogadores dos Lobos

Que jogadores jogam nos Lobos? A consulta escolhe a equipa pelo nome, e não pelo número, e mostra o nome no jogo e o nome verdadeiro de cada jogador.

| Resultado esperado |
| --- |
| 2 linhas: o `lobo1`, Leo Brás, e o `zeca`, José Costa |

Rever: [O JOIN com o WHERE e o ORDER BY](../04-join-e-agregacao-introdutorios.md#o-join-com-o-where-e-o-order-by).

## Exercício 3: As equipas sem jogadores

Que equipas ainda não têm nenhum jogador?

| Resultado esperado |
| --- |
| 1 linha: as Corujas |

Rever: [O JOIN deixa de fora as linhas sem par](../04-join-e-agregacao-introdutorios.md#o-join-deixa-de-fora-as-linhas-sem-par) e [O LEFT JOIN guarda as linhas da esquerda](../04-join-e-agregacao-introdutorios.md#o-left-join-guarda-as-linhas-da-esquerda).

<details>
<summary>Pista</summary>

Se a resposta é `(0 rows)`, corre a junção sem o `WHERE` e procura a linha das Corujas.

</details>

## Exercício 4: O resumo das partidas

Escreve uma consulta que dê, numa só linha, quatro colunas:

- quantas partidas há;
- quantas já se jogaram;
- quanto duraram em média as que se jogaram, com uma casa decimal;
- quanto durou a mais longa.

| Resultado esperado |
| --- |
| 1 linha: 7 partidas, 4 jogadas, 66.3 minutos de média e 90 minutos a mais longa |

Rever: [As funções de agregação resumem uma coluna](../04-join-e-agregacao-introdutorios.md#as-funções-de-agregação-resumem-uma-coluna).

## Exercício 5: Os jogadores de cada equipa

Quantos jogadores tem cada equipa, incluindo as que não têm nenhum, e qual é o primeiro nome no jogo de cada uma, por ordem alfabética? A lista vai da equipa com mais jogadores para a equipa com menos, e o nome da equipa desempata.

| Resultado esperado |
| --- |
| 5 linhas, por esta ordem: as Raposas com 3 e a `fenix`; as Águias com 2 e a `nina`; os Lobos com 2 e o `lobo1`; os Tubarões com 2 e o `rexy`; as Corujas com 0 e sem nome |

Rever: [O GROUP BY faz um resumo por grupo](../04-join-e-agregacao-introdutorios.md#o-group-by-faz-um-resumo-por-grupo) e o [exemplo guiado](../04-join-e-agregacao-introdutorios.md#exemplo-guiado-os-pokémon-de-cada-treinador-com-o-gary).

<details>
<summary>Pista</summary>

Se as Corujas aparecem com 1, a contagem está a contar as linhas, e não os jogadores.

</details>

## Exercício 6: As equipas com mais de dois jogadores

Que equipas têm mais de dois jogadores, e quantos tem cada uma?

| Resultado esperado |
| --- |
| 1 linha: as Raposas, com 3 |

Rever: [O HAVING escolhe os grupos](../04-join-e-agregacao-introdutorios.md#o-having-escolhe-os-grupos).

## Desafios

### Desafio 1: As partidas com o nome das equipas

Escreve a lista das partidas, por data, com o nome da equipa da casa, o nome da equipa de fora e os pontos de cada uma. As sete partidas têm de aparecer. Rever: [A mesma tabela duas vezes](../04-join-e-agregacao-introdutorios.md#a-mesma-tabela-duas-vezes).

### Desafio 2: Jogadores e partidas em casa

Um colega quer, para cada equipa, o número de jogadores e o número de partidas que tem em casa, jogadas ou por jogar, numa só consulta. Escreveu dois `LEFT JOIN` a partir das equipas, um para os jogadores e outro para as partidas em casa, e as Raposas apareceram com 6 jogadores. Explica num comentário porque é que o número está errado, e escreve a consulta certa. As Raposas têm 3 jogadores e 2 partidas em casa. Rever: [Uma junção a mais pode multiplicar as contagens](../04-join-e-agregacao-introdutorios.md#uma-junção-a-mais-pode-multiplicar-as-contagens).

### Desafio 3: Os pontos marcados em casa

Quantos pontos marcou cada equipa nas partidas que jogou em casa? As partidas por jogar não têm pontos. Com o `JOIN`, as Corujas não aparecem. Explica num comentário porquê, e o que aparece na linha delas com o `LEFT JOIN`.

## Critérios de conclusão

- O `torneio-relatorios.sql` tem as consultas dos exercícios 1 a 6, cada uma com um comentário com a pergunta.
- Numa base acabada de construir pelo `torneio.sql` e pelo `torneio-dados.sql`, com as linhas novas do cenário, as consultas dão os resultados das tabelas.

![Rodapé](../../imagens/rodape.png)
