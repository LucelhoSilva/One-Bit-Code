# 📚 Aula 20: Utilizando List Comprehension

#### O recurso de **List Comprehension** em Python permite criar listas de maneira concisa e eficiente, utilizando uma única linha de código.

- Simplifica a criação e filtragem de listas.
- Suporta condições (`if`) e operações em cada item iterado.
- É mais legível e performático em comparação ao uso tradicional de loops para manipular listas.

#### Exemplo e Sintaxe

```python
gamesList = ["Mario Odyssey", "Donkey Kong Country",
             "Luigi's Mansion", "Kirby"]

"""
List Comprehension combina 'for' e 'if' em uma única expressão para criar listas com base em condições.

Sintaxe: novaLista = [expressão for item in iterável if condição]
"""

# 1 - Selecionar jogos que contêm a letra 'a'
newList = [x for x in gamesList if "a" in x]
print(newList)

# 2 - Criar uma lista sem incluir "Kirby"
gamesFinished = [x for x in gamesList if x != "Kirby"]
print(gamesFinished)

# 3 - Gerar uma lista de números menores que 4
listNumbers = [x for x in range(10) if x < 4]
print(listNumbers)
```

### Explicação Detalhada

#### 1 - **Filtrar itens com base em uma condição**

O comando **`if "a" in x`** verifica se o nome do jogo contém a letra "a".

```python
newList = [x for x in gamesList if "a" in x]
print(newList)
# Saída: ['Mario Odyssey', 'Luigi\'s Mansion']
```

#### 2 - **Excluir itens de uma lista**

Podemos criar uma nova lista excluindo um item específico:

```python
gamesFinished = [x for x in gamesList if x != "Kirby"]
print(gamesFinished)
# Saída: ['Mario Odyssey', 'Donkey Kong Country', 'Luigi\'s Mansion']
```

#### 3 - **Criar listas a partir de intervalos**

A lista é gerada com números menores que 4 usando a função `range`:

```python
listNumbers = [x for x in range(10) if x < 4]
print(listNumbers)
# Saída: [0, 1, 2, 3]
```

### Sintaxe Geral

```python
novaLista = [expressão for item in iterável if condição]
```

- **`expressão`**: O valor ou operação a ser incluído na lista.
- **`for item in iterável`**: Itera sobre uma sequência ou coleção.
- **`if condição`**: Condição opcional para incluir o item.

### Desempenho e Vantagens

1. ** List Comprehension é geralmente mais rápida**:
   É otimizada internamente em C, o que resulta em maior desempenho para operações simples.

2. ** Uso eficiente de memória**:
   Cria uma única lista em memória, evitando as múltiplas chamadas de `append` necessárias em loops tradicionais.

3. ** Legibilidade**:
   Mais fácil de entender e manter quando aplicada em listas pequenas ou médias.

4. ** Loop tradicional é preferível**:
   Em situações com lógica mais complexa ou quando múltiplas operações precisam ser realizadas em cada item, o `for ` tradicional pode ser mais adequado.

### Aplicações

- **Filtrar dados**: Criar listas com base em condições específicas.
- **Transformar dados**: Modificar itens de uma coleção ao iterar sobre ela.
- **Gerar listas**: Criar listas a partir de intervalos ou outras coleções.
