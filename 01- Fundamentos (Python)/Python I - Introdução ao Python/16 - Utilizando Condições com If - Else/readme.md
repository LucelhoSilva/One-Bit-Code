# 📚 Aula 16: Utilizando Condições com If - Else

#### Em Python, a estrutura condicional `if-else` permite executar diferentes blocos de código dependendo de uma condição lógica. É essencial para implementar lógica de decisão em programas.

- **`if`**: Avalia uma condição. Se for verdadeira, executa o bloco correspondente.
- **`else`**: Define o que acontece quando a condição do `if` não é verdadeira.
- Suporte para múltiplas condições com **`elif`**.
- Permite criar fluxos de controle dinâmicos baseados em variáveis e entradas.

#### Exemplo e Sintaxe

```python
# Exemplo de condição com entrada de dados
name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Informe o ano de lançamento do jogo\n"))
classification = float(input("Informe a nota de classificação do jogo\n"))

if classification > 8.0:
    print(f"O jogo {name} é bom. Recomendo jogá-lo.")
else:
    print(f"O jogo {name} ainda não atingiu uma boa nota, por isso não recomendo.")

# Exemplo simples com comparação entre números
a = 20
b = 30

if a != b:
    print("Os números são diferentes.")
else:
    print("Os números são iguais.")
```

### Explicação Detalhada

#### 1 - **Condição com `if` e entrada de dados**
No exemplo acima, o programa avalia a nota de classificação de um jogo.  
Se a nota for superior a **8.0**, ele recomenda o jogo, caso contrário, sugere não jogá-lo.  
**Entrada esperada**:
- Nome do jogo (string).
- Ano de lançamento (inteiro).
- Nota de classificação (float).

**Exemplo de saída:**
```python
Digite o nome do jogo
FIFA 23
Informe o ano de lançamento do jogo
2022
Informe a nota de classificação do jogo
8.5
O jogo FIFA 23 é bom. Recomendo jogá-lo.
```

#### 2 - **Comparação entre variáveis**
O segundo exemplo usa a comparação de igualdade e desigualdade (`!=`) para avaliar dois números.  
Se os números forem diferentes, imprime uma mensagem correspondente.  

**Exemplo de saída:**
```python
Os números são diferentes.
```

### Operadores Condicionais em Python
- **`==`**: Igualdade  
- **`!=`**: Desigualdade  
- **`>`**: Maior que  
- **`<`**: Menor que  
- **`>=`**: Maior ou igual  
- **`<=`**: Menor ou igual  