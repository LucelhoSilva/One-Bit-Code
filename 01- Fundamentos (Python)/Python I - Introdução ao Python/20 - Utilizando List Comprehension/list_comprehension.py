"""
Em uma única expressão aplicamos o for e o 
if para selecionar jogos que tenham a letra a

Sintaxe: novalista = 
[expression for item in iterable if condition == True]

"""
# 1- lise valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#    if i < 4:
#       print(i)
listNumbers = [x for x in range(10) if x < 4]
print(listNumbers)

gamesList = ["Mario Odyssey", "Donkey Kong Country",
             "Luigi's mansion", "Kirby"]

# 2 - Jogos que possuem a letra a
# for game in gamesList:
#    if "a" in game:
#        print(game)
newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos que não são Kirby
# for game in gamesList:
# if game != "Kirby":
#    print(game)
gamesFinished = [x for x in gamesList if x != "Kirby"]
print(gamesFinished)


