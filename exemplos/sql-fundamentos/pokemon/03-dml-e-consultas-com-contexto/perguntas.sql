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
