-- recusas.sql: linhas que a base ginasio recusa, cada uma por causa de uma regra.
-- Corre-se depois do esquema.sql e do dados.sql, com \i recusas.sql. Todos os INSERT
-- dão erro, e a base fica como estava.

-- O treinador não tem cidade, e a coluna cidade é NOT NULL.
-- Erro: null value in column "cidade" of relation "treinadores" violates not-null constraint
INSERT INTO treinadores (nome) VALUES ('Tracey');

-- Não há nenhum tipo com o id 9, e o tipo_id é uma chave estrangeira.
-- Erro: insert or update on table "especies" violates foreign key constraint "especies_tipo_id_fkey"
INSERT INTO especies (nome, tipo_id) VALUES ('Mewtwo', 9);

-- Já há um tipo chamado Água, e o nome dos tipos é UNIQUE.
-- Erro: duplicate key value violates unique constraint "tipos_nome_key"
INSERT INTO tipos (nome) VALUES ('Água');

-- O Ash já tem um Pokémon com a alcunha Pika.
-- Erro: duplicate key value violates unique constraint "pokemons_treinador_id_alcunha_key"
INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 1, 'Pika', 100, 30);

-- A vida 200 passa do limite de 150.
-- Erro: new row for relation "pokemons" violates check constraint "pokemons_vida_check"
INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 4, NULL, 200, 30);

-- O ataque 0 fica abaixo do limite de 1.
-- Erro: new row for relation "pokemons" violates check constraint "pokemons_ataque_check"
INSERT INTO pokemons (especie_id, treinador_id, alcunha, vida, ataque) VALUES (2, 4, NULL, 100, 0);

-- Só há oito medalhas para ganhar.
-- Erro: new row for relation "treinadores" violates check constraint "treinadores_medalhas_check"
INSERT INTO treinadores (nome, cidade, medalhas) VALUES ('Tracey', 'Pallet', 9);
