# 📚 Aula 21: Utilizando Funções

#### Funções em Python são blocos de código reutilizáveis, que permitem organizar e modularizar um programa.

- Definidas com a palavra-chave **`def`**.
- Podem aceitar **parâmetros** e retornar **valores**.
- Melhoram a legibilidade e reduzem a repetição de código.

### Exemplo da aula

```python
# Função simples de boas-vindas
def wellcome():
    print("Hello World")

# Função para criar um jogo
def create_game():
    name = input("Digite o nome do jogo:\n")
    yearLaunch = int(input("Digite o ano de lançamento:\n"))
    gamePrice = float(input("Digite o preço do jogo:\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo:\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

# Chamando as funções
wellcome()
create_game()
```

#### Saida do programa:

```python
Hello World
Digite o nome do jogo:
Fifa 23
Digite o ano de lançamento:
2023
Digite o preço do jogo:
299.90
Digite a nota de avaliação do jogo:
9.0
Fifa 23
2023
299.9
9.0
```

### Explicação Detalhada

#### 1 - **Definição de Funções**

- A função **`wellcome`** não possui parâmetros e apenas exibe uma mensagem.
- A função **`create_game`** não possui parâmetros, mas solicita entradas do usuário para criar um jogo e exibir suas informações.

### Sintaxe Geral de uma Função

```python
def nome_da_funcao(parâmetro1, parâmetro2, ...):
    # Bloco de código
    return valor  # (opcional)
```

- **`def`**: Define a função.
- **`nome_da_funcao`**: Nome único para identificar a função.
- **`parâmetros`**: Variáveis opcionais que podem ser passadas para a função.
- **`return`**: Retorna um valor processado pela função (opcional).

### Vantagens de Utilizar Funções

1. **Reutilização de código**: Evita repetir lógica em várias partes do programa.
2. **Legibilidade**: Organiza o código em blocos lógicos.
3. **Modularização**: Facilita a manutenção e testes ao separar funcionalidades.
4. **Redução de erros**: Centraliza a lógica em um único local.
