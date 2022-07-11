def winner(lista):

    el = list(set(lista))

    if len(el) == 1 and el[0] == 1:
        #print("Primul jucator a castigat ")
        return 1
    if len(el) == 1 and el[0] == 2:
        #print("Al doilea jucator a castigat ")
        return 2
    return 0


def diagonala1(joc):

    diagonala = []
    for element in range(0, len(joc)):
        diagonala.append(joc[len(joc)-1-element][element])

    return diagonala

 
def diagonala2(joc):

    diagonala = []
    for element in range(0, len(joc)):
        diagonala.append(joc[element][element])

    return diagonala


def col_matrix(matrix, col_nr):
     x = []
     for row in matrix:
          # print(row[0])
          x.append(row[col_nr])
     return x

def diagonala(game,x):
    if x == 1:
        diagonala = []
        for element in range(0, len(game)):
            diagonala.append(game[len(game)-1-element][element])
        return diagonala

    elif x == 2:
        diagonala = []
        for element in range(0, len(game)):
            diagonala.append(game[element][element])
        return diagonala

    else:
        return None

    
# game = [[2, 0, 1],
#         [0, 2, 0],
#         [1, 0, 2]]


# print(diagonala2(game))