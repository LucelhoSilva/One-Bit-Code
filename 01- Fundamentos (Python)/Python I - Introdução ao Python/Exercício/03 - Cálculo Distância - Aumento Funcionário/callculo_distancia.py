distancia = int(input('Qual distância voce deseja percorrer ? \n'))

if distancia <= 200:
    preco = distancia * 0.5
    print(f'Para percorrer a distancia de {distancia}KM, o preço da passagem é R$ {preco}')
else:
    preco = distancia * 0.35
    print(f'Para percorrer a distancia de {distancia}KM, o preço da passagem é R$ {preco}')