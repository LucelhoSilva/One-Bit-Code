# 📚 Aula 6: Detalhando a Utilização de Strings

### Objetivos de Aprendizagem:

- Compreender os diferentes modos de criar strings em Python
- Entender o conceito de case sensitivity em strings
- Aprender a trabalhar com strings de múltiplas linhas
- Explorar as características básicas de manipulação de texto

### Código da Aula:

```python
# Criando strings com aspas simples
gameName = 'Fifa 23'

# Criando outra string para comparação
gameName2 = 'fifa 23'

# Criando uma string de múltiplas linhas usando três aspas simples
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar localmente ou online.
'''

# Exibindo o nome do jogo
print(gameName)

# Comparando strings (demonstração de case sensitivity)
print(gameName == gameName2)  # Python é case sensitive

# Exibindo a descrição completa
print(gameDescription)
```

### Exemplo de Saída:

```
Fifa 23
False

Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar localmente ou online.
```

### Conceitos Importantes:

1. Formas de Criar Strings:

   - Aspas simples ('texto'): Para strings de uma linha
   - Aspas duplas ("texto"): Funcionalmente idêntica às aspas simples
   - Três aspas simples (''' texto '''): Para strings de múltiplas linhas
   - Três aspas duplas (""" texto """): Alternativa para múltiplas linhas

2. Case Sensitivity:

   - Python diferencia maiúsculas de minúsculas
   - 'Fifa' e 'fifa' são consideradas strings diferentes
   - Comparações (==) levam em conta essa diferenciação

3. Strings Multilinha:
   - Preservam quebras de linha e espaçamentos
   - Úteis para textos longos e formatados
   - Mantêm a indentação do texto

### Características das Strings em Python:

1. Imutabilidade:

   - Strings são imutáveis em Python
   - Uma vez criada, não pode ser modificada diretamente
   - Qualquer modificação cria uma nova string

2. Indexação:

   - Cada caractere tem uma posição (índice)
   - O primeiro caractere está na posição 0
   - Podemos acessar caracteres individuais usando índices

3. Espaços em Branco:
   - São preservados nas strings
   - Incluem espaços, tabs (\t) e quebras de linha (\n)
   - São importantes na formatação do texto
