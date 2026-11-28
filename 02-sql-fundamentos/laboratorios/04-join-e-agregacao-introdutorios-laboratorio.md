![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: JOIN e agregação introdutórios

## O que vais construir

Vais escrever os relatórios do ginásio num ficheiro novo, o `relatorios.sql`: consultas que juntam duas ou mais tabelas e resumos com contagens, cada um com o resultado esperado num comentário. No fim, a pasta do projeto tem estes ficheiros:

```text
pokemon-sql/
├── .env
├── .gitignore
├── compose.yaml
├── dados.sql
├── esquema.sql
├── perguntas.sql
├── pokemon.sql
├── recusas.sql
└── relatorios.sql
```

1. [Fase 1: O JOIN junta as linhas de duas tabelas](#fase-1-o-join-junta-as-linhas-de-duas-tabelas)
2. [Fase 2: Os nomes das colunas dizem de que tabela vêm](#fase-2-os-nomes-das-colunas-dizem-de-que-tabela-vêm)
3. [Fase 3: Três tabelas numa consulta](#fase-3-três-tabelas-numa-consulta)
4. [Fase 4: O JOIN com o WHERE e o ORDER BY](#fase-4-o-join-com-o-where-e-o-order-by)
5. [Fase 5: A mesma tabela duas vezes](#fase-5-a-mesma-tabela-duas-vezes)
6. [Fase 6: O JOIN deixa de fora as linhas sem par](#fase-6-o-join-deixa-de-fora-as-linhas-sem-par)
7. [Fase 7: O LEFT JOIN guarda as linhas da esquerda](#fase-7-o-left-join-guarda-as-linhas-da-esquerda)
8. [Fase 8: As funções de agregação resumem uma coluna](#fase-8-as-funções-de-agregação-resumem-uma-coluna)
9. [Fase 9: O GROUP BY faz um resumo por grupo](#fase-9-o-group-by-faz-um-resumo-por-grupo)
10. [Fase 10: O HAVING escolhe os grupos](#fase-10-o-having-escolhe-os-grupos)
11. [Fase 11: Uma junção a mais pode multiplicar as contagens](#fase-11-uma-junção-a-mais-pode-multiplicar-as-contagens)

## O que precisas

- O Docker Desktop, aberto: o `docker info`, no terminal, responde sem erro.
- O VS Code, onde escreves os ficheiros e abres o terminal.
- A pasta `pokemon-sql` do laboratório do tema 03, com o `esquema.sql` e o `dados.sql` do fim dele. Se não a tiveres, cria-a como diz o "Como correr" da [versão 03 do exemplo dos Pokémon](../../exemplos/sql-fundamentos/pokemon/README.md#como-correr-a-versão-03), e volta aqui.

## Preparar o projeto

1. Abre a pasta `pokemon-sql` no VS Code e abre um terminal, no menu Terminal, com a opção New Terminal. Arranca o servidor, se estiver parado:

   ```bash
   docker compose up -d
   ```

   O que deves ver, no fim: a linha do servidor, `pokemon-sql-db-1`, com `Running` ou `Started`.

2. Entra no `psql`, na base `ginasio`:

   ```bash
   docker compose exec db psql -U postgres -d ginasio
   ```

   O que deves ver: o início da linha é `ginasio=#`.

3. Os resultados esperados deste laboratório são os da base que o `dados.sql` constrói. Reconstrói-a, para desfazer o que mudaste no tema 03:

   ```text
   \i esquema.sql
   \i dados.sql
   ```

   O que deves ver: os cinco `DROP TABLE`, os cinco `CREATE TABLE` e oito linhas `INSERT`, a acabar em `INSERT 0 2`, `INSERT 0 2` e `INSERT 0 1`. Se aparecerem só cinco linhas `INSERT`, o teu `dados.sql` é o do tema 02: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. As respostas deste laboratório têm até nove linhas, e num terminal pequeno o `psql` mostra-as por páginas, e para. Escreve `\pset pager off`, para ele mostrar tudo de seguida. O que deves ver: `Pager usage is off.`. Dura até saíres do `psql`.

5. No painel Explorer do VS Code, cria o ficheiro `relatorios.sql`, na pasta do projeto, com estas linhas de comentário, e guarda-o:

   ```sql
   -- relatorios.sql: os relatórios do ginásio, que juntam tabelas e fazem resumos.
   -- Corre-se no psql, ligado à base ginasio, com \i relatorios.sql, numa base acabada
   -- de construir pelo esquema.sql e pelo dados.sql. Cada comentário diz o resultado esperado.
   ```

## Fase 1: O JOIN junta as linhas de duas tabelas

Juntas os Pokémon às espécies, para cada Pokémon aparecer com o nome da sua espécie. O `ON` diz que linhas fazem par: a chave estrangeira de uma tabela igual à chave primária da outra. Rever: [O JOIN junta as linhas de duas tabelas](../04-join-e-agregacao-introdutorios.md#o-join-junta-as-linhas-de-duas-tabelas).

1. No `psql`, pede os Pokémon com o nome da espécie. Escreve a consulta numa só linha, ou em várias, como aqui. Enquanto o ponto e vírgula não chega, as linhas começam por `ginasio-#`, e o `psql` espera pelo resto:

   ```sql
   SELECT p.id, e.nome, p.vida
   FROM pokemons AS p
   JOIN especies AS e ON p.especie_id = e.id
   ORDER BY p.id;
   ```

   O que deves ver:

   ```text
    id |    nome    | vida
   ----+------------+------
     1 | Charmander |   90
     2 | Bulbasaur  |  110
     3 | Pikachu    |   80
     4 | Starmie    |    0
     5 | Psyduck    |  100
     6 | Onix       |  140
     7 | Geodude    |    0
     8 | Staryu     |    0
   (8 rows)
   ```

   Cada Pokémon tem o nome da espécie para onde aponta o seu `especie_id`. O `p` e o `e` são os nomes curtos das duas tabelas.

2. Provoca um erro de propósito: escreve uma junção sem o `ON`, como esta, `SELECT p.id, e.nome FROM pokemons AS p JOIN especies AS e WHERE p.vida > 0;`. O que deves ver: `ERROR:  syntax error at or near "WHERE"`. O `JOIN` precisa do `ON` logo a seguir à segunda tabela, e o PostgreSQL encontrou o `WHERE`.

3. No fim do `relatorios.sql`, acrescenta o primeiro relatório e guarda:

   ```sql

   -- Que espécie é cada Pokémon?
   -- Esperado: 8 linhas, do Charmander, o Pokémon 1, ao Staryu, o 8.
   SELECT p.id, e.nome, p.vida
   FROM pokemons AS p
   JOIN especies AS e ON p.especie_id = e.id
   ORDER BY p.id;
   ```

4. Corre o ficheiro com `\i relatorios.sql`. O que deves ver: as oito linhas do passo 1. Se aparecer `relatorios.sql: No such file or directory`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

O `relatorios.sql` tem o primeiro relatório, e o `\i` corre-o.

Pensa antes de continuares: a junção tem oito linhas. Porque não nove, se há nove espécies? A resposta: a junção faz uma linha por par, e há oito Pokémon, cada um com uma espécie. O Squirtle não é a espécie de nenhum Pokémon, e não faz par.

## Fase 2: Os nomes das colunas dizem de que tabela vêm

Juntas as espécies aos tipos, que têm as duas uma coluna `id` e uma coluna `nome`. Cada coluna leva o nome curto da tabela à frente, e as colunas da resposta podem receber um nome com o `AS`. Rever: [Os nomes das colunas dizem de que tabela vêm](../04-join-e-agregacao-introdutorios.md#os-nomes-das-colunas-dizem-de-que-tabela-vêm) e, para o `AS` nas colunas, [Três tabelas numa consulta](../04-join-e-agregacao-introdutorios.md#três-tabelas-numa-consulta).

1. Provoca um erro de propósito: pede o `id` e o `nome` sem dizer de que tabela.

   ```sql
   SELECT id, nome
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id;
   ```

   O que deves ver: `ERROR:  column reference "id" is ambiguous`. As duas tabelas têm um `id`, e o PostgreSQL não sabe de qual falas.

2. Escreve as colunas com o nome curto da tabela, e dá um nome a cada uma na resposta:

   ```sql
   SELECT e.nome AS especie, tp.nome AS tipo
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   ORDER BY e.id;
   ```

   O que deves ver: nove linhas, com duas colunas, `especie` e `tipo`. A primeira é o Charmander, do Fogo, e a última o Staryu, da Água.

3. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- De que tipo é cada espécie?
   -- Esperado: 9 linhas. A Água tem quatro espécies: o Squirtle, o Starmie, o Psyduck e o Staryu.
   SELECT e.nome AS especie, tp.nome AS tipo
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   ORDER BY e.id;
   ```

### Paragem 2

O `relatorios.sql` tem dois relatórios.

Pensa antes de continuares: sem os dois `AS` das colunas, que cabeçalho tinha a resposta? A resposta: `nome | nome`, duas colunas com o mesmo nome, e não se saberia qual é a espécie e qual é o tipo.

## Fase 3: Três tabelas numa consulta

Juntas três tabelas em cadeia: os Pokémon às espécies, e as espécies aos tipos. Cada `JOIN` tem o seu `ON`. Rever: [Três tabelas numa consulta](../04-join-e-agregacao-introdutorios.md#três-tabelas-numa-consulta).

1. Antes de correres, prevê: quantas linhas tem a resposta desta junção, e porquê?

   ```sql
   SELECT p.id, e.nome AS especie, tp.nome AS tipo
   FROM pokemons AS p
   JOIN especies AS e ON p.especie_id = e.id
   JOIN tipos AS tp ON e.tipo_id = tp.id
   ORDER BY p.id;
   ```

   O que deves ver: oito linhas, uma por Pokémon, com a espécie e o tipo. Cada Pokémon tem uma espécie, e cada espécie tem um tipo, e por isso nenhuma das junções acrescenta nem tira linhas. O Pokémon 6, o Onix, é da Pedra.

2. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- De que espécie e de que tipo é cada Pokémon?
   -- Esperado: 8 linhas. O Onix e o Geodude são da Pedra; o Starmie, o Psyduck e o Staryu, da Água.
   SELECT p.id, e.nome AS especie, tp.nome AS tipo
   FROM pokemons AS p
   JOIN especies AS e ON p.especie_id = e.id
   JOIN tipos AS tp ON e.tipo_id = tp.id
   ORDER BY p.id;
   ```

### Paragem 3

O `relatorios.sql` tem três relatórios. O terceiro chega aos tipos através das espécies, porque os Pokémon não têm uma coluna para o tipo. Corre o `\i relatorios.sql`: a última resposta é a do passo 1, com oito linhas.

Pensa antes de continuares: o `JOIN tipos` pode vir antes do `JOIN especies`? A resposta: não. O `ON e.tipo_id = tp.id` usa o `e`, que ainda não estava na consulta, e o PostgreSQL responde `missing FROM-clause entry for table "e"`. Cada `JOIN` só pode usar as tabelas que já entraram.

## Fase 4: O JOIN com o WHERE e o ORDER BY

Escolhes, na junção das três tabelas, só os Pokémon de um tipo, pelo nome do tipo, e ordenas a resposta. Rever: [O JOIN com o WHERE e o ORDER BY](../04-join-e-agregacao-introdutorios.md#o-join-com-o-where-e-o-order-by).

1. Pede os Pokémon de Água, do que tem mais vida para o que tem menos:

   ```sql
   SELECT p.id, e.nome AS especie, p.vida
   FROM pokemons AS p
   JOIN especies AS e ON p.especie_id = e.id
   JOIN tipos AS tp ON e.tipo_id = tp.id
   WHERE tp.nome = 'Água'
   ORDER BY p.vida DESC, p.id;
   ```

   O que deves ver: três linhas, o Psyduck, com 100, o Starmie e o Staryu, com 0. O `p.id` desempata os dois KO. O `WHERE` usa o nome do tipo, da tabela `tipos`, e a resposta mostra colunas das outras duas.

2. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Que Pokémon de Água há, do que tem mais vida para o que tem menos?
   -- Esperado: 3 linhas, os Pokémon 5, 4 e 8.
   SELECT p.id, e.nome AS especie, p.vida
   FROM pokemons AS p
   JOIN especies AS e ON p.especie_id = e.id
   JOIN tipos AS tp ON e.tipo_id = tp.id
   WHERE tp.nome = 'Água'
   ORDER BY p.vida DESC, p.id;
   ```

### Paragem 4

O `relatorios.sql` tem quatro relatórios. Corre o `\i relatorios.sql`: a última resposta é a do passo 1, com três linhas.

Pensa antes de continuares: o que dava o `WHERE tp.nome = 'agua'`? A resposta: `(0 rows)`. O texto compara-se letra a letra, como no tema 03, e o nome na base é `Água`, com o A grande e o acento.

## Fase 5: A mesma tabela duas vezes

Juntas os treinadores aos combates duas vezes, uma para o desafiante e outra para o líder. Cada entrada da tabela tem o seu nome curto. Rever: [A mesma tabela duas vezes](../04-join-e-agregacao-introdutorios.md#a-mesma-tabela-duas-vezes).

1. Provoca um erro de propósito: dá o mesmo nome curto às duas entradas.

   ```sql
   SELECT c.id, t.nome
   FROM combates AS c
   JOIN treinadores AS t ON c.desafiante_id = t.id
   JOIN treinadores AS t ON c.lider_id = t.id;
   ```

   O que deves ver: `ERROR:  table name "t" specified more than once`. O nome `t` foi dado duas vezes, e o PostgreSQL não saberia de qual das entradas é o `t.nome`.

2. Dá a cada entrada o seu nome, `d` para o desafiante e `l` para o líder:

   ```sql
   SELECT c.id, d.nome AS desafiante, l.nome AS lider
   FROM combates AS c
   JOIN treinadores AS d ON c.desafiante_id = d.id
   JOIN treinadores AS l ON c.lider_id = l.id
   ORDER BY c.id;
   ```

   O que deves ver: quatro linhas. Nos três primeiros combates, o Ash é o desafiante; no 4, é a Misty, contra o Brock.

3. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Quem desafiou, e quem era o líder, em cada combate?
   -- Esperado: 4 linhas. O Ash desafiou a Misty duas vezes e o Brock uma; a Misty desafiou o Brock.
   SELECT c.id, d.nome AS desafiante, l.nome AS lider
   FROM combates AS c
   JOIN treinadores AS d ON c.desafiante_id = d.id
   JOIN treinadores AS l ON c.lider_id = l.id
   ORDER BY c.id;
   ```

### Paragem 5

O `relatorios.sql` tem cinco relatórios, e o último usa a mesma tabela duas vezes.

Pensa antes de continuares: e o nome do vencedor? A resposta: precisava de uma terceira entrada dos treinadores, com outro nome curto, pelo `vencedor_id`.

## Fase 6: O JOIN deixa de fora as linhas sem par

Juntas os treinadores aos combates que desafiaram, e vês que os treinadores sem combates desaparecem. Antes, prevês quantas linhas vais ter. Rever: [O JOIN deixa de fora as linhas sem par](../04-join-e-agregacao-introdutorios.md#o-join-deixa-de-fora-as-linhas-sem-par).

1. Antes de correres, prevê: quantas linhas tem esta junção, e que treinadores aparecem?

   ```sql
   SELECT t.nome, c.id AS combate
   FROM treinadores AS t
   JOIN combates AS c ON c.desafiante_id = t.id
   ORDER BY t.id, c.id;
   ```

   O que deves ver: quatro linhas, uma por combate. O Ash aparece três vezes e a Misty uma. O Brock e o Gary nunca foram o desafiante, e não aparecem: não têm par.

2. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Em que combates foi cada treinador o desafiante?
   -- Esperado: 4 linhas, o Ash nos combates 1, 2 e 3 e a Misty no 4. O Brock e o Gary
   -- não aparecem, porque o JOIN deixa de fora quem não tem par.
   SELECT t.nome, c.id AS combate
   FROM treinadores AS t
   JOIN combates AS c ON c.desafiante_id = t.id
   ORDER BY t.id, c.id;
   ```

### Paragem 6

O `relatorios.sql` tem seis relatórios.

Pensa antes de continuares: a ligação dos treinadores aos combates, pelo desafiante, é de um para muitos. Em que lado está o "muitos"? A resposta: nos combates. Um treinador pode ser o desafiante em vários combates, e cada combate tem um só desafiante.

## Fase 7: O LEFT JOIN guarda as linhas da esquerda

Trocas o `JOIN` da fase 6 pelo `LEFT JOIN`, para os treinadores sem combates ficarem na resposta. Depois, usas o NULL da linha sem par para encontrar quem nunca desafiou. Rever: [O LEFT JOIN guarda as linhas da esquerda](../04-join-e-agregacao-introdutorios.md#o-left-join-guarda-as-linhas-da-esquerda).

1. Corre a junção da fase 6 com o `LEFT JOIN`:

   ```sql
   SELECT t.nome, c.id AS combate
   FROM treinadores AS t
   LEFT JOIN combates AS c ON c.desafiante_id = t.id
   ORDER BY t.id, c.id;
   ```

   O que deves ver: seis linhas. As quatro da fase 6, e mais duas, o Brock e o Gary, com o `combate` em branco, que é o NULL.

2. Pede só os treinadores que nunca desafiaram ninguém, com o `IS NULL` do tema 03:

   ```sql
   SELECT t.nome
   FROM treinadores AS t
   LEFT JOIN combates AS c ON c.desafiante_id = t.id
   WHERE c.id IS NULL
   ORDER BY t.id;
   ```

   O que deves ver: duas linhas, o Brock e o Gary.

3. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Que treinadores nunca desafiaram ninguém?
   -- Esperado: 2 linhas, o Brock e o Gary.
   SELECT t.nome
   FROM treinadores AS t
   LEFT JOIN combates AS c ON c.desafiante_id = t.id
   WHERE c.id IS NULL
   ORDER BY t.id;
   ```

### Paragem 7

O `relatorios.sql` tem sete relatórios. Corre o `\i relatorios.sql`: a última resposta é a do passo 2, com o Brock e o Gary.

Pensa antes de continuares: com o `JOIN` em vez do `LEFT JOIN`, o que dava o relatório do passo 2? A resposta: `(0 rows)`. O `JOIN` não deixa linhas sem par, e por isso nenhuma linha tem o `c.id` a NULL.

## Fase 8: As funções de agregação resumem uma coluna

Resumes a tabela dos combates numa só linha, com o `COUNT`, o `MIN` e o `MAX`. O `COUNT(*)` conta as linhas, e o `COUNT` de uma coluna conta só as que têm valor nela. Rever: [As funções de agregação resumem uma coluna](../04-join-e-agregacao-introdutorios.md#as-funções-de-agregação-resumem-uma-coluna).

1. Antes de correres, prevê: que valores dá esta consulta?

   ```sql
   SELECT COUNT(*) AS combates, COUNT(vencedor_id) AS acabados,
          MIN(data) AS primeiro, MAX(data) AS ultimo
   FROM combates;
   ```

   O que deves ver:

   ```text
    combates | acabados |  primeiro  |   ultimo
   ----------+----------+------------+------------
           4 |        3 | 2026-11-03 | 2026-11-17
   (1 row)
   ```

   Há quatro combates, e três acabaram: o `COUNT(vencedor_id)` não conta o combate 3, que tem o vencedor a NULL. O `MIN` e o `MAX` servem também para datas, e dão a mais antiga e a mais recente.

2. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Quantos combates há, quantos acabaram, e quando foram o primeiro e o último?
   -- Esperado: 1 linha: 4 combates, 3 acabados, de 2026-11-03 a 2026-11-17.
   SELECT COUNT(*) AS combates, COUNT(vencedor_id) AS acabados,
          MIN(data) AS primeiro, MAX(data) AS ultimo
   FROM combates;
   ```

### Paragem 8

O `relatorios.sql` tem oito relatórios. O último resume uma tabela inteira numa só linha.

Pensa antes de continuares: o que dá o `SELECT MIN(vida), MAX(vida) FROM pokemons;`? A resposta: 0 e 140. A vida mais baixa é a dos três Pokémon KO, e a mais alta a do Onix.

## Fase 9: O GROUP BY faz um resumo por grupo

Contas as espécies de cada tipo, com o `GROUP BY`, que faz um grupo por tipo. Rever: [O GROUP BY faz um resumo por grupo](../04-join-e-agregacao-introdutorios.md#o-group-by-faz-um-resumo-por-grupo).

1. Pede o número de espécies de cada tipo, do tipo com mais para o tipo com menos:

   ```sql
   SELECT tp.nome AS tipo, COUNT(*) AS especies
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   GROUP BY tp.id, tp.nome
   ORDER BY especies DESC, tipo;
   ```

   O que deves ver:

   ```text
      tipo   | especies
   ----------+----------
    Água     |        4
    Pedra    |        2
    Elétrico |        1
    Fogo     |        1
    Planta   |        1
   (5 rows)
   ```

   As nove linhas da junção, uma por espécie, ficaram em cinco grupos, um por tipo. O nome do tipo desempata os três que têm 1.

2. Provoca um erro de propósito: junta à resposta o nome da espécie, que não está no `GROUP BY`. Troca a primeira linha da consulta por `SELECT tp.nome AS tipo, e.nome, COUNT(*) AS especies` e corre-a. O que deves ver: `ERROR:  column "e.nome" must appear in the GROUP BY clause or be used in an aggregate function`. Um tipo tem várias espécies, e a resposta só tem uma linha por tipo.

3. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Quantas espécies tem cada tipo?
   -- Esperado: 5 linhas: a Água com 4, a Pedra com 2, e o Elétrico, o Fogo e a Planta com 1.
   SELECT tp.nome AS tipo, COUNT(*) AS especies
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   GROUP BY tp.id, tp.nome
   ORDER BY especies DESC, tipo;
   ```

### Paragem 9

O `relatorios.sql` tem nove relatórios.

Pensa antes de continuares: porque é que o `GROUP BY` tem o `tp.id` e o `tp.nome`, e não só o nome? A resposta: o `id` é o que distingue os tipos, e o nome é o que aparece na resposta. Aqui o nome dos tipos é único, mas nos treinadores, que podem ter o mesmo nome, só o `id` os separa.

## Fase 10: O HAVING escolhe os grupos

Escolhes os tipos com mais de uma espécie, com o `HAVING`, que escolhe os grupos depois de os contar. Rever: [O HAVING escolhe os grupos](../04-join-e-agregacao-introdutorios.md#o-having-escolhe-os-grupos).

1. Provoca um erro de propósito: escolhe os grupos no `WHERE`.

   ```sql
   SELECT tp.nome AS tipo
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   WHERE COUNT(*) > 1
   GROUP BY tp.id, tp.nome;
   ```

   O que deves ver: `ERROR:  aggregate functions are not allowed in WHERE`. O `WHERE` escolhe as linhas antes de os grupos existirem, e ainda não há contagens.

2. Escolhe os grupos com o `HAVING`, depois do `GROUP BY`:

   ```sql
   SELECT tp.nome AS tipo, COUNT(*) AS especies
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   GROUP BY tp.id, tp.nome
   HAVING COUNT(*) > 1
   ORDER BY especies DESC;
   ```

   O que deves ver: duas linhas, a Água, com 4, e a Pedra, com 2. Os três tipos com uma só espécie ficaram de fora.

3. No fim do `relatorios.sql`, acrescenta o relatório e guarda:

   ```sql

   -- Que tipos têm mais de uma espécie?
   -- Esperado: 2 linhas: a Água com 4 e a Pedra com 2.
   SELECT tp.nome AS tipo, COUNT(*) AS especies
   FROM especies AS e
   JOIN tipos AS tp ON e.tipo_id = tp.id
   GROUP BY tp.id, tp.nome
   HAVING COUNT(*) > 1
   ORDER BY especies DESC;
   ```

### Paragem 10

O `relatorios.sql` tem dez relatórios. Corre o `\i relatorios.sql`: a última resposta é a do passo 2, com a Água e a Pedra.

Pensa antes de continuares: o `HAVING COUNT(*) = 1` dava que tipos? A resposta: o Elétrico, o Fogo e a Planta, os três com uma só espécie.

## Fase 11: Uma junção a mais pode multiplicar as contagens

Contas, numa só consulta, os Pokémon de cada treinador e os combates em que foi o líder, e vês as contagens multiplicarem-se. Depois, corriges com o `COUNT(DISTINCT)`. Rever: [Uma junção a mais pode multiplicar as contagens](../04-join-e-agregacao-introdutorios.md#uma-junção-a-mais-pode-multiplicar-as-contagens).

1. Antes de correres, prevê o que deve dar, para cada treinador: quantos Pokémon tem, e em quantos combates foi o líder. Depois, corre:

   ```sql
   SELECT t.nome, COUNT(p.id) AS pokemons, COUNT(c.id) AS liderados
   FROM treinadores AS t
   LEFT JOIN pokemons AS p ON p.treinador_id = t.id
   LEFT JOIN combates AS c ON c.lider_id = t.id
   GROUP BY t.id, t.nome
   ORDER BY t.id;
   ```

   O que deves ver:

   ```text
    nome  | pokemons | liderados
   -------+----------+-----------
    Ash   |        3 |         0
    Misty |        6 |         6
    Brock |        4 |         4
    Gary  |        0 |         0
   (4 rows)
   ```

   A Misty não tem seis Pokémon: tem três, e foi líder em dois combates. Cada um dos três Pokémon dela juntou-se aos dois combates, e as linhas passaram a seis. O Ash, que nunca foi líder, ficou certo: com nenhum combate, os Pokémon dele não se multiplicaram.

2. Conta os valores diferentes, com o `COUNT(DISTINCT)`:

   ```sql
   SELECT t.nome, COUNT(DISTINCT p.id) AS pokemons, COUNT(DISTINCT c.id) AS liderados
   FROM treinadores AS t
   LEFT JOIN pokemons AS p ON p.treinador_id = t.id
   LEFT JOIN combates AS c ON c.lider_id = t.id
   GROUP BY t.id, t.nome
   ORDER BY t.id;
   ```

   O que deves ver: o Ash com 3 e 0, a Misty com 3 e 2, o Brock com 2 e 2, e o Gary com 0 e 0. Cada Pokémon e cada combate contam uma só vez, mesmo repetidos.

3. No fim do `relatorios.sql`, acrescenta o último relatório e guarda:

   ```sql

   -- Quantos Pokémon tem cada treinador, e em quantos combates foi o líder?
   -- Esperado: 4 linhas: o Ash com 3 e 0, a Misty com 3 e 2, o Brock com 2 e 2 e o Gary
   -- com 0 e 0. Sem o DISTINCT, a Misty e o Brock ficavam com os números multiplicados.
   SELECT t.nome, COUNT(DISTINCT p.id) AS pokemons, COUNT(DISTINCT c.id) AS liderados
   FROM treinadores AS t
   LEFT JOIN pokemons AS p ON p.treinador_id = t.id
   LEFT JOIN combates AS c ON c.lider_id = t.id
   GROUP BY t.id, t.nome
   ORDER BY t.id;
   ```

4. Corre o ficheiro inteiro com `\i relatorios.sql`. O que deves ver: onze respostas, uma por relatório, cada uma com o resultado do seu comentário. Se o terminal mostrar `(END)` ou `:` na última linha, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 11

O `relatorios.sql` tem os onze relatórios, cada um com o resultado esperado, como na [versão 04 do exemplo](../../exemplos/sql-fundamentos/pokemon/04-join-e-agregacao-introdutorios/relatorios.sql).

Pensa antes de continuares: como se confirma, sem o `GROUP BY`, que as linhas da Misty se multiplicaram? A resposta: com as duas junções sem o resumo, só para ela, com `WHERE t.nome = 'Misty'`. Aparecem seis linhas, cada Pokémon dela com cada combate em que foi líder.

## Se alguma coisa falhar

1. O Docker Desktop está aberto e o servidor está a correr? Corre `docker compose ps`, no terminal normal, na pasta do projeto: o `db` tem de aparecer com `Up`. Se estiver parado, arranca-o com `docker compose up -d`.
2. Estás na base certa? No `psql`, o início da linha tem de começar por `ginasio`. Se for `pokemon`, sai com o `\q` e entra com `-d ginasio`.
3. O início da linha tem um `-`, como `ginasio-#`? A consulta ainda não acabou, e o `psql` espera pelo resto. Escreve `;` e carrega em Enter.
4. Guardaste o ficheiro? O `\i` corre o ficheiro como está guardado no disco. No VS Code, um ficheiro por guardar tem um círculo no separador, em vez do `X`.

### Os resultados não batem com os comentários

A base não é a que o `dados.sql` constrói: ficou com mudanças do tema 03, ou o teu `dados.sql` não tem as linhas que o tema 03 acrescentou. Corre o `\i esquema.sql` e o `\i dados.sql`. Se o `dados.sql` não acabar em `INSERT 0 2`, `INSERT 0 2` e `INSERT 0 1`, copia o [`dados.sql` da versão 03 do exemplo](../../exemplos/sql-fundamentos/pokemon/03-dml-e-consultas-com-contexto/dados.sql) para a tua pasta e corre os dois ficheiros outra vez.

### `missing FROM-clause entry for table "p"`

A consulta usa um nome curto que não foi dado, como o `p.id` sem o `AS p` a seguir a `pokemons`, ou que só entra num `JOIN` mais abaixo. Confirma que cada nome curto do `SELECT`, do `ON` e do `WHERE` está dado no `FROM` ou num `JOIN` que vem antes dele.

### `syntax error at or near "SELECT"`

Falta o ponto e vírgula no fim da consulta de cima, e o `psql` juntou-a à de baixo. Nenhuma das duas correu. No ficheiro, a mensagem começa por `psql:relatorios.sql:` e diz a linha onde acaba a consulta que falhou. Fecha com `;` a consulta de cima dessa linha, guarda e corre o `\i` outra vez.

### `column "especies" does not exist`

O `WHERE` ou o `HAVING` usam o nome que o `AS` deu a uma coluna da resposta, como em `HAVING especies > 1`. Esse nome só existe na resposta, e só o `ORDER BY` o aceita. Repete a função: `HAVING COUNT(*) > 1`.

### `relatorios.sql: No such file or directory`

O `psql` não encontrou o ficheiro na pasta do projeto. Escreve `\! ls` no `psql` e procura-o na lista. Se o nome for outro, como `relatorio.sql` ou `relatorios.sql.txt`, corrige-o no painel Explorer.

### O terminal mostra `(END)` ou `:` na última linha

A resposta é maior do que o terminal, e o `psql` mostra-a por páginas. Lê-a, carrega na barra de espaço para veres o resto e, no fim, em `q`. Ao carregares em `q`, a resposta sai do ecrã. Com o `\i`, isto repete-se em cada resposta grande. Para o `psql` mostrar tudo de seguida, escreve outra vez o `\pset pager off` do passo 4 de [Preparar o projeto](#preparar-o-projeto): dura só até saíres.

## Desafios

1. Escreve o relatório dos combates com o nome do desafiante, do líder e do vencedor, e junta-o ao `relatorios.sql`, com o resultado esperado. Os quatro combates têm de aparecer, também o 3, que ainda não tem vencedor.
2. Escreve o relatório da vida média dos Pokémon de cada treinador, com uma casa decimal. Tem todos os treinadores, do que tem a média mais alta para o que tem a mais baixa. Explica num comentário o que aparece na linha do Gary.
3. Escreve o relatório do número de Pokémon de cada tipo, com os cinco tipos. Pista: os Pokémon não têm uma coluna para o tipo, como viste na fase 3.

## Antes de terminares

- [ ] O `relatorios.sql` tem os onze relatórios das fases, cada um com o comentário do resultado esperado.
- [ ] Numa base acabada de construir pelo `esquema.sql` e pelo `dados.sql`, o `\i relatorios.sql` dá os resultados dos comentários.
- [ ] Sabes dizer, antes de correres uma junção, quantas linhas esperas, e se precisas do `JOIN` ou do `LEFT JOIN`.
- [ ] No fim da aula, paras o servidor com `docker compose stop`, no terminal normal, na pasta do projeto.

![Rodapé](../../imagens/rodape.png)
