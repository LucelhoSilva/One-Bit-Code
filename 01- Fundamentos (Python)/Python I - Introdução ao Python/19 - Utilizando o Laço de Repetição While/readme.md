# 📚 Aula 19: Utilizando o Laço de Repetição `while`

#### O laço de repetição `while` em Python é usado para executar um bloco de código enquanto uma condição lógica for verdadeira.

- **`while`** avalia a condição antes de cada iteração.
- Útil quando o número de repetições não é conhecido previamente.
- Pode ser combinado com os comandos **`break`** e **`continue`** para maior controle do fluxo.

#### Exemplo e Sintaxe

```python
# Avaliação de jogo com laço while
gameName = input("Digite o nome do jogo\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while rating != -1:  # Continua enquanto a nota não for -1
    rating = float(input("Informe a nota do jogo\n"))
    if rating != -1:  # Ignora a nota de encerramento (-1)
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating

print(f"Média das avaliações do jogo {gameName} é: {average:.2f}")
```

### Explicação Detalhada

#### 1 - **Estrutura básica do `while`**

O loop `while` continua executando o bloco de código enquanto a condição for verdadeira.  
No exemplo acima, o loop só encerra quando a nota digitada for **-1**.

**Exemplo de entrada:**

```python
Digite o nome do jogo
Fifa 23
Informe a nota do jogo
8.0
Informe a nota do jogo
9.0
Informe a nota do jogo
7.5
Informe a nota do jogo
-1
```

**Saída:**

```python
Média das avaliações do jogo Fifa 23 é: 8.17
```

### Detalhes Importantes

- **Nota de parada**: O valor **-1** é usado para encerrar o loop e não é incluído na média.
- **Cálculo da média**: A cada iteração, as notas são somadas, e o total de avaliações é contado para calcular a média.
- **Formatando a média**: O uso de `:.2f` no `f-string` garante que a média seja exibida com duas casas decimais.

### Aplicações

- Recolher e processar entradas de dados até que uma condição de saída seja atendida.
- Criar sistemas dinâmicos, como menus interativos ou cálculos acumulativos.
- Automatizar tarefas repetitivas em que o número de repetições é indefinido.
