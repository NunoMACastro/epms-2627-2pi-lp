![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: DDL e integridade

## O que vais construir

Vais criar no teu servidor a base de dados `ginasio` e escrever o `esquema.sql`, que constrói as cinco tabelas do ginásio com as regras que a base garante. Escreves também o `dados.sql`, com os dados do tema 01, e o `recusas.sql`, com linhas que a base tem de recusar. No fim, a pasta do projeto tem estes ficheiros:

```text
pokemon-sql/
├── .env
├── .gitignore
├── compose.yaml
├── dados.sql
├── esquema.sql
├── pokemon.sql
└── recusas.sql
```

1. [Fase 1: Uma base de dados nova começa vazia](#fase-1-uma-base-de-dados-nova-começa-vazia)
2. [Fase 2: O CREATE TABLE escreve uma tabela do modelo](#fase-2-o-create-table-escreve-uma-tabela-do-modelo)
3. [Fase 3: Um ficheiro que se volta a correr começa por apagar](#fase-3-um-ficheiro-que-se-volta-a-correr-começa-por-apagar)
4. [Fase 4: O INSERT acrescenta linhas](#fase-4-o-insert-acrescenta-linhas)
5. [Fase 5: A base pode dar o número da chave primária](#fase-5-a-base-pode-dar-o-número-da-chave-primária)
6. [Fase 6: A chave estrangeira recusa o que não existe](#fase-6-a-chave-estrangeira-recusa-o-que-não-existe)
7. [Fase 7: A ordem das tabelas segue as chaves estrangeiras](#fase-7-a-ordem-das-tabelas-segue-as-chaves-estrangeiras)
8. [Fase 8: O UNIQUE recusa os repetidos](#fase-8-o-unique-recusa-os-repetidos)
9. [Fase 9: O CHECK recusa os valores fora da regra](#fase-9-o-check-recusa-os-valores-fora-da-regra)
10. [Fase 10: O ALTER TABLE muda uma tabela sem perder os dados](#fase-10-o-alter-table-muda-uma-tabela-sem-perder-os-dados)

## O que precisas

- O Docker Desktop, aberto.
- O VS Code, onde escreves os ficheiros e abres o terminal.
- A pasta `pokemon-sql` do laboratório do tema 01, com o servidor a funcionar. Se não a tiveres, cria-a como diz o "Como correr" da [versão 01 do exemplo dos Pokémon](../../exemplos/sql-fundamentos/pokemon/README.md#como-correr-a-versão-01), e volta aqui. Se tens o `consultas.sql` do tema 01, pode ficar na pasta; este laboratório não o usa.

## Preparar o projeto

1. Abre a pasta `pokemon-sql` no VS Code e abre um terminal, no menu Terminal, com a opção New Terminal. Arranca o servidor, se estiver parado:

   ```bash
   docker compose up -d
   ```

   O que deves ver, no fim: a linha do servidor, `pokemon-sql-db-1`, com `Running` ou `Started`. As duas querem dizer que o servidor está ligado.

2. Troca o conteúdo do teu `compose.yaml` pelo do [`compose.yaml` da versão 02](../../exemplos/sql-fundamentos/pokemon/02-ddl-e-integridade/compose.yaml) dos exemplos: abre-o, copia tudo, cola no teu `compose.yaml` no lugar do que lá estava e guarda. A versão nova tem duas linhas a mais, com os seus comentários: o servidor passa a ver a pasta do projeto, e o `psql` procura os teus ficheiros nessa pasta.

3. Volta a arrancar o servidor, para ele ler o `compose.yaml` novo:

   ```bash
   docker compose up -d
   ```

   O que deves ver: a linha do servidor passa por `Recreate` e acaba em `Started`. O Docker criou o servidor de novo, com a pasta do projeto à vista. A base `pokemon` continua lá, porque os dados estão guardados à parte, no Docker, e não no servidor que foi recriado.

4. Entra no `psql`, na base `pokemon`, e confirma que o servidor vê os teus ficheiros. O `\!` corre, dentro do servidor, um comando do terminal, e o `ls` lista os ficheiros da pasta onde o `psql` está:

   ```bash
   docker compose exec db psql -U postgres -d pokemon
   ```

   Depois, no `psql`, escreve `\! ls` e carrega em Enter. O que deves ver: os ficheiros da tua pasta, entre eles o `compose.yaml` e o `pokemon.sql`. Se aparecerem pastas como `bin`, `boot` e `dev`, ou nada, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

## Fase 1: Uma base de dados nova começa vazia

Crias a base `ginasio`, ao lado da `pokemon`, e entras nela. A base nova não tem tabelas: és tu que as vais escrever. Rever: [Uma base de dados nova começa vazia](../02-ddl-e-integridade.md#uma-base-de-dados-nova-começa-vazia).

1. No `psql`, ainda na base `pokemon`, cria a base `ginasio`:

   ```sql
   CREATE DATABASE ginasio;
   ```

   O que deves ver: `CREATE DATABASE`. A base foi criada no mesmo servidor.

2. Sai do `psql` com o `\q` e entra na base nova:

   ```bash
   docker compose exec db psql -U postgres -d ginasio
   ```

   O que deves ver: o início da linha passa a ser `ginasio=#`. A partir daqui, trabalhas sempre nesta base.

3. Antes de correres, prevê: o que mostra o `\dt` numa base acabada de criar? Escreve `\dt` e carrega em Enter. O que deves ver: `Did not find any relations.`, "não encontrei nenhuma tabela". As cinco tabelas do tema 01 são da base `pokemon`, e não se veem daqui.

### Paragem 1

O servidor tem a base `ginasio` ao lado da `pokemon`, e estás na `ginasio`, que está vazia.

Pensa antes de continuares: como sabes, a olhar para o terminal, em que base estás? A resposta: pelo início da linha do `psql`, `ginasio=#` ou `pokemon=#`. Confirma-o sempre antes de correres um ficheiro deste laboratório.

## Fase 2: O CREATE TABLE escreve uma tabela do modelo

Escreves a primeira tabela, a dos tipos, num ficheiro novo, o `esquema.sql`, e corres o ficheiro no `psql` com o `\i`. Rever: [O CREATE TABLE escreve uma tabela do modelo](../02-ddl-e-integridade.md#o-create-table-escreve-uma-tabela-do-modelo).

1. No painel Explorer do VS Code, cria o ficheiro `esquema.sql`, na pasta do projeto, com esta primeira versão, e guarda-o:

   ```sql
   -- esquema.sql: as tabelas da base ginasio, com as regras que a base de dados garante.
   -- Corre-se no psql, ligado à base ginasio, com \i esquema.sql.

   -- Os tipos dos Pokémon, como o Fogo e a Água.
   CREATE TABLE tipos (
       id INTEGER PRIMARY KEY,
       nome VARCHAR(20) NOT NULL
   );
   ```

2. No `psql`, corre o ficheiro:

   ```text
   \i esquema.sql
   ```

   O que deves ver: `CREATE TABLE`. O `psql` leu o ficheiro e correu o único comando que lá está. Se aparecer `esquema.sql: No such file or directory`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Confirma a tabela com o `\d tipos`. O que deves ver:

   ```text
                         Table "public.tipos"
    Column |         Type          | Collation | Nullable | Default
   --------+-----------------------+-----------+----------+---------
    id     | integer               |           | not null |
    nome   | character varying(20) |           | not null |
   Indexes:
       "tipos_pkey" PRIMARY KEY, btree (id)
   ```

   É a tabela que escreveste: as duas colunas, com os tipos de dados, o `not null` nas duas e a chave primária no `id`.

### Paragem 2

A base `ginasio` tem uma tabela, a `tipos`, criada pelo teu `esquema.sql`.

Pensa antes de continuares: porque é que o `id` aparece com `not null`, se não escreveste `NOT NULL` nele? A resposta: a chave primária nunca fica sem valor. O `PRIMARY KEY` já inclui o `NOT NULL`.

## Fase 3: Um ficheiro que se volta a correr começa por apagar

Juntas os treinadores ao esquema, vês o que acontece quando o ficheiro corre outra vez e acrescentas os `DROP` que o deixam correr sempre. Rever: [Um ficheiro que se volta a correr começa por apagar](../02-ddl-e-integridade.md#um-ficheiro-que-se-volta-a-correr-começa-por-apagar).

1. No fim do `esquema.sql`, acrescenta a tabela dos treinadores e guarda:

   ```sql

   -- Os treinadores, com a cidade de onde vêm.
   CREATE TABLE treinadores (
       id INTEGER PRIMARY KEY,
       nome VARCHAR(30) NOT NULL,
       cidade VARCHAR(30) NOT NULL
   );
   ```

2. Antes de correres, prevê: o que acontece à tabela `tipos`, que já existe, quando o ficheiro correr outra vez? Depois, corre `\i esquema.sql`. O que deves ver:

   ```text
   psql:esquema.sql:8: ERROR:  relation "tipos" already exists
   CREATE TABLE
   ```

   A tabela `tipos` já existia, e o PostgreSQL recusou criá-la outra vez. O `8` é a linha do ficheiro onde acaba o comando que falhou. Os treinadores foram criados, porque ainda não existiam.

3. Para o ficheiro poder correr sempre, junta os `DROP` no início. No `esquema.sql`, logo a seguir à segunda linha de comentário, acrescenta:

   ```sql

   -- Apaga as tabelas, se existirem, para as criar de novo, vazias.
   DROP TABLE IF EXISTS treinadores;
   DROP TABLE IF EXISTS tipos;
   ```

4. Guarda e corre outra vez `\i esquema.sql`. O que deves ver:

   ```text
   DROP TABLE
   DROP TABLE
   CREATE TABLE
   CREATE TABLE
   ```

   As duas tabelas foram apagadas e criadas de novo, sem erros. Corre o ficheiro mais uma vez, e a resposta é a mesma.

### Paragem 3

O `esquema.sql` corre as vezes que quiseres e deixa sempre as duas tabelas criadas. O ficheiro completo, como deve estar agora:

```sql
-- esquema.sql: as tabelas da base ginasio, com as regras que a base de dados garante.
-- Corre-se no psql, ligado à base ginasio, com \i esquema.sql.

-- Apaga as tabelas, se existirem, para as criar de novo, vazias.
DROP TABLE IF EXISTS treinadores;
DROP TABLE IF EXISTS tipos;

-- Os tipos dos Pokémon, como o Fogo e a Água.
CREATE TABLE tipos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(20) NOT NULL
);

-- Os treinadores, com a cidade de onde vêm.
CREATE TABLE treinadores (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cidade VARCHAR(30) NOT NULL
);
```

Primeiro apaga, depois cria. Cada vez que corre, deixa as tabelas como o ficheiro as descreve.

Pensa antes de continuares: numa base acabada de criar, sem tabelas, o `DROP TABLE IF EXISTS tipos;` dá erro? A resposta: não. O `IF EXISTS` salta a tabela que não existe e escreve só um aviso, `NOTICE: table "tipos" does not exist, skipping`.

## Fase 4: O INSERT acrescenta linhas

Pões linhas nas tabelas com o `INSERT`, primeiro uma à mão e depois num ficheiro, o `dados.sql`, e vês a base recusar uma linha. Rever: [O INSERT acrescenta linhas](../02-ddl-e-integridade.md#o-insert-acrescenta-linhas) e [Uma restrição é uma regra que a base garante](../02-ddl-e-integridade.md#uma-restrição-é-uma-regra-que-a-base-garante).

1. No `psql`, acrescenta um tipo à mão e vê a tabela:

   ```sql
   INSERT INTO tipos (id, nome) VALUES (1, 'Fogo');
   SELECT * FROM tipos;
   ```

   O que deves ver: `INSERT 0 1`, uma linha entrou, e por baixo a tabela com o Fogo, com o `id` 1.

2. Cria o ficheiro `dados.sql`, na pasta do projeto, com os tipos e os treinadores do tema 01, e guarda-o:

   ```sql
   -- dados.sql: os dados do ginásio, para as tabelas do esquema.sql.
   -- Corre-se depois do esquema.sql, com \i dados.sql.

   -- Os tipos dos Pokémon.
   INSERT INTO tipos (id, nome) VALUES
       (1, 'Fogo'),
       (2, 'Água'),
       (3, 'Planta'),
       (4, 'Elétrico'),
       (5, 'Pedra');

   -- Os treinadores.
   INSERT INTO treinadores (id, nome, cidade) VALUES
       (1, 'Ash', 'Pallet'),
       (2, 'Misty', 'Cerulean'),
       (3, 'Brock', 'Pewter'),
       (4, 'Gary', 'Pallet');
   ```

3. Corre os dois ficheiros, por esta ordem:

   ```text
   \i esquema.sql
   \i dados.sql
   ```

   O que deves ver: os dois `DROP TABLE` e os dois `CREATE TABLE` do esquema, e depois `INSERT 0 5` e `INSERT 0 4`. O esquema apagou o Fogo que puseste à mão, e o `dados.sql` voltou a pôr os cinco tipos e os quatro treinadores. Confirma com `SELECT * FROM treinadores;`: quatro linhas, do Ash ao Gary.

4. Cria o ficheiro `recusas.sql`, onde vais juntar as linhas que a base tem de recusar, cada uma com um comentário a dizer porquê. A primeira é um treinador sem cidade:

   ```sql
   -- recusas.sql: linhas que a base ginasio recusa, cada uma por causa de uma regra.
   -- Corre-se depois do esquema.sql e do dados.sql, com \i recusas.sql. Todos os INSERT
   -- dão erro, e a base fica como estava.

   -- O treinador não tem cidade, e a coluna cidade é NOT NULL.
   -- Erro: null value in column "cidade" of relation "treinadores" violates not-null constraint
   INSERT INTO treinadores (id, nome) VALUES (5, 'Tracey');
   ```

5. Guarda e corre `\i recusas.sql`. O que deves ver:

   ```text
   psql:recusas.sql:7: ERROR:  null value in column "cidade" of relation "treinadores" violates not-null constraint
   DETAIL:  Failing row contains (5, Tracey, null).
   ```

   A base recusou o Tracey, porque a coluna `cidade` não aceita o NULL, e a tabela ficou com os mesmos quatro treinadores. Uma regra que a base verifica assim, como o `NOT NULL`, chama-se restrição.

### Paragem 4

A base tem os tipos e os treinadores do `dados.sql`, e o `recusas.sql` tem a primeira linha recusada.

Pensa antes de continuares: se correres o `\i dados.sql` outra vez, sem o esquema antes, o que acontece? A resposta: os dois `INSERT` são recusados, porque os `id` de 1 a 5 e de 1 a 4 já existem, e a chave primária não deixa repeti-los. Por isso, corre-se sempre o esquema primeiro, que deixa as tabelas vazias.

## Fase 5: A base pode dar o número da chave primária

Passas os `id` para colunas de identidade, que a base numera sozinha, e tiras os números dos `INSERT`. Rever: [A base pode dar o número da chave primária](../02-ddl-e-integridade.md#a-base-pode-dar-o-número-da-chave-primária).

1. No `esquema.sql`, troca os dois `CREATE TABLE`, o dos tipos e o dos treinadores, e os comentários deles, por estes. Só muda a linha do `id`:

   ```sql
   -- Os tipos dos Pokémon, como o Fogo e a Água.
   CREATE TABLE tipos (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       nome VARCHAR(20) NOT NULL
   );

   -- Os treinadores, com a cidade de onde vêm.
   CREATE TABLE treinadores (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       nome VARCHAR(30) NOT NULL,
       cidade VARCHAR(30) NOT NULL
   );
   ```

2. No `dados.sql`, troca tudo o que está por baixo das duas primeiras linhas de comentário por este texto, sem os `id`:

   ```sql

   -- Os INSERT não dizem o id: a base numera as linhas de cada tabela pela ordem
   -- em que entram, a começar no 1. Os comentários dizem o número de cada linha.

   -- Os tipos dos Pokémon.
   INSERT INTO tipos (nome) VALUES
       ('Fogo'),        -- 1
       ('Água'),        -- 2
       ('Planta'),      -- 3
       ('Elétrico'),    -- 4
       ('Pedra');       -- 5

   -- Os treinadores.
   INSERT INTO treinadores (nome, cidade) VALUES
       ('Ash', 'Pallet'),         -- 1
       ('Misty', 'Cerulean'),     -- 2
       ('Brock', 'Pewter'),       -- 3
       ('Gary', 'Pallet');        -- 4
   ```

3. No `recusas.sql`, tira também o `id` do Tracey. A linha do `INSERT` fica assim:

   ```sql
   INSERT INTO treinadores (nome) VALUES ('Tracey');
   ```

4. Guarda os três ficheiros e corre-os, por esta ordem:

   ```text
   \i esquema.sql
   \i dados.sql
   \i recusas.sql
   ```

   O que deves ver: os `DROP TABLE` e os `CREATE TABLE`, o `INSERT 0 5` e o `INSERT 0 4`, e por fim o mesmo erro do Tracey, sem a cidade. A partir daqui, depois de cada mudança nos ficheiros, corres estes três comandos por esta ordem. No `psql`, a seta para cima repete os comandos anteriores.

5. Confirma os números com `SELECT * FROM tipos;`. O que deves ver: os mesmos cinco tipos, com os números de 1 a 5, pela ordem em que entraram. Corre também o `\d tipos`: na coluna `Default` do `id` aparece `generated by default as identity`.

### Paragem 5

Os `id` são dados pela base, e nenhum `INSERT` do `dados.sql` diz os números.

Pensa antes de continuares: o Tracey foi recusado, e a base já lhe tinha reservado o número 5. Se acrescentares agora um treinador válido, que número recebe? A resposta: o 6. Um número gasto por um `INSERT` recusado não volta a ser dado, e por isso os `id` podem saltar números.

## Fase 6: A chave estrangeira recusa o que não existe

Acrescentas a tabela das espécies, com a chave estrangeira para os tipos, e vês a base recusar uma espécie de um tipo que não existe. Rever: [A chave estrangeira recusa o que não existe](../02-ddl-e-integridade.md#a-chave-estrangeira-recusa-o-que-não-existe).

1. No `esquema.sql`, entre o `CREATE TABLE` dos tipos e o dos treinadores, acrescenta a tabela das espécies:

   ```sql

   -- As espécies. Cada espécie tem um tipo que existe.
   CREATE TABLE especies (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       nome VARCHAR(30) NOT NULL,
       tipo_id INTEGER NOT NULL REFERENCES tipos (id)
   );
   ```

2. Ainda no `esquema.sql`, junta o `DROP` das espécies, entre os dois `DROP` que lá estão, para ficarem por esta ordem:

   ```sql
   DROP TABLE IF EXISTS treinadores;
   DROP TABLE IF EXISTS especies;
   DROP TABLE IF EXISTS tipos;
   ```

   As espécies apontam para os tipos, e por isso apagam-se antes deles.

3. No `dados.sql`, entre o `INSERT` dos tipos e o dos treinadores, acrescenta as espécies:

   ```sql

   -- As espécies entram depois dos tipos, porque cada uma aponta para um tipo.
   INSERT INTO especies (nome, tipo_id) VALUES
       ('Charmander', 1),   -- 1
       ('Squirtle', 2),     -- 2
       ('Bulbasaur', 3),    -- 3
       ('Pikachu', 4),      -- 4
       ('Starmie', 2),      -- 5
       ('Psyduck', 2),      -- 6
       ('Onix', 5);         -- 7
   ```

4. No fim do `recusas.sql`, acrescenta uma espécie de um tipo que não existe:

   ```sql

   -- Não há nenhum tipo com o id 9, e o tipo_id é uma chave estrangeira.
   -- Erro: insert or update on table "especies" violates foreign key constraint "especies_tipo_id_fkey"
   INSERT INTO especies (nome, tipo_id) VALUES ('Mewtwo', 9);
   ```

5. Guarda os três ficheiros e corre-os, pela ordem de sempre. O que deves ver, no fim, depois do erro do Tracey:

   ```text
   psql:recusas.sql:11: ERROR:  insert or update on table "especies" violates foreign key constraint "especies_tipo_id_fkey"
   DETAIL:  Key (tipo_id)=(9) is not present in table "tipos".
   ```

   A base recusou o Mewtwo, porque o `tipo_id` 9 não está na tabela `tipos`. Antes disso, o esquema escreveu um `NOTICE` para as espécies, que ainda não existiam, e o `dados.sql` escreveu `INSERT 0 7` para elas.

### Paragem 6

A base tem três tabelas, e as espécies só aceitam tipos que existem. O `recusas.sql` tem duas linhas recusadas.

Pensa antes de continuares: o `\d tipos` mostra agora uma secção nova, `Referenced by`. O que diz ela? A resposta: diz que a tabela `especies` aponta para os tipos, pela chave estrangeira `especies_tipo_id_fkey`. É por isso que os tipos não se podem apagar antes das espécies.

## Fase 7: A ordem das tabelas segue as chaves estrangeiras

Vês o que acontece quando os `DROP` estão pela ordem errada e acabas o esquema com os Pokémon e os combates, pela ordem das ligações. Rever: [A ordem das tabelas segue as chaves estrangeiras](../02-ddl-e-integridade.md#a-ordem-das-tabelas-segue-as-chaves-estrangeiras).

1. Provoca um erro de propósito: no `esquema.sql`, troca a ordem das duas últimas linhas `DROP`, para os tipos se apagarem antes das espécies. Guarda e corre só o `\i esquema.sql`. O que deves ver, entre outras linhas:

   ```text
   psql:esquema.sql:6: ERROR:  cannot drop table tipos because other objects depend on it
   DETAIL:  constraint especies_tipo_id_fkey on table especies depends on table tipos
   HINT:  Use DROP ... CASCADE to drop the dependent objects too.
   ```

   O PostgreSQL não apagou os tipos, porque as espécies ainda apontavam para eles. A seguir, o `CREATE TABLE` dos tipos também falhou, com `already exists`, porque a tabela ficou lá. Não sigas a dica do `HINT`: o `CASCADE` tirava a chave estrangeira das espécies, sem avisar. Volta a pôr as duas linhas como estavam, com as espécies antes dos tipos, guarda e corre o esquema e os dados: tudo volta a correr sem erros.

2. Acrescenta, no fim do `esquema.sql`, as duas tabelas que faltam. Os Pokémon apontam para as espécies e para os treinadores, e os combates para os treinadores, por isso vêm depois deles:

   ```sql

   -- Os Pokémon capturados. Cada um é de uma espécie e pertence a um treinador.
   CREATE TABLE pokemons (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       especie_id INTEGER NOT NULL REFERENCES especies (id),
       treinador_id INTEGER NOT NULL REFERENCES treinadores (id),
       -- A alcunha pode ficar sem valor: nem todos os Pokémon têm alcunha.
       alcunha VARCHAR(30),
       vida INTEGER NOT NULL,
       ataque INTEGER NOT NULL
   );

   -- Os combates nos ginásios. Três colunas apontam para treinadores: quem desafiou,
   -- o líder do ginásio e quem venceu. O vencedor fica sem valor enquanto o combate
   -- não acaba.
   CREATE TABLE combates (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       data DATE NOT NULL,
       cidade VARCHAR(30) NOT NULL,
       desafiante_id INTEGER NOT NULL REFERENCES treinadores (id),
       lider_id INTEGER NOT NULL REFERENCES treinadores (id),
       vencedor_id INTEGER REFERENCES treinadores (id)
   );
   ```

3. Os combates e os Pokémon apontam para outras tabelas, e nenhuma aponta para eles, por isso apagam-se primeiro. Os `DROP` e o seu comentário ficam assim:

   ```sql
   -- Apaga as tabelas, se existirem, para as criar de novo, vazias.
   -- As tabelas que apontam para outras apagam-se primeiro.
   DROP TABLE IF EXISTS combates;
   DROP TABLE IF EXISTS pokemons;
   DROP TABLE IF EXISTS treinadores;
   DROP TABLE IF EXISTS especies;
   DROP TABLE IF EXISTS tipos;
   ```

4. No fim do `dados.sql`, acrescenta os Pokémon e os combates do tema 01:

   ```sql

   -- Os Pokémon entram depois das espécies e dos treinadores, para onde apontam.
   -- O Starmie da Misty está KO, com a vida 0, e o Psyduck tem a alcunha vazia.
   INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES
       (1, 1, NULL, 90, 40),      -- 1, o Charmander do Ash
       (3, 1, NULL, 110, 25),     -- 2, o Bulbasaur do Ash
       (4, 1, 'Pika', 80, 45),    -- 3, o Pikachu do Ash
       (5, 2, NULL, 0, 35),       -- 4, o Starmie da Misty
       (6, 2, '', 100, 20),       -- 5, o Psyduck da Misty
       (7, 3, NULL, 140, 30);     -- 6, o Onix do Brock

   -- O combate 3 ainda não acabou, e por isso o vencedor fica sem valor.
   INSERT INTO combates (data, cidade, desafiante_id, lider_id, vencedor_id) VALUES
       ('2026-11-03', 'Cerulean', 1, 2, 2),    -- 1
       ('2026-11-03', 'Cerulean', 1, 2, 1),    -- 2
       ('2026-11-10', 'Pewter', 1, 3, NULL);   -- 3
   ```

5. Guarda e corre os três ficheiros, pela ordem de sempre. O que deves ver: cinco `DROP TABLE`, cinco `CREATE TABLE`, cinco linhas `INSERT`, a acabar em `INSERT 0 6` e `INSERT 0 3`, e os dois erros do `recusas.sql`. Dois dos `DROP` escrevem um `NOTICE`, porque os Pokémon e os combates ainda não existiam. Confirma com o `\dt`: as cinco tabelas do tema 01, agora na base `ginasio`.

### Paragem 7

A base `ginasio` tem as cinco tabelas e os dados do tema 01, criados pelos teus ficheiros. O `dados.sql` está completo, como deve estar agora:

```sql
-- dados.sql: os dados do ginásio, para as tabelas do esquema.sql.
-- Corre-se depois do esquema.sql, com \i dados.sql.

-- Os INSERT não dizem o id: a base numera as linhas de cada tabela pela ordem
-- em que entram, a começar no 1. Os comentários dizem o número de cada linha.

-- Os tipos dos Pokémon.
INSERT INTO tipos (nome) VALUES
    ('Fogo'),        -- 1
    ('Água'),        -- 2
    ('Planta'),      -- 3
    ('Elétrico'),    -- 4
    ('Pedra');       -- 5

-- As espécies entram depois dos tipos, porque cada uma aponta para um tipo.
INSERT INTO especies (nome, tipo_id) VALUES
    ('Charmander', 1),   -- 1
    ('Squirtle', 2),     -- 2
    ('Bulbasaur', 3),    -- 3
    ('Pikachu', 4),      -- 4
    ('Starmie', 2),      -- 5
    ('Psyduck', 2),      -- 6
    ('Onix', 5);         -- 7

-- Os treinadores.
INSERT INTO treinadores (nome, cidade) VALUES
    ('Ash', 'Pallet'),         -- 1
    ('Misty', 'Cerulean'),     -- 2
    ('Brock', 'Pewter'),       -- 3
    ('Gary', 'Pallet');        -- 4

-- Os Pokémon entram depois das espécies e dos treinadores, para onde apontam.
-- O Starmie da Misty está KO, com a vida 0, e o Psyduck tem a alcunha vazia.
INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES
    (1, 1, NULL, 90, 40),      -- 1, o Charmander do Ash
    (3, 1, NULL, 110, 25),     -- 2, o Bulbasaur do Ash
    (4, 1, 'Pika', 80, 45),    -- 3, o Pikachu do Ash
    (5, 2, NULL, 0, 35),       -- 4, o Starmie da Misty
    (6, 2, '', 100, 20),       -- 5, o Psyduck da Misty
    (7, 3, NULL, 140, 30);     -- 6, o Onix do Brock

-- O combate 3 ainda não acabou, e por isso o vencedor fica sem valor.
INSERT INTO combates (data, cidade, desafiante_id, lider_id, vencedor_id) VALUES
    ('2026-11-03', 'Cerulean', 1, 2, 2),    -- 1
    ('2026-11-03', 'Cerulean', 1, 2, 1),    -- 2
    ('2026-11-10', 'Pewter', 1, 3, NULL);   -- 3
```

Os dados entram pela ordem em que as tabelas se criam, e cada linha só aponta para linhas que já entraram.

Pensa antes de continuares: o `dados.sql` diz que o Pikachu do Ash é da espécie 4. Como sabes que a espécie 4 é o Pikachu, se o `id` não está escrito no `INSERT` das espécies? A resposta: a base numera as espécies pela ordem em que entram, a começar no 1, e o Pikachu é a quarta. O comentário `-- 4` ao lado ajuda a confirmar.

## Fase 8: O UNIQUE recusa os repetidos

Juntas o `UNIQUE` aos nomes dos tipos e das espécies, e ao par do treinador com a alcunha. Rever: [O UNIQUE recusa os repetidos](../02-ddl-e-integridade.md#o-unique-recusa-os-repetidos).

1. No `esquema.sql`, troca o `CREATE TABLE` dos tipos e o das espécies por estes, com `UNIQUE` no fim da linha do nome. Não mexas no nome dos treinadores, que se pode repetir:

   ```sql
   -- Os tipos dos Pokémon, como o Fogo e a Água.
   CREATE TABLE tipos (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       nome VARCHAR(20) NOT NULL UNIQUE
   );

   -- As espécies. Cada espécie tem um tipo que existe.
   CREATE TABLE especies (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       nome VARCHAR(30) NOT NULL UNIQUE,
       tipo_id INTEGER NOT NULL REFERENCES tipos (id)
   );
   ```

2. Nos Pokémon, a regra junta duas colunas e fica numa linha própria, no fim da tabela, com uma vírgula no fim da linha do `ataque`. Troca o `CREATE TABLE` dos Pokémon por este:

   ```sql
   -- Os Pokémon capturados. Cada um é de uma espécie e pertence a um treinador.
   CREATE TABLE pokemons (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       especie_id INTEGER NOT NULL REFERENCES especies (id),
       treinador_id INTEGER NOT NULL REFERENCES treinadores (id),
       -- A alcunha pode ficar sem valor: nem todos os Pokémon têm alcunha.
       alcunha VARCHAR(30),
       vida INTEGER NOT NULL,
       ataque INTEGER NOT NULL,
       -- O mesmo treinador não dá a mesma alcunha a dois Pokémon.
       UNIQUE (treinador_id, alcunha)
   );
   ```

3. No fim do `recusas.sql`, acrescenta um tipo repetido e um segundo Pika do Ash:

   ```sql

   -- Já há um tipo chamado Água, e o nome dos tipos é UNIQUE.
   -- Erro: duplicate key value violates unique constraint "tipos_nome_key"
   INSERT INTO tipos (nome) VALUES ('Água');

   -- O Ash já tem um Pokémon com a alcunha Pika.
   -- Erro: duplicate key value violates unique constraint "pokemons_treinador_id_alcunha_key"
   INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 1, 'Pika', 100, 30);
   ```

4. Guarda os ficheiros e corre os três. O que deves ver, no fim, depois dos dois erros que já conheces:

   ```text
   psql:recusas.sql:15: ERROR:  duplicate key value violates unique constraint "tipos_nome_key"
   DETAIL:  Key (nome)=(Água) already exists.
   psql:recusas.sql:19: ERROR:  duplicate key value violates unique constraint "pokemons_treinador_id_alcunha_key"
   DETAIL:  Key (treinador_id, alcunha)=(1, Pika) already exists.
   ```

5. Antes de correres, prevê: o Ash já tem dois Pokémon sem alcunha. A base aceita um terceiro? Depois, no `psql`, acrescenta um Squirtle do Ash, sem alcunha, e vê os Pokémon:

   ```sql
   INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 1, NULL, 100, 30);
   SELECT * FROM pokemons;
   ```

   O que deves ver: `INSERT 0 1`, e o Squirtle na última linha da tabela, com o `treinador_id` 1 e a célula da alcunha em branco: é o NULL do `INSERT`. Para o `UNIQUE`, os NULL não se repetem, porque não são valores. Este `INSERT` não vai para o `recusas.sql`, porque a base o aceita.

### Paragem 8

Os nomes dos tipos e das espécies não se repetem, e nenhum treinador repete uma alcunha. O `recusas.sql` tem quatro linhas recusadas.

Pensa antes de continuares: o Squirtle do Ash ficou com o `id` 8, e não com o 7. Porquê? A resposta: o segundo Pika do Ash, no `recusas.sql`, foi recusado depois de a base lhe dar o 7. Esse número ficou gasto. Se correste outros `INSERT` recusados nos Pokémon, o número pode ser outro, e não é um erro.

## Fase 9: O CHECK recusa os valores fora da regra

Pões na vida e no ataque os limites que o Python já usava, e vês a base recusar o que passa deles, em vez de o corrigir. Rever: [O CHECK recusa os valores fora da regra](../02-ddl-e-integridade.md#o-check-recusa-os-valores-fora-da-regra).

1. No `esquema.sql`, troca o `CREATE TABLE` dos Pokémon por este. Mudam as linhas da vida e do ataque, e entra um comentário por cima delas:

   ```sql
   -- Os Pokémon capturados. Cada um é de uma espécie e pertence a um treinador.
   CREATE TABLE pokemons (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       especie_id INTEGER NOT NULL REFERENCES especies (id),
       treinador_id INTEGER NOT NULL REFERENCES treinadores (id),
       -- A alcunha pode ficar sem valor: nem todos os Pokémon têm alcunha.
       alcunha VARCHAR(30),
       -- Os limites do Python, mas aqui um valor fora deles é recusado, e não corrigido.
       vida INTEGER NOT NULL CHECK (vida >= 0 AND vida <= 150),
       ataque INTEGER NOT NULL CHECK (ataque >= 1 AND ataque <= 50),
       -- O mesmo treinador não dá a mesma alcunha a dois Pokémon.
       UNIQUE (treinador_id, alcunha)
   );
   ```

2. No fim do `recusas.sql`, acrescenta um Pokémon com vida a mais e outro sem ataque:

   ```sql

   -- A vida 200 passa do limite de 150.
   -- Erro: new row for relation "pokemons" violates check constraint "pokemons_vida_check"
   INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 4, NULL, 200, 30);

   -- O ataque 0 fica abaixo do limite de 1.
   -- Erro: new row for relation "pokemons" violates check constraint "pokemons_ataque_check"
   INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 4, NULL, 100, 0);
   ```

3. Guarda e corre os três ficheiros. O que deves ver, no fim:

   ```text
   psql:recusas.sql:23: ERROR:  new row for relation "pokemons" violates check constraint "pokemons_vida_check"
   DETAIL:  Failing row contains (8, 2, 4, null, 200, 30).
   psql:recusas.sql:27: ERROR:  new row for relation "pokemons" violates check constraint "pokemons_ataque_check"
   DETAIL:  Failing row contains (9, 2, 4, null, 100, 0).
   ```

   No Python, a propriedade punha a vida 200 a 150 e o ataque 0 a 1. A base não corrige: recusa as duas linhas, e a tabela fica com os seis Pokémon do `dados.sql`.

4. Confirma as regras da tabela com o `\d pokemons`. O que deves ver, depois das colunas, nas linhas de `Check constraints`:

   ```text
   Check constraints:
       "pokemons_ataque_check" CHECK (ataque >= 1 AND ataque <= 50)
       "pokemons_vida_check" CHECK (vida >= 0 AND vida <= 150)
   ```

### Paragem 9

A vida e o ataque só aceitam os valores dos limites, e o `recusas.sql` tem seis linhas recusadas.

Pensa antes de continuares: o Starmie da Misty tem a vida 0. Porque é que o `dados.sql` não deu erro com ele? A resposta: a condição é `vida >= 0`, e o `>=` inclui o 0. A vida 0 está dentro da regra: o Starmie está KO, mas existe.

## Fase 10: O ALTER TABLE muda uma tabela sem perder os dados

Acrescentas as medalhas aos treinadores com o `ALTER TABLE`, sem apagar os dados, e depois passas a coluna para o esquema. Rever: [O ALTER TABLE muda uma tabela sem perder os dados](../02-ddl-e-integridade.md#o-alter-table-muda-uma-tabela-sem-perder-os-dados).

1. Provoca um erro de propósito: no `psql`, acrescenta a coluna das medalhas aos treinadores sem lhe dares um valor por omissão:

   ```sql
   ALTER TABLE treinadores ADD COLUMN medalhas INTEGER NOT NULL;
   ```

   O que deves ver: `ERROR:  column "medalhas" of relation "treinadores" contains null values`. Os quatro treinadores ficavam sem valor na coluna nova, e o `NOT NULL` não deixa.

2. Acrescenta a coluna com o valor por omissão e o limite das oito medalhas, e vê os treinadores:

   ```sql
   ALTER TABLE treinadores ADD COLUMN medalhas INTEGER NOT NULL DEFAULT 0 CHECK (medalhas >= 0 AND medalhas <= 8);
   SELECT * FROM treinadores;
   ```

   O que deves ver:

   ```text
   ALTER TABLE
    id | nome  |  cidade  | medalhas
   ----+-------+----------+----------
     1 | Ash   | Pallet   |        0
     2 | Misty | Cerulean |        0
     3 | Brock | Pewter   |        0
     4 | Gary  | Pallet   |        0
   (4 rows)
   ```

   A tabela mudou, e os quatro treinadores continuam lá. O `DEFAULT 0` é o valor por omissão: cada treinador que já lá estava ficou com 0 medalhas.

3. Se correres agora o `esquema.sql`, as medalhas desaparecem, porque o ficheiro ainda cria os treinadores sem elas. Passa a coluna para o ficheiro: troca o `CREATE TABLE` dos treinadores por este, com uma vírgula no fim da linha da `cidade` e a coluna nova por baixo:

   ```sql
   -- Os treinadores, com a cidade de onde vêm.
   CREATE TABLE treinadores (
       id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       nome VARCHAR(30) NOT NULL,
       cidade VARCHAR(30) NOT NULL,
       -- Um treinador novo começa sem medalhas, e há oito medalhas para ganhar.
       medalhas INTEGER NOT NULL DEFAULT 0 CHECK (medalhas >= 0 AND medalhas <= 8)
   );
   ```

4. No fim do `recusas.sql`, acrescenta um treinador com medalhas a mais:

   ```sql

   -- Só há oito medalhas para ganhar.
   -- Erro: new row for relation "treinadores" violates check constraint "treinadores_medalhas_check"
   INSERT INTO treinadores (nome, cidade, medalhas) VALUES ('Tracey', 'Pallet', 9);
   ```

5. Guarda e corre os três ficheiros. O que deves ver: o esquema e os dados sem erros, e os sete erros do `recusas.sql`, o último com a restrição `treinadores_medalhas_check`. O `SELECT * FROM treinadores;` mostra outra vez os quatro treinadores com 0 medalhas, agora criados pelos teus ficheiros.

### Paragem 10

O `esquema.sql` constrói a base `ginasio` de raiz, com todas as regras, e diz o mesmo que a base. O ficheiro completo, como deve estar agora:

```sql
-- esquema.sql: as tabelas da base ginasio, com as regras que a base de dados garante.
-- Corre-se no psql, ligado à base ginasio, com \i esquema.sql.

-- Apaga as tabelas, se existirem, para as criar de novo, vazias.
-- As tabelas que apontam para outras apagam-se primeiro.
DROP TABLE IF EXISTS combates;
DROP TABLE IF EXISTS pokemons;
DROP TABLE IF EXISTS treinadores;
DROP TABLE IF EXISTS especies;
DROP TABLE IF EXISTS tipos;

-- Os tipos dos Pokémon, como o Fogo e a Água.
CREATE TABLE tipos (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nome VARCHAR(20) NOT NULL UNIQUE
);

-- As espécies. Cada espécie tem um tipo que existe.
CREATE TABLE especies (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nome VARCHAR(30) NOT NULL UNIQUE,
    tipo_id INTEGER NOT NULL REFERENCES tipos (id)
);

-- Os treinadores, com a cidade de onde vêm.
CREATE TABLE treinadores (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cidade VARCHAR(30) NOT NULL,
    -- Um treinador novo começa sem medalhas, e há oito medalhas para ganhar.
    medalhas INTEGER NOT NULL DEFAULT 0 CHECK (medalhas >= 0 AND medalhas <= 8)
);

-- Os Pokémon capturados. Cada um é de uma espécie e pertence a um treinador.
CREATE TABLE pokemons (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    especie_id INTEGER NOT NULL REFERENCES especies (id),
    treinador_id INTEGER NOT NULL REFERENCES treinadores (id),
    -- A alcunha pode ficar sem valor: nem todos os Pokémon têm alcunha.
    alcunha VARCHAR(30),
    -- Os limites do Python, mas aqui um valor fora deles é recusado, e não corrigido.
    vida INTEGER NOT NULL CHECK (vida >= 0 AND vida <= 150),
    ataque INTEGER NOT NULL CHECK (ataque >= 1 AND ataque <= 50),
    -- O mesmo treinador não dá a mesma alcunha a dois Pokémon.
    UNIQUE (treinador_id, alcunha)
);

-- Os combates nos ginásios. Três colunas apontam para treinadores: quem desafiou,
-- o líder do ginásio e quem venceu. O vencedor fica sem valor enquanto o combate
-- não acaba.
CREATE TABLE combates (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    data DATE NOT NULL,
    cidade VARCHAR(30) NOT NULL,
    desafiante_id INTEGER NOT NULL REFERENCES treinadores (id),
    lider_id INTEGER NOT NULL REFERENCES treinadores (id),
    vencedor_id INTEGER REFERENCES treinadores (id)
);
```

Os `DROP` apagam primeiro as tabelas que apontam para outras, e os `CREATE TABLE` criam pela ordem contrária. Cada regra do ginásio está numa restrição, a seguir à sua coluna ou numa linha própria, quando junta duas colunas.

Pensa antes de continuares: o `dados.sql` não diz as medalhas dos treinadores. Porque é que não deu erro, se a coluna é `NOT NULL`? A resposta: a coluna tem o valor por omissão 0. Quando o `INSERT` não diz as medalhas, a base põe o 0, e o `NOT NULL` fica cumprido.

## Se alguma coisa falhar

1. O Docker Desktop está aberto e o servidor está a correr? Corre `docker compose ps`, no terminal normal, na pasta do projeto: o `db` tem de aparecer com `Up`. Se estiver parado, arranca-o com `docker compose up -d`.
2. Estás na base certa? No `psql`, o início da linha tem de ser `ginasio=#`. Se for `pokemon=#`, sai com o `\q` e entra com `-d ginasio`.
3. Guardaste o ficheiro? O `\i` corre o ficheiro como está guardado no disco. No VS Code, um ficheiro por guardar tem um círculo no separador, em vez do `X`. Guarda-o e corre o `\i` outra vez.
4. Correste os ficheiros pela ordem certa? Primeiro o `esquema.sql`, depois o `dados.sql` e por fim o `recusas.sql`.

### `esquema.sql: No such file or directory`

O `psql` não encontrou o ficheiro na pasta do projeto. Escreve `\! ls` no `psql` e procura o ficheiro na lista. Se a lista estiver certa e o ficheiro não aparecer, o nome é outro, como `Esquema.sql` ou `esquema.sql.txt`: corrige-o no painel Explorer. Se a lista não mostrar os teus ficheiros, vê a entrada seguinte.

### O `\! ls` mostra `bin`, `boot`, `dev`, em vez dos teus ficheiros, ou não mostra nada

O servidor não está a correr com o `compose.yaml` da versão 02: o `compose.yaml` não foi trocado ou guardado, ou faltou o `docker compose up -d` do passo 3 de [Preparar o projeto](#preparar-o-projeto). Confirma que o teu `compose.yaml` tem as duas linhas novas, `working_dir: /projeto` e `- ./:/projeto:ro`, e que o guardaste. Depois, sai do `psql`, corre `docker compose up -d` e volta a entrar.

### `database "ginasio" already exists`

A base `ginasio` já foi criada, numa aula anterior ou noutra tentativa. Não faz mal: sai do `psql` e entra nela com `-d ginasio`.

### Um erro de sintaxe ao correr o `esquema.sql`

A mensagem diz o nome do ficheiro e a linha onde acaba o comando que falhou, como em `psql:esquema.sql:21: ERROR:  syntax error at or near ")"`. Abre o ficheiro nessa linha e compara o comando com o do passo. Os erros de sintaxe mais comuns, uma vírgula a mais ou a menos, ou um ponto e vírgula em falta, estão em [Erros frequentes](../02-ddl-e-integridade.md#erros-frequentes), no guia. Depois de corrigires, corre o esquema e os dados outra vez.

### `duplicate key value violates unique constraint` ao correr o `dados.sql`

Correste o `dados.sql` sem correr antes o `esquema.sql`, e as linhas que lá estavam chocaram com as novas. Corre o `\i esquema.sql`, que deixa as tabelas vazias, e depois o `\i dados.sql`.

### Um `INSERT` do `recusas.sql` foi aceite

O `psql` escreveu `INSERT 0 1` numa linha do `recusas.sql`, em vez de um `ERROR`. A regra que a devia recusar não está no `esquema.sql`, ou correste o `recusas.sql` antes de correr o esquema novo. Confirma a restrição no `esquema.sql` e no `\d` da tabela, e corre os três ficheiros pela ordem.

### Correste o `esquema.sql` na base `pokemon`

O início da linha era `pokemon=#` quando correste o `\i esquema.sql`. O que aconteceu depende do que o esquema já tinha:

- Se apareceram erros `cannot drop table ... because other objects depend on it` e `already exists`, o esquema ainda não tinha as cinco tabelas, e a base `pokemon` ficou como estava. Entra na `ginasio` e corre lá o esquema.
- Se o esquema correu sem erros, os `DROP` apagaram as tabelas da `pokemon`, e os `CREATE TABLE` criaram lá as do teu esquema, vazias. Corre também lá o `\i dados.sql`: a `pokemon` volta a ter os dados do tema 01, com as regras novas, e as consultas do tema 01 continuam a funcionar. Depois, entra na `ginasio`.

## Desafios

1. Junta aos combates uma regra que obrigue o vencedor a ser o desafiante ou o líder desse combate. Antes de correres o `dados.sql`, prevê se o combate 3, que não tem vencedor, é aceite. Pista: um `CHECK` pode usar várias colunas da linha, ligadas por `OR`.
2. Junta aos Pokémon a regra do guia que recusa a alcunha vazia, `CHECK (alcunha <> '')`, e corre o esquema e os dados. Quantos Pokémon ficam na tabela, e porquê? Depois, decide o que mudar no `dados.sql` para os seis Pokémon voltarem a entrar.
3. Um combate novo é quase sempre de hoje. Dá à data dos combates um valor por omissão, para o `INSERT` de um combate de hoje não ter de dizer a data. Pista: no PostgreSQL, o valor `CURRENT_DATE` é a data de hoje.

## Antes de terminares

- [ ] A base `ginasio` existe no teu servidor, ao lado da `pokemon`.
- [ ] O `esquema.sql` corre sem erros, as vezes que quiseres, e cria as cinco tabelas com as regras do ginásio.
- [ ] O `dados.sql` corre sem erros depois do esquema e põe os dados do tema 01 nas cinco tabelas.
- [ ] O `recusas.sql` tem sete `INSERT`, cada um com o comentário da regra que o recusa, e todos dão erro.
- [ ] O `\d pokemons` mostra as chaves estrangeiras, os dois `CHECK` e o `UNIQUE` das alcunhas.
- [ ] No fim da aula, paras o servidor com `docker compose stop`, no terminal normal, na pasta do projeto.

![Rodapé](../../imagens/rodape.png)
