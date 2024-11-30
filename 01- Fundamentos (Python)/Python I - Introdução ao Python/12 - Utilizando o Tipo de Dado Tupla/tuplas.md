# 📚Aula 12: Utilizando o Tipo de Dado Tupla

#### Uma tupla é uma estrutura de dados imutável em Python que, assim como as listas, pode armazenar uma sequência ordenada de elementos. No entanto, ao contrário das listas, as tuplas são imutáveis, o que significa que seus elementos não podem ser modificados após a criação.

### Características Fundamentais das Tuplas:

Em Python, as tuplas são estruturas de dados que oferecem importantes vantagens em termos de desempenho e segurança de dados. Elas são definidas usando parênteses () e, devido à sua imutabilidade, são mais eficientes em termos de memória e processamento que as listas. Esta característica as torna ideais para dados que não devem ser alterados durante a execução do programa.

### Exemplos práticos do uso de tuplas:

```python
# Criando tuplas de exemplo
gamesTuple = ("Fifa23", 22, "Star Wars", "The Legend of Zelda", "Mario Odyssey", "Red Dead 2")
print(gamesTuple)  # Mostra toda a tupla
print(type(gamesTuple))  # Mostra que é do tipo 'tuple'

# Criando tuplas com diferentes números de elementos
exampleTuple = ("Fifa23")  # Cuidado: isso cria uma string, não uma tupla
exampleTuple2 = ("Fifa23", 20, True)  # Tupla com diferentes tipos de dados
print(type(exampleTuple2))  # Confirma que é uma tupla
print(exampleTuple2)  # Mostra o conteúdo da tupla

# 1 - Acessando elementos com slice
# Obtém os dois primeiros itens
print(gamesTuple[0:2])  # Resultado: ("Fifa23", 22)

# 2 - Acessando o último elemento
# Usa índice negativo para o último item
print(gamesTuple[-1])  # Resultado: "Red Dead 2"

# 3 - Fatiamento até uma posição
# Obtém elementos do início até o índice 3 (exclusivo)
print(gamesTuple[:3])  # Resultado: ("Fifa23", 22, "Star Wars")

# 4 - Fatiamento a partir de uma posição
# Obtém elementos do índice 2 até o final
print(gamesTuple[2:])  # Resultado: ("Star Wars", "The Legend of Zelda", "Mario Odyssey", "Red Dead 2")

# 5 - Localizando elementos
# Encontra a posição do primeiro elemento especificado
print(gamesTuple.index("Fifa23"))  # Resultado: 0
```

### Conceitos Importantes:

1. **Imutabilidade**: Uma vez criada, uma tupla não pode ser modificada
2. **Eficiência**: Tuplas são mais rápidas e usam menos memória que listas
3. **Segurança**: A imutabilidade previne modificações acidentais nos dados
4. **Múltiplos Tipos**: Podem conter elementos de diferentes tipos de dados
5. **Indexação**: Suportam acesso por índice e fatiamento, como as listas

### Usos Comuns:

- Armazenamento de dados que não devem ser alterados
- Retorno de múltiplos valores em funções
- Chaves de dicionários (quando necessário usar sequências como chaves)
- Dados estruturados imutáveis (como coordenadas)
- Otimização de performance em grandes conjuntos de dados

### Limitações das Tuplas:

- Não permitem adição de novos elementos
- Não permitem remoção de elementos
- Não podem ser reordenadas
- Elementos individuais não podem ser modificados

A compreensão das tuplas e suas características únicas é fundamental para utilizá-las efetivamente em Python, especialmente quando a imutabilidade e a eficiência são requisitos importantes do programa.
