![Cabeçalho](../../../imagens/cabecalho.png)

# Exemplo dos Pokémon em SQL

A base de dados do ginásio Pokémon, guardada no PostgreSQL: os treinadores, os Pokémon que capturaram, as espécies e os tipos, e os combates nos ginásios. Cresce com a matéria, e cada pasta é uma versão completa, que corre sozinha. É usado no tema [01 Modelo relacional e ambiente PostgreSQL](../../../02-sql-fundamentos/01-modelo-relacional-e-postgresql.md).

## O que está nesta pasta

- `01-modelo-relacional-e-postgresql`, a versão do tema 01. O `pokemon.sql` cria as cinco tabelas e põe lá os dados. O `compose.yaml` arranca o servidor PostgreSQL no Docker e, na primeira vez, corre o `pokemon.sql`. O `.env.example` diz que linha leva o ficheiro `.env`, onde fica a palavra-passe do servidor, e o `.gitignore` deixa o `.env` fora do Git.

## Como correr

Precisas do Docker Desktop aberto. Copia o `compose.yaml`, o `pokemon.sql` e o `.gitignore` para uma pasta tua, fora da pasta do repositório dos alunos. Cria nessa pasta um ficheiro `.env`, com a linha do `.env.example` e uma palavra-passe tua a seguir ao `=`. Depois, abre o terminal nessa pasta, arranca o servidor e entra no `psql`:

```bash
docker compose up -d
docker compose exec db psql -U postgres -d pokemon
```

O que deves ver: o `psql` escreve a versão e, por baixo, `pokemon=#`, à espera de um comando. Escreve `\dt` e carrega em Enter: aparece a lista das cinco tabelas, `combates`, `especies`, `pokemons`, `tipos` e `treinadores`. Para sair do `psql`, escreve `\q`. Para parar o servidor, escreve `docker compose stop`; os dados ficam guardados para a próxima vez.

O servidor também aceita ligações do pgAdmin, neste computador, no endereço `127.0.0.1` e na porta `5433`, com o utilizador `postgres` e a palavra-passe do `.env`.

![Rodapé](../../../imagens/rodape.png)
