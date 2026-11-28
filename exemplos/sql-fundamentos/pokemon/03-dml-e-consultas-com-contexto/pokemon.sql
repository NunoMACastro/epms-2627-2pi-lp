-- pokemon.sql: a base de dados do ginásio Pokémon, com cinco tabelas e os seus dados.
-- O servidor do compose.yaml corre este ficheiro uma vez, na primeira vez que arranca,
-- e a base de dados pokemon fica pronta para as consultas.

-- Os tipos dos Pokémon, como o Fogo e a Água.
CREATE TABLE tipos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(20) NOT NULL
);

-- As espécies. Cada espécie tem um tipo: o tipo_id aponta para uma linha de tipos.
CREATE TABLE especies (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    tipo_id INTEGER NOT NULL REFERENCES tipos (id)
);

-- Os treinadores, com a cidade de onde vêm.
CREATE TABLE treinadores (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    cidade VARCHAR(30) NOT NULL
);

-- Os Pokémon capturados. Cada um é de uma espécie e pertence a um treinador.
-- A alcunha pode ficar sem valor: nem todos os Pokémon têm alcunha.
CREATE TABLE pokemons (
    id INTEGER PRIMARY KEY,
    especie_id INTEGER NOT NULL REFERENCES especies (id),
    treinador_id INTEGER NOT NULL REFERENCES treinadores (id),
    alcunha VARCHAR(30),
    vida INTEGER NOT NULL,
    ataque INTEGER NOT NULL
);

-- Os combates nos ginásios. Três colunas apontam para treinadores: quem desafiou,
-- o líder do ginásio e quem venceu. O vencedor fica sem valor enquanto o combate
-- não acaba.
CREATE TABLE combates (
    id INTEGER PRIMARY KEY,
    data DATE NOT NULL,
    cidade VARCHAR(30) NOT NULL,
    desafiante_id INTEGER NOT NULL REFERENCES treinadores (id),
    lider_id INTEGER NOT NULL REFERENCES treinadores (id),
    vencedor_id INTEGER REFERENCES treinadores (id)
);

-- Os dados entram pela ordem das ligações: primeiro as linhas para onde as outras
-- apontam. Uma espécie só pode apontar para um tipo que já exista.
INSERT INTO tipos (id, nome) VALUES
    (1, 'Fogo'),
    (2, 'Água'),
    (3, 'Planta'),
    (4, 'Elétrico'),
    (5, 'Pedra');

INSERT INTO especies (id, nome, tipo_id) VALUES
    (1, 'Charmander', 1),
    (2, 'Squirtle', 2),
    (3, 'Bulbasaur', 3),
    (4, 'Pikachu', 4),
    (5, 'Starmie', 2),
    (6, 'Psyduck', 2),
    (7, 'Onix', 5);

INSERT INTO treinadores (id, nome, cidade) VALUES
    (1, 'Ash', 'Pallet'),
    (2, 'Misty', 'Cerulean'),
    (3, 'Brock', 'Pewter'),
    (4, 'Gary', 'Pallet');

-- O Starmie da Misty está KO: tem vida 0, que é um valor.
-- O Psyduck tem a alcunha vazia, que também é um valor: um texto sem letras.
INSERT INTO pokemons (id, especie_id, treinador_id, alcunha, vida, ataque) VALUES
    (1, 1, 1, NULL, 90, 40),
    (2, 3, 1, NULL, 110, 25),
    (3, 4, 1, 'Pika', 80, 45),
    (4, 5, 2, NULL, 0, 35),
    (5, 6, 2, '', 100, 20),
    (6, 7, 3, NULL, 140, 30);

-- O combate 3 ainda não acabou, e por isso o vencedor fica sem valor.
INSERT INTO combates (id, data, cidade, desafiante_id, lider_id, vencedor_id) VALUES
    (1, '2026-11-03', 'Cerulean', 1, 2, 2),
    (2, '2026-11-03', 'Cerulean', 1, 2, 1),
    (3, '2026-11-10', 'Pewter', 1, 3, NULL);
