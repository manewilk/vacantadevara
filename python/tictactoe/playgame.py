from methods import diagonala, winner, col_matrix, drawdashrow, draw_game, str_game
from random import randint


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


player_start = randint(1,2)

win = 0
while win == 0:

    player_start = player_start%2 + 1
    print(f"Urmeaza jucatorul {player_start}")

    r = int(input("Introdu randul: "))
    c = int(input("Introdu coloana: "))
    game[r][c] = player_start

    """
    Verific winner pe rand
    """
    for row in game: 
        win = winner(row)
        if win > 0:
            print(f"Winner {win} on row {row}")
            break

    """
    Verific winner pe diagonala
    """
    d1 = diagonala(game,1)
    win = winner(d1)
    if win > 0:
        print(f"Winner {win} on diagonal 1")
        break

    d2 = diagonala(game,2)
    win = winner(d2)
    if win > 0:
        print(f"Winner {win} on diagonal 2")
        break

    """
    Verific winner pe coloana
    """
    for i in range(3):
        cc = col_matrix(game, i)
        win = winner(cc)
        if win > 0:
            print(f"Winner {win} on column {i}")
            break

    # print(game)
    game_string = str_game(game)

    draw_game(game_string)





print(f"The winner is {win}")