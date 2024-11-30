teams = {}

def print_teams():
    print("\nTimes listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

def print_team_players(team):
    print(f"\nJogadores do {team['name']}:")
    for i, player in enumerate(team['players']):
        print(f"{i+1}. {player}")

def main():
    while True:
        print("\nO que você deseja fazer?")
        print("1. Adicionar um time")
        print("2. Remover um time")
        print("3. Listar times")
        print("4. Adicionar jogador em um time")
        print("5. Remover jogador em um time")
        print("6. Listar jogadores de um time")
        print("7. Sair")

        choice = input("> ")

        match choice:
            case "1":  # Adicionar time
                team_name = input("Digite o nome do time: ")
                teams[team_name] = {'name': team_name, 'players': []}
                print("Time adicionado.")

            case "2":  # Remover time
                print_teams()
                team_num = int(input("Informe o número do time para remover: "))
                if team_num <= len(teams):
                    team_name = list(teams.keys())[team_num-1]
                    del teams[team_name]
                    print("Time removido.")
                else:
                    print("Número de time inválido.")

            case "3":  # Listar times
                print_teams()

            case "4":  # Adicionar jogador
                print_teams()
                team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
                if team_num <= len(teams):
                    team_name = list(teams.keys())[team_num-1]
                    player_name = input("Informe o nome do jogador: ")
                    teams[team_name]['players'].append(player_name)
                    print("Jogador adicionado no time.")
                else:
                    print("Número do time inválido")

            case "5":  # Remover jogador
                print_teams()
                team_num = int(input("Informe o número do time que deseja remover jogador: "))
                if team_num <= len(teams):
                    team_name = list(teams.keys())[team_num-1]
                    print_team_players(teams[team_name])
                    player_num = int(input("Informe o número do jogador para remover: "))
                    if player_num <= len(teams[team_name]['players']):
                        del teams[team_name]['players'][player_num-1]
                        print("Jogador removido do time.")
                    else:
                        print("Número do jogador inválido.")
                else:
                    print("Número do time inválido.")

            case "6":  # Listar jogadores
                print_teams()
                team_num = int(input("Informe o número do time para listar jogadores: "))
                if team_num <= len(teams):
                    team_name = list(teams.keys())[team_num-1]
                    print_team_players(teams[team_name])
                else:
                    print("Número do time inválido.")

            case "7":  # Sair
                print("Programa finalizado.")
                break

            case _:  # Opção inválida
                print("Opção inválida.")

if __name__ == "__main__":
    main()