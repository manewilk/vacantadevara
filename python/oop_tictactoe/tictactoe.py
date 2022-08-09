from random import randint

class Player:

    def __init__(self, p_name):
        self.name = p_name

    def score(self):
        return 1

    def draw(self):
        #print("---- X----")
        return "X"


class Board:
    
    def __init__(self, board_dim = 3):
        print("Desenez un board!")
        self.bdim = board_dim
        
    def __drawdashrow(self, myrow):
        print(" --- --- --- ")
        print("| "+ str(myrow[0]) + " | "+ str(myrow[1]) + " | "+ str(myrow[2]) + " |")

    def draw_game(self, joc):
        for row in joc:
            self.__drawdashrow(row)
        print(" --- --- --- ")
        return None


    def game_n(self):

        m = []
        
        for i in range(self.bdim):
            m.append([])
        for row in m:
            for x in range(self.bdim):
                row.append("")
            # print(row)
        return m

    def str_game(self, joc):

        dim_joc= len(joc[0])
        em_joc = self.game_n()

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

    


class Game:

    def __init__(self, *args):
        self.game = [[2, 0, 0],
                    [0, 3, 0],
                    [0, 0, 66],]
        self.player_start = randint(1,2)
        self.coordonate = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
        # self.win = 0

        # self.player_start = randint(1,2)

        if not args:
            self.player_start = randint(1,2)
        else:
            self.player_start = args[0]

    def intro(self):
        """This is the main game class
           here are the core methods.
           here are the core methods.
           here are the core methods.
           here are the core methods.
           here are the core methods.
        """
        print("Let's start!\n\n\n")


    def col_matrix(self, matrix, col_nr):
        x = []
        for row in matrix:
            # print(row[0])
            x.append(row[col_nr])
        return x
    
    def diagonala(self, x):
        if x == 1:
            diagonala = []
            for element in range(0, len(self.game)):
                diagonala.append(self.game[len(self.game)-1-element][element])
            return diagonala

        elif x == 2:
            diagonala = []
            for element in range(0, len(self.game)):
                diagonala.append(self.game[element][element])
            return diagonala

        else:
            return None


    def winner(self, lista):

        el = list(set(lista))

        if len(el) == 1 and el[0] == 1:
            #print("Primul jucator a castigat ")
            return 1
        if len(el) == 1 and el[0] == 2:
            #print("Al doilea jucator a castigat ")
            return 2
        return 0


    def play(self):
        win = 0

        while win == 0:

            self.player_start = self.player_start%2 + 1
            print(f"Urmeaza jucatorul {self.player_start}")

            cell = int(input("Introdu celula: "))
            r = self.coordonate[cell][0]
            c = self.coordonate[cell][1]
            self.game[r][c] = self.player_start

            """
            Verific winner pe rand
            """
            for row in self.game: 
                win = self.winner(row)
                if win > 0:
                    print(f"Winner {win} on row {row}")
                    break

            """
            Verific winner pe diagonala
            """
            d1 = self.diagonala(1)
            win = self.winner(d1)
            if win > 0:
                print(f"Winner {win} on diagonal 1")
                break

            d2 = self.diagonala(2)
            win = self.winner(d2)
            if win > 0:
                print(f"Winner {win} on diagonal 2")
                break

            """
            Verific winner pe coloana
            """
            for i in range(3):
                cc = self.col_matrix(self.game, i)
                win = self.winner(cc)
                if win > 0:
                    print(f"Winner {win} on column {i}")
                    break

            # print(game)
            game_string = Board().str_game(self.game)

            Board().draw_game(game_string)


if __name__ == "__main__":

    # b1 = Board()

    # print("----------->", b1.game_n())

    # p1 = Player("Marius")

    # # print(p1.score())
    # # print(p1.name)
    # # print(p1.draw())

    # g1 = Game(1,4,9)
    # # print(g1.game)
    # # print(g1.player_start)

    # g2 = Game(None,4,4)
    # # print(g2.game)
    # # print(g2.player_start)

    # g3 = Game()
    # # print(g3.game)
    # # print(g3.player_start)

    # print(g1.diagonala(1))
    # print(g1.diagonala(2))

    Game().intro()
    g1 = Game()
    g1.play()
    # Board().__drawdashrow([2,3,4])