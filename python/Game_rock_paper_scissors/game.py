
from random import randint

games = 0
wins = 0
losses = 0
draws = 0


while games < 3:


    player1 = input("Choose between rock, paper and scissors \n")

    rps = ["rock", "paper", "scissors"]

    while player1 not in rps:
        player1 = input("Choose between rock, paper and scissors \n")
            
    player2 = rps[randint(0,2)]

    index1 = rps.index(player1)
    index2 = rps.index(player2)

    print(f"Eu am ales {player1} ")
    print(f"Pc-ul a ales {player2} ")

    if player1 == player2:
        print("It s a draw")
        draws = draws + 1
        games = games + 1
    elif index1 == 0 and index2 == 1:
        print("PC wins!")
        losses = losses + 1
        games = games + 1
    elif index1 == 0 and index2 == 2:
        print("I win!!!:)")
        wins = wins + 1
        games = games + 1
    elif index1 == 1 and index2 == 0:
        print("I win!!!:)")
        wins = wins + 1
        games = games + 1
    elif index1 == 1 and index2 == 2:
        print("PC wins")
        losses = losses + 1
        games = games + 1
    elif index1 == 2 and index2 == 0:
        print("PC wins")
        losses = losses + 1
        games = games + 1
    elif index1 == 2 and index2 == 1:
        print("I win!!!:)")
        wins = wins + 1
        games = games + 1
    else:
        print("Aceatsa versiune nu se joaca")

        if input('Do you want to repeat(y/n)') == 'n':
            break

    print(games)
    print(wins)
    print(losses)
    print(draws)


if wins == 2:
    print("Best of three winner")
elif losses == 2:
    print('The PC won')
else:
    print("It s a tie")
    


 