gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar 
localmente ou online.
                '''
line = '='
gameName = 'Fifa'
gameVersion = '24'
gameFullName = gameName + gameVersion # Concatenação de strings juntando o nome do jogo com a versão
print(line*30) # Imprime o caractere '=' 30 vezes, possivel multiplicar strings
print(gameFullName)
print(gameDescription)
print("Fifa" in gameDescription) # Verifica se a string "Fifa" está contida na variável gameDescription, Procura um palavra dentro de outra string
print("futebol" in gameDescription)
print(line*30)