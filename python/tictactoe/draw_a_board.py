
numar = int(input("introdu dimensiunea boardului "))



def drawdash(numar):
    for i in range(0,numar):
        print(" --- "*numar)
        print("|    "*(numar+1))
    print(" --- "*numar)

drawdash(numar)

