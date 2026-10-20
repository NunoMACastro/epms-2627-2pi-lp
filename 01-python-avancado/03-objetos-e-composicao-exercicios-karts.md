![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento no Grande Prémio de Karts

Ficha do tema Objetos, composição e comportamento, do módulo 10794, Programação avançada com Python. Constróis um jogo de corridas de karts completo, num só programa, e decides tu como o escrever a partir das regras do jogo. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](03-objetos-e-composicao.md) e o [laboratório](03-objetos-e-composicao-laboratorio.md). Convém teres feito antes a [ficha principal do tema](03-objetos-e-composicao-exercicios.md), porque este exercício junta num só programa o que lá praticaste por partes. Usas também três coisas do 10.º ano que o guia não usa: a divisão inteira `//`, o resto da divisão `%` e o `range`.

## Como trabalhar

A ficha tem um só exercício, o Grande Prémio de Karts, que é a parte obrigatória. O desafio e a secção "Para ires mais longe" são opcionais.

O enunciado não te diz como escrever o programa. Diz-te as regras do jogo, e cada regra pede-te uma decisão: que classes crias, o que cada uma guarda e sabe fazer, e como as ligas umas às outras. Os nomes que o programa final usa, como `Kart`, `Piloto` ou `com_turbo`, são obrigatórios. Os outros escolhes tu.

Lê as regras todas antes de começares. Depois começa pelos karts e testa-os sozinhos, antes de passares aos pilotos e à corrida. Cria um kart, põe-no a fazer as três coisas da regra 2 e mostra a velocidade e a distância com `print`. Faz o exercício todo num só ficheiro, por exemplo `karts.py`.

## Exercício 1: Grande Prémio de Karts

Vais programar uma corrida de karts ao estilo do Mario Kart: três pilotos, quatro voltas e, pelo caminho, caixas com power-ups.

### Os karts

1. Cada kart tem um nome, uma velocidade e a distância que já percorreu. Normalmente, sai da garagem parado, com velocidade 0 e distância 0.
2. Um kart sabe fazer três coisas:
   - acelerar, e ganha 20 de velocidade;
   - avançar, e soma à distância tantos metros quanto a velocidade;
   - sofrer um choque, e fica com metade da velocidade, arredondada para baixo. A 35, fica com 17.
3. A velocidade nunca passa de 100 nem fica abaixo de 0, aconteça o que acontecer. Se uma conta der 130, fica 100. Se der `-20`, fica 0. Esta regra escreve-se num só sítio do programa e vale também quando alguém escreve `kart.velocidade = 500`.
4. Além dos karts normais, há karts leves e karts pesados:
   - um kart leve acelera mais 10 do que os outros;
   - num choque, um kart pesado só perde 10 de velocidade.

   Em tudo o resto, os três tipos são iguais, e o que é igual escreve-se uma só vez.
5. Alguns karts saem da garagem com arranque turbo, já a 50. Tem de ser possível criar numa só linha um kart de qualquer tipo com arranque turbo. Um kart leve com arranque turbo continua a ser um kart leve.

### Os pilotos e a corrida

6. Cada piloto tem um nome e conduz um kart que escolheu na garagem. O kart já existia antes de o piloto o escolher e continua a existir se o piloto sair do jogo.
7. Uma corrida tem o nome do circuito, o número de voltas e os pilotos inscritos. Os pilotos já existem antes da corrida e continuam a existir depois dela, para poderem correr outras.
8. Em cada volta, os pilotos jogam pela ordem em que se inscreveram. Cada um acelera, abre uma caixa e avança. O power-up que estiver na caixa é aplicado ao kart desse piloto.
9. No fim de cada volta, a corrida regista três coisas: o número da volta, o nome de quem vai à frente (quem percorreu mais distância) e a distância dele. Num empate, fica à frente quem se inscreveu primeiro. É a própria corrida que faz estes registos, enquanto corre, e só ela os guarda. No fim, mostra o registo e o vencedor, que é quem vai à frente no fim da última volta.

### Os power-ups

10. Cada power-up é uma função que recebe o kart que abriu a caixa. Há quatro, escritos por esta ordem:
    - `banana`: o kart escorrega e sofre um choque;
    - `cogumelo`: o kart ganha 30 de velocidade;
    - `tinta`: o piloto deixa de ver e trava, e o kart perde 40 de velocidade;
    - `estrela`: o kart fica com a velocidade máxima.
11. As caixas dão os power-ups pela ordem em que estão escritos no programa, um por caixa, e depois do último volta-se ao primeiro. A ordem não recomeça em cada piloto nem em cada volta. Não há números ao acaso.
12. Os criadores do jogo vão inventar power-ups novos. Para isso, querem escrever só a função do power-up novo e uma linha por cima dela, e a corrida tem de passar logo a usá-lo. Nenhuma outra linha do programa muda.

### O programa que tem de funcionar

O teu programa tem de acabar com estas linhas, sem as mudar:

```python
teste = Kart("Teste")
teste.velocidade = 500
print("Teste dos limites:", teste.velocidade)
print()

ines = Piloto("Inês", KartLeve.com_turbo("Foguete"))
rui = Piloto("Rui", KartPesado("Rinoceronte"))
ana = Piloto("Ana", Kart("Clássico"))

corrida = Corrida("Arco-Íris", 4)
corrida.inscrever(ines)
corrida.inscrever(rui)
corrida.inscrever(ana)
corrida.correr()
corrida.mostrar_registo()
```

### A saída

Com essas linhas no fim, o teu programa tem de mostrar exatamente isto:

```text
Teste dos limites: 100

=== Grande Prémio do Arco-Íris: 4 voltas ===
 - Inês no Foguete (KartLeve)
 - Rui no Rinoceronte (KartPesado)
 - Ana no Clássico (Kart)

Volta 1
  Inês: banana, velocidade 40, distância 40
  Rui: cogumelo, velocidade 50, distância 50
  Ana: tinta, velocidade 0, distância 0

Volta 2
  Inês: estrela, velocidade 100, distância 140
  Rui: banana, velocidade 60, distância 110
  Ana: cogumelo, velocidade 50, distância 50

Volta 3
  Inês: tinta, velocidade 60, distância 200
  Rui: estrela, velocidade 100, distância 210
  Ana: banana, velocidade 35, distância 85

Volta 4
  Inês: cogumelo, velocidade 100, distância 300
  Rui: tinta, velocidade 60, distância 270
  Ana: estrela, velocidade 100, distância 185

Registo da corrida:
 - Volta 1: à frente Rui, com 50 m
 - Volta 2: à frente Inês, com 140 m
 - Volta 3: à frente Rui, com 210 m
 - Volta 4: à frente Inês, com 300 m
Vencedor: Inês
```

## Apoio

Pistas que ajudam sem dar a resposta. Tenta primeiro sozinho, e usa só a pista da regra em que estás preso.

- Regra 3: nos Pokémon das aulas, a vida também nunca passa de 150, mesmo com `bulbasaur.vida = 200`. Como é que o programa garante isso, sem repetir a verificação em cada método?
- Regra 4: diz em voz alta "um kart leve é um kart" e "um kart leve tem um kart". Qual das duas frases é verdadeira? Como é que o fogo e a água dos Pokémon partilham o que têm em comum?
- Regra 5: no ginásio das aulas, o `Lider` também se criava numa linha, já com a equipa. Quem escreve `KartLeve.com_turbo("Foguete")` está a pedir um kart de que classe? Como é que o código que cria o kart fica a saber isso?
- Regras 6, 7 e 9: para cada coisa que um piloto ou uma corrida guarda, faz as duas perguntas do guia. Faz sentido sem o todo? Quem a cria?
- Regra 10: antes de escreveres a banana, pensa num kart normal e num kart pesado, os dois a 70. Com que velocidade fica cada um depois de escorregar? Quem sabe de que tipo é o kart: a banana ou o próprio kart?
- Regra 11: quem abre as caixas, e onde guarda quantas já abriu? Se o contador vai 0, 1, 2, 3, 4, 5, 6, que conta te dá as posições 0, 1, 2, 3, 0, 1, 2? E continua certa com cinco power-ups?
- Regra 12: na parte 8 do guia, viste que o Python pode fazer alguma coisa a uma função no momento em que lê o `def`. O que podia fazer a cada power-up?
- A saída: se um número não bate certo, procura a primeira linha em que a tua saída se afasta da do enunciado. Depois faz à mão as contas desse piloto nessa volta.

## Desafio opcional

### Um power-up novo

Acrescenta um quinto power-up, `cogumelo_dourado`, que dá 50 de velocidade. Escreve-o a seguir à `estrela`, sem mudar mais nenhuma linha do programa. Antes de executares, prevê quem vai à frente no fim da volta 2, e com quantos metros. Depois executa e confirma.

## Para ires mais longe

### Uma segunda corrida

A seguir à corrida do Arco-Íris, os mesmos três pilotos correm outra, no circuito do Castelo, também com quatro voltas. Acrescenta ao fim do programa as linhas que criam esta corrida, inscrevem os três pilotos e a correm.

1. Antes de executares, prevê com que velocidade e com que distância começa cada kart a corrida do Castelo. Explica porquê.
2. Muda o programa para que os karts comecem cada corrida como começaram a primeira, no início da pista. Confirma que a corrida do Arco-Íris continua a dar a saída do enunciado.

## Critérios de conclusão

Concluíste a ficha quando:

- o teu programa acaba com as linhas do enunciado, sem mudanças, e mostra exatamente a saída indicada;
- a regra dos limites da velocidade está escrita num só sítio, e o que os três tipos de kart têm em comum também;
- acrescentar um power-up novo cumpre a regra 12;
- consegues explicar a um colega, regra a regra, o que decidiste e porquê.

O desafio e a secção "Para ires mais longe" são opcionais e não entram nestes critérios.

## Autoavaliação

1. Que regra do jogo te levou mais tempo a perceber como se escrevia?
2. Houve alguma regra que escreveste de uma maneira e tiveste de mudar porque a saída não batia certo? Qual, e o que mudaste?
3. Se tivesses de acrescentar um quarto tipo de kart, que partes do programa mudavas?

![Rodapé](../imagens/rodape.png)
