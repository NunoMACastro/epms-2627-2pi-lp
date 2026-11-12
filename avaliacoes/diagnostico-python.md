![Cabeçalho](../imagens/cabecalho.png)

# Diagnóstico de Python: os pedidos de assistência

Este diagnóstico é uma revisão opcional do Python do 10.º ano, para fazeres por tua conta, quando quiseres. Não é recolhido nem tem nota: serve para veres o que ainda dominas e o que te convém rever. Os exemplos são pedidos de assistência a computadores.

Podes consultar os guias do 10.º e correr o código no teu computador. Não peças a solução a um assistente de inteligência artificial, porque o objetivo é veres o teu próprio raciocínio. Escreve cada parte num ficheiro teu, como `parte_a.py`. Quando uma pergunta começa por "Sem correres o programa", pensa na resposta de cabeça e só depois corre; as outras respostas escreve-as em comentários no ficheiro. Se não te lembrares de como se escreve alguma coisa em Python, explica em português o que querias fazer. Se não terminares uma parte, escreve num comentário o passo em que paraste.

## Parte A: ler e explicar

```python
"""Mostra os identificadores dos pedidos abertos."""
pedidos = [
    {"id": 1, "titulo": "Substituir teclado", "estado": "aberto"},
    {"id": 2, "titulo": "Instalar editor", "estado": "fechado"},
    {"id": 3, "titulo": "Verificar cabo", "estado": "aberto"},
]


def ids_abertos(registos):
    """Devolve os identificadores dos pedidos que estão abertos."""
    return [pedido["id"] for pedido in registos if pedido["estado"] == "aberto"]


resultado = ids_abertos(pedidos)
print(resultado)
```

1. Sem correres o programa, pensa no que ele escreve e no tipo de `pedidos`, `pedidos[0]`, `pedidos[0]["id"]` e `resultado`. Depois corre-o e confirma a saída, e os tipos com `type()`.
2. Identifica o parâmetro, o argumento da chamada e o valor de retorno. Depois explica, na comprehension, que parte filtra os pedidos e que parte os transforma.
3. A função altera a lista `pedidos`? Justifica. Depois reescreve o corpo da função com um ciclo `for` em vez da comprehension, com o mesmo resultado.

## Parte B: encontrar e corrigir um erro

A função seguinte devia devolver quantos pedidos estão abertos, mas o programa mostra valores inesperados.

```python
"""Exemplo com um erro de propósito, para encontrares e corrigires."""
total = 99


def contar_abertos(registos):
    """Devolve quantos pedidos da lista estão abertos."""
    total = 0
    for pedido in registos:
        if pedido["estado"] == "aberto":
            total += 1
    print(total)


pedidos = [{"estado": "aberto"}, {"estado": "fechado"}]
resultado = contar_abertos(pedidos)
print(resultado, total)
```

1. Sem correres o programa, pensa nas duas linhas que ele escreve, e depois confirma. Explica se o `total` de fora da função e o `total` de dentro dela são a mesma variável.
2. Corrige a função para que devolva a contagem e não mostre nada no ecrã. Explica a diferença entre `print` e `return`.
3. Diz o que devolve a função corrigida quando recebe uma lista vazia, e escreve um `assert` que confirme esse resultado.

## Parte C: escrever uma função

Escreve a função `selecionar_por_estado(registos, estado)`, que devolve uma lista nova com os identificadores dos pedidos cujo estado é igual ao parâmetro `estado`. A função não deve alterar `registos`. Acrescenta uma docstring curta a dizer para que serve a função.

O parâmetro `registos` é sempre uma lista de dicionários. Cada dicionário tem uma chave `"id"`, com um número inteiro, e uma chave `"estado"`, com um texto. Não precisas de verificar dados que não sejam assim.

Mostra o resultado em três casos: uma lista com dois pedidos abertos, uma lista sem nenhum pedido no estado que procuras e uma lista vazia. Explica porque escolheste um ciclo ou uma comprehension.

## Parte D: ficheiro, JSON e erros

A função seguinte devia ler uma lista de pedidos guardada num ficheiro JSON.

```python
"""Exemplo com erros de propósito, para encontrares e corrigires."""
import json


def carregar(caminho):
    """Devolve a lista de pedidos guardada no ficheiro JSON indicado."""
    try:
        with open(caminho, encoding="utf-8") as ficheiro:
            return json.loads(ficheiro)
    except Exception:
        return []
```

1. Explica porque é que `json.loads(ficheiro)` não é a chamada certa, e indica que função do módulo `json` lê diretamente um ficheiro aberto. Para veres o erro, tira o `try` e o `except`, corre `carregar` com um ficheiro válido e lê a última linha da mensagem.
2. Explica porque é que devolver `[]` em qualquer falha esconde informação a quem chama a função.
3. Corrige a função `carregar`, de forma que os erros cheguem a quem a chama. Deve devolver a lista lida do ficheiro e, se o valor guardado no JSON não for uma lista, deve lançar `ValueError`. Não precisas de verificar os campos de cada pedido.
4. Escreve o código que chama `carregar` e trata três erros, com uma mensagem diferente para cada um. O primeiro é o `OSError`, quando o ficheiro não se consegue ler (o `FileNotFoundError` do 10.º é um deles). O segundo é o `json.JSONDecodeError`, quando o texto não é JSON válido, e o terceiro é o `ValueError`, quando o JSON é válido mas não é uma lista. Não apanhes todos os erros com `except Exception`.
5. Diz por que ordem escreveste os `except`, sabendo que o `JSONDecodeError` é filho do `ValueError`. Esta ideia vem do tema 04 deste ano: [Os except pela ordem errada](../01-python-avancado/04-excecoes-depuracao-e-logging.md#os-except-pela-ordem-errada).
6. Para que serve o `with`?

Para confirmares o teu código, cria três ficheiros na pasta do teu programa e corre-o a partir dessa pasta. O primeiro é um ficheiro válido, com `[{"id": 1, "estado": "aberto"}]`, e o segundo tem JSON válido que não é uma lista, `{}`. O terceiro tem JSON mal formado, só com `[`. O quarto caso é um caminho para um ficheiro que não existe.

## Parte E: decompor e organizar

Propõe uma organização em módulos e funções para três tarefas: carregar os pedidos, selecionar os pedidos por estado e mostrar os identificadores. Podes partir das funções das partes C e D. Descreve, num comentário, o que recebe e o que devolve cada função, e pelo que é responsável. Explica onde colocarias o código que arranca o programa e para que serve `if __name__ == "__main__":`. Diz também qual das funções conseguirias testar sem abrir nenhum ficheiro, e porquê.

## Revisão final

As partes em que o resultado não foi o que esperavas, ou em que paraste, mostram-te a matéria do 10.º que vale a pena rever:

- parte A: as listas e os dicionários, as funções e as list comprehensions;
- parte B: as funções, a diferença entre `print` e `return` e onde vive cada variável;
- parte C: as funções e as list comprehensions;
- parte D: os ficheiros, o JSON e as exceções, e o guia do tema 04 deste ano;
- parte E: os módulos e a organização de um projeto.

![Rodapé](../imagens/rodape.png)
