game = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],]



def over_diag(matrix = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]):
    mone = [[None,None ,None],[None , None, None],[None ,None ,None]]
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            if i < j:
                mone[i][j] = matrix[i][j]
            else:
                mone[i][j] = 0
    return mone

print(over_diag(game))