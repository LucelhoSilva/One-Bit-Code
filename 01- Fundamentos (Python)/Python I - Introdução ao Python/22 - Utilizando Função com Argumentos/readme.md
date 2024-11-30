# 📚 Aula 22: Utilizando Funções com Argumentos

#### Funções com argumentos permitem passar valores durante a chamada da função, tornando-as mais dinâmicas e reutilizáveis.

- Suportam **argumentos posicionais**, **argumentos padrão (default)** e **número variável de argumentos**.
- Melhoram a flexibilidade e personalização das funções.

### Exemplo e Sintaxe

```python
# 1 - Função que recebe dois argumentos: primeiro nome e sobrenome
def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name("Lucelho", "Silva")

# 2 - Função que soma dois números via parâmetros
def sum(a, b):
    print(a + b)

sum(20, 10)

# 3 - Função com argumento padrão
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()
address("Canadá")  # Sobrescreve o padrão

# 4 - Função que aceita um número variável de argumentos
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo:\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo:\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))
rating_game(rating)
```

### Explicação Detalhada

#### 1 - **Funções com Argumentos Posicionais**

Argumentos são passados diretamente na ordem em que aparecem na definição da função:

```python
def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name("Lucelho", "Silva")
# Saída: Lucelho Silva
```

#### 2 - **Funções com Operações entre Argumentos**

Permitem executar cálculos ou operações diretamente nos parâmetros:

```python
def sum(a, b):
    print(a + b)

sum(20, 10)
# Saída: 30
```

#### 3 - **Funções com Argumentos Default (Padrão)**

Caso nenhum argumento seja passado, utiliza um valor pré-definido:

```python
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()        # Saída: Eu moro no Brasil
address("Canadá") # Saída: Eu moro no Canadá
```

#### 4 - **Funções com Número Variável de Argumentos**

Podem processar entradas dinâmicas como a quantidade de avaliações:

```python
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo:\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo:\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))
rating_game(rating)
```

### Sintaxe Geral

```python
def nome_da_funcao(parâmetro1, parâmetro2=valor_padrão, *args):
    # Bloco de código
    return valor  # (opcional)
```

- **`parâmetro1, parâmetro2`**: Argumentos obrigatórios e posicionais.
- **`parâmetro2=valor_padrão`**: Argumentos com valores padrão (opcionais).
- **`*args`**: Aceita uma quantidade variável de argumentos.

### Vantagens de Usar Argumentos

1. **Flexibilidade**: Permite criar funções dinâmicas e reutilizáveis.
2. **Modularidade**: Divide lógicas complexas em blocos menores.
3. **Clareza**: Argumentos nomeados tornam o código mais legível.
4. **Personalização**: Possibilidade de valores padrão evita a necessidade de passar argumentos repetitivos.
