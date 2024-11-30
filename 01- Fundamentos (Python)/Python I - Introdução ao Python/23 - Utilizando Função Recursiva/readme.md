# 📚 Aula 23: Utilizando Função Recursiva

#### **O que é uma Função Recursiva?**  
Uma função recursiva é uma função que chama a si mesma durante sua execução.  
- É útil para resolver problemas que podem ser divididos em subproblemas menores e semelhantes ao problema original.  
- Deve sempre ter uma **condição de parada** para evitar loops infinitos.  

### Exemplo e Sintaxe

```python
"""
Fatorial:
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

number = int(input("Digite o número para fatorial\n"))
print(f"O fatorial de {number} é: {factorial(number)}")

"""
Soma Total:
3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1
"""

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

num = int(input("Digite um número para soma\n"))
print(f"A soma total do {num} é: {total_sum(num)}")
```

### Explicação Detalhada

#### **1 - Função Recursiva para Cálculo de Fatorial**
O fatorial de um número **n** é o produto de todos os números inteiros positivos até **n**:
```python
def factorial(num):
    if num == 1:           # Condição de parada
        return 1
    else:
        return (num * factorial(num - 1))  # Chamada recursiva
```

Exemplo de execução:  
Para calcular o fatorial de 3:  
- `factorial(3) → 3 * factorial(2)`  
- `factorial(2) → 2 * factorial(1)`  
- `factorial(1) → 1`  
Resultado: **6**

#### **2 - Função Recursiva para Soma de Números**
A soma total de um número **n** é o somatório de todos os números inteiros positivos até **n**:
```python
def total_sum(num):
    if num == 1:           # Condição de parada
        return 1
    else:
        return (num + total_sum(num - 1))  # Chamada recursiva
```

Exemplo de execução:  
Para calcular a soma de 3:  
- `total_sum(3) → 3 + total_sum(2)`  
- `total_sum(2) → 2 + total_sum(1)`  
- `total_sum(1) → 1`  
Resultado: **6**

### Conceitos Fundamentais

1. **Condição de Parada**  
   Garante que a função recursiva interrompa sua execução ao atingir um caso base, evitando loops infinitos.  
   
2. **Chamada Recursiva**  
   A função chama a si mesma, reduzindo o problema em direção à condição de parada.  

3. **Divisão de Problema**  
   Recursão é ideal para problemas que podem ser quebrados em subproblemas menores e independentes.  

### Sintaxe Geral de uma Função Recursiva

```python
def funcao_recursiva(parametro):
    if condicao_de_parada:
        return resultado
    else:
        return expressao_com_chamada_recursiva
```

### Vantagens e Desvantagens

#### **Vantagens:**
1. **Código Limpo e Elegante**: Reduz a necessidade de loops explícitos.  
2. **Aplicável a Estruturas Recursivas**: Ideal para problemas como árvores e grafos.  

#### **Desvantagens:**
1. **Alto Consumo de Memória**: Cada chamada cria um novo quadro de pilha.  
2. **Risco de Erros**: Caso a condição de parada não seja implementada corretamente.  
