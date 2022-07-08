from random import randint, seed


#seed(297597)

def randmat(nr):

    m = []
    
    for i in range(nr):
        m.append([])
    for row in m:
        for x in range(nr):
            rnr = randint(0,10)
            row.append(rnr)
        # print(row)
    return m


matric1 = randmat(40)
print(matric1)

#[[2,2,2],[2,2,2],[2,2,2]]

# [
#     [2,2,2],
#     [2,2,2],
#     [2,2,2]
# ]