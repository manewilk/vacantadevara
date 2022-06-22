a = [1, 3, 5, 30, 42, 43, 500]

# def myfunc(nr):
#     if nr < a[0]:
#         return False
#     elif nr > a[-1]:
#         return False
#     else:
#         return True


# def myfunc(nr):
#     if nr in a:
#         return True
#     else:
#         return False


def myfunc(nr):
    for el in a:
        if el == nr:
            return True
    return False
    

b = int(input("Enter your number "))

print(myfunc(b))