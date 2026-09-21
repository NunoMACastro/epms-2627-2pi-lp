![Cabeçalho](../imagens/cabecalho.png)

# Diagnóstico inicial: Python em contexto de serviço

Duração: 60 min, integrada no bloco inicial de 2 h com bridge. Finalidade: perceber como raciocinas, para orientar a revisão.

Podes consultar os guias do 10.º e executar código localmente. Antes de executar, escreve a tua previsão; depois compara-a com o resultado. Não uses um gerador de soluções durante o diagnóstico: precisamos de observar o teu raciocínio. Uma sintaxe esquecida não impede uma explicação em português. Usa apenas os dados fictícios apresentados; não são pedidos dados reais. Não são atribuídas percentagens institucionais.

Reserva A: 12 min; B: 10 min; C: 13 min; D: 15 min; E: 5 min; revisão/entrega: 5 min. Se não conseguires terminar uma parte, explica o passo em que paraste.

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
2. Identifica o parâmetro, o argumento da chamada e o valor de retorno. Explica filtro e transformação na comprehension.
3. A função altera pedidos? Justifica. Reescreve o corpo com um ciclo explícito que preserve o resultado.

## B: encontrar e corrigir um erro

O código seguinte está **propositadamente errado no comportamento**: pretende devolver a contagem, mas o valor observado é inesperado.

```python
"""Exemplo deliberadamente incorreto para diagnosticar retorno e scope."""
total = 99


def contar_abertos(registos):
    """Tentativa incorreta: imprime a contagem em vez de a devolver."""
    total = 0
    for pedido in registos:
        if pedido["estado"] == "aberto":
            total += 1
    print(total)


pedidos = [{"estado": "aberto"}, {"estado": "fechado"}]
resultado = contar_abertos(pedidos)
print(resultado, total)
```

1. Prevê as duas linhas impressas e explica a relação entre o total exterior e o total da função.
2. Corrige a função para devolver a contagem sem imprimir dentro dela. Explica a diferença entre print e return.
3. Indica o resultado da função corrigida com uma lista vazia e um teste que confirmaria a correção.

## C: alterar e escrever uma função

Usa o contrato: registos é uma lista de dicionários; cada dicionário tem id inteiro e estado textual. Não precisas de validar dados fora deste contrato neste item.

Escreve selecionar_por_estado(registos, estado) para devolver uma **nova lista com os identificadores** dos pedidos cujo estado corresponde ao parâmetro. Não alteres os registos. Acrescenta uma docstring curta com o propósito.

Demonstra três casos: dois pedidos abertos, nenhum pedido no estado pedido e lista vazia. Explica a escolha de ciclo ou comprehension. Não basta apresentar código sem justificar.

## D: ficheiro, JSON e erros

Um serviço local precisa de ler uma lista de pedidos a partir de JSON. São dados fictícios. O bloco é **propositadamente incorreto no comportamento**.

```python
"""Exemplo deliberadamente incorreto: confunde ficheiro, texto e dados."""
import json


def carregar(caminho):
    """Tentativa incorreta de carregar JSON."""
    try:
        with open(caminho, encoding="utf-8") as ficheiro:
            return json.loads(ficheiro)
    except Exception:
        return []
```

1. Explica por que motivo json.loads(ficheiro) não é a chamada correta e indica a alternativa que lê o ficheiro aberto.
2. Corrige carregar: deve devolver uma lista lida com json.load; se o JSON de topo não for uma lista, deve lançar ValueError. Não é pedida validação dos campos de cada pedido.
3. No código que chama carregar, distingue OSError (leitura), json.JSONDecodeError (formato) e ValueError (contrato de lista). Indica a ordem adequada das capturas, sabendo que JSONDecodeError é uma subclasse de ValueError. Não captures todos os erros com except Exception.
4. Explica por que devolver [] para qualquer falha esconde informação. Explica para que serve with.

Dados para testar manualmente: ficheiro válido com `[{"id": 1, "estado": "aberto"}]`; ficheiro válido mas incompatível com `{}`; ficheiro malformado com `[`; caminho inexistente. Decide a resposta esperada antes de correr cada caso.

## E: decompor e organizar

Sem escrever uma API nem instalar bibliotecas, propõe módulos/funções para **carregar pedidos, selecionar por estado e apresentar identificadores**. Para cada função, indica entrada, saída e responsabilidade. Explica onde colocarias o arranque e para que serve `if __name__ == "__main__":`. Qual das funções testarias sem abrir ficheiros?

## Entrega e checkpoint

Entrega código e explicações no canal indicado pelo professor, sem credenciais nem dados pessoais de terceiros. Marca quais os resultados que previste e quais os que efetivamente executaste. O professor usa esta evidência para a revisão dirigida; não confundir terminar rapidamente com compreender.

![Rodapé](../imagens/rodape.png)
