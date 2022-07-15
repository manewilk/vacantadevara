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


def drawdashrow(myrow):
    print(" --- --- --- ")
    print("| "+ str(myrow[0]) + " | "+ str(myrow[1]) + " | "+ str(myrow[2]) + " |")


#r = [1, 2 , 3, 4]
# drawdash(numar)
#drawdashrow(r)

def draw_game(joc):
    for row in joc:
        drawdashrow(row)
    print(" --- --- --- ")
    return None


def game_n(nr):

    m = []
    
    for i in range(nr):
        m.append([])
    for row in m:
        for x in range(nr):
            rnr = ""
            row.append(rnr)
        # print(row)
    return m

def str_game(joc):

    dim_joc= len(joc[0])
    em_joc = game_n(dim_joc)

    for i in range(len(joc)):
        for j in range(len(joc[i])):
            if joc[i][j] == 0:
                em_joc[i][j] = " "
            elif joc[i][j] == 1:
                 em_joc[i][j] = "X"
            elif joc[i][j] == 2:
                 em_joc[i][j] = "O"
            else:
                continue

    return em_joc



