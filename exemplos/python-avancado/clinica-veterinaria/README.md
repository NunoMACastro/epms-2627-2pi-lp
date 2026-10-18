![Cabeçalho](../../../imagens/cabecalho.png)

# Clínica veterinária

Este exemplo junta, numa clínica veterinária, a matéria do tema até aqui: herança, propriedades, métodos do objeto e estáticos, agregação e composição. Acrescenta-lhe o método de classe, o `@classmethod`, que foi o assunto novo da aula de 6 de outubro. É usado no tema [03 Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md), como revisão num contexto diferente dos Pokémon.

## O que está nesta pasta

- `clinica.py`: as classes `Animal`, `Cao`, `Gato`, `Consulta` e `Clinica`, e uma demonstração no fim, que só corre quando executas o ficheiro diretamente. O `Cao` e o `Gato` herdam do `Animal` e reescrevem o som. O `Cao` reescreve também o preço da consulta, e usa o `super()` para pedir à classe-mãe o preço base. A idade do animal é uma propriedade, e o seu set usa um método estático. O método de classe `recem_nascido` cria um animal com 0 anos da classe por onde é chamado. A `Clinica` recebe animais criados fora dela (agregação) e cria as suas consultas (composição).

## Como correr

Se não tens este repositório no teu computador, copia o `clinica.py` para uma pasta tua, como fizeste com o `pokemon.py`. Depois abre o terminal na pasta do exemplo, ou nessa pasta tua, e escreve:

```bash
python3 clinica.py
```

No Windows, se `python3` não funcionar, experimenta `python` ou `py`.

O que deves ver, por esta ordem:

- o resultado de dois testes do método estático;
- três animais a apresentarem-se;
- uma idade inválida, corrigida para 0;
- uma recusa, porque o Bobi não está registado na clínica;
- a lista das duas consultas;
- o Rex ainda a apresentar-se, depois de a clínica ser apagada.

A saída é esta:

```text
True
False

Rex, 7 anos: Ão ão!
Bobi, 0 anos: Ão ão!
Tareco, 0 anos: Miau!

Idade -5 inválida para Rex: fica com 0 anos.
Rex, 0 anos: Ão ão!
Bobi não está registado na Clínica Patudos.

Consultas da Clínica Patudos:
 - Rex: Dor numa pata (45 euros)
 - Tareco: Cortar as unhas (30 euros)

Rex, 0 anos: Ão ão!
```

O Rex paga 45 euros e o Tareco 30 porque o `Cao` reescreve o `preco_consulta`. Pede à classe-mãe o preço base, que é 30, com o `super()`, e soma-lhe 15 da vacina. O `Gato` não o reescreve, e por isso paga o preço base.

## Versões com que foi testado

Python 3.9 e Python 3.14, a 18 de outubro de 2026, com a mesma saída nas duas.

![Rodapé](../../../imagens/rodape.png)
