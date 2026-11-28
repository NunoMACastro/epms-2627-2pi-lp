-- relatorios.sql: os relatórios do ginásio, que juntam tabelas e fazem resumos.
-- Corre-se no psql, ligado à base ginasio, com \i relatorios.sql, numa base acabada
-- de construir pelo esquema.sql e pelo dados.sql. Cada comentário diz o resultado esperado.

-- Que espécie é cada Pokémon?
-- Esperado: 8 linhas, do Charmander, o Pokémon 1, ao Staryu, o 8.
SELECT p.id, e.nome, p.vida
FROM pokemons AS p
JOIN especies AS e ON p.especie_id = e.id
ORDER BY p.id;

-- De que tipo é cada espécie?
-- Esperado: 9 linhas. A Água tem quatro espécies: o Squirtle, o Starmie, o Psyduck e o Staryu.
SELECT e.nome AS especie, tp.nome AS tipo
FROM especies AS e
JOIN tipos AS tp ON e.tipo_id = tp.id
ORDER BY e.id;

-- De que espécie e de que tipo é cada Pokémon?
-- Esperado: 8 linhas. O Onix e o Geodude são da Pedra; o Starmie, o Psyduck e o Staryu, da Água.
SELECT p.id, e.nome AS especie, tp.nome AS tipo
FROM pokemons AS p
JOIN especies AS e ON p.especie_id = e.id
JOIN tipos AS tp ON e.tipo_id = tp.id
ORDER BY p.id;

-- Que Pokémon de Água há, do que tem mais vida para o que tem menos?
-- Esperado: 3 linhas, os Pokémon 5, 4 e 8.
SELECT p.id, e.nome AS especie, p.vida
FROM pokemons AS p
JOIN especies AS e ON p.especie_id = e.id
JOIN tipos AS tp ON e.tipo_id = tp.id
WHERE tp.nome = 'Água'
ORDER BY p.vida DESC, p.id;

-- Quem desafiou, e quem era o líder, em cada combate?
-- Esperado: 4 linhas. O Ash desafiou a Misty duas vezes e o Brock uma; a Misty desafiou o Brock.
SELECT c.id, d.nome AS desafiante, l.nome AS lider
FROM combates AS c
JOIN treinadores AS d ON c.desafiante_id = d.id
JOIN treinadores AS l ON c.lider_id = l.id
ORDER BY c.id;

-- Em que combates foi cada treinador o desafiante?
-- Esperado: 4 linhas, o Ash nos combates 1, 2 e 3 e a Misty no 4. O Brock e o Gary
-- não aparecem, porque o JOIN deixa de fora quem não tem par.
SELECT t.nome, c.id AS combate
FROM treinadores AS t
JOIN combates AS c ON c.desafiante_id = t.id
ORDER BY t.id, c.id;

-- Que treinadores nunca desafiaram ninguém?
-- Esperado: 2 linhas, o Brock e o Gary.
SELECT t.nome
FROM treinadores AS t
LEFT JOIN combates AS c ON c.desafiante_id = t.id
WHERE c.id IS NULL
ORDER BY t.id;

-- Quantos combates há, quantos acabaram, e quando foram o primeiro e o último?
-- Esperado: 1 linha: 4 combates, 3 acabados, de 2026-11-03 a 2026-11-17.
SELECT COUNT(*) AS combates, COUNT(vencedor_id) AS acabados,
       MIN(data) AS primeiro, MAX(data) AS ultimo
FROM combates;

-- Quantas espécies tem cada tipo?
-- Esperado: 5 linhas: a Água com 4, a Pedra com 2, e o Elétrico, o Fogo e a Planta com 1.
SELECT tp.nome AS tipo, COUNT(*) AS especies
FROM especies AS e
JOIN tipos AS tp ON e.tipo_id = tp.id
GROUP BY tp.id, tp.nome
ORDER BY especies DESC, tipo;

-- Que tipos têm mais de uma espécie?
-- Esperado: 2 linhas: a Água com 4 e a Pedra com 2.
SELECT tp.nome AS tipo, COUNT(*) AS especies
FROM especies AS e
JOIN tipos AS tp ON e.tipo_id = tp.id
GROUP BY tp.id, tp.nome
HAVING COUNT(*) > 1
ORDER BY especies DESC;

-- Quantos Pokémon tem cada treinador, e em quantos combates foi o líder?
-- Esperado: 4 linhas: o Ash com 3 e 0, a Misty com 3 e 2, o Brock com 2 e 2 e o Gary
-- com 0 e 0. Sem o DISTINCT, a Misty e o Brock ficavam com os números multiplicados.
SELECT t.nome, COUNT(DISTINCT p.id) AS pokemons, COUNT(DISTINCT c.id) AS liderados
FROM treinadores AS t
LEFT JOIN pokemons AS p ON p.treinador_id = t.id
LEFT JOIN combates AS c ON c.lider_id = t.id
GROUP BY t.id, t.nome
ORDER BY t.id;
