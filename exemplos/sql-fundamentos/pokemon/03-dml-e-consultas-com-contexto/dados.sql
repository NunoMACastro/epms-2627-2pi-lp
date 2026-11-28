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
