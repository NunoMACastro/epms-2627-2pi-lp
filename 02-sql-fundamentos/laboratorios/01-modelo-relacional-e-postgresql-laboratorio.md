![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Modelo relacional e ambiente PostgreSQL

## O que vais construir

Vais pôr a funcionar o teu servidor PostgreSQL, com a base de dados do ginásio Pokémon, e escrever o ficheiro `consultas.sql`, com as primeiras consultas a essa base. No fim, corres as mesmas consultas no pgAdmin e vês o modelo da base desenhado por ele. A pasta acaba com estes ficheiros:

```text
pokemon-sql/
├── .env
├── .gitignore
├── compose.yaml
├── consultas.sql
└── pokemon.sql
```

1. [Fase 1: O SGBD guarda as bases de dados](#fase-1-o-sgbd-guarda-as-bases-de-dados)
2. [Fase 2: O cliente faz as perguntas](#fase-2-o-cliente-faz-as-perguntas)
3. [Fase 3: O SQL pergunta, e o SGBD responde](#fase-3-o-sql-pergunta-e-o-sgbd-responde)
4. [Fase 4: Escolher as colunas](#fase-4-escolher-as-colunas)
5. [Fase 5: Cada coluna tem um tipo de dados](#fase-5-cada-coluna-tem-um-tipo-de-dados)
6. [Fase 6: O NULL quer dizer que não há valor](#fase-6-o-null-quer-dizer-que-não-há-valor)
7. [Fase 7: A chave estrangeira aponta para outra tabela](#fase-7-a-chave-estrangeira-aponta-para-outra-tabela)
8. [Fase 8: A mesma consulta no pgAdmin](#fase-8-a-mesma-consulta-no-pgadmin)

## O que precisas

- O Docker Desktop, aberto. Confirmas que está a funcionar em [Preparar o projeto](#preparar-o-projeto).
- O VS Code, para os ficheiros e para o terminal.
- O pgAdmin, para a fase 8.
- Os ficheiros `compose.yaml`, `pokemon.sql` e `.gitignore` da [versão 01 do exemplo dos Pokémon](../../exemplos/sql-fundamentos/pokemon/01-modelo-relacional-e-postgresql/), que copias na preparação.

## Preparar o projeto

1. Cria uma pasta nova, `pokemon-sql`, onde guardas os trabalhos da disciplina, fora da pasta do repositório dos alunos, se a tiveres no computador. Abre-a no VS Code, com a opção `Open Folder...` do menu File. Abre um terminal no menu Terminal, com a opção New Terminal, e escreve `pwd`. O que deves ver: o caminho da tua pasta, a acabar em `pokemon-sql`.

2. Copia para a pasta o [`compose.yaml`](../../exemplos/sql-fundamentos/pokemon/01-modelo-relacional-e-postgresql/compose.yaml), o [`pokemon.sql`](../../exemplos/sql-fundamentos/pokemon/01-modelo-relacional-e-postgresql/pokemon.sql) e o [`.gitignore`](../../exemplos/sql-fundamentos/pokemon/01-modelo-relacional-e-postgresql/.gitignore) dos exemplos. Para cada um: abre-o, copia tudo, cria no painel Explorer do VS Code um ficheiro com o mesmo nome, cola e guarda. O `compose.yaml` diz ao Docker que servidor arrancar, o `pokemon.sql` cria as tabelas e os dados da base, e o `.gitignore` diz ao Git que ficheiros deixar de fora.

3. Cria o ficheiro `.env`, que guarda a palavra-passe do servidor. No painel Explorer, cria um ficheiro chamado `.env`, com o ponto no início e sem mais nada no nome. Escreve nele esta linha, com uma palavra-passe tua no lugar de `escolhe-uma-palavra-passe`:

   ```text
   POSTGRES_PASSWORD=escolhe-uma-palavra-passe
   ```

   Guarda o ficheiro. A palavra-passe fica no `.env`, e não no `compose.yaml`, para poderes mostrar e partilhar o `compose.yaml` sem ela. O `.gitignore` que copiaste deixa o `.env` fora do Git. Escolhe uma que não uses noutro sítio e não leve espaços, e não a esqueças: vais precisar dela na fase 8.

4. Confirma que o Docker Desktop está a funcionar:

   ```bash
   docker ps
   ```

   O que deves ver: uma linha de títulos, que começa por `CONTAINER ID`, e talvez nada por baixo. Isto quer dizer que o Docker responde. Se aparecer uma mensagem de erro, abre o Docker Desktop, espera que acabe de arrancar e corre outra vez o `docker ps`.

## Fase 1: O SGBD guarda as bases de dados

Arrancas o servidor PostgreSQL dentro do Docker, e ele cria a base de dados `pokemon`. O PostgreSQL é o SGBD, e funciona como um servidor. Rever: [O SGBD guarda as bases de dados](../01-modelo-relacional-e-postgresql.md#o-sgbd-guarda-as-bases-de-dados).

1. Arranca o servidor. O `up` arranca o que o `compose.yaml` descreve, e o `-d` deixa-o a correr por trás e devolve-te o terminal:

   ```bash
   docker compose up -d
   ```

   Na primeira vez, o Docker descarrega o PostgreSQL da internet, e isso pode levar alguns minutos. O que deves ver, no fim: uma linha com o nome do servidor, `pokemon-sql-db-1`, e a palavra `Started`. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Confirma que o servidor está a correr:

   ```bash
   docker compose ps
   ```

   O que deves ver:

   ```text
   NAME               IMAGE                  COMMAND                  SERVICE   CREATED          STATUS          PORTS
   pokemon-sql-db-1   postgres:17-bookworm   "docker-entrypoint.s…"   db        20 seconds ago   Up 19 seconds   127.0.0.1:5433->5432/tcp
   ```

   O `db` é o nome do servidor no `compose.yaml`, e o `Up` quer dizer que está ligado. Os tempos são outros no teu computador.

3. Vê o que o servidor escreveu quando arrancou:

   ```bash
   docker compose logs db
   ```

   O que deves ver: muitas linhas, que começam por `db-1  |`. A meio, há cinco linhas `CREATE TABLE` e cinco linhas `INSERT`: são o `pokemon.sql` a criar as tabelas e os dados. A última linha acaba em `database system is ready to accept connections`, "o sistema de base de dados está pronto para aceitar ligações".

### Paragem 1

O servidor está a correr e já tem a base de dados `pokemon`, com as tabelas e os dados do `pokemon.sql`. Confirmas com o `docker compose ps`, que mostra o `db` com `Up`.

Pensa antes de continuares: se desligares o computador, perdes a base de dados? A resposta: não, se voltares a este computador. Os dados ficam guardados no Docker deste computador, e na aula seguinte o `docker compose up -d` arranca o mesmo servidor, com os mesmos dados. O `pokemon.sql` não volta a correr, porque a base já existe.

## Fase 2: O cliente faz as perguntas

Entras na base de dados com o `psql`, o cliente do terminal, e usas os primeiros comandos do psql. Rever: [O cliente faz as perguntas](../01-modelo-relacional-e-postgresql.md#o-cliente-faz-as-perguntas).

1. Entra no `psql`. O `exec db` corre um programa dentro do servidor `db`, e o programa é o `psql`, com o utilizador `postgres` e a base `pokemon`:

   ```bash
   docker compose exec db psql -U postgres -d pokemon
   ```

   O que deves ver:

   ```text
   psql (17.12 (Debian 17.12-1.pgdg12+1))
   Type "help" for help.

   pokemon=#
   ```

   A versão pode ser outra. O `pokemon=#` quer dizer que estás na base `pokemon` e que o `psql` espera um comando. A partir daqui, o SQL e os comandos com `\` escrevem-se no `psql`.

2. Lista as tabelas da base com o `\dt`. O que deves ver:

   ```text
               List of relations
    Schema |    Name     | Type  |  Owner
   --------+-------------+-------+----------
    public | combates    | table | postgres
    public | especies    | table | postgres
    public | pokemons    | table | postgres
    public | tipos       | table | postgres
    public | treinadores | table | postgres
   (5 rows)
   ```

   São as cinco tabelas que o `pokemon.sql` criou. Se aparecer `Did not find any relations.`, a base está vazia: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Sai do `psql` com o `\q`. O que deves ver: o terminal normal outra vez, à espera de um comando. Volta a entrar: no terminal, a seta para cima repete o comando anterior, e o Enter corre-o.

### Paragem 2

Entras e sais do `psql`, e o `\dt` mostra as cinco tabelas da base `pokemon`.

Pensa antes de continuares: o `\dt` é SQL? A resposta: não. É um comando do psql, porque começa por `\`, e só o `psql` o entende. Mostra que tabelas há, mas não mostra os dados que estão nelas.

## Fase 3: O SQL pergunta, e o SGBD responde

Escreves a primeira consulta em SQL e começas o `consultas.sql`, onde guardas as consultas deste laboratório. Rever: [O SQL pergunta, e o SGBD responde](../01-modelo-relacional-e-postgresql.md#o-sql-pergunta-e-o-sgbd-responde) e [Uma tabela tem linhas e colunas](../01-modelo-relacional-e-postgresql.md#uma-tabela-tem-linhas-e-colunas).

1. Cria o ficheiro `consultas.sql`, na pasta do projeto, com esta primeira versão. Uma linha que começa por `--` é um comentário, que o SGBD ignora:

   ```sql
   -- consultas.sql: as primeiras consultas à base de dados do ginásio Pokémon.

   -- Os treinadores, com todas as colunas.
   SELECT * FROM treinadores;
   ```

2. Copia a linha do `SELECT` para o `psql`, com o ponto e vírgula, e carrega em Enter. O que deves ver:

   ```text
    id | nome  |  cidade
   ----+-------+----------
     1 | Ash   | Pallet
     2 | Misty | Cerulean
     3 | Brock | Pewter
     4 | Gary  | Pallet
   (4 rows)
   ```

   É a tabela `treinadores`, com uma linha por treinador e uma coluna por dado. O `(4 rows)` diz que a resposta tem quatro linhas.

3. Experimenta um engano de propósito: no `psql`, escreve `SELECT * FROM tipos`, sem o ponto e vírgula, e carrega em Enter. O que deves ver: nenhuma resposta, e o início da linha passa de `pokemon=#` para `pokemon-#`. O `psql` está à espera do resto da consulta, porque não encontrou o ponto e vírgula. Escreve `;` e carrega em Enter: aparece a tabela `tipos`, com cinco linhas, do `Fogo` à `Pedra`.

4. Junta ao `consultas.sql`, no fim, as consultas dos tipos e das espécies, cada uma com o seu comentário:

   ```sql
   -- Os tipos dos Pokémon.
   SELECT * FROM tipos;

   -- As espécies, com o número do tipo de cada uma.
   SELECT * FROM especies;
   ```

   Copia a das espécies para o `psql` e corre-a. O que deves ver: sete linhas, do `Charmander` ao `Onix`, cada uma com um número na coluna `tipo_id`.

### Paragem 3

O `consultas.sql` tem três consultas, e cada uma corre no `psql` e mostra uma tabela inteira.

Pensa antes de continuares: o que faz o `*` no `SELECT * FROM especies;`? A resposta: pede todas as colunas da tabela. Por isso, a resposta tem o `id`, o `nome` e o `tipo_id`.

## Fase 4: Escolher as colunas

Pedes só as colunas de que precisas, pelos seus nomes. Rever: [Escolher as colunas](../01-modelo-relacional-e-postgresql.md#escolher-as-colunas).

1. Antes de correres, prevê: quantas linhas e quantas colunas tem a resposta desta consulta? Depois, corre-a no `psql`:

   ```sql
   SELECT nome, cidade FROM treinadores;
   ```

   O que deves ver:

   ```text
    nome  |  cidade
   -------+----------
    Ash   | Pallet
    Misty | Cerulean
    Brock | Pewter
    Gary  | Pallet
   (4 rows)
   ```

   São quatro linhas e duas colunas. A consulta escolhe as colunas, mas continuam a aparecer todos os treinadores.

2. Junta-a ao `consultas.sql`, no fim, com o seu comentário:

   ```sql
   -- O nome e a cidade de cada treinador.
   SELECT nome, cidade FROM treinadores;
   ```

3. Experimenta um engano de propósito: corre a mesma consulta sem a vírgula, `SELECT nome cidade FROM treinadores;`. O que deves ver: uma só coluna, chamada `cidade`, com os nomes dos treinadores. Isto acontece porque, sem a vírgula, o PostgreSQL lê `cidade` como um nome novo para a coluna `nome`. Não dá erro, e por isso é fácil não reparar. Esta consulta não vai para o `consultas.sql`.

### Paragem 4

O `consultas.sql` tem quatro consultas, e a última mostra só o nome e a cidade dos treinadores.

Pensa antes de continuares: que consulta mostra a cidade antes do nome? A resposta: `SELECT cidade, nome FROM treinadores;`. As colunas aparecem pela ordem em que as escreves.

## Fase 5: Cada coluna tem um tipo de dados

Vês o tipo de dados de cada coluna com o `\d`. Rever: [Cada coluna tem um tipo de dados](../01-modelo-relacional-e-postgresql.md#cada-coluna-tem-um-tipo-de-dados).

1. Vê as colunas da tabela `treinadores`. Escreve `\d treinadores` e carrega em Enter. O que deves ver, no início:

   ```text
                      Table "public.treinadores"
    Column |         Type          | Collation | Nullable | Default
   --------+-----------------------+-----------+----------+---------
    id     | integer               |           | not null |
    nome   | character varying(30) |           | not null |
    cidade | character varying(30) |           | not null |
   ```

   O `id` é um número inteiro, e o `nome` e a `cidade` são textos com 30 caracteres no máximo. O `not null`, nas três, quer dizer que nenhuma pode ficar sem valor. Por baixo, há mais linhas, com outras regras da tabela. Se o terminal mostrar `(END)` ou `:` na última linha, carrega em `q` para voltares ao `pokemon=#`.

2. Vê as colunas da tabela `combates`, com `\d combates`. O que deves ver, no início:

   ```text
                           Table "public.combates"
       Column     |         Type          | Collation | Nullable | Default
   ---------------+-----------------------+-----------+----------+---------
    id            | integer               |           | not null |
    data          | date                  |           | not null |
    cidade        | character varying(30) |           | not null |
    desafiante_id | integer               |           | not null |
    lider_id      | integer               |           | not null |
    vencedor_id   | integer               |           |          |
   ```

   A `data` é do tipo `date`, uma data; as outras colunas são números inteiros e texto.

### Paragem 5

Sabes ler, no `\d` de uma tabela, o nome de cada coluna e o tipo de dados dela.

Pensa antes de continuares: porque é que a coluna `data` é do tipo de dados `date` e não um texto? A resposta: com o tipo `date`, o SGBD sabe que é uma data. Recusa uma data que não existe, como `'2026-02-30'`, que num texto ficava guardada sem aviso.

## Fase 6: O NULL quer dizer que não há valor

Encontras o NULL no combate sem vencedor e distingue-lo do zero e do texto vazio. Rever: [O NULL quer dizer que não há valor](../01-modelo-relacional-e-postgresql.md#o-null-quer-dizer-que-não-há-valor).

1. Corre a consulta dos combates no `psql`:

   ```sql
   SELECT * FROM combates;
   ```

   O que deves ver:

   ```text
    id |    data    |  cidade  | desafiante_id | lider_id | vencedor_id
   ----+------------+----------+---------------+----------+-------------
     1 | 2026-11-03 | Cerulean |             1 |        2 |           2
     2 | 2026-11-03 | Cerulean |             1 |        2 |           1
     3 | 2026-11-10 | Pewter   |             1 |        3 |
   (3 rows)
   ```

   O combate 3 tem a `vencedor_id` vazia: é o NULL, porque o combate ainda não acabou.

2. Antes de correres, prevê: na tabela `combates`, que colunas podem ficar sem valor? Depois, escreve outra vez `\d combates` e olha para a coluna `Nullable`. O que deves ver: só a `vencedor_id` tem a `Nullable` vazia, sem `not null`. É a única coluna dos combates que aceita o NULL, porque todas as outras se sabem quando o combate começa.

3. Pede ao `psql` que escreva o NULL, para não o confundires com um texto vazio. Escreve `\pset null '(nulo)'` e carrega em Enter. O que deves ver: `Null display is "(nulo)".`. Corre outra vez a consulta dos combates: no combate 3, aparece `(nulo)` na `vencedor_id`.

4. Corre a consulta da alcunha e da vida dos Pokémon:

   ```sql
   SELECT alcunha, vida FROM pokemons;
   ```

   O que deves ver:

   ```text
    alcunha | vida
   ---------+------
    (nulo)  |   90
    (nulo)  |  110
    Pika    |   80
    (nulo)  |    0
            |  100
    (nulo)  |  140
   (6 rows)
   ```

   Quatro Pokémon não têm alcunha: o NULL. O da quarta linha tem a vida 0, que é um valor: está KO. O da quinta linha tem a alcunha vazia, que também é um valor, um texto sem letras.

5. Junta as duas consultas ao `consultas.sql`, no fim. O `\pset` não vai para o ficheiro, porque é um comando do psql, e não SQL:

   ```sql
   -- Os combates. O combate 3 ainda não tem vencedor.
   SELECT * FROM combates;

   -- A alcunha e a vida de cada Pokémon capturado.
   SELECT alcunha, vida FROM pokemons;
   ```

### Paragem 6

No `psql`, o NULL aparece como `(nulo)`, e distingue-lo do zero e do texto vazio.

Pensa antes de continuares: que diferença há entre a alcunha do primeiro Pokémon e a do quinto? A resposta: o primeiro não tem alcunha, e a célula tem o NULL. O quinto tem uma alcunha, que é um texto vazio, `''`.

## Fase 7: A chave estrangeira aponta para outra tabela

Encontras as chaves da tabela `pokemons` e segues as chaves estrangeiras à mão, para saber de quem é cada Pokémon. Rever: [A chave estrangeira aponta para outra tabela](../01-modelo-relacional-e-postgresql.md#a-chave-estrangeira-aponta-para-outra-tabela) e [A chave primária identifica cada linha](../01-modelo-relacional-e-postgresql.md#a-chave-primária-identifica-cada-linha).

1. Escreve `\d pokemons` e lê as linhas de baixo. O que deves ver, depois das colunas:

   ```text
   Indexes:
       "pokemons_pkey" PRIMARY KEY, btree (id)
   Foreign-key constraints:
       "pokemons_especie_id_fkey" FOREIGN KEY (especie_id) REFERENCES especies(id)
       "pokemons_treinador_id_fkey" FOREIGN KEY (treinador_id) REFERENCES treinadores(id)
   ```

   A chave primária, a coluna que identifica cada linha, é o `id`. As duas chaves estrangeiras dizem que o `especie_id` aponta para o `id` das espécies, e o `treinador_id` para o `id` dos treinadores.

2. Vê os Pokémon capturados, com todas as colunas:

   ```sql
   SELECT * FROM pokemons;
   ```

   O que deves ver: seis linhas. A última é o Pokémon 6, com o `especie_id` 7 e o `treinador_id` 3.

3. Segue as duas chaves estrangeiras do Pokémon 6. Corre a consulta do número e do nome das espécies, e procura a linha com o `id` 7:

   ```sql
   SELECT id, nome FROM especies;
   ```

   O que deves ver: sete linhas, e a do `id` 7 é o `Onix`. Corre agora `SELECT id, nome FROM treinadores;` e procura a linha com o `id` 3: é o `Brock`. O Pokémon 6 é o Onix do Brock.

4. Junta as três consultas ao `consultas.sql`, no fim:

   ```sql
   -- Os Pokémon capturados. O especie_id e o treinador_id são chaves estrangeiras.
   SELECT * FROM pokemons;

   -- O número e o nome de cada espécie, para seguir o especie_id.
   SELECT id, nome FROM especies;

   -- O número e o nome de cada treinador, para seguir o treinador_id.
   SELECT id, nome FROM treinadores;
   ```

5. Sai do `psql` com o `\q`.

### Paragem 7

O `consultas.sql` está completo, e sabes seguir uma chave estrangeira até à linha para onde aponta. O ficheiro completo, como deve estar agora:

```sql
-- consultas.sql: as primeiras consultas à base de dados do ginásio Pokémon.

-- Os treinadores, com todas as colunas.
SELECT * FROM treinadores;

-- Os tipos dos Pokémon.
SELECT * FROM tipos;

-- As espécies, com o número do tipo de cada uma.
SELECT * FROM especies;

-- O nome e a cidade de cada treinador.
SELECT nome, cidade FROM treinadores;

-- Os combates. O combate 3 ainda não tem vencedor.
SELECT * FROM combates;

-- A alcunha e a vida de cada Pokémon capturado.
SELECT alcunha, vida FROM pokemons;

-- Os Pokémon capturados. O especie_id e o treinador_id são chaves estrangeiras.
SELECT * FROM pokemons;

-- O número e o nome de cada espécie, para seguir o especie_id.
SELECT id, nome FROM especies;

-- O número e o nome de cada treinador, para seguir o treinador_id.
SELECT id, nome FROM treinadores;
```

As consultas estão pela ordem das fases, cada uma com um comentário a dizer o que mostra. Só tem SQL: os comandos do psql, como o `\pset`, ficaram de fora.

Pensa antes de continuares: porque é que a tabela `treinadores` não tem uma coluna com os Pokémon de cada treinador? A resposta: uma célula guarda um só valor, e um treinador pode ter muitos Pokémon. Por isso, a chave estrangeira fica do lado dos muitos, em cada Pokémon.

## Fase 8: A mesma consulta no pgAdmin

Ligas o pgAdmin ao teu servidor e corres nele as consultas do `consultas.sql`. O pgAdmin é outro cliente, e o SQL é o mesmo. Rever: [A mesma consulta no pgAdmin](../01-modelo-relacional-e-postgresql.md#a-mesma-consulta-no-pgadmin).

1. Abre o pgAdmin. Na árvore do lado esquerdo, clica com o botão direito em `Servers` e escolhe `Register`, depois `Server...`. Abre-se a janela `Register - Server`.

2. No separador `General`, escreve `Pokémon` no campo `Name`. É só o nome com que o servidor aparece na árvore.

3. No separador `Connection`, preenche estes campos e deixa os outros como estão:

   - `Host name/address`: `127.0.0.1`, o endereço deste computador.
   - `Port`: `5433`, a porta por onde o teu computador chega ao servidor.
   - `Username`: `postgres`.
   - `Password`: a palavra-passe que escreveste no `.env`.
   - `Save password?`: ligado, para o pgAdmin não ta pedir de cada vez.

   Carrega em `Save`. O que deves ver: o servidor `Pokémon` na árvore, debaixo de `Servers`. Se aparecer uma mensagem de erro, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Abre, na árvore, `Pokémon`, depois `Databases`. O que deves ver: duas bases, `pokemon` e `postgres`. A `postgres` é a que o PostgreSQL cria para uso próprio. Dentro de `pokemon`, as tabelas estão em `Schemas`, `public`, `Tables`.

5. Clica na base `pokemon` e escolhe a opção `Query Tool` do menu Tools. Abre-se um separador novo, com um espaço para escrever SQL. Copia para lá o conteúdo do `consultas.sql`.

6. Seleciona, com o rato, a linha `SELECT * FROM pokemons;` e carrega em F5. O pgAdmin corre só o texto selecionado. O que deves ver: no separador `Data Output`, por baixo, uma grelha com os seis Pokémon. Por baixo do nome de cada coluna, aparece o tipo de dados dela, e a coluna `id` tem `[PK]`, a marca da chave primária. As alcunhas sem valor aparecem como `[null]`, e a alcunha vazia do quinto Pokémon aparece em branco. Se carregares em F5 sem selecionar nada, o pgAdmin corre todas as consultas, mas a grelha só mostra a resposta da última.

7. Provoca um erro de propósito: numa linha nova da Query Tool, escreve `\dt`, seleciona-a e carrega em F5. O que deves ver, no separador `Messages`: `ERROR: syntax error at or near "\"`. Isto acontece porque o `\dt` é um comando do psql, e o pgAdmin envia o texto ao servidor como SQL, onde a barra não quer dizer nada. Apaga a linha.

8. Vê o modelo da base desenhado pelo pgAdmin. Na árvore, clica com o botão direito na base `pokemon` e escolhe `ERD For Database`. O que deves ver: as cinco tabelas, em caixas, com as colunas, uma chave ao lado de cada chave primária e linhas entre as tabelas ligadas. É o modelo do [exemplo guiado do guia](../01-modelo-relacional-e-postgresql.md#o-modelo-completo), com outro desenho.

### Paragem 8

O pgAdmin está ligado ao teu servidor, corre as consultas do `consultas.sql` e desenha o modelo da base.

Pensa antes de continuares: o `psql` e o pgAdmin mostram os mesmos dados? A resposta: sim. São dois clientes ligados ao mesmo servidor e à mesma base de dados, e a mesma consulta dá a mesma resposta nos dois. Muda só a forma de a mostrar: texto no `psql`, uma grelha no pgAdmin.

## Se alguma coisa falhar

1. O Docker Desktop está aberto? Corre `docker ps`. Se aparecer uma mensagem de erro, abre o Docker Desktop, espera que acabe de arrancar e tenta outra vez.
2. Estás na pasta do projeto? Corre `pwd`: o caminho tem de acabar em `pokemon-sql`. Os comandos `docker compose` só funcionam na pasta que tem o `compose.yaml`.
3. O servidor está a correr? Corre `docker compose ps`: o `db` tem de aparecer com `Up`. Se não aparecer, corre `docker compose up -d`.
4. Estás no `psql` ou no terminal normal? No `psql`, o início da linha é `pokemon=#`; os comandos `docker` escrevem-se no terminal normal, e o SQL e os comandos com `\` escrevem-se no `psql`.

### `Falta o ficheiro .env com a POSTGRES_PASSWORD`

O `docker compose up -d` não encontrou a palavra-passe. O ficheiro `.env` não existe, não está na pasta do `compose.yaml`, tem outro nome, como `.env.txt`, ou a linha não tem nada depois do `=`. Confirma o nome e a linha, como no passo 3 de [Preparar o projeto](#preparar-o-projeto), e corre outra vez o `docker compose up -d`.

### `no configuration file provided: not found`

O terminal não está na pasta do projeto, e o Docker não encontra o `compose.yaml`. Muda para a pasta `pokemon-sql`, ou abre-a no VS Code e abre um terminal novo.

### `service "db" is not running`

O servidor está parado, e o `docker compose exec` não tem onde correr o `psql`. Arranca-o com `docker compose up -d` e entra outra vez.

### `port is already allocated`

Outro programa já usa a porta 5433 deste computador, muitas vezes um servidor de outra pasta ainda a correr. O `docker ps` mostra os servidores ligados e as portas de cada um. Para o outro servidor, na pasta dele, com `docker compose stop`, e corre outra vez o `docker compose up -d` na tua.

### Apareceu uma pasta `pokemon.sql`, e o servidor não fica ligado

O `pokemon.sql` não estava na pasta, ou tinha outro nome, no primeiro `docker compose up -d`. O Docker criou uma pasta vazia com esse nome, e o servidor parou, porque não a consegue correr. O `docker compose ps` não mostra o `db`, e o `docker compose exec` responde `service "db" is not running`. Apaga o servidor e os dados com `docker compose down -v` e apaga a pasta `pokemon.sql`. Copia o ficheiro como no passo 2 de [Preparar o projeto](#preparar-o-projeto) e corre outra vez `docker compose up -d`.

### `Did not find any relations.`, ou faltam tabelas

A base `pokemon` existe, mas está vazia ou incompleta: o `pokemon.sql` estava vazio, ou a cópia ficou a meio, no primeiro `docker compose up -d`. O `docker compose logs db` mostra linhas com `ERROR` no sítio onde o ficheiro falhou. Sai do `psql`, apaga o servidor e os dados com `docker compose down -v`, copia outra vez o `pokemon.sql` inteiro e corre `docker compose up -d`.

### O terminal mostra `(END)` ou `:` na última linha

A resposta não coube no terminal, e o `psql` mostra-a página a página. Carrega em espaço para veres o resto, ou em `q` para voltares ao `pokemon=#`.

### No pgAdmin, `password authentication failed for user "postgres"`

A palavra-passe não é a do servidor. O servidor ficou com a palavra-passe que estava no `.env` no primeiro `docker compose up -d`, e mudar o `.env` depois disso não a muda. Escreve a palavra-passe original. Se não a souberes, apaga o servidor e os dados com `docker compose down -v` e arranca-o outra vez com `docker compose up -d`: o servidor novo fica com a palavra-passe que está agora no `.env`.

### No pgAdmin, `Is the server running on that host and accepting TCP/IP connections?`

A mensagem começa por `Unable to connect to server` e acaba nesta pergunta: "o servidor está a correr nesse endereço e aceita ligações?". O pgAdmin não encontrou nenhum servidor no endereço e na porta que escreveste. Confirma que o servidor está a correr, com o `docker compose ps`, e que escreveste `127.0.0.1` e a porta `5433`, e não a 5432.

## Desafios

1. Descobre que treinadores não têm nenhum Pokémon capturado, só com consultas `SELECT` às tabelas, seguindo as chaves à mão. Pista: compara os números da coluna `treinador_id` dos Pokémon com os números da coluna `id` dos treinadores.
2. Descobre que espécies não têm nenhum Pokémon capturado, da mesma maneira.
3. A tabela `combates` não guarda com que Pokémon lutou cada treinador. Que colunas lhe acrescentavas para o guardar, e para onde apontaria cada uma? Escreve a linha nova dos combates na forma do modelo relacional do guia. Pista: num combate lutam dois Pokémon, um de cada treinador.

## Antes de terminares

- [ ] O servidor arranca com `docker compose up -d`, e o `docker compose ps` mostra o `db` com `Up`.
- [ ] Entras na base `pokemon` com o `psql`, e o `\dt` mostra as cinco tabelas.
- [ ] O `consultas.sql` tem as nove consultas das fases 3 a 7, cada uma com o seu comentário, e todas correm no `psql`.
- [ ] O pgAdmin está ligado ao teu servidor e corre as consultas do `consultas.sql`.
- [ ] Sabes seguir uma chave estrangeira até à linha da tabela para onde aponta.
- [ ] No fim da aula, paras o servidor com `docker compose stop`, na pasta do projeto. Os dados ficam guardados para a próxima vez.

![Rodapé](../../imagens/rodape.png)
