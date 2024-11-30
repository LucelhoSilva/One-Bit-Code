# 📚Aula 13: Utilizando o Tipo de Dado Set

#### Um set (conjunto) é uma estrutura de dados única em Python que foi inspirada na teoria matemática dos conjuntos. É especialmente projetado para armazenar elementos únicos de forma não ordenada, oferecendo operações eficientes para verificação de membros e eliminação de duplicatas.

### Características Fundamentais dos Sets:

Em Python, os sets combinam a eficiência de busca das hashtables com os conceitos matemáticos de teoria dos conjuntos. Diferentemente das listas e tuplas, os sets não mantêm uma ordem específica e automaticamente eliminam duplicatas, tornando-os ideais para certas operações de dados.

### Exemplos práticos do uso de sets:

```python
# Criando nosso primeiro set de exemplo
gamesSet = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}

# 0 - Verificando conteúdo e tamanho do set
# Note que "Red Dead 2" aparece apenas uma vez, pois sets eliminam duplicatas
print(gamesSet)  # Resultado: set sem duplicatas
print(len(gamesSet))  # Resultado: 4 (não 5, pois uma duplicata foi removida)

# 1 - Demonstração de equivalência de valores
# Em sets, True e 1 são considerados o mesmo valor devido à equivalência em Python
exampleSet = {"Fifa23", True, 1, 90.50}
print(exampleSet)  # True e 1 são tratados como o mesmo valor

# 2 - Adicionando elementos individuais
# add() insere um novo elemento se ele ainda não existir
gamesSet.add("Resident Evil 4")
print(gamesSet)  # Set atualizado com o novo jogo

# 3 - Combinando sets
# update() adiciona elementos de outro set (ou iterável)
gamesSet.update(exampleSet)
print(gamesSet)  # Set atualizado com elementos de ambos os sets

# 4 - Removendo elementos
# remove() elimina elementos específicos
gamesSet.remove(True)  # Remove True/1
gamesSet.remove(90.5)  # Remove o valor float
print(gamesSet)  # Set com os elementos removidos
```

### Conceitos Importantes:

1. **Unicidade**: Cada elemento pode aparecer apenas uma vez no set
2. **Não-ordenação**: A ordem dos elementos não é mantida ou garantida
3. **Hashable**: Elementos devem ser imutáveis (não podem ser listas ou dicionários)
4. **Eficiência**: Verificação de pertencimento é muito rápida (O(1))
5. **Equivalência**: Alguns valores são considerados iguais (como True e 1)

### Usos Comuns:

- Remoção de duplicatas de sequências
- Verificação rápida de pertencimento
- Operações matemáticas de conjuntos
- Armazenamento de valores únicos
- Comparação de coleções

### Operações Matemáticas de Conjuntos:

Sets em Python suportam operações clássicas da teoria dos conjuntos:

- União (union ou |)
- Interseção (intersection ou &)
- Diferença (difference ou -)
- Diferença simétrica (symmetric_difference ou ^)

### Vantagens e Considerações:

- **Performance**: Busca e verificação de membros são muito eficientes
- **Memória**: Geralmente usa menos memória que listas com os mesmos elementos
- **Flexibilidade**: Excelente para operações de conjunto
- **Limitações**: Não mantém ordem e só aceita elementos imutáveis

A compreensão dos sets é crucial para manipulação eficiente de dados em Python, especialmente quando trabalhamos com coleções que exigem unicidade de elementos ou operações de conjunto.
