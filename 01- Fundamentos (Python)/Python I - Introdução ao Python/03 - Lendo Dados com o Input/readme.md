# 📚 Aula 3: Lendo Dados com o Input

### Objetivos de Aprendizagem:

- Entender como receber dados do usuário usando input()
- Aprender a converter tipos de dados (type casting)
- Compreender a importância da formatação de entrada de dados
- Praticar a combinação de input com diferentes tipos de dados

### Código da Aula:

```python
# Recebendo o nome do jogo como texto (string)
name = input("Digite o nome do jogo: ")

# Convertendo a entrada para número inteiro
yearLaunch = int(input("Digite o ano de lançamento: "))

# Convertendo a entrada para número decimal
gamePrice = float(input("Digite o preço do jogo: "))

# Convertendo a entrada para número decimal (nota de avaliação)
noteRating = float(input("Digite a nota de avaliação do jogo: "))

# Exibindo os dados recebidos
print(name)
print(yearLaunch)
print(gamePrice)
print(noteRating)
```

### Output Esperado:

```Python
Digite o nome do jogo: The Legend of Zelda: Breath of the Wild
Digite o ano de lançamento: 2017
Digite o preço do jogo: 250.00
Digite a nota de avaliação do jogo: 9.5
The Legend of Zelda: Breath of the Wild
2017
250.0
9.5
```

### Conceitos Importantes

- Função input(): Sempre retorna uma string (texto) por padrão
- Conversão de Tipos:

  - int(): Converte para número inteiro
  - float(): Converte para número decimal

- Type Casting: É o processo de converter um tipo de dado em outro

### Observações Importantes:

1. O input() sempre captura dados como texto (string), mesmo quando o usuário digita números
2. Para trabalhar com números, precisamos converter a string usando int() ou float()
3. Se o usuário digitar texto quando esperamos um número, o programa gerará um erro
