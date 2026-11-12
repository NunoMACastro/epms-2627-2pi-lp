![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Objetos, composição e comportamento no livro de receitas

Programas um livro de receitas e decides tu como escrever cada regra, como na [ficha dos karts](03-objetos-e-composicao-exercicios-karts.md). Tem um só exercício, obrigatório. É um trabalho individual, para fazeres em casa: escreves o programa num só ficheiro e entregas-o ao professor pelo meio que ele indicar. Conta como a ficha dos karts, para as atitudes e valores, a autonomia e o empenho. Para rever: o [guia do tema](../03-objetos-e-composicao.md) e o [laboratório](../laboratorios/03-objetos-e-composicao-laboratorio.md).

## Exercício 1: O livro de receitas

Queremos um programa para guardar receitas e o tempo que cada uma leva a preparar. As três classes são `Receita`, `ReceitaDeForno` e `LivroDeReceitas`. Para saber se um valor é um número inteiro, serve o `type`, que já usaste no 10.º ano.

### As receitas

Para cada receita, guardamos um código, um nome e o tempo de preparação, em minutos. O código não se repete no livro, o nome não pode ficar vazio, e o tempo é sempre um número inteiro maior do que 0. A regra do tempo escreve-se num só sítio do programa e vale também quando alguém escreve `receita.tempo = 0`: nesse caso, o tempo fica como estava.

Por exemplo:

| Código | Nome | Tempo, em minutos |
| --- | --- | ---: |
| R01 | Sopa de legumes | 40 |
| R03 | Panquecas | 20 |

Algumas receitas vão ao forno. Uma receita de forno tem tudo o que uma receita tem, e mais a temperatura do forno, um número inteiro de 100 a 250 graus. A regra da temperatura também se escreve num só sítio e vale quando alguém muda a temperatura para um valor fora dela: nesse caso, a temperatura fica como estava. O que os dois tipos de receita têm em comum escreve-se uma só vez. Por exemplo, a R02, Bolo de laranja, prepara-se em 45 minutos e vai ao forno a 180 graus.

### O livro

O livro guarda as receitas pela ordem em que entram. Quando se acrescenta uma receita, é o livro que a cria, a partir dos dados que recebe.

Cada receita sabe descrever-se numa linha, e é assim que aparece na lista. Uma receita de forno acrescenta a temperatura no fim:

```text
R01 Sopa de legumes, 40 minutos
R02 Bolo de laranja, 45 minutos, forno a 180 graus
```

Para mostrar uma receita, o livro pede-lhe que se descreva, sem perguntar se é de forno. Quando não há receitas para mostrar, mostra `Não há receitas.`.

Deves poder:

- acrescentar uma receita, simples ou de forno, e o livro devolve a mensagem `Receita R01 acrescentada.`;
- corrigir o tempo de uma receita, com a mesma regra, e o livro também devolve uma mensagem;
- mostrar as receitas todas, uma por linha;
- mostrar só as que se fazem em certo número de minutos, ou em menos.

O programa recusa:

- um código que já existe;
- um nome vazio;
- um tempo que não cumpre a regra;
- numa receita de forno, uma temperatura que não cumpre a regra;
- ao corrigir o tempo, um código que não existe ou um tempo que não cumpre a regra.

Antes de acrescentar uma receita, o livro verifica os dados por esta ordem: o código, o nome, o tempo e, numa receita de forno, a temperatura. Quando recusa, nada muda no livro, e devolve uma mensagem que diz porquê. As mensagens estão na saída, mais abaixo.

### O programa que tem de funcionar

O programa do livro acaba com estas linhas, sem as mudares. Os nomes que elas usam, como `Receita` ou `acrescentar`, são obrigatórios, e os outros escolhes tu.

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

Com essas linhas no fim, o programa do livro mostra exatamente isto:

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

<details>
<summary>Pista</summary>

- Para começar: a receita pode ser testada sozinha, antes de haver a receita de forno e o livro.
- A regra do tempo: nos karts, a velocidade nunca passava de 100, mesmo com `kart.velocidade = 500`. Como é que o programa o garantia, sem repetir a verificação em cada método? Aqui, em vez de corrigir o valor, o tempo fica como estava.
- O livro e as regras: o livro tem de saber se um tempo cumpre a regra antes de criar a receita. Onde pões essa verificação para ela ficar escrita uma só vez e servir ao livro e ao set?
- A descrição: a receita de forno descreve-se como a receita, com mais um bocado no fim. Como é que a classe-filha usa o que a classe-mãe já faz?
- A lista: se o livro perguntar a cada receita de que tipo é, que linhas tens de mudar quando aparecer outro tipo de receita?
- A saída: se uma linha não bate certo, procura a primeira em que a tua saída se afasta da do enunciado.

</details>

## Desafios

Faz o desafio numa cópia do programa, por exemplo `receitas_desafio.py`.

### Desafio 1: Uma receita vegetariana

Acrescenta ao programa uma receita vegetariana, classe-filha da receita, que se descreve como uma receita com ` (vegetariana)` no fim. Acrescenta também ao livro o método `acrescentar_vegetariana`, com as mesmas verificações. No fim do programa, junta estas linhas:

```python
print()
print(livro.acrescentar_vegetariana("R08", "Salada de grão", 15))
livro.mostrar()
```

Responde, num comentário no início do ficheiro: que métodos do livro tiveste de mudar para a lista mostrar a receita nova?

## Critérios de conclusão

- O programa do livro acaba com as linhas do enunciado, sem mudanças, e mostra exatamente a saída indicada.
- A regra do tempo e a da temperatura estão escritas cada uma num só sítio, e o que os dois tipos de receita têm em comum também.
- O livro mostra as receitas sem perguntar de que tipo é cada uma.
- Consegues explicar cada regra do enunciado: o que decidiste para a cumprir e porquê.

O desafio da receita vegetariana é opcional e não entra nestes critérios.

Se quiseres treinar mais, tens cinco [temas de treino](03-objetos-e-composicao-exercicios-treino.md) com a mesma estrutura do livro, que são opcionais.

![Rodapé](../../imagens/rodape.png)
