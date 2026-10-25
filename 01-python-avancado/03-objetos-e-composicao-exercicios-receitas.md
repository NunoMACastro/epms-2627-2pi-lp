![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento no livro de receitas

Ficha do tema Objetos, composição e comportamento, do módulo 10794, Programação avançada com Python. Programas um livro de receitas, num só programa, e decides tu como o escrever a partir das regras. É um trabalho individual, para fazeres em casa. Entregas o programa ao professor pelo meio que ele indicar.

## O que precisas de saber

O [guia do tema](03-objetos-e-composicao.md) e o [laboratório](03-objetos-e-composicao-laboratorio.md). Convém teres feito antes a [ficha dos karts](03-objetos-e-composicao-exercicios-karts.md), porque este exercício trabalha da mesma maneira.

## Como trabalhar

A ficha tem um só exercício, o livro de receitas, e um desafio opcional. Se quiseres treinar antes ou depois, tens cinco [temas de treino](03-objetos-e-composicao-exercicios-treino.md) com a mesma estrutura, que são opcionais.

O enunciado não te diz como escrever o programa. Diz-te as regras, e cada regra pede-te uma decisão: que classes crias, o que cada uma guarda e sabe fazer, e como as ligas umas às outras. Os nomes que o programa final usa, como `Receita` ou `acrescentar`, são obrigatórios. Os outros nomes escolhes tu.

Lê as regras todas antes de começares. Depois começa pela receita e testa-a sozinha, antes de passares à receita de forno e ao livro.

## Exercício 1: O livro de receitas

### As receitas

1. Cada receita tem um código, um nome e o tempo de preparação, em minutos.
2. O tempo é sempre um número inteiro maior do que 0. Esta regra escreve-se num só sítio do programa e vale também quando alguém escreve `receita.tempo = 0`: nesse caso, o tempo fica como estava.
3. Algumas receitas vão ao forno. Uma receita de forno tem tudo o que uma receita tem e também a temperatura do forno, um número inteiro de 100 a 250 graus. A regra da temperatura também se escreve num só sítio e vale também quando alguém muda a temperatura. O que as duas receitas têm em comum escreve-se uma só vez.
4. Cada receita sabe descrever-se numa linha, como `R01 Sopa de legumes, 40 minutos`. Uma receita de forno acrescenta a temperatura no fim, como `R02 Bolo de laranja, 45 minutos, forno a 180 graus`.

### O livro

5. O livro guarda as receitas pela ordem em que entram. Quando se acrescenta uma receita, é o livro que a cria, a partir dos dados que recebe.
6. Antes de acrescentar uma receita, o livro verifica os dados por esta ordem: o código, o nome, o tempo e, numa receita de forno, a temperatura. Recusa um código que já existe, um nome vazio, um tempo que não cumpre a regra e uma temperatura que não cumpre a regra.
7. Quando aceita, o livro devolve a mensagem `Receita R01 acrescentada.`. Quando recusa, nada muda no livro, e devolve uma mensagem que diz porquê. As mensagens estão na saída, mais abaixo.
8. O livro corrige o tempo de uma receita, com a mesma regra, e também devolve uma mensagem.
9. O livro mostra as receitas todas, uma por linha, ou só as que se fazem num tempo máximo. Para mostrar uma receita, pede-lhe que se descreva, sem perguntar se é de forno. Quando não há receitas para mostrar, mostra `Não há receitas.`.

### O programa que tem de funcionar

O teu programa tem de acabar com estas linhas, sem as mudar:

```python
teste = Receita("R00", "Teste", 10)
teste.tempo = 0
print("Teste da regra do tempo:", teste.tempo)
teste_forno = ReceitaDeForno("R00", "Teste", 10, 180)
teste_forno.temperatura = 300
print("Teste da regra da temperatura:", teste_forno.temperatura)
print()

livro = LivroDeReceitas()
livro.mostrar()
print(livro.acrescentar("R01", "Sopa de legumes", 40))
print(livro.acrescentar_de_forno("R02", "Bolo de laranja", 45, 180))
print(livro.acrescentar("R03", "Panquecas", 20))
print(livro.acrescentar("R01", "Arroz de pato", 50))
print(livro.acrescentar("R04", "", 15))
print(livro.acrescentar("R05", "Gelado de fruta", 0))
print(livro.acrescentar_de_forno("R06", "Pão caseiro", 50, 260))
print(livro.acrescentar_de_forno("R07", "Pizza", 2.5, 220))
print()
livro.mostrar()
print()
print(livro.corrigir_tempo("R03", 25))
print(livro.corrigir_tempo("R02", -5))
print(livro.corrigir_tempo("R09", 30))
print()
print("Até 30 minutos:")
livro.mostrar_rapidas(30)
print("Até 10 minutos:")
livro.mostrar_rapidas(10)
```

### A saída

Com essas linhas no fim, o teu programa tem de mostrar exatamente isto:

```text
Teste da regra do tempo: 10
Teste da regra da temperatura: 180

Não há receitas.
Receita R01 acrescentada.
Receita R02 acrescentada.
Receita R03 acrescentada.
Recusada: já existe uma receita com o código R01.
Recusada: o nome não pode ficar vazio.
Recusada: o tempo tem de ser um número inteiro maior do que 0.
Recusada: a temperatura tem de ser um número inteiro de 100 a 250.
Recusada: o tempo tem de ser um número inteiro maior do que 0.

R01 Sopa de legumes, 40 minutos
R02 Bolo de laranja, 45 minutos, forno a 180 graus
R03 Panquecas, 20 minutos

Tempo da R03 corrigido para 25 minutos.
Recusada: o tempo tem de ser um número inteiro maior do que 0.
Recusada: não há nenhuma receita com o código R09.

Até 30 minutos:
R03 Panquecas, 25 minutos
Até 10 minutos:
Não há receitas.
```

## Apoio

Pistas que ajudam sem dar a resposta. Tenta primeiro sozinho, e usa só a pista da regra em que estás preso.

- Regra 2: nos karts, a velocidade nunca passava de 100, mesmo com `kart.velocidade = 500`. Como é que o programa o garantia, sem repetir a verificação em cada método? Aqui, em vez de corrigir o valor, o tempo fica como estava.
- Regra 3: compara as frases "uma receita de forno é uma receita" e "uma receita de forno tem uma receita". Qual das duas é verdadeira?
- Regras 2, 3 e 6: o livro tem de saber se um tempo cumpre a regra antes de criar a receita. Onde pões essa verificação para ela ficar escrita uma só vez e servir ao livro e ao set?
- Regra 4: a receita de forno descreve-se como a receita, com mais um bocado no fim. Como é que a classe derivada usa o que a classe base já faz?
- Regra 5: faz as duas perguntas do guia sobre as receitas e o livro. Faz sentido sem o todo? Quem a cria?
- Regra 9: se o livro perguntar a cada receita de que tipo é, que linhas tens de mudar quando aparecer outro tipo de receita?
- A saída: se uma linha não bate certo, procura a primeira em que a tua saída se afasta da do enunciado.

## Desafio opcional

### Uma receita vegetariana

Acrescenta ao programa uma receita vegetariana, derivada da receita, que se descreve como uma receita com ` (vegetariana)` no fim. Acrescenta também ao livro o método `acrescentar_vegetariana`, com as mesmas verificações. No fim do programa, junta estas linhas:

```python
print()
print(livro.acrescentar_vegetariana("R08", "Salada de grão", 15))
livro.mostrar()
```

Antes de executares, escreve a última linha que esperas. Depois responde: que métodos do livro tiveste de mudar para a lista mostrar a receita nova?

## Critérios de conclusão

Concluíste a ficha quando:

- o teu programa acaba com as linhas do enunciado, sem mudanças, e mostra exatamente a saída indicada;
- a regra do tempo e a da temperatura estão escritas cada uma num só sítio, e o que as duas receitas têm em comum também;
- o livro mostra as receitas sem perguntar de que tipo é cada uma;
- consegues explicar a um colega, regra a regra, o que decidiste e porquê.

O desafio é opcional e não entra nestes critérios.

## Autoavaliação

1. Que regra te levou mais tempo a perceber como se escrevia?
2. Houve alguma regra que escreveste de uma maneira e tiveste de mudar porque a saída não batia certo? Qual, e o que mudaste?
3. Se aparecesse um terceiro tipo de receita, por exemplo uma receita vegetariana, que partes do programa mudavas?

![Rodapé](../imagens/rodape.png)
