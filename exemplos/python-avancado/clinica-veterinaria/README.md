![Cabeçalho](../../../imagens/cabecalho.png)

# Clínica veterinária

Uma clínica veterinária que junta, fora dos Pokémon, a matéria do tema: herança, propriedades, métodos do objeto e estáticos, agregação e composição, e o método de classe, com o `@classmethod`. É usado no tema [03 Objetos, composição e comportamento](../../../01-python-avancado/03-objetos-e-composicao.md), para reveres os três tipos de método noutro contexto.

## O que está nesta pasta

- `clinica.py`: as classes `Animal`, `Cao`, `Gato`, `Consulta` e `Clinica`, e uma demonstração no fim, que só corre quando executas o ficheiro diretamente. O `Cao` e o `Gato` herdam do `Animal` e reescrevem o som. O `Cao` reescreve também o preço da consulta, e usa o `super()` para pedir à classe-mãe o preço base. A idade do animal é uma propriedade, e o seu set usa um método estático. O método de classe `recem_nascido` cria um animal com 0 anos da classe por onde é chamado. A `Clinica` recebe animais criados fora dela (agregação) e cria as suas consultas (composição).

## Como correr

Abre o terminal na pasta onde está o `clinica.py` e escreve:

```bash
python3 clinica.py
```

O que deves ver: os dois testes do método estático, os três animais a apresentarem-se e a idade inválida do Rex, corrigida para 0. A seguir, vêm a recusa do Bobi, que não está registado, e as duas consultas. No fim, depois de a clínica ser apagada, o Rex continua a existir. A saída é esta:

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

## Versões e compatibilidade

Precisas do Python 3.9 ou mais recente. Foram usados o Python 3.9 e o 3.14, com a mesma saída nas duas. No Windows, o comando pode ser `python` ou `py`, em vez de `python3`.

![Rodapé](../../../imagens/rodape.png)
