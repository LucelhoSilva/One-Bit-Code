# 📚 Aula 9: Principais Métodos em Strings

### Objetivos de Aprendizagem:

Vamos explorar os métodos mais úteis para manipular strings em Python. Estes métodos são fundamentais para processar e transformar texto de maneira eficiente em nossos programas.

### Código da Aula:

```python
# Definindo nossas strings de exemplo
gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar
localmente ou online.
'''

# Métodos de transformação de caso
print(gameName.upper())      # Transforma em maiúsculas: 'FIFA23'
print(gameName.lower())      # Transforma em minúsculas: 'fifa23'
print(gameName.capitalize()) # Primeira letra maiúscula: 'Fifa23'
print(gameName.title())      # Cada Palavra Com Maiúscula: 'Fifa23'

# Método de centralização
print(gameName.center(10, '-'))  # Centraliza: '--Fifa23--'

# Métodos de busca e contagem
print(gameName.find("f"))        # Encontra posição: 2
print(gameDescription.count('a')) # Conta ocorrências de 'a'
print(gameDescription.count('A')) # Conta ocorrências de 'A'

# Métodos de substituição e divisão
print(gameDescription.replace("Fifa", "Pes"))  # Substitui texto
print(gameDescription.split(','))  # Divide em lista nas vírgulas
```

### Saída do Programa:

```python

FIFA23
fifa23
Fifa23
Fifa23
--Fifa23--
2
5
0

Pes 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar
localmente ou online

['\nFifa 23 é um jogo de futebol\n desenvolvido pela EA Sports\n e que possibilita jogar\n localmente ou online\n']
```

### Explicação Detalhada dos Métodos:

1. **Métodos de Transformação de Caso**

   - `upper()`: Transforma toda a string em maiúsculas. Muito útil para comparações sem distinguir maiúsculas/minúsculas.
   - `lower()`: Transforma toda a string em minúsculas. Também excelente para comparações padronizadas.
   - `capitalize()`: Deixa apenas a primeira letra da string em maiúscula. Ideal para formatar nomes próprios.
   - `title()`: Transforma a primeira letra de cada palavra em maiúscula. Perfeito para títulos.

2. **Método de Centralização**

   - `center(width, fillchar)`:
     - `width`: Largura total desejada
     - `fillchar`: Caractere usado para preencher os espaços (opcional, padrão é espaço)
     - Útil para criar cabeçalhos ou menus centralizados

3. **Métodos de Busca e Contagem**

   - `find(substring)`:
     - Retorna o índice da primeira ocorrência da substring
     - Retorna -1 se não encontrar
     - Diferencia maiúsculas de minúsculas
   - `count(substring)`:
     - Conta quantas vezes uma substring aparece
     - Também diferencia maiúsculas de minúsculas

4. **Métodos de Manipulação**
   - `replace(old, new)`:
     - Substitui todas as ocorrências de 'old' por 'new'
     - Cria uma nova string (strings são imutáveis)
     - Útil para correções ou atualizações em massa
   - `split(separator)`:
     - Divide a string em uma lista
     - Usa o separador especificado (vírgula no exemplo)
     - Se nenhum separador for especificado, divide nos espaços em branco

### Exemplos Práticos e Resultados:

```python
texto = "Python Programming"

# Transformações de caso
print(texto.upper())       # PYTHON PROGRAMMING
print(texto.lower())       # python programming
print(texto.title())       # Python Programming

# Centralização
print(texto.center(25, '*'))  # ***Python Programming****

# Busca e contagem
print(texto.find('P'))       # 0 (primeira ocorrência de 'P')
print(texto.count('m'))      # 2 (duas ocorrências de 'm')

# Substituição e divisão
print(texto.replace('P', 'J'))  # Jython Jrogramming
print("a,b,c".split(','))      # ['a', 'b', 'c']
```

### Dicas Importantes:

1. **Imutabilidade**: Lembre-se que strings em Python são imutáveis. Cada método retorna uma nova string ao invés de modificar a original.

2. **Case Sensitivity**: A maioria dos métodos de busca e contagem são sensíveis a maiúsculas/minúsculas. Use `lower()` ou `upper()` antes para buscas que ignoram caso.

3. **Encadeamento de Métodos**: Você pode encadear métodos em uma única linha:

   ```python
   texto.lower().replace(' ', '_').split('_')
   ```

4. **Performance**: Para operações complexas com muitas strings, considere usar métodos mais eficientes como `join()` ao invés de concatenação repetitiva.
