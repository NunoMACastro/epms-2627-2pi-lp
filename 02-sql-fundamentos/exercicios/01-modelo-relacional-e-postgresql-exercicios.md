![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Modelo relacional e ambiente PostgreSQL

Praticas a leitura das tabelas, a escolha das colunas, o NULL, as chaves e o desenho das tabelas de um problema. Os exercícios 1 a 6 são obrigatórios. Os exercícios 1 a 4 fazem-se na base `pokemon` do laboratório, com o servidor a correr. As consultas e as respostas por palavras dos exercícios 1 a 5 ficam num ficheiro `.sql` teu, com as respostas em comentários. Para rever: o [guia do tema](../01-modelo-relacional-e-postgresql.md) e o [laboratório](../laboratorios/01-modelo-relacional-e-postgresql-laboratorio.md).

## Perguntar à base dos Pokémon

### Exercício 1: A lista dos combates

Queremos uma lista dos combates com o vencedor, a data e o líder de cada um, por esta ordem. Escreve a consulta. A resposta tem 3 linhas e 3 colunas, e a primeira linha é `2 | 2026-11-03 | 2`.

Rever: [Escolher as colunas](../01-modelo-relacional-e-postgresql.md#escolher-as-colunas).

### Exercício 2: Duas consultas parecidas

Antes de as correres, diz, para cada uma destas consultas, quantas linhas e quantas colunas tem a resposta, que nome tem cada coluna e o que está nela:

```sql
SELECT nome, tipo_id FROM especies;
SELECT tipo_id nome FROM especies;
```

Rever: [Escolher as colunas](../01-modelo-relacional-e-postgresql.md#escolher-as-colunas).

<details>
<summary>Pista</summary>

Compara o nome de cada coluna da resposta com o que está dentro dela.

</details>

### Exercício 3: NULL, zero ou texto vazio

Para cada caso, diz que valor devia ficar na célula, NULL, `0`, `''` ou outro, e porquê. Confirma no `\d` da tabela se a base de dados o aceita.

1. A alcunha de um Pokémon a quem o treinador nunca deu alcunha.
2. O ataque de um Pokémon acabado de capturar, que ainda ninguém mediu.
3. A vida de um Pokémon que acabou de ficar KO.

Rever: [O NULL quer dizer que não há valor](../01-modelo-relacional-e-postgresql.md#o-null-quer-dizer-que-não-há-valor).

### Exercício 4: Seguir as chaves

Responde só com consultas `SELECT` às tabelas, seguindo as chaves estrangeiras à mão.

1. De que tipo de Pokémon é o Pokémon com a alcunha vazia?
2. No combate 1, quem venceu, e contra quem?

Rever: [A chave estrangeira aponta para outra tabela](../01-modelo-relacional-e-postgresql.md#a-chave-estrangeira-aponta-para-outra-tabela).

<details>
<summary>Pista</summary>

Para chegar ao tipo de um Pokémon capturado, há uma tabela pelo meio. E a alcunha vazia não é a mesma coisa que não ter alcunha.

</details>

## Desenhar as tabelas do torneio

A escola organiza um torneio de um jogo de equipas, e quer guardá-lo numa base de dados. Estes dados servem aos exercícios 5 e 6 e aos desafios:

- Cada equipa tem um nome.
- Cada jogador tem o nome com que joga, que é único no torneio, e o nome verdadeiro, e joga numa só equipa.
- Cada partida é entre duas equipas, numa data. Quando a partida acaba, guardam-se os pontos de cada equipa. Antes disso, a partida está marcada e ainda não tem pontos.

Um exemplo:

- as equipas Raposas e Tubarões;
- a jogadora Rita Matos, que joga como `ritaxx`, nos Tubarões;
- a partida de 5 de dezembro, Raposas contra Tubarões, que acabou 13 a 9;
- a partida de 12 de dezembro, Tubarões contra Raposas, ainda por jogar.

### Exercício 5: A chave primária dos jogadores

Para cada coluna que a tabela dos jogadores pode ter, diz se servia de chave primária e porquê.

Rever: [A chave primária identifica cada linha](../01-modelo-relacional-e-postgresql.md#a-chave-primária-identifica-cada-linha).

### Exercício 6: O modelo do torneio

Desenha o modelo relacional do torneio, com as tabelas e as colunas de cada uma. Marca a chave primária e as chaves estrangeiras de cada tabela, e as colunas que podem ficar sem valor. O modelo tem de conseguir guardar o exemplo do enunciado.

Rever: [O modelo desenha-se antes das tabelas](../01-modelo-relacional-e-postgresql.md#o-modelo-desenha-se-antes-das-tabelas) e [Exemplo guiado: o modelo do ginásio](../01-modelo-relacional-e-postgresql.md#exemplo-guiado-o-modelo-do-ginásio).

<details>
<summary>Pista</summary>

Começa pelas coisas do enunciado que têm dados próprios. Depois, para cada par de tabelas ligadas, pergunta nos dois sentidos quantos há de cada lado.

</details>

## Desafios

### Desafio 1: A tabela que repete tudo

Um colega guardou as partidas do torneio numa só tabela:

| data | equipa_casa | equipa_fora | pontos_casa | pontos_fora |
| --- | --- | --- | ---: | ---: |
| 2026-12-05 | Raposas | Tubarões | 13 | 9 |
| 2026-12-12 | Tubaroes | Raposas | | |

Diz que problemas tem esta tabela e como a dividias, com o teu modelo do exercício 6.

### Desafio 2: O jogador que muda de equipa

A meio do torneio, um jogador muda de equipa, e queremos saber por que equipa jogou cada partida. O teu modelo do exercício 6 consegue guardá-lo? Se não consegue, o que lhe mudavas?

## Critérios de conclusão

- As consultas dos exercícios 1 e 4 correm na base `pokemon` e dão as respostas que o enunciado pede.
- As respostas dos exercícios 2 a 5 estão escritas, em comentários.
- O modelo do torneio tem as tabelas, as colunas, as chaves primárias e as estrangeiras, e guarda o exemplo do enunciado.

![Rodapé](../../imagens/rodape.png)
