![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: DML e consultas com contexto

## O que vais construir

Vais guardar num ficheiro novo, o `perguntas.sql`, as perguntas à base `ginasio`, cada uma com a consulta e o resultado esperado. Depois, mudas e apagas dados no `psql`, também dentro de transações, que deixam desfazer um engano. No fim, a pasta do projeto tem estes ficheiros:

```text
pokemon-sql/
├── .env
├── .gitignore
├── compose.yaml
├── dados.sql
├── esquema.sql
├── perguntas.sql
├── pokemon.sql
└── recusas.sql
```

1. [Fase 1: O WHERE escolhe as linhas](#fase-1-o-where-escolhe-as-linhas)
2. [Fase 2: As comparações servem para números, textos e datas](#fase-2-as-comparações-servem-para-números-textos-e-datas)
3. [Fase 3: O AND, o OR e o NOT juntam condições](#fase-3-o-and-o-or-e-o-not-juntam-condições)
4. [Fase 4: O IS NULL encontra o que não tem valor](#fase-4-o-is-null-encontra-o-que-não-tem-valor)
5. [Fase 5: O BETWEEN escolhe um intervalo](#fase-5-o-between-escolhe-um-intervalo)
6. [Fase 6: O IN escolhe de uma lista](#fase-6-o-in-escolhe-de-uma-lista)
7. [Fase 7: O LIKE procura um padrão num texto](#fase-7-o-like-procura-um-padrão-num-texto)
8. [Fase 8: O ORDER BY ordena o resultado](#fase-8-o-order-by-ordena-o-resultado)
9. [Fase 9: O LIMIT corta o resultado](#fase-9-o-limit-corta-o-resultado)
10. [Fase 10: O UPDATE muda as linhas que o WHERE escolhe](#fase-10-o-update-muda-as-linhas-que-o-where-escolhe)
11. [Fase 11: O DELETE apaga linhas](#fase-11-o-delete-apaga-linhas)
12. [Fase 12: Uma transação deixa desfazer as mudanças](#fase-12-uma-transação-deixa-desfazer-as-mudanças)
13. [Fase 13: Um erro a meio desfaz a transação inteira](#fase-13-um-erro-a-meio-desfaz-a-transação-inteira)

## O que precisas

- O Docker Desktop, aberto: o `docker info`, no terminal, responde sem erro.
- O VS Code, onde escreves os ficheiros e abres o terminal.
- A pasta `pokemon-sql` do laboratório do tema 02, com a base `ginasio`, o `esquema.sql` e o `dados.sql`. Se não a tiveres, cria-a como diz o "Como correr" da [versão 02 do exemplo dos Pokémon](../../exemplos/sql-fundamentos/pokemon/README.md#como-correr-a-versão-02), e volta aqui.

## Preparar o projeto

1. Abre a pasta `pokemon-sql` no VS Code e abre um terminal, no menu Terminal, com a opção New Terminal. Arranca o servidor, se estiver parado:

   ```bash
   docker compose up -d
   ```

   O que deves ver, no fim: a linha do servidor, `pokemon-sql-db-1`, com `Running` ou `Started`.

2. As perguntas deste laboratório precisam de mais Pokémon KO e de mais um combate. No fim do teu `dados.sql`, acrescenta estas linhas e guarda:

   ```sql

   -- Mais duas espécies, dois Pokémon KO, um do Brock e outro da Misty, e mais um combate.
   -- Entram no fim, para os números das linhas que já lá estavam não mudarem.
   INSERT INTO especies (nome, tipo_id) VALUES
       ('Geodude', 5),      -- 8
       ('Staryu', 2);       -- 9

   INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES
       (8, 3, NULL, 0, 30),       -- 7, o Geodude do Brock, KO
       (9, 2, NULL, 0, 25);       -- 8, o Staryu da Misty, KO

   -- A Misty desafiou o Brock no ginásio de Pewter, e o Brock venceu.
   INSERT INTO combates (data, cidade, desafiante_id, lider_id, vencedor_id) VALUES
       ('2026-11-17', 'Pewter', 2, 3, 3);    -- 4
   ```

   São `INSERT` como os do tema 02. As espécies entram antes dos Pokémon que apontam para elas.

3. Entra no `psql`, na base `ginasio`:

   ```bash
   docker compose exec db psql -U postgres -d ginasio
   ```

   O que deves ver: o início da linha é `ginasio=#`.

4. Reconstrói a base com os dois ficheiros, pela ordem de sempre:

   ```text
   \i esquema.sql
   \i dados.sql
   ```

   O que deves ver: os cinco `DROP TABLE` e os cinco `CREATE TABLE` do esquema, e oito linhas `INSERT`, a acabar em `INSERT 0 2`, `INSERT 0 2` e `INSERT 0 1`, que são as linhas novas. Se aparecer um `ERROR` no `dados.sql`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

5. No painel Explorer do VS Code, cria o ficheiro `perguntas.sql`, na pasta do projeto, com estas linhas de comentário, e guarda-o. As consultas entram por baixo, uma em cada fase:

   ```sql
   -- perguntas.sql: perguntas sobre o ginásio, cada uma com a consulta que a responde.
   -- Corre-se no psql, ligado à base ginasio, com \i perguntas.sql, numa base acabada
   -- de construir pelo esquema.sql e pelo dados.sql. Cada comentário diz o resultado esperado.
   ```

## Fase 1: O WHERE escolhe as linhas

Fazes a primeira pergunta com o `WHERE`, que deixa na resposta só as linhas que cumprem uma condição. Rever: [O WHERE escolhe as linhas](../03-dml-e-consultas-com-contexto.md#o-where-escolhe-as-linhas).

1. No `psql`, pede os Pokémon do Ash, que é o treinador 1:

   ```sql
   SELECT * FROM pokemons WHERE treinador_id = 1;
   ```

   O que deves ver:

   ```text
    id | especie_id | treinador_id | alcunha | vida | ataque
   ----+------------+--------------+---------+------+--------
     1 |          1 |            1 |         |   90 |     40
     2 |          3 |            1 |         |  110 |     25
     3 |          4 |            1 | Pika    |   80 |     45
   (3 rows)
   ```

   Das oito linhas da tabela, ficaram as três em que o `treinador_id` é 1. Os comentários do teu `dados.sql` dizem que Pokémon é cada número: o 3, por exemplo, é o Pikachu do Ash.

2. Antes de correres, prevê o tamanho da resposta desta consulta, em linhas e em colunas:

   ```sql
   SELECT alcunha, vida FROM pokemons WHERE treinador_id = 1;
   ```

   O que deves ver: três linhas e duas colunas, a `alcunha` e a `vida`. O `WHERE` escolheu as mesmas três linhas, e o `SELECT` ficou só com as duas colunas que pediste.

3. No fim do `perguntas.sql`, acrescenta a primeira pergunta e guarda:

   ```sql

   -- Que Pokémon tem o Ash, o treinador 1?
   -- Esperado: 3 linhas, os Pokémon 1, 2 e 3.
   SELECT * FROM pokemons WHERE treinador_id = 1;
   ```

4. Corre o ficheiro com `\i perguntas.sql`. O que deves ver: a mesma resposta do passo 1. Se aparecer `perguntas.sql: No such file or directory`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

O `perguntas.sql` tem a primeira pergunta, e o `\i` corre-a.

Pensa antes de continuares: o `WHERE` tirou cinco Pokémon da tabela? A resposta: não. O `WHERE` só escolhe o que entra na resposta. O `SELECT * FROM pokemons;` continua a mostrar os oito.

## Fase 2: As comparações servem para números, textos e datas

Usas as comparações com um texto e com uma data, que se escrevem entre plicas. Rever: [As comparações servem para números, textos e datas](../03-dml-e-consultas-com-contexto.md#as-comparações-servem-para-números-textos-e-datas).

1. Pede os treinadores de Pallet:

   ```sql
   SELECT * FROM treinadores WHERE cidade = 'Pallet';
   ```

   O que deves ver: duas linhas, o Ash e o Gary.

2. Provoca um engano de propósito: escreve a cidade com o p pequeno.

   ```sql
   SELECT * FROM treinadores WHERE cidade = 'pallet';
   ```

   O que deves ver: os nomes das colunas e `(0 rows)`, sem erro. A consulta está bem escrita, mas o `=` compara os textos letra a letra, e nenhuma cidade se escreve assim.

3. Pede os combates de 10 de novembro em diante:

   ```sql
   SELECT * FROM combates WHERE data >= '2026-11-10';
   ```

   O que deves ver: duas linhas, os combates 3 e 4. O combate 3 é do próprio dia 10, que o `>=` inclui.

4. No fim do `perguntas.sql`, acrescenta as duas perguntas e guarda:

   ```sql

   -- Que treinadores são de Pallet?
   -- Esperado: 2 linhas, o Ash e o Gary.
   SELECT * FROM treinadores WHERE cidade = 'Pallet';

   -- Que combates houve de 10 de novembro em diante?
   -- Esperado: 2 linhas, os combates 3 e 4.
   SELECT * FROM combates WHERE data >= '2026-11-10';
   ```

### Paragem 2

O `perguntas.sql` tem três perguntas, uma com um número, uma com um texto e uma com uma data.

Pensa antes de continuares: com o `>` em vez do `>=`, quantos combates dava a terceira pergunta? A resposta: um só, o combate 4. O `>` deixa de fora o próprio dia 10.

## Fase 3: O AND, o OR e o NOT juntam condições

O `AND` pede as duas condições verdadeiras, e ao `OR` basta uma. Juntas os dois numa condição e vês porque é que os parênteses fazem falta. Rever: [O AND, o OR e o NOT juntam condições](../03-dml-e-consultas-com-contexto.md#o-and-o-or-e-o-not-juntam-condições).

1. Queres os Pokémon KO da Misty ou do Brock, os treinadores 2 e 3. Antes de correres, prevê quantas linhas dá esta consulta:

   ```sql
   SELECT * FROM pokemons WHERE vida = 0 AND treinador_id = 2 OR treinador_id = 3;
   ```

   O que deves ver: quatro linhas, os Pokémon 4, 6, 7 e 8. O Pokémon 6 é o Onix do Brock, que tem a vida 140 e não está KO. O `AND` foi feito primeiro, e a condição ficou "(vida 0 e treinador 2) ou treinador 3": todos os Pokémon do Brock entraram.

2. Põe o `OR` entre parênteses, para ser feito primeiro:

   ```sql
   SELECT * FROM pokemons WHERE vida = 0 AND (treinador_id = 2 OR treinador_id = 3);
   ```

   O que deves ver: três linhas, os Pokémon 4, 7 e 8, todos com a vida 0. O Onix já não aparece.

3. No fim do `perguntas.sql`, acrescenta a pergunta, com os parênteses, e guarda:

   ```sql

   -- Que Pokémon da Misty ou do Brock estão KO?
   -- Esperado: 3 linhas, os Pokémon 4, 7 e 8. Sem os parênteses, aparecia também o Onix
   -- do Brock, que tem vida.
   SELECT * FROM pokemons WHERE vida = 0 AND (treinador_id = 2 OR treinador_id = 3);
   ```

### Paragem 3

O `perguntas.sql` tem quatro perguntas. A última junta três condições, com os parênteses no sítio certo.

Pensa antes de continuares: o que dá o `SELECT * FROM treinadores WHERE NOT cidade = 'Pallet';`? A resposta: a Misty e o Brock. O `NOT` troca o verdadeiro pelo falso, e dá o mesmo que o `cidade <> 'Pallet'`.

## Fase 4: O IS NULL encontra o que não tem valor

Procuras as linhas sem valor numa coluna, primeiro com o `= NULL`, que não funciona, e depois com o `IS NULL`. Rever: [O IS NULL encontra o que não tem valor](../03-dml-e-consultas-com-contexto.md#o-is-null-encontra-o-que-não-tem-valor).

1. Pede ao `psql` que escreva o NULL, como no tema 01, com `\pset null '(nulo)'`. O que deves ver: `Null display is "(nulo)".`.

2. Provoca um engano de propósito: procura os combates sem vencedor com o `=`.

   ```sql
   SELECT * FROM combates WHERE vencedor_id = NULL;
   ```

   O que deves ver: `(0 rows)`. A comparação com o NULL nunca é verdadeira, e o `WHERE` não deixa entrar nenhuma linha.

3. Troca o `= NULL` pelo `IS NULL`:

   ```sql
   SELECT * FROM combates WHERE vencedor_id IS NULL;
   ```

   O que deves ver:

   ```text
    id |    data    | cidade | desafiante_id | lider_id | vencedor_id
   ----+------------+--------+---------------+----------+-------------
     3 | 2026-11-10 | Pewter |             1 |        3 |      (nulo)
   (1 row)
   ```

4. Pede os Pokémon sem alcunha, com `SELECT * FROM pokemons WHERE alcunha IS NULL;`. O que deves ver: seis linhas, com `(nulo)` na alcunha. O Pikachu, com a alcunha Pika, e o Psyduck, com a alcunha vazia, não aparecem.

5. No fim do `perguntas.sql`, acrescenta as duas perguntas e guarda. O `\pset` fica de fora, porque o ficheiro só tem SQL:

   ```sql

   -- Que combates ainda não acabaram?
   -- Esperado: 1 linha, o combate 3, sem vencedor.
   SELECT * FROM combates WHERE vencedor_id IS NULL;

   -- Que Pokémon não têm alcunha?
   -- Esperado: 6 linhas. O Pikachu, com a alcunha Pika, e o Psyduck, com a alcunha vazia,
   -- não aparecem.
   SELECT * FROM pokemons WHERE alcunha IS NULL;
   ```

### Paragem 4

O `perguntas.sql` tem seis perguntas. Corre o `\i perguntas.sql`: as duas últimas respostas são as dos passos 3 e 4, com uma linha e com seis.

Pensa antes de continuares: porque é que o Psyduck não aparece nos Pokémon sem alcunha? A resposta: a alcunha dele é um texto vazio, `''`, que é um valor. O `IS NULL` só escolhe as linhas onde não há valor nenhum.

## Fase 5: O BETWEEN escolhe um intervalo

Escolhes os Pokémon com o ataque num intervalo, com o `BETWEEN`, que inclui os dois limites. Rever: [O BETWEEN escolhe um intervalo](../03-dml-e-consultas-com-contexto.md#o-between-escolhe-um-intervalo).

1. Pede os Pokémon com o ataque de 30 a 40:

   ```sql
   SELECT * FROM pokemons WHERE ataque BETWEEN 30 AND 40;
   ```

   O que deves ver: quatro linhas, os Pokémon 1, 4, 6 e 7. O Charmander, com 40, e o Onix e o Geodude, com 30, estão na resposta: o `BETWEEN` inclui os limites.

2. Provoca um engano de propósito: troca os limites, com `BETWEEN 40 AND 30`. O que deves ver: `(0 rows)`. O limite de baixo tem de vir primeiro.

3. No fim do `perguntas.sql`, acrescenta a pergunta e guarda:

   ```sql

   -- Que Pokémon têm o ataque de 30 a 40?
   -- Esperado: 4 linhas, os Pokémon 1, 4, 6 e 7. O BETWEEN inclui o 30 e o 40.
   SELECT * FROM pokemons WHERE ataque BETWEEN 30 AND 40;
   ```

### Paragem 5

O `perguntas.sql` tem sete perguntas.

Pensa antes de continuares: como escreves a mesma condição sem o `BETWEEN`? A resposta: `ataque >= 30 AND ataque <= 40`. O `BETWEEN` é a forma curta destas duas comparações.

## Fase 6: O IN escolhe de uma lista

Escolhes as espécies de dois tipos com o `IN`, em vez de dois `OR`. Rever: [O IN escolhe de uma lista](../03-dml-e-consultas-com-contexto.md#o-in-escolhe-de-uma-lista).

1. Pede as espécies de Água ou de Pedra, que são os tipos 2 e 5:

   ```sql
   SELECT * FROM especies WHERE tipo_id IN (2, 5);
   ```

   O que deves ver: seis linhas, o Squirtle, o Starmie, o Psyduck, o Onix, o Geodude e o Staryu. Cada uma tem o `tipo_id` 2 ou 5.

2. No fim do `perguntas.sql`, acrescenta a pergunta e guarda:

   ```sql

   -- Que espécies são de Água ou de Pedra, os tipos 2 e 5?
   -- Esperado: 6 linhas, as espécies 2, 5, 6, 7, 8 e 9.
   SELECT * FROM especies WHERE tipo_id IN (2, 5);
   ```

### Paragem 6

O `perguntas.sql` tem oito perguntas.

Pensa antes de continuares: que espécies dá o `WHERE tipo_id NOT IN (2, 5)`? A resposta: as três que sobram, o Charmander, o Bulbasaur e o Pikachu.

## Fase 7: O LIKE procura um padrão num texto

Procuras as espécies pelo nome com o `LIKE`, em que o `%` vale por qualquer sequência de letras. Rever: [O LIKE procura um padrão num texto](../03-dml-e-consultas-com-contexto.md#o-like-procura-um-padrão-num-texto).

1. Provoca um engano de propósito: procura as espécies que começam por S com o `*`, como nos nomes de ficheiros, em `*.sql`.

   ```sql
   SELECT * FROM especies WHERE nome LIKE 'S*';
   ```

   O que deves ver: `(0 rows)`. No `LIKE`, o `*` é uma letra como as outras, e nenhum nome é "S*".

2. Troca o `*` pelo `%`, com `LIKE 'S%'`. O que deves ver: três linhas, o Squirtle, o Starmie e o Staryu.

3. Pede as espécies que têm um u em qualquer sítio do nome:

   ```sql
   SELECT * FROM especies WHERE nome LIKE '%u%';
   ```

   O que deves ver: seis linhas, o Squirtle, o Bulbasaur, o Pikachu, o Psyduck, o Geodude e o Staryu. O `%` dos dois lados aceita letras antes e depois do u, e também nenhuma.

4. No fim do `perguntas.sql`, acrescenta a pergunta e guarda:

   ```sql

   -- Que espécies têm um u no nome?
   -- Esperado: 6 linhas, o Squirtle, o Bulbasaur, o Pikachu, o Psyduck, o Geodude e o Staryu.
   SELECT * FROM especies WHERE nome LIKE '%u%';
   ```

### Paragem 7

O `perguntas.sql` tem nove perguntas. Corre o `\i perguntas.sql`: a última resposta é a do passo 3, com seis espécies.

Pensa antes de continuares: quantas espécies dá o `LIKE '%U%'`, com o U grande? A resposta: nenhuma. As maiúsculas contam, e nenhum nome tem um U grande.

## Fase 8: O ORDER BY ordena o resultado

Ordenas os Pokémon pelo ataque e resolves os empates com uma segunda coluna. Rever: [O ORDER BY ordena o resultado](../03-dml-e-consultas-com-contexto.md#o-order-by-ordena-o-resultado).

1. Pede os Pokémon do ataque mais alto para o mais baixo:

   ```sql
   SELECT * FROM pokemons ORDER BY ataque DESC;
   ```

   O que deves ver: as oito linhas, a começar no Pikachu do Ash, com 45, e a acabar no Psyduck, com 20. Há dois empates: o Onix e o Geodude têm 30, e o Staryu e o Bulbasaur têm 25. A ordem entre eles não está garantida.

2. Desempata pelo `id`:

   ```sql
   SELECT * FROM pokemons ORDER BY ataque DESC, id;
   ```

   O que deves ver: a mesma ordem, mas com o Bulbasaur, o `id` 2, antes do Staryu, o `id` 8. O `DESC` vale só para o ataque, e o `id` fica a subir.

3. No fim do `perguntas.sql`, acrescenta a pergunta e guarda:

   ```sql

   -- Os Pokémon, do ataque mais alto para o mais baixo. Nos empates, o id desempata.
   -- Esperado: 8 linhas, do Pikachu do Ash, com 45, ao Psyduck da Misty, com 20.
   SELECT * FROM pokemons ORDER BY ataque DESC, id;
   ```

### Paragem 8

O `perguntas.sql` tem dez perguntas, e a última dá sempre a mesma ordem.

Pensa antes de continuares: que ordem dá o `ORDER BY ataque`, sem o `DESC`? A resposta: do menor para o maior, a começar no Psyduck, com 20, e a acabar no Pikachu, com 45.

## Fase 9: O LIMIT corta o resultado

Ficas só com os primeiros da lista, com o `LIMIT`, e experimentas a forma do SQL Server, que o PostgreSQL não conhece. Rever: [O LIMIT corta o resultado](../03-dml-e-consultas-com-contexto.md#o-limit-corta-o-resultado) e [O Transact-SQL escreve o LIMIT de outra maneira](../03-dml-e-consultas-com-contexto.md#o-transact-sql-escreve-o-limit-de-outra-maneira).

1. Pede os três Pokémon com mais vida:

   ```sql
   SELECT * FROM pokemons ORDER BY vida DESC LIMIT 3;
   ```

   O que deves ver: três linhas, o Onix do Brock, com 140, o Bulbasaur do Ash, com 110, e o Psyduck da Misty, com 100. O servidor ordenou os oito pela vida e cortou depois do terceiro.

2. Experimenta a mesma pergunta como se escreve no SQL Server, com o `TOP`:

   ```sql
   SELECT TOP 3 * FROM pokemons ORDER BY vida DESC;
   ```

   O que deves ver: `ERROR:  syntax error at or near "3"`. O `TOP` é do Transact-SQL, o dialeto do SQL Server, e o PostgreSQL não o conhece.

3. No fim do `perguntas.sql`, acrescenta a última pergunta e guarda:

   ```sql

   -- Quais são os três Pokémon com mais vida?
   -- Esperado: 3 linhas, os Pokémon 6, 2 e 5, com 140, 110 e 100.
   SELECT * FROM pokemons ORDER BY vida DESC LIMIT 3;
   ```

4. Corre o ficheiro inteiro com `\i perguntas.sql`. O que deves ver: onze respostas, uma por pergunta, cada uma com o número de linhas do seu comentário. Se o terminal mostrar `(END)` ou `:` na última linha, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 9

O `perguntas.sql` está completo, como deve estar agora:

```sql
-- perguntas.sql: perguntas sobre o ginásio, cada uma com a consulta que a responde.
-- Corre-se no psql, ligado à base ginasio, com \i perguntas.sql, numa base acabada
-- de construir pelo esquema.sql e pelo dados.sql. Cada comentário diz o resultado esperado.

-- Que Pokémon tem o Ash, o treinador 1?
-- Esperado: 3 linhas, os Pokémon 1, 2 e 3.
SELECT * FROM pokemons WHERE treinador_id = 1;

-- Que treinadores são de Pallet?
-- Esperado: 2 linhas, o Ash e o Gary.
SELECT * FROM treinadores WHERE cidade = 'Pallet';

-- Que combates houve de 10 de novembro em diante?
-- Esperado: 2 linhas, os combates 3 e 4.
SELECT * FROM combates WHERE data >= '2026-11-10';

-- Que Pokémon da Misty ou do Brock estão KO?
-- Esperado: 3 linhas, os Pokémon 4, 7 e 8. Sem os parênteses, aparecia também o Onix
-- do Brock, que tem vida.
SELECT * FROM pokemons WHERE vida = 0 AND (treinador_id = 2 OR treinador_id = 3);

-- Que combates ainda não acabaram?
-- Esperado: 1 linha, o combate 3, sem vencedor.
SELECT * FROM combates WHERE vencedor_id IS NULL;

-- Que Pokémon não têm alcunha?
-- Esperado: 6 linhas. O Pikachu, com a alcunha Pika, e o Psyduck, com a alcunha vazia,
-- não aparecem.
SELECT * FROM pokemons WHERE alcunha IS NULL;

-- Que Pokémon têm o ataque de 30 a 40?
-- Esperado: 4 linhas, os Pokémon 1, 4, 6 e 7. O BETWEEN inclui o 30 e o 40.
SELECT * FROM pokemons WHERE ataque BETWEEN 30 AND 40;

-- Que espécies são de Água ou de Pedra, os tipos 2 e 5?
-- Esperado: 6 linhas, as espécies 2, 5, 6, 7, 8 e 9.
SELECT * FROM especies WHERE tipo_id IN (2, 5);

-- Que espécies têm um u no nome?
-- Esperado: 6 linhas, o Squirtle, o Bulbasaur, o Pikachu, o Psyduck, o Geodude e o Staryu.
SELECT * FROM especies WHERE nome LIKE '%u%';

-- Os Pokémon, do ataque mais alto para o mais baixo. Nos empates, o id desempata.
-- Esperado: 8 linhas, do Pikachu do Ash, com 45, ao Psyduck da Misty, com 20.
SELECT * FROM pokemons ORDER BY ataque DESC, id;

-- Quais são os três Pokémon com mais vida?
-- Esperado: 3 linhas, os Pokémon 6, 2 e 5, com 140, 110 e 100.
SELECT * FROM pokemons ORDER BY vida DESC LIMIT 3;
```

Cada pergunta tem a consulta que a responde e o resultado esperado. Os comentários valem para a base que o `esquema.sql` e o `dados.sql` constroem.

Pensa antes de continuares: o que dava o `LIMIT 3` sem o `ORDER BY`? A resposta: três Pokémon quaisquer, os primeiros do caminho que o servidor escolheu. Sem a ordem, "os três primeiros" não quer dizer nada.

## Fase 10: O UPDATE muda as linhas que o WHERE escolhe

Dás uma medalha ao Ash com o `UPDATE`, depois de veres, com um `SELECT`, a linha que vai mudar. Rever: [O UPDATE muda as linhas que o WHERE escolhe](../03-dml-e-consultas-com-contexto.md#o-update-muda-as-linhas-que-o-where-escolhe) e [Antes de mudar, o mesmo WHERE num SELECT](../03-dml-e-consultas-com-contexto.md#antes-de-mudar-o-mesmo-where-num-select).

1. O Ash venceu o combate 2 e ganhou uma medalha. Antes de mudares, vê a linha que vai mudar:

   ```sql
   SELECT * FROM treinadores WHERE id = 1;
   ```

   O que deves ver: uma linha, o Ash, com 0 medalhas. É esta, e só esta, que o `UPDATE` vai mudar.

2. Muda-a, com o mesmo `WHERE`:

   ```sql
   UPDATE treinadores SET medalhas = medalhas + 1 WHERE id = 1;
   ```

   O que deves ver: `UPDATE 1`. Bate com a linha do `SELECT`.

3. Vê todos os treinadores, com `SELECT * FROM treinadores;`. O que deves ver:

   ```text
    id | nome  |  cidade  | medalhas
   ----+-------+----------+----------
     2 | Misty | Cerulean |        0
     3 | Brock | Pewter   |        0
     4 | Gary  | Pallet   |        0
     1 | Ash   | Pallet   |        1
   (4 rows)
   ```

   O Ash tem 1 medalha, e passou para o fim da lista. Uma linha mudada pode mudar de lugar, porque a ordem sem `ORDER BY` não está garantida. Com `ORDER BY id`, o Ash volta ao princípio.

4. Provoca um erro de propósito: dá nove medalhas ao Ash.

   ```sql
   UPDATE treinadores SET medalhas = 9 WHERE id = 1;
   ```

   O que deves ver: `ERROR:  new row for relation "treinadores" violates check constraint "treinadores_medalhas_check"`. O `CHECK` do tema 02 também verifica as linhas que mudam, e o Ash fica com 1 medalha.

### Paragem 10

O Ash tem 1 medalha, e a base recusou a mudança que passava das oito.

Pensa antes de continuares: o que fazia o `UPDATE treinadores SET medalhas = medalhas + 1;`, sem o `WHERE`? A resposta: dava uma medalha a cada um dos quatro treinadores, com `UPDATE 4`. Por isso se corre primeiro o `SELECT` com o `WHERE`.

## Fase 11: O DELETE apaga linhas

Apagas um combate cancelado com o `DELETE` e vês a chave estrangeira recusar o `DELETE` de um treinador. Rever: [O DELETE apaga linhas](../03-dml-e-consultas-com-contexto.md#o-delete-apaga-linhas).

1. O combate 3 foi cancelado. Vê primeiro a linha que vai sair, com `SELECT * FROM combates WHERE id = 3;`. O que deves ver: uma linha, o combate do Ash contra o Brock, sem vencedor.

2. Apaga-a, com o mesmo `WHERE`:

   ```sql
   DELETE FROM combates WHERE id = 3;
   ```

   O que deves ver: `DELETE 1`. O `SELECT * FROM combates;` mostra agora três combates, o 1, o 2 e o 4.

3. Provoca um erro de propósito: apaga o Brock, que tem Pokémon.

   ```sql
   DELETE FROM treinadores WHERE id = 3;
   ```

   O que deves ver:

   ```text
   ERROR:  update or delete on table "treinadores" violates foreign key constraint "pokemons_treinador_id_fkey" on table "pokemons"
   DETAIL:  Key (id)=(3) is still referenced from table "pokemons".
   ```

   O Onix e o Geodude apontam para o Brock, e a base não o deixa sair.

4. Corre o `\i perguntas.sql`. O que deves ver: duas respostas já não batem com os comentários. A dos combates de 10 de novembro em diante dá só o combate 4, e a dos combates por acabar dá `(0 rows)`. A dos treinadores de Pallet continua a bater, mas com o Gary primeiro e o Ash com 1 medalha. As perguntas valem para a base que o `dados.sql` constrói, e esta já mudou.

5. Reconstrói a base, com `\i esquema.sql` e `\i dados.sql`, e corre outra vez o `\i perguntas.sql`. O que deves ver: as onze respostas voltam a bater com os comentários. O combate 3 voltou, e o Ash voltou a ter 0 medalhas.

### Paragem 11

A base está outra vez como o `dados.sql` a constrói, e o `perguntas.sql` dá os resultados dos comentários.

Pensa antes de continuares: o passo 5 desfez o `DELETE`, mas também a medalha do Ash, que estava certa. Havia maneira de desfazer só o `DELETE`? A resposta: depois de feito, não. Para se poder desfazer, uma mudança faz-se dentro de uma transação, aberta antes dela com o `BEGIN`.

## Fase 12: Uma transação deixa desfazer as mudanças

Fazes de propósito um `UPDATE` sem `WHERE` dentro de uma transação e desfazes com o `ROLLBACK`. Depois, confirmas uma mudança certa com o `COMMIT`. Rever: [Uma transação deixa desfazer as mudanças](../03-dml-e-consultas-com-contexto.md#uma-transação-deixa-desfazer-as-mudanças).

1. Abre uma transação:

   ```sql
   BEGIN;
   ```

   O que deves ver: `BEGIN`, e o início da linha passa a `ginasio=*#`. O asterisco diz que estás dentro de uma transação.

2. Provoca um estrago de propósito: um `UPDATE` sem `WHERE`.

   ```sql
   UPDATE pokemons SET vida = 100;
   ```

   O que deves ver: `UPDATE 8`. Os oito Pokémon mudaram.

3. Confirma o estrago, com `SELECT id, vida FROM pokemons ORDER BY id;`. O que deves ver: os oito com a vida 100, também os três KO e o Onix, que tinha 140.

4. Desfaz tudo:

   ```sql
   ROLLBACK;
   ```

   O que deves ver: `ROLLBACK`, e o início da linha volta a `ginasio=#`. Corre outra vez o `SELECT id, vida FROM pokemons ORDER BY id;`: cada Pokémon tem a vida de antes, do 90 do Charmander ao 0 do Staryu.

5. A reconstrução da fase 11 tirou ao Ash a medalha do combate 2, que estava certa. Devolve-lha, numa transação inteira, confirmada no fim:

   ```sql
   BEGIN;
   UPDATE treinadores SET medalhas = medalhas + 1 WHERE id = 1;
   SELECT * FROM treinadores WHERE id = 1;
   COMMIT;
   ```

   O que deves ver: `BEGIN`, `UPDATE 1`, a linha do Ash com 1 medalha e, por fim, `COMMIT`. O início da linha volta a `ginasio=#`, e a medalha fica guardada.

### Paragem 12

O `UPDATE` sem `WHERE` foi desfeito, e a medalha do Ash ficou guardada.

Pensa antes de continuares: se escreveres agora `ROLLBACK`, a medalha do Ash desaparece? A resposta: não. O `COMMIT` já fechou a transação, e o `ROLLBACK` só desfaz uma transação aberta. O `psql` responde com o aviso `WARNING:  there is no transaction in progress`, "não há nenhuma transação a decorrer".

## Fase 13: Um erro a meio desfaz a transação inteira

Fazes uma transação com dois `UPDATE`, em que o segundo falha, e vês que o primeiro também é desfeito. Rever: [Um erro a meio desfaz a transação inteira](../03-dml-e-consultas-com-contexto.md#um-erro-a-meio-desfaz-a-transação-inteira).

1. O Ash e o Gary venceram, cada um, o líder de outro ginásio, e ganham uma medalha cada. São duas mudanças, que têm de ficar as duas. Abre uma transação e dá a medalha ao Ash:

   ```sql
   BEGIN;
   UPDATE treinadores SET medalhas = medalhas + 1 WHERE id = 1;
   ```

   O que deves ver: `BEGIN` e `UPDATE 1`. O início da linha é `ginasio=*#`.

2. Provoca um erro de propósito, na mesma transação: na medalha do Gary, escreve `9` em vez de `medalhas + 1`.

   ```sql
   UPDATE treinadores SET medalhas = 9 WHERE id = 4;
   ```

   O que deves ver: o erro do `CHECK`, `treinadores_medalhas_check`, e o início da linha passa a `ginasio=!#`. O `!` quer dizer que esta transação falhou.

3. Tenta ver os treinadores, com `SELECT * FROM treinadores;`. O que deves ver:

   ```text
   ERROR:  current transaction is aborted, commands ignored until end of transaction block
   ```

   A transação falhou, e a base ignora todos os comandos até ela fechar, mesmo um `SELECT`.

4. Fecha-a com `ROLLBACK;` e vê os treinadores, com `SELECT * FROM treinadores ORDER BY id;`. O que deves ver:

   ```text
    id | nome  |  cidade  | medalhas
   ----+-------+----------+----------
     1 | Ash   | Pallet   |        1
     2 | Misty | Cerulean |        0
     3 | Brock | Pewter   |        0
     4 | Gary  | Pallet   |        0
   (4 rows)
   ```

   O Ash tem 1 medalha, a da fase 12, que já estava confirmada. A medalha do primeiro `UPDATE`, que tinha corrido bem, também foi desfeita: senão, o Ash tinha 2.

### Paragem 13

Uma transação com um erro a meio não deixa nada feito: ou ficam todas as mudanças, ou não fica nenhuma.

Pensa antes de continuares: no passo 4, o que acontecia com o `COMMIT;` em vez do `ROLLBACK;`? A resposta: o `psql` respondia `ROLLBACK`. Uma transação que falhou não se confirma, e o resultado era o mesmo.

## Se alguma coisa falhar

1. O Docker Desktop está aberto e o servidor está a correr? Corre `docker compose ps`, no terminal normal, na pasta do projeto: o `db` tem de aparecer com `Up`. Se estiver parado, arranca-o com `docker compose up -d`.
2. Estás na base certa? No `psql`, o início da linha tem de começar por `ginasio`. Se for `pokemon`, sai com o `\q` e entra com `-d ginasio`.
3. O início da linha tem um `*` ou um `!`? Estás dentro de uma transação. Fecha-a com `ROLLBACK;` antes de continuares, a não ser que o passo te mande fazer o `COMMIT`. Se o início da linha tiver também um `-`, como `ginasio-*#`, escreve primeiro `;` e carrega em Enter.
4. Guardaste o ficheiro? O `\i` corre o ficheiro como está guardado no disco. No VS Code, um ficheiro por guardar tem um círculo no separador, em vez do `X`.

### `duplicate key value violates unique constraint` ao correr o `dados.sql`

Correste o `dados.sql` sem correr antes o `esquema.sql`, e as linhas que lá estavam chocaram com as novas. As tabelas sem `UNIQUE` ficaram com linhas repetidas. Corre o `\i esquema.sql`, que deixa as tabelas vazias, e depois o `\i dados.sql`.

### Outro `ERROR` ao correr o `dados.sql`, nas linhas novas

As linhas que acrescentaste em [Preparar o projeto](#preparar-o-projeto) têm um engano. A mensagem diz a linha do ficheiro. Compara-a com o bloco do passo 2: uma vírgula ou uma plica em falta, ou as espécies depois dos Pokémon. Corrige, guarda e corre outra vez o `\i esquema.sql` e o `\i dados.sql`.

### `perguntas.sql: No such file or directory`

O `psql` não encontrou o ficheiro na pasta do projeto. Escreve `\! ls` no `psql` e procura-o na lista. Se o nome for outro, como `pergunta.sql` ou `perguntas.sql.txt`, corrige-o no painel Explorer.

### O `psql` fica à espera, com `ginasio-#` ou `ginasio-*#`

A consulta não tem o ponto e vírgula no fim, e o `psql` está à espera do resto. Escreve `;` e carrega em Enter. O `ginasio-*#` quer dizer o mesmo, dentro de uma transação. Não escrevas logo o `ROLLBACK;`: juntava-se ao comando por acabar e dava um erro de sintaxe.

### O terminal mostra `(END)` ou `:` na última linha

A resposta é maior do que o terminal, e o `psql` mostra-a por páginas. Lê-a, carrega na barra de espaço para veres o resto e, no fim, em `q`. Ao carregares em `q`, a resposta sai do ecrã. Com o `\i`, isto repete-se em cada resposta grande. Para o `psql` mostrar tudo de seguida, escreve `\pset pager off`, que dura até saíres.

### `current transaction is aborted, commands ignored until end of transaction block`

Um comando da transação falhou, e a base ignora os outros até a fechares. Escreve `ROLLBACK;`. As mudanças dessa transação são todas desfeitas, e voltas a `ginasio=#`.

### Um `UPDATE` ou um `DELETE` mudou mais linhas do que devia

O número da resposta, como `UPDATE 8`, é maior do que o do `SELECT` que o devia preceder. Se estavas numa transação, escreve `ROLLBACK;`. Se o `ROLLBACK` responder `WARNING:  there is no transaction in progress`, faltou o `BEGIN`, e a mudança já está feita: reconstrói a base com o `\i esquema.sql` e o `\i dados.sql`.

### O `IS NULL` das alcunhas dá sete Pokémon, com o Psyduck

O teu `esquema.sql` ou o teu `dados.sql` não são os do fim do laboratório do tema 02: o Psyduck tem de ter a alcunha vazia, `''`, e não o NULL. Copia o `esquema.sql` e o `dados.sql` da [versão 03 do exemplo](../../exemplos/sql-fundamentos/pokemon/README.md#como-correr-a-versão-03), que já têm as linhas novas, e corre-os.

### O `\i perguntas.sql` dá resultados diferentes dos comentários

A base já não é a que o `dados.sql` constrói, por causa de um `UPDATE` ou de um `DELETE`. Reconstrói-a com o `\i esquema.sql` e o `\i dados.sql`, e corre outra vez o `\i perguntas.sql`. Se mesmo assim uma resposta não bater, compara a consulta com a do passo da fase.

## Desafios

1. Escreve a pergunta "Em que combates entrou o Ash, como desafiante ou como líder, sem os ter vencido?" e junta-a ao `perguntas.sql`, com o resultado esperado. O combate 3, que ainda não tem vencedor, tem de aparecer.
2. Numa transação, apaga o Gary e a espécie Squirtle. A base deixa, ao contrário do que fez com o Brock. Explica porquê num comentário, no fim do `perguntas.sql`, e desfaz a transação no fim.
3. Escreve a consulta que dá o segundo e o terceiro Pokémon com mais ataque, sem o primeiro. Pista: lê o bloco "Para ires mais longe" de [O LIMIT corta o resultado](../03-dml-e-consultas-com-contexto.md#o-limit-corta-o-resultado).

## Antes de terminares

- [ ] O `perguntas.sql` tem as onze perguntas das fases, cada uma com o comentário do resultado esperado.
- [ ] Numa base acabada de construir pelo `esquema.sql` e pelo `dados.sql`, o `\i perguntas.sql` dá os resultados dos comentários.
- [ ] Sabes, pelo início da linha do `psql`, se estás dentro de uma transação e se ela falhou.
- [ ] A base `ginasio` está como o `dados.sql` a constrói: no fim, corres o `\i esquema.sql` e o `\i dados.sql`.
- [ ] No fim da aula, paras o servidor com `docker compose stop`, no terminal normal, na pasta do projeto.

![Rodapé](../../imagens/rodape.png)
