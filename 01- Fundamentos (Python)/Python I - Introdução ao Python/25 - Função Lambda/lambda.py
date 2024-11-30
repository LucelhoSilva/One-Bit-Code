# 1 - Crie uma função lambda que eleva um número ao quadrado
power = lambda num: num ** 2
# 2 - Crie uma função lambda que verifica se um número é par
pair = lambda x: x%2==0
# 3 - Crie uma função lambda que divide o primeiro número pelo segundo
divNum = lambda x,y : x/y
# 4 - Crie uma função lambda que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10,2))
print(divNum(7,2))
print(reverse("Função"))
print(reverse("Tecnologia"))