# 📚 Aula 25: Função Lambda

#### **O que é uma Função Lambda?**

- As funções **lambda** são pequenas funções anônimas, ou seja, não possuem um nome fixo como as funções definidas com `def`.
- São criadas utilizando a palavra-chave `lambda`, seguidas pelos parâmetros e pela expressão que será avaliada e retornada.
- São frequentemente usadas para tarefas simples ou como argumentos para funções como `map`, `filter` e `sorted`.

### **Sintaxe**

```python
lambda argumentos: expressão
```

- **Argumentos**: Parâmetros que a função irá receber.
- **Expressão**: Operação ou valor a ser retornado.

### **Exemplo e Código**

```python
# Exemplo 1: Elevar ao quadrado
power = lambda num: num ** 2
print(power(5))  # Saída: 25
print(power(9))  # Saída: 81

# Exemplo 2: Verificar se é par
pair = lambda x: x % 2 == 0
print(pair(27))  # Saída: False
print(pair(30))  # Saída: True

# Exemplo 3: Divisão entre dois números
divNum = lambda x, y: x / y
print(divNum(10, 2))  # Saída: 5.0
print(divNum(7, 2))   # Saída: 3.5

# Exemplo 4: Inverter uma string
reverse = lambda s: s[::-1]
print(reverse("Função"))      # Saída: oãçnuF
print(reverse("Tecnologia"))  # Saída: aigolonceT
```

### **Explicação Detalhada**

#### **1 - Função Lambda para Elevar ao Quadrado**
```python
power = lambda num: num ** 2
print(power(5))  # Saída: 25
```
- **Objetivo**: Retorna o número elevado ao quadrado.
- **Vantagem**: Substitui uma função tradicional simples, como:
  ```python
  def power(num):
      return num ** 2
  ```

#### **2 - Função Lambda para Verificar Paridade**
```python
pair = lambda x: x % 2 == 0
print(pair(30))  # Saída: True
```
- **Objetivo**: Retorna `True` se o número for par e `False` caso contrário.

#### **3 - Função Lambda para Divisão**
```python
divNum = lambda x, y: x / y
print(divNum(10, 2))  # Saída: 5.0
```
- **Objetivo**: Retorna o resultado da divisão entre dois números.

#### **4 - Função Lambda para Inverter uma String**
```python
reverse = lambda s: s[::-1]
print(reverse("Tecnologia"))  # Saída: aigolonceT
```
- **Objetivo**: Retorna a string invertida.

### **Vantagens e Desvantagens**

#### **Vantagens**
1. **Simplicidade**: Reduz o código para tarefas simples.
2. **Leveza**: Criada de forma compacta, sem a necessidade de um `def`.
3. **Ideal para uso temporário**: Usada como função anônima em operações únicas.

#### **Desvantagens**
1. **Legibilidade**: Pode dificultar a leitura de expressões complexas.
2. **Limitações**: Só pode conter uma única expressão, sem múltiplas instruções.

### **Comparação com Funções Tradicionais**

| **Características**               | **Função Tradicional**               | **Função Lambda**                |
|-----------------------------------|--------------------------------------|----------------------------------|
| Definição                         | Usando `def`                         | Usando `lambda`                  |
| Nome                              | Necessário                           | Não possui (anônima)             |
| Linhas de Código                  | Pode conter várias linhas            | Sempre uma única expressão       |
| Legibilidade em Operações Simples | Menos legível                        | Mais legível                     |

### **Quando Usar Funções Lambda?**
1. **Tarefas Simples**: Ideal para operações pequenas e rápidas.  
   Exemplo: Ordenar uma lista de tuplas por um valor específico.  
   ```python
   lista = [(1, 'a'), (2, 'b'), (3, 'c')]
   sorted(lista, key=lambda x: x[1])
   ```

2. **Funções Temporárias**: Quando a função será usada apenas uma vez ou como argumento para outra função.  
   Exemplo: Usar com `map` ou `filter`.  
   ```python
   numeros = [1, 2, 3, 4, 5]
   quadrados = map(lambda x: x ** 2, numeros)
   print(list(quadrados))  # Saída: [1, 4, 9, 16, 25]
   ```