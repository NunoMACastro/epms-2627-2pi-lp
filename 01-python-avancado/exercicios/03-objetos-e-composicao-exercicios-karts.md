![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento no Grande Prémio de Karts

Juntas num só programa, um jogo de corridas de karts, o que treinaste por partes na [ficha principal do tema](03-objetos-e-composicao-exercicios.md), e decides tu como escrever cada regra do jogo. Tem um só exercício, obrigatório. Escreves o programa num só ficheiro, por exemplo `karts.py`, e entregas-o ao professor. Conta para as atitudes e valores, a autonomia e o empenho, e não para a avaliação prática. Para rever: o [guia do tema](../03-objetos-e-composicao.md) e o [laboratório](../laboratorios/03-objetos-e-composicao-laboratorio.md).

## Exercício 1: Grande Prémio de Karts

Queremos um programa para uma corrida de karts ao estilo do Mario Kart: três pilotos, quatro voltas e, pelo caminho, caixas com power-ups. Além do que o guia mostra, usas três coisas do 10.º ano: a divisão inteira `//`, o resto da divisão `%` e o `range`.

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
9. No fim de cada volta, a corrida regista três coisas: o número da volta, o nome de quem vai à frente (quem percorreu mais distância) e a distância dele. Num empate, fica à frente quem se inscreveu primeiro. É a própria corrida que faz estes registos, enquanto corre, e só ela os guarda. No fim, mostra o registo e o vencedor, que é quem vai à frente no fim da última volta. Ao começar, a corrida mostra o circuito, as voltas e os pilotos, com o kart e o tipo dele. Em cada volta, mostra, para cada piloto, o power-up que lhe calhou e a velocidade e a distância com que ficou. O registo e o vencedor mostram-se com `mostrar_registo`.

### Os power-ups

10. Cada power-up é uma função que recebe o kart do piloto que abriu a caixa. Há quatro, escritos por esta ordem:
    - `banana`: o kart escorrega e sofre um choque;
    - `cogumelo`: o kart ganha 30 de velocidade;
    - `tinta`: o piloto deixa de ver e trava, e o kart perde 40 de velocidade;
    - `estrela`: o kart fica com a velocidade máxima.
11. As caixas dão os power-ups pela ordem em que estão escritos no programa, um por caixa, e depois do último volta-se ao primeiro. A ordem não recomeça em cada piloto nem em cada volta. Não há números ao acaso.
12. Os criadores do jogo vão inventar power-ups novos. Para isso, querem escrever só a função do power-up novo e uma linha por cima dela, e a corrida tem de passar logo a usá-lo. Nenhuma outra linha do programa muda.

### O programa que tem de funcionar

O programa acaba com estas linhas, sem as mudares. Os nomes que elas usam, como `Kart`, `Piloto` ou `com_turbo`, são obrigatórios, e os outros escolhes tu.

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

Com essas linhas no fim, o programa mostra exatamente isto:

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

<details>
<summary>Pista</summary>

- Para começar: os karts podem ser testados sozinhos, antes de haver pilotos e corrida. Cria um kart, põe-no a fazer as três coisas da regra 2 e mostra a velocidade e a distância com `print`.
- Regra 3: nos Pokémon do guia, a vida também nunca passa de 150, mesmo com `charmander.vida = 999`. Como é que o programa garante isso, sem repetir a verificação em cada método?
- Regra 4: compara as relações "um kart leve é um kart" e "um kart leve tem um kart". Qual das duas frases é verdadeira? Como é que o fogo e a água dos Pokémon partilham o que têm em comum?
- Regra 5: no ginásio das aulas, o `Lider` também se criava numa linha, já com a equipa. Quem escreve `KartLeve.com_turbo("Foguete")` está a pedir um kart de que classe? Como é que o código que cria o kart fica a saber isso?
- Regras 6, 7 e 9: para cada coisa que um piloto ou uma corrida guarda, faz as duas perguntas do guia. Faz sentido sem o todo? Quem a cria?
- Regra 10: antes de escreveres a banana, pensa num kart normal e num kart pesado, os dois a 70. Com que velocidade fica cada um depois de escorregar? Quem sabe de que tipo é o kart: a banana ou o próprio kart?
- Regra 11: as caixas são as mesmas para todos os pilotos e não recomeçam em cada volta. Que objeto vê todas as caixas que se abrem e pode contar quantas já se abriram? Se o contador vai 0, 1, 2, 3, 4, 5, 6, que conta te dá as posições 0, 1, 2, 3, 0, 1, 2? E continua certa com cinco power-ups?
- Regra 12: na ficha principal, o decorador `comando` do exercício 19 fazia uma coisa a cada função no momento do `def`. O que podia fazer a cada power-up?
- A saída: se um número não bate certo, procura a primeira linha em que a tua saída se afasta da do enunciado. Depois segue, uma a uma, as contas desse piloto nessa volta.
- A saída não tem empates nem metades de números ímpares. Experimenta numa cópia um kart a 35 que sofre um choque, e dois karts empatados.

</details>

## Desafios

Faz cada desafio numa cópia do programa, por exemplo `karts_desafio1.py` e `karts_desafio2.py`.

### Desafio 1: Um power-up novo

Acrescenta um quinto power-up, `cogumelo_dourado`, que dá 50 de velocidade. Escreve-o a seguir à `estrela`, sem mudar mais nenhuma linha do programa. Antes de executares, prevê quem vai à frente no fim da volta 2, e com quantos metros, e confirma executando.

### Desafio 2: Uma segunda corrida

A seguir à corrida do Arco-Íris, os mesmos três pilotos correm outra, no circuito do Castelo, também com quatro voltas. Acrescenta ao fim do programa as linhas que criam esta corrida, inscrevem os três pilotos e a correm.

1. Antes de executares, prevê com que velocidade e com que distância começa cada kart a corrida do Castelo. Explica porquê, num comentário por cima das linhas da corrida do Castelo.
2. Muda o programa para que os karts comecem cada corrida com a velocidade e a distância com que começaram a primeira. A Inês parte outra vez a 50 e a 0 m. A corrida do Arco-Íris tem de continuar a dar a saída do enunciado.

## Critérios de conclusão

- O teu programa acaba com as linhas do enunciado, sem mudanças, e mostra exatamente a saída indicada.
- A regra dos limites da velocidade está escrita num só sítio, e o que os três tipos de kart têm em comum também.
- Acrescentar um power-up novo cumpre a regra 12.
- Consegues explicar, regra a regra, o que decidiste e porquê.

Os dois desafios são opcionais e não entram nestes critérios.

![Rodapé](../../imagens/rodape.png)
