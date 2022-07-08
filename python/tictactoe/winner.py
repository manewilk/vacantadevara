
game2 = [[1, 2, 3, 4, 99],
	    [5, 6, 7, 8, 98],
	    [9, 10, 11, 12, 97],
        [13, 14, 15, 16, 96],
        [17, 18, 19, 20, 95]]

game1 = [[9, 10, 11],
        [13, 14, 15],
        [17, 18, 19]]

game3 = [[5, 6, 7, 8],
	    [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]]


for element in range(0,5):
    print(game2[4-element][element])


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def diagonala1(joc):

    diagonala = []
    for element in range(0, len(joc)):
        diagonala.append(joc[len(joc)-1-element][element])

    return diagonala

d = diagonala1(game2)
print(d)

def diagonala2(joc):

    diagonala = []
    for element in range(0, len(joc)):
        diagonala.append(joc[element][element])

    return diagonala

d = diagonala2(game2)
print(d)


for element in range(0,5):
     print(game2[element][element])