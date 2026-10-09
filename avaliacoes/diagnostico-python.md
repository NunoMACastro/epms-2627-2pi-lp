![Cabeçalho](../imagens/cabecalho.png)

# Diagnóstico inicial: Python em contexto de serviço

Este diagnóstico é uma revisão opcional da matéria de Python do 10.º ano, para fazeres por tua conta, quando quiseres. Não é recolhido nem corrigido em aula. Serve para perceberes como raciocinas e o que ainda dominas, e para escolheres o que te convém rever. Feito de seguida, demora cerca de 60 minutos.

Podes consultar os guias do 10.º e executar código localmente. Antes de executar, escreve a tua previsão; depois compara-a com o resultado. Não uses um gerador de soluções durante o diagnóstico: o objetivo é veres o teu próprio raciocínio, e um gerador mostrava-te o dele. Uma sintaxe esquecida não impede uma explicação em português. Usa apenas os dados fictícios apresentados; não são pedidos dados reais. Não tem nota.

Se o fizeres de seguida, conta com cerca de 12 minutos para a parte A, 10 para a B, 13 para a C, 15 para a D, 5 para a E e 5 para a revisão final. Se não conseguires terminar uma parte, escreve o passo em que paraste.

## A: ler e explicar

```python
"""Exemplo de leitura de pedidos fictícios, sem acesso externo."""
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

1. Prevê a saída e identifica o tipo de `pedidos`, `pedidos[0]`, `pedidos[0]["id"]` e `resultado`.
2. Identifica o parâmetro, o argumento da chamada e o valor de retorno. Depois explica, na comprehension, que parte filtra os pedidos e que parte os transforma, e o que faz cada uma.
3. A função altera a lista `pedidos`? Justifica. Depois reescreve o corpo da função com um ciclo `for` em vez da comprehension, de forma que o resultado seja o mesmo.

## B: encontrar e corrigir um erro

O código seguinte está errado de propósito: a função devia devolver quantos pedidos estão abertos, mas o programa mostra valores inesperados.

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

1. Prevê as duas linhas que o programa escreve. Depois explica se a variável `total` de fora da função e a variável `total` de dentro da função são a mesma variável.
2. Corrige a função para que devolva a contagem, sem escrever nada dentro dela. Explica a diferença entre `print` e `return`.
3. Indica o que devolve a função corrigida quando recebe uma lista vazia, e escreve um teste que confirmaria que a correção funciona.

## C: alterar e escrever uma função

A função recebe dados que cumprem este contrato: `registos` é uma lista de dicionários, e cada dicionário tem uma chave `"id"`, com um número inteiro, e uma chave `"estado"`, com um texto. Não precisas de verificar dados que não cumpram o contrato.

Escreve a função `selecionar_por_estado(registos, estado)`, que devolve uma lista nova com os identificadores dos pedidos cujo estado é igual ao parâmetro `estado`. A função não deve alterar `registos`. Acrescenta uma docstring curta a dizer para que serve a função.

Mostra o resultado em três casos: uma lista com dois pedidos abertos, uma lista sem nenhum pedido no estado pedido e uma lista vazia. Explica porque escolheste um ciclo ou uma comprehension: o código sozinho, sem a justificação, não chega.

## D: ficheiro, JSON e erros

Um serviço local precisa de ler uma lista de pedidos guardada num ficheiro JSON, com dados fictícios. A função seguinte está errada de propósito.

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

1. Explica porque é que `json.loads(ficheiro)` não é a chamada certa e indica que função do módulo `json` lê diretamente um ficheiro aberto.
2. Corrige a função `carregar`. Deve devolver a lista lida do ficheiro e, se o valor guardado no JSON não for uma lista, deve lançar `ValueError`. Não precisas de verificar os campos de cada pedido.
3. Escreve o código que chama `carregar` e trata, cada um à sua maneira, três erros: `OSError`, quando o ficheiro não se consegue ler; `json.JSONDecodeError`, quando o texto não é JSON válido; e `ValueError`, quando o JSON é válido mas não é uma lista. Indica por que ordem escreves os `except`, sabendo que `JSONDecodeError` é uma subclasse de `ValueError`. Não apanhes todos os erros com `except Exception`.
4. Explica porque é que devolver `[]` em qualquer falha esconde informação a quem chama a função. Explica também para que serve o `with`.

Para testares à mão, prepara quatro casos: um ficheiro válido com `[{"id": 1, "estado": "aberto"}]`; um ficheiro com JSON válido que não é uma lista, `{}`; um ficheiro com JSON mal formado, só com `[`; e um caminho para um ficheiro que não existe. Antes de correres cada caso, escreve a resposta que esperas.

## E: decompor e organizar

Sem escrever uma API nem instalar bibliotecas, propõe uma organização em módulos e funções para três tarefas: carregar os pedidos, selecionar os pedidos por estado e mostrar os identificadores. Para cada função, indica o que recebe, o que devolve e de que é responsável. Explica onde colocarias o código que arranca o programa e para que serve `if __name__ == "__main__":`. Diz também qual das funções conseguirias testar sem abrir nenhum ficheiro, e porquê.

## Revisão final

Não há entrega: o código e as explicações ficam contigo. Marca quais os resultados que previste e quais os que efetivamente executaste, e compara cada previsão com o que aconteceu. As partes em que a previsão falhou, ou em que paraste, mostram-te a matéria do 10.º que vale a pena rever nos guias desse ano. Não confundas terminar rapidamente com compreender.

![Rodapé](../imagens/rodape.png)
