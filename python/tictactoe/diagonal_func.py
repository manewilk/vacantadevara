


game = [[9, 10, 11],
        [13, 14, 15],
        [17, 18, 19]]


x = int(input("Ce diagonala doresti? 1 sau 2?: "))

def diagonala(game,x):
    if x == 1:
        diagonala = []
        for element in range(0, len(game)):
            diagonala.append(game[len(game)-1-element][element])

    elif x == 2:
        diagonala = []
        for element in range(0, len(game)):
            diagonala.append(game[element][element])
    else:
        return None

#Sprint(diagonala)

#diagonala(game,x)


def diagonala_II(game,x):
    if x == 1:
        return [ game[i][i] for i in range(dim_game) ]
    else:
        return [ game[i][dim_game - i - 1] for i in range(dim_game ) ]

print(diagonala_II(game,x))