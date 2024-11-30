# 📚 Aula 2: Entendendo os Tipos de Dados

### bjetivos de Aprendizagem:

- Compreender os tipos de dados básicos em Python
- Aprender a criar e atribuir valores a variáveis
- Entender como verificar o tipo de uma variável usando type()
- Reconhecer a diferença entre strings, números inteiros, números decimais e booleanos

### Código da Aula:

```python
# String (texto) - representa o nome do jogo
name = 'Resident Evil 4 Remake'

# Integer (número inteiro) - representa o ano de lançamento
yearLaunch = 2023

# Float (número decimal) - representa o preço do jogo
gamePrice = 300.00

# Boolean (verdadeiro/falso) - representa se está incluído em algum plano
planIncluded = False

# Exibindo os valores das variáveis
print(name)
print(yearLaunch)
print(gamePrice)
print(planIncluded)

# Verificando o tipo de cada variável
print(type(name))        # Vai mostrar: <class 'str'>
print(type(yearLaunch))  # Vai mostrar: <class 'int'>
print(type(gamePrice))   # Vai mostrar: <class 'float'>
print(type(planIncluded))# Vai mostrar: <class 'bool'>
```

### Output Esperado:

```python
Resident Evil 4 Remake
2023
300.0
False
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

### Conceitos Importantes

- Variáveis: São espaços na memória que armazenam dados e podem ter seu conteúdo alterado durante a execução do programa.

- Tipos de Dados em Python:

  - str (string): Usado para textos e caracteres
  - int (integer): Usado para números inteiros
  - float: Usado para números decimais
  - bool (boolean): Usado para valores verdadeiro (True) ou falso (False)

- Função type(): Retorna o tipo de dado de uma variável, útil para debugging e verificação de dados.
