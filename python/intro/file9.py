a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for element in a:
    if element < 5 and element not in b:
        b.append(element)
        # print(element)

c = list(set(b))

print(c)