# 📚 Aula 17: Utilizando Condições com If, Elif e Else

#### Em Python, a estrutura condicional **`if-elif-else`** permite avaliar múltiplas condições sequencialmente. É útil quando existem várias possibilidades e queremos tomar ações diferentes para cada caso.

- **`if`**: Avalia a primeira condição.
- **`elif`**: Avalia condições adicionais caso a primeira seja falsa.
- **`else`**: Executa quando nenhuma das condições anteriores é verdadeira.
- Torna o código mais organizado e eficiente ao evitar múltiplos **`if`** isolados.

#### Exemplo e Sintaxe

```python
# Calculadora Python
num1 = float(input("Digite o número 1\n"))
num2 = float(input("Digite o número 2\n"))
operation = input("Digite a operação a realizar (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operação inválida")
    result = 0

print(f"Resultado: {result:.2f}")  # :.2f formata o número com duas casas decimais
```

### Explicação Detalhada

#### 1 - **Usando múltiplas condições com `if`, `elif` e `else`**
O programa solicita dois números e uma operação matemática, avaliando qual operação realizar com base na entrada do usuário.  
Se a operação for inválida, uma mensagem de erro é exibida, e o resultado é definido como **0**.

#### **Entradas esperadas:**
- Dois números (float).
- Operação matemática: **+**, **-**, **\*** ou **/**.

#### **Exemplo de saída:**
1. Entrada:  
```python
Digite o número 1
10
Digite o número 2
2
Digite a operação a realizar (+ - * /)
/
```
Saída:  
```python
Resultado: 5.00
```

2. Entrada inválida:  
```python
Digite o número 1
10
Digite o número 2
5
Digite a operação a realizar (+ - * /)
^
```
Saída:  
```python
Operação inválida
Resultado: 0.00
```

### Operadores Suportados na Calculadora
- **`+`**: Soma.  
- **`-`**: Subtração.  
- **`*`**: Multiplicação.  
- **`/`**: Divisão.  

### Observações Importantes
- A divisão por **0** resultará em erro. Pode-se implementar uma validação para evitar isso.  
- O formato **`{:.2f}`** é usado para exibir o resultado com duas casas decimais.  
