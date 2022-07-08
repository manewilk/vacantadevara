from methods import diagonala1, diagonala2, winner, col_matrix
from random import randint

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


player_start = randint(1,2)
print(f"Incepe jucatorul numarl {player_start}")

win = 0
while win == 0:

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
    d1 = diagonala1(game)
    win = winner(d1)
    if win > 0:
        print(f"Winner {win} on diagonal 1")
        break

    d2 = diagonala2(game)
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

    print(game)
    player_start = player_start%2 + 1
    print(f"Urmeaza jucatorul {player_start}")




print(f"The winner is {win}")