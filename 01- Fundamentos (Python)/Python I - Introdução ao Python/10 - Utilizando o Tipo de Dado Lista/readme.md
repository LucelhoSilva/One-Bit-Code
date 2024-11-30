# 📚 Aula 10: Utilizando o Tipo de Dado Lista

#### Uma lista é uma estrutura de dados mutável e ordenada que pode conter elementos de diferentes tipos. Em Python, ela é definida usando colchetes []. Neste documento, vamos explorar como trabalhar com fatias (slices) de listas e acessar elementos específicos.

### Características do Slicing em Listas:

Em Python, o slicing permite que você acesse partes específicas de uma lista usando a sintaxe [início:fim]. É uma ferramenta poderosa que oferece grande flexibilidade na manipulação de dados. Alguns pontos importantes:

- O índice inicial é inclusivo (o elemento nesta posição é incluído)
- O índice final é exclusivo (o elemento nesta posição não é incluído)
- Índices negativos contam a partir do final da lista
- Se omitir o índice inicial, Python assume 0
- Se omitir o índice final, Python assume o tamanho da lista

### Exemplos práticos de uso de slicing em listas:

```python
# Criando nossas listas de exemplo
gameData = ["Fifa23", 2022, 90.50, 8.5]  # Lista com tipos mistos
gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 - Busca os dois primeiros itens da lista
# O comando gamesList[3:] retorna uma lista a partir do índice 3 até o final
# Neste caso, retorna ['Red Dead 2']
print(gamesList[3:])

# 2 - Busca o último item da lista
# O índice -1 sempre se refere ao último elemento
# Neste caso, retorna 'Red Dead 2'
print(gamesList[-1])

# 3 - Busca jogos até uma posição
# gamesList[:2] retorna elementos do início até o índice 2 (exclusivo)
# Neste caso, retorna ['Fifa23', 'Star Wars']
print(gamesList[:2])

# 4 - Busca jogos de uma posição em diante
# gamesList[2:] retorna elementos do índice 2 até o final
# Neste caso, retorna ['The Legend of Zelda', 'Red Dead 2']
print(gamesList[2:])
```

### Conceitos Importantes:

1. **Índices Positivos**: Começam do 0 e vão até len(lista)-1
2. **Índices Negativos**: Começam do -1 (último elemento) e vão até -len(lista)
3. **Slice [início:fim]**: Retorna uma nova lista com os elementos do índice início (inclusive) até fim (exclusive)
4. **Lista Mista**: Como demonstrado em gameData, uma lista pode conter diferentes tipos de dados (strings, números, decimais)

### Usos Comuns:

- Extrair sublistas para processamento específico
- Acessar elementos em posições específicas
- Criar cópias parciais de listas
- Manipular sequências de dados de forma eficiente

Este tipo de manipulação de listas é especialmente útil quando trabalhamos com grandes conjuntos de dados e precisamos acessar ou processar apenas partes específicas da informação.
