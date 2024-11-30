# 📚 Aula 18: Utilizando o Laço de Repetição `for`

#### O laço de repetição `for` em Python é usado para iterar sobre elementos de uma sequência (listas, tuplas, strings, etc.) ou para executar um bloco de código um número determinado de vezes.

- **`for`** percorre cada elemento de uma sequência.
- Suporta os comandos **`break`** (interrompe o laço) e **`continue`** (pula para a próxima iteração).
- Ideal para iterar sobre coleções e realizar cálculos ou operações em sequência.

---

#### Exemplo e Sintaxe

```python
# Lista de jogos
gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando sobre uma lista
for game in gamesList:
    print(game)

# 2 - Interrompendo o loop com 'break'
for game in gamesList:
    if game == "God of War":
        break
    print(game)

# 3 - Pulando para a próxima iteração com 'continue'
for game in gamesList:
    if game == "God of War":
        continue
    print(game)

# 4 - Avaliação de jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo \n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating:.2f}")
```

---

### Explicação Detalhada

#### 1 - **Iteração básica com `for`**
O loop percorre todos os itens de uma lista, exibindo cada elemento.  
Exemplo:
```python
gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]
for game in gamesList:
    print(game)
```
Saída:
```plaintext
Fifa
God of War
Red Dead 2
Uncharted
```

#### 2 - **Interrompendo o loop com `break`**
Quando a condição é atendida, o comando **`break`** encerra o laço imediatamente.  
Exemplo:
```python
for game in gamesList:
    if game == "God of War":
        break
    print(game)
```
Saída:
```plaintext
Fifa
```

#### 3 - **Pulando iterações com `continue`**
O comando **`continue`