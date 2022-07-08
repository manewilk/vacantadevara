def col_matrix(matrix, col_nr):
     x = []
     for row in matrix:
          # print(row[0])
          x.append(row[col_nr])
     return x


game1 = [[9, 10, 11],
        [13, 14, 15],
        [17, 18, 19]]

# cc = col_matrix(game1, 2)
# print(cc)

# cc = col_matrix(game1, 0)
# print(cc)

# cc = col_matrix(game1, 3)
# print(cc)