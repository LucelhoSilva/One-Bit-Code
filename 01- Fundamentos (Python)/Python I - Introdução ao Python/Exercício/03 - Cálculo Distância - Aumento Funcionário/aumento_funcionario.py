salario = float(input('Qual é o seu salário ? \n'))

if salario > 1250:
    aumento = salario * 0.1 # 10%
    novo_salario = salario + aumento
    print(f'Seu salário de R${salario:.2f} teve um aumento de R${aumento:.2f} e foi para R${novo_salario:.2f}')
else:
    aumento = salario * 0.15 # 15%
    novo_salario = salario + aumento
    print(f'Seu salário de R${salario:.2f} teve um aumento de R${aumento:.2f} e foi para R${novo_salario:.2f}')