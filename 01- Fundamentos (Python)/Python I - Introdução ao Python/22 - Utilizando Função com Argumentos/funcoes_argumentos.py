# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome.
def full_name(fname, lname):
    print(f"{fname} {lname}")

full_name("Lucelho", "Silva")

# 2 - Crie uma função que some dois números via parâmetros.
def sum(a, b):
    print(a + b)

sum(20, 10)

# 3 - Crie uma função com argumentos default (padrão).
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()
address("Canadá") # Se passar um argumento, ele sobrescreve o padrão

# 4 - Crie uma função que receba um número variável(dinâmico) de argumentos.
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo:\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo:\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")


rating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))
rating_game(rating)
