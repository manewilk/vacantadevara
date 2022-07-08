
a = int(input("scrie un numar: "))

for element in range(0, a):
    # print(element)
    if element % 15 == 0:
        print("fizzbuzz")
    elif element % 5 == 0:
        print("buzz")
    elif element % 3 ==0:
        print("fizz")
    else:
        print(element)