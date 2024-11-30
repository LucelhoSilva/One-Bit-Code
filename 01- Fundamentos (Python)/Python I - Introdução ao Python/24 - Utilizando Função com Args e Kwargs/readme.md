# 📚 Aula 24: Utilizando Função com *Args e **Kwargs

#### **O que são *Args e **Kwargs?**

- **`*args`**:  
  Usado quando não sabemos quantos argumentos serão passados para uma função.  
  - Recebe os argumentos como uma **tupla**.
  - Ideal para funções que precisam trabalhar com um número variável de parâmetros.  

- **`**kwargs`**:  
  Usado para passar argumentos nomeados (chave-valor) dinamicamente.  
  - Recebe os argumentos como um **dicionário**.
  - Permite identificar cada valor por sua respectiva chave.

### Exemplo e Sintaxe

```python
"""
*args: Permite passar um número variável de valores como argumentos.
- Os valores são armazenados em uma tupla.
"""
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

"""
**kwargs: Permite passar argumentos nomeados (chave-valor).
- Os valores são armazenados em um dicionário.
"""
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")
```

### Explicação Detalhada

#### **1 - Uso do `*Args`**
- **Objetivo**: Aceitar múltiplos valores sem especificar o número exato de argumentos.  
- **Como funciona**: Todos os valores são agrupados em uma tupla, que pode ser iterada.

Exemplo:  
```python
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")

sum(4, 5, 9)
# Saída: Soma é: 18
```

**Vantagens:**
- Flexibilidade para trabalhar com listas ou múltiplos valores.  

#### **2 - Uso do `**Kwargs`**
- **Objetivo**: Passar argumentos nomeados como chave-valor.  
- **Como funciona**: Todos os pares são agrupados em um dicionário.

Exemplo:  
```python
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

presentation(name="Python", category="Backend", level="Iniciante")
# Saída:
# name - Python
# category - Backend
# level - Iniciante
```

**Vantagens:**
- Ideal para funções que precisam de argumentos com nomes claros.  
- Facilita a passagem de informações mais estruturadas.  

### Sintaxe Geral

```python
def funcao(*args, **kwargs):
    # args é uma tupla
    for arg in args:
        print(arg)

    # kwargs é um dicionário
    for key, value in kwargs.items():
        print(f"{key} -> {value}")
```

### Aplicações
#### **Quando usar `*Args`?**
- Ao trabalhar com uma quantidade variável de valores.  
- Exemplo: Soma de múltiplos números, impressão de vários itens.

#### **Quando usar `**Kwargs`?**
- Quando precisar identificar cada valor passado com uma chave.  
- Exemplo: Configurações de funções, dados estruturados (como nome, idade, etc.).  

### Vantagens e Desvantagens

#### **Vantagens:**
1. **Flexibilidade**: Permite funções mais dinâmicas e reutilizáveis.  
2. **Legibilidade**: `**kwargs` facilita a leitura ao usar nomes para identificar argumentos.  
3. **Estruturação**: Separa valores (*args) e informações nomeadas (**kwargs).  

#### **Desvantagens:**
1. **Complexidade**: Pode dificultar o entendimento em funções muito genéricas.  
2. **Sobrecarga de Dados**: Facilita a passagem de muitos argumentos, o que pode confundir.  

### Comparação entre `*Args` e `**Kwargs`

| **Características**    | **`*Args`**                      | **`**Kwargs`**                 |
|------------------------|----------------------------------|--------------------------------|
| Tipo de Dados          | Tupla                            | Dicionário                     |
| Uso                    | Múltiplos valores sem nome       | Valores nomeados (chave-valor) |
| Exemplo de Aplicação   | Soma de números                  | Configurações de uma função    |

Funções que utilizam `*args` e `**kwargs` tornam seu código mais flexível e adaptável a diferentes cenários, permitindo o desenvolvimento de aplicações robustas e reutilizáveis.