
# numar = int(input("introdu dimensiunea boardului "))

# game = [[1, 0, 0],
#         [0, 1, 0],
#         [2, 0, 2],]

# game = [["X", " ", " "],
#         [" ", "X", " "],
#         ["O", " ", "O"],]


# game = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],]


# def drawdash(numar):
#     for i in range(0,numar):
#         print(" --- "*numar)
#         print("|    "*(numar+1))
#     print(" --- "*numar)


# def drawdashrow(myrow):
#     print(" --- --- --- ")
#     print("| "+ str(myrow[0]) + " | "+ str(myrow[1]) + " | "+ str(myrow[2]) + " |")


#r = [1, 2 , 3, 4]
# drawdash(numar)
#drawdashrow(r)

# def draw_game(joc):
#     for row in joc:
#         drawdashrow(row)
#     print(" --- --- --- ")
#     return None

#draw_game(game)

# def str_game(joc):
#     for i in range(len(joc)):
#         for j in range(len(joc[i])):
#             if joc[i][j] == 0:
#                 joc[i][j] = " "
#             elif joc[i][j] == 1:
#                 joc[i][j] = "X"
#             elif joc[i][j] == 2:
#                 joc[i][j] = "O"
#             else:
#                 print("error")
#     return joc


# print(str_game(game))