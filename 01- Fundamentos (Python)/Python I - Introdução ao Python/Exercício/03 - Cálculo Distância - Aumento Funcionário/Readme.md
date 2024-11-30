# 🎯 Desafio 1: Cálculo da Distância

#### Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.

**Solução fornecida pela OBC:**

```python
distance = float(input("Digite a distância a percorrer: "))
if distance <= 200:
    ticket = 0.5 * distance
else:
    ticket = 0.35 * distance
print(f"Preço da passagem: R$ {ticket:.2f}")
```

# 🎯 Desafio 2: Aumento salário funcionário

#### Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

**Solução fornecida pela OBC:**

```python
salary = float(input("Digite seu salário: "))
perc_increase = 0.15
if salary > 1250:
    perc_increase = 0.10
incresase = salary * perc_increase
print(f"Seu aumento será de: R$ {incresase:.2f}")
```
