![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: DDL e integridade

Praticas a criação das tabelas de um problema, com as restrições que fazem cumprir as regras dele, e a previsão do que a base aceita. Os exercícios 1 a 5 são obrigatórios. Trabalhas no servidor do laboratório, numa base nova. O esquema fica no ficheiro `torneio.sql`, os dados do exemplo no `torneio-dados.sql`, e as previsões e as respostas por palavras em comentários no `torneio-respostas.sql`, os três na pasta do projeto. Para rever: o [guia do tema](../02-ddl-e-integridade.md) e o [laboratório](../laboratorios/02-ddl-e-integridade-laboratorio.md).

## O cenário

A escola vai guardar o torneio de um jogo de equipas numa base de dados, a base `torneio`. O modelo das tabelas já está decidido:

```text
equipas (id PK, nome)
jogadores (id PK, nome_no_jogo, nome_verdadeiro, equipa_id FK -> equipas)
partidas (id PK, data, equipa_casa_id FK -> equipas, equipa_fora_id FK -> equipas, pontos_casa NULL, pontos_fora NULL)
```

As regras do torneio são estas:

- Cada equipa tem um nome, com 30 caracteres no máximo, que não se repete.
- Cada jogador tem o nome com que joga, com 20 caracteres no máximo, que é único no torneio, e o nome verdadeiro, com 50 no máximo. Cada jogador joga numa equipa que existe.
- Cada partida tem uma data e duas equipas que existem, a da casa e a de fora, e uma equipa não joga contra si própria. Quando a partida acaba, guardam-se os pontos de cada equipa, que nunca são negativos. Uma partida marcada ainda não tem pontos.
- Tudo o que estas regras dizem que uma linha tem é obrigatório, menos os pontos de uma partida marcada.
- A base dá os números das linhas.

Um exemplo de dados:

- as equipas Raposas e Tubarões;
- a jogadora Rita Matos, que joga como `ritaxx`, nos Tubarões;
- a partida de 5 de dezembro, Raposas contra Tubarões, que acabou 13 a 9;
- a partida de 12 de dezembro, Tubarões contra Raposas, ainda por jogar.

## Exercício 1: A base e as equipas

Cria a base `torneio`, no mesmo servidor da `ginasio`, e escreve no `torneio.sql` a tabela das equipas, com as regras do cenário. O ficheiro tem de poder correr as vezes que quiseres.

Casos de teste, numa base acabada de construir pelo `torneio.sql`, pela ordem:

| `INSERT` | Resultado |
| --- | --- |
| `INSERT INTO equipas (nome) VALUES ('Raposas');` | Aceite, com o `id` 1 |
| `INSERT INTO equipas (nome) VALUES ('Tubarões');` | Aceite, com o `id` 2 |
| `INSERT INTO equipas (nome) VALUES ('Raposas');` | Recusado |
| `INSERT INTO equipas (nome) VALUES (NULL);` | Recusado |

Rever: [Uma base de dados nova começa vazia](../02-ddl-e-integridade.md#uma-base-de-dados-nova-começa-vazia) e [Um ficheiro que se volta a correr começa por apagar](../02-ddl-e-integridade.md#um-ficheiro-que-se-volta-a-correr-começa-por-apagar). Para as regras da tabela: [A base pode dar o número da chave primária](../02-ddl-e-integridade.md#a-base-pode-dar-o-número-da-chave-primária) e [O UNIQUE recusa os repetidos](../02-ddl-e-integridade.md#o-unique-recusa-os-repetidos).

## Exercício 2: Os jogadores

Acrescenta ao `torneio.sql` a tabela dos jogadores.

Casos de teste, depois das duas equipas do exercício 1, pela ordem:

| `INSERT` | Resultado |
| --- | --- |
| `INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('ritaxx', 'Rita Matos', 2);` | Aceite |
| `INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('ritaxx', 'Rita Almeida', 1);` | Recusado |
| `INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('kiko', 'Rita Matos', 1);` | Aceite |
| `INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('zeca', 'José Costa', 5);` | Recusado |

Rever: [A chave estrangeira recusa o que não existe](../02-ddl-e-integridade.md#a-chave-estrangeira-recusa-o-que-não-existe) e [A ordem das tabelas segue as chaves estrangeiras](../02-ddl-e-integridade.md#a-ordem-das-tabelas-segue-as-chaves-estrangeiras).

<details>
<summary>Pista</summary>

Corre o `torneio.sql` duas vezes seguidas. Da segunda vez, as equipas já têm uma tabela a apontar para elas.

</details>

## Exercício 3: As partidas

Acrescenta ao `torneio.sql` a tabela das partidas.

Casos de teste, numa base com as duas equipas do exercício 1, pela ordem:

| `INSERT` | Resultado |
| --- | --- |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora) VALUES ('2026-12-05', 1, 2, 13, 9);` | Aceite |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora) VALUES ('2026-12-12', 2, 1, NULL, NULL);` | Aceite |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora) VALUES ('2026-12-19', 1, 1, NULL, NULL);` | Recusado |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora) VALUES ('2026-12-19', 1, 2, -3, 10);` | Recusado |

Rever: [O CHECK recusa os valores fora da regra](../02-ddl-e-integridade.md#o-check-recusa-os-valores-fora-da-regra).

<details>
<summary>Pista</summary>

Uma das regras não fala de uma coluna, mas de duas colunas da mesma linha. E a partida de 12 de dezembro, que ainda não tem pontos, tem de entrar.

</details>

## Exercício 4: Aceite ou recusado

Com o `torneio.sql` dos exercícios 1 a 3, constrói a base e põe lá os dados do exemplo do cenário, sem nenhum `INSERT` recusado pelo caminho. Assim, as Raposas ficam com o número 1, e os Tubarões com o 2. Guarda esses `INSERT` no `torneio-dados.sql`, para os voltares a pôr sempre que correres o `torneio.sql`. Depois, estes seis `INSERT` correm um a seguir ao outro:

```sql
INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('lobo1', 'Leo Brás', 3);
INSERT INTO equipas (nome) VALUES ('Lobos');
INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('lobo1', 'Leo Brás', 3);
INSERT INTO jogadores (nome_no_jogo, nome_verdadeiro, equipa_id) VALUES ('lobo2', NULL, 3);
INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora) VALUES ('2026-12-20', 2, 3, 0, 0);
INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id) VALUES ('2026-12-21', 3, 3);
```

Para cada um, escreve no `torneio-respostas.sql`, antes de o correres, se a base o aceita e, se o recusa, que regra do cenário o recusa. Depois, corre-os e confirma. Se a base fizer outra coisa, volta às regras do cenário. Se a tua previsão está de acordo com elas, o erro está no `torneio.sql`; se não está, o erro está na previsão.

Rever: [Prever o que a base aceita](../02-ddl-e-integridade.md#prever-o-que-a-base-aceita).

## Exercício 5: A duração das partidas

A escola passa a guardar a duração de cada partida, em minutos, de 1 a 90. A duração só se sabe quando a partida acaba. Acrescenta a coluna `duracao` à tabela das partidas sem apagar as partidas que lá estão, e deixa o `torneio.sql` a dizer o mesmo que a base. Escreve no `torneio-respostas.sql` o comando que usaste.

Casos de teste, na base do exercício 4, pela ordem:

| Comando | Resultado |
| --- | --- |
| `SELECT * FROM partidas;` | As partidas que já lá estavam aparecem sem duração |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora, duracao) VALUES ('2026-12-26', 1, 2, 7, 7, 90);` | Aceite |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id) VALUES ('2026-12-27', 2, 1);` | Aceite, sem duração |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora, duracao) VALUES ('2026-12-28', 2, 1, 3, 4, 0);` | Recusado |
| `INSERT INTO partidas (data, equipa_casa_id, equipa_fora_id, pontos_casa, pontos_fora, duracao) VALUES ('2026-12-29', 1, 2, 5, 2, 95);` | Recusado |

Rever: [O ALTER TABLE muda uma tabela sem perder os dados](../02-ddl-e-integridade.md#o-alter-table-muda-uma-tabela-sem-perder-os-dados).

<details>
<summary>Pista</summary>

Pensa no valor que a coluna nova deve ter nas partidas que ainda não acabaram.

</details>

## Desafios

### Desafio 1: A mesma partida duas vezes

A escola não quer a mesma partida marcada duas vezes: as mesmas duas equipas, na mesma data. Junta essa regra às partidas e confirma que um segundo `INSERT` da partida de 5 de dezembro, Raposas contra Tubarões, é recusado. Depois, experimenta a mesma data com as equipas trocadas, Tubarões contra Raposas. A tua regra apanha-a? Escreve porquê num comentário.

### Desafio 2: Raposas e raposas

A base do exercício 4 já tem as Raposas. Corre `INSERT INTO equipas (nome) VALUES ('raposas');`: a base aceita-o ou recusa-o? Explica o resultado num comentário, e diz se isso pode ser um problema para o torneio.

## Critérios de conclusão

- O `torneio.sql` corre as vezes que quiseres, sem erros, e cria as três tabelas com as regras do cenário, incluindo a coluna `duracao`.
- Os casos de teste dos exercícios 1, 2, 3 e 5 dão os resultados das tabelas.
- O `torneio-respostas.sql` tem as seis previsões do exercício 4, escritas antes de correres, e o comando do exercício 5.

![Rodapé](../../imagens/rodape.png)
