# 📚 Aula 5: Utilizando Operadores Aritméticos e Relacionais

### Objetivos de Aprendizagem:

- Dominar os operadores aritméticos básicos e avançados em Python
- Compreender operadores relacionais para comparações
- Entender os operadores de atribuição composta
- Aplicar diferentes tipos de operadores em situações práticas

### Código da Aula:

```python
# Recebendo dois números do usuário
num1 = int(input("Digite o primeiro número\n"))
num2 = int(input("Digite o segundo número\n"))

# Operadores Aritméticos
sum = num1 + num2         # Soma
sub = num1 - num2         # Subtração
div = num1 / num2         # Divisão
mult = num1 * num2        # Multiplicação
mod = num1 % num2         # Módulo (resto da divisão)
exp = num1 ** num2        # Exponenciação

# Exibindo resultados das operações especiais
print(f"Resto da divisão de {num1} por {num2} é {mod}")
print(f"Potência do número {num1} por {num2} é {exp}")

# Operadores de Comparação
bigger = num1 > num2          # Maior que
smaller = num1 < num2         # Menor que
equal = num1 == num2          # Igual a
different = num1 != num2      # Diferente de
bigger_equal = num1 >= num2   # Maior ou igual a
smaller_equal = num1 <= num2  # Menor ou igual a

# Exibindo resultados das comparações
print(f"Os números {num1} e {num2} são iguais? {equal}")
print(f"O número {num1} é maior ou igual a {num2}? {bigger_equal}")

# Operadores de Atribuição Composta
num1 += 1  # Equivalente a: num1 = num1 + 1
num1 -= 1  # Equivalente a: num1 = num1 - 1
num1 *= 1  # Equivalente a: num1 = num1 * 1
num1 /= 1  # Equivalente a: num1 = num1 / 1
```

### Conceitos Importantes

1. Operadores Aritméticos:

   - Soma (+): Adiciona dois números
   - Subtração (-): Subtrai o segundo número do primeiro
   - Multiplicação (\*): Multiplica dois números
   - Divisão (/): Divide o primeiro número pelo segundo
   - Módulo (%): Retorna o resto da divisão
   - Exponenciação (\*\*): Eleva o primeiro número à potência do segundo

2. Operadores Relacionais:

   - Maior que (>): Verifica se o primeiro número é maior
   - Menor que (<): Verifica se o primeiro número é menor
   - Igual a (==): Verifica se os números são iguais
   - Diferente de (!=): Verifica se os números são diferentes
   - Maior ou igual a (>=): Verifica se é maior ou igual
   - Menor ou igual a (<=): Verifica se é menor ou igual

3. Operadores de Atribuição Composta:
   - += : Soma e atribui
   - -= : Subtrai e atribui
   - \*= : Multiplica e atribui
   - /= : Divide e atribui

### Exemplo de Saída:

```
Digite o primeiro número
5
Digite o segundo número
2

Resto da divisão de 5 por 2 é 1
Potência do número 5 por 2 é 25
Os números 5 e 2 são iguais? False
O número 5 é maior ou igual a 2? True
```

### Observações Importantes:

1. Módulo (%):

   - Muito útil para verificar se um número é par ou ímpar
   - Exemplo: num % 2 == 0 (verifica se é par)

2. Exponenciação (\*\*):

   - Forma mais simples de calcular potências em Python
   - Exemplo: 2 \*\* 3 = 8 (2 elevado à terceira potência)

3. Operadores de Atribuição Composta:
   - Simplificam operações de atualização de variáveis
   - São mais concisos que suas formas expandidas
   - Muito usados em contadores e acumuladores
