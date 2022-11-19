
from figurine import HANGMANPICS, my_hangman_list
from random import choice

tries = len(HANGMANPICS)-1

word = choice(my_hangman_list)
word_guess = '_'*len(word) 


print("-------", word)


if __name__ == '__main__':

    while tries>0:
        print(list(word_guess), "\n")

        my_let = input("enter a letter: \n").lower()

        if len(my_let) != 1:
            print("Please enter one letter!")
            continue
        
        if my_let in word:
            print("Corect!")
            idx = [i for i, x in enumerate(word) if x == my_let]
            #print(idx)

            for i in idx:
                word_guess = word_guess[:i] + my_let + word_guess[i + 1:]

            if ["_" in word_guess]:
                continue   

        else:
            print('\n\n', HANGMANPICS[7-tries])
            tries=tries-1
            # print(tries)
            if tries == 0:
                print("game over")
            else:
                print(f"Wrong! there are {tries} tries\n")
            
 