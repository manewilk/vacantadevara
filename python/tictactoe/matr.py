
def game_n(nr):

    m = []
    
    for i in range(nr):
        m.append([])
    for row in m:
        for x in range(nr):
            rnr = 0
            row.append(rnr)
        # print(row)
    return m


joc = game_n(5)
print(joc)

#[[2,2,2],[2,2,2],[2,2,2]]

# [
#     [2,2,2],
#     [2,2,2],
#     [2,2,2]
# ]