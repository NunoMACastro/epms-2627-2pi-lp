![Cabeçalho](../../../imagens/cabecalho.png)

# Exemplo dos Pokémon em SQL

A base de dados do ginásio Pokémon, guardada no PostgreSQL: os treinadores, os Pokémon que capturaram, as espécies e os tipos, e os combates nos ginásios. Cresce com a matéria, e cada pasta é uma versão completa, que corre sozinha. É usado nos temas [01 Modelo relacional e ambiente PostgreSQL](../../../02-sql-fundamentos/01-modelo-relacional-e-postgresql.md), [02 DDL e integridade](../../../02-sql-fundamentos/02-ddl-e-integridade.md), [03 DML e consultas com contexto](../../../02-sql-fundamentos/03-dml-e-consultas-com-contexto.md) e [04 JOIN e agregação introdutórios](../../../02-sql-fundamentos/04-join-e-agregacao-introdutorios.md).

## O que está nesta pasta

- `01-modelo-relacional-e-postgresql`, a versão do tema 01. O `pokemon.sql` cria as cinco tabelas e põe lá os dados. O `compose.yaml` arranca o servidor PostgreSQL no Docker e, na primeira vez, corre o `pokemon.sql`. O `.env.example` diz que linha leva o ficheiro `.env`, onde fica a palavra-passe do servidor, e o `.gitignore` deixa o `.env` fora do Git.
- `02-ddl-e-integridade`, a versão do tema 02. Tem tudo o que a versão 01 tem, e o `compose.yaml` mostra a pasta do projeto ao servidor, para o `psql` correr os ficheiros com o `\i`. O `esquema.sql` cria as cinco tabelas da base `ginasio`, com as regras que a base garante. O `dados.sql` põe lá os dados, e o `recusas.sql` tem linhas que a base recusa, uma por regra.
- `03-dml-e-consultas-com-contexto`, a versão do tema 03. Tem tudo o que a versão 02 tem, e o `dados.sql` tem, no fim, mais duas espécies, dois Pokémon KO e um combate. O `perguntas.sql` tem onze perguntas ao ginásio, cada uma com a consulta que a responde e o resultado esperado num comentário.
- `04-join-e-agregacao-introdutorios`, a versão do tema 04. Tem tudo o que a versão 03 tem, com os mesmos dados. O `relatorios.sql` tem onze relatórios que juntam tabelas e fazem resumos, cada um com o resultado esperado num comentário.

## Como correr a versão 01

Precisas do Docker Desktop aberto. Copia o `compose.yaml`, o `pokemon.sql` e o `.gitignore` para uma pasta tua, fora da pasta do repositório dos alunos. Cria nessa pasta um ficheiro `.env`, com a linha do `.env.example` e uma palavra-passe tua a seguir ao `=`. Depois, abre o terminal nessa pasta, arranca o servidor e entra no `psql`:

```bash
docker compose up -d
docker compose exec db psql -U postgres -d pokemon
```

O que deves ver: o `psql` escreve a versão e, por baixo, `pokemon=#`, à espera de um comando. Escreve `\dt` e carrega em Enter: aparece a lista das cinco tabelas, `combates`, `especies`, `pokemons`, `tipos` e `treinadores`. Para sair do `psql`, escreve `\q`. Para parar o servidor, escreve `docker compose stop`; os dados ficam guardados para a próxima vez.

O servidor também aceita ligações do pgAdmin, neste computador, no endereço `127.0.0.1` e na porta `5433`, com o utilizador `postgres` e a palavra-passe do `.env`.

## Como correr a versão 02

Precisas do Docker Desktop aberto. Copia para uma pasta tua, fora da pasta do repositório dos alunos, o `compose.yaml`, o `pokemon.sql`, o `.gitignore`, o `esquema.sql`, o `dados.sql` e o `recusas.sql`. Cria o `.env` como na versão 01. Se já tens a pasta da versão 01 a funcionar, basta trocar o `compose.yaml` pelo desta versão e juntar-lhe os três ficheiros novos.

No terminal, nessa pasta, arranca o servidor e entra no `psql`, na base `pokemon`:

```bash
docker compose up -d
docker compose exec db psql -U postgres -d pokemon
```

No `psql`, cria a base `ginasio` e sai, com `CREATE DATABASE ginasio;` e `\q`. Depois, entra na base nova:

```bash
docker compose exec db psql -U postgres -d ginasio
```

O início da linha passa a ser `ginasio=#`. Corre os três ficheiros, por esta ordem, com `\i esquema.sql`, `\i dados.sql` e `\i recusas.sql`.

O que deves ver: o `esquema.sql` escreve cinco `DROP TABLE` e cinco `CREATE TABLE`, e o `dados.sql` escreve cinco linhas `INSERT`, com o número de linhas de cada tabela. O `recusas.sql` escreve sete `ERROR`, um por cada linha que a base recusa. Na primeira vez, o `esquema.sql` escreve também cinco `NOTICE`, porque ainda não havia tabelas para apagar. O `\dt` mostra as cinco tabelas, e o `\d pokemons` mostra as regras da tabela dos Pokémon.

Se já tinhas a base `ginasio`, o `CREATE DATABASE` diz `database "ginasio" already exists`, e podes passar à base nova. O `esquema.sql` e o `dados.sql` voltam a construir a base `ginasio` de raiz sempre que os corres.

## Como correr a versão 03

Precisas do Docker Desktop aberto e de uma pasta com a versão 02 a funcionar, com a base `ginasio`. Se não a tens, faz primeiro o "Como correr a versão 02". Troca o `dados.sql` da tua pasta pelo desta versão e junta-lhe o `perguntas.sql`.

No terminal, nessa pasta, arranca o servidor e entra no `psql`, na base `ginasio`:

```bash
docker compose up -d
docker compose exec db psql -U postgres -d ginasio
```

Corre os três ficheiros, por esta ordem, com `\i esquema.sql`, `\i dados.sql` e `\i perguntas.sql`.

O que deves ver: o `dados.sql` escreve oito linhas `INSERT`, a acabar em `INSERT 0 2`, `INSERT 0 2` e `INSERT 0 1`, e o `SELECT * FROM pokemons;` mostra oito Pokémon. O `perguntas.sql` escreve onze respostas, cada uma com o número de linhas do comentário da sua pergunta.

## Como correr a versão 04

Precisas do Docker Desktop aberto e de uma pasta com a versão 03 a funcionar, com a base `ginasio`. Se não a tens, faz primeiro o "Como correr a versão 03". Junta-lhe o `relatorios.sql` desta versão.

No terminal, nessa pasta, arranca o servidor e entra no `psql`, na base `ginasio`, como na versão 03. Corre os três ficheiros, por esta ordem, com `\i esquema.sql`, `\i dados.sql` e `\i relatorios.sql`.

O que deves ver: o `relatorios.sql` escreve onze respostas, cada uma com o resultado do comentário do seu relatório. A primeira tem os oito Pokémon com o nome da espécie, e a última os quatro treinadores, com os Pokémon e os combates em que foram o líder.

![Rodapé](../../../imagens/rodape.png)
