
joc = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]



# for row in joc:
#     for el in row:
#         print(el)


# for i in [0, 1, 2]:
#     for j in [0, 1, 2]:
#         print(joc[i][j])

print("randuri -----", len(joc))
print("coloane -----", len(joc[1]))



def under_diag(matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]):
    mone = [[None,None ,None],[None , None, None],[None ,None ,None]]
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            if i >= j:
                mone[i][j] = matrix[i][j]
            else:
                mone[i][j] = 0
    return mone


# print(under_diag(joc))
# print(under_diag([[1, 5, 2], [1, 5, 2], [1, 5, 2]]))
# print(under_diag())


# 
# print(joc)
len(joc)

l1 = [7, 2, 3]
l2 = ["mere", "pere", "nuci"]

l3 = list(zip(l1, l2))
# print(l3)

# for t in l3:
#     print(f"Ana are {t[0]} {t[1]}")

### UDF


### Functional programming

mylist = [1, 2 , 3, 4]

def cubecri(x):
    return x*x*x

def sqcri(y):
    return y*y

m1 = map(cubecri, mylist)
# print(list(m1))

m2 = map(sqcri, mylist)
# print(list(m2))

m3 = map(lambda x: x*x*x, mylist)
# print(list(m3))

m4 = map(lambda x: x*x, mylist)
# print(list(m4))


# Recursion function

# def count_down(start):
#     print(start)
#     if start > 0:
#         count_down(start - 1)


# count_down(5)
