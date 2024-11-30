gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar
localmente ou online.
'''

print(gameName.upper()) # Retornar string toda em Maiúsculo
print(gameName.lower()) # Retornar string toda em  Minúsculo
print(gameName.capitalize()) # Apenas primeira letra maiúscula
print(gameName.title()) # Apenas primeira letra maiúscula
print(gameName.center(10, '-')) # Retorna a string centralizada com o caractere de preenchimento
print(gameName.find("f")) # Retorna a posição do caractere
print(gameDescription.count('a')) # Conta quantos caracteres
print(gameDescription.count('A')) # Conta quantos caracteres
print(gameDescription.replace("Fifa", "Pes")) # Substitui uma string por outra, primeiro voce informa a string que deseja substituir e depois a string que deseja colocar no lugar
print(gameDescription.split(',')) # Separa a string em uma lista, onde o separador é a vírgula