a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# c=set(c)
# c=list(c)

# [c.append(element) for element in a if element in b and element not in c]
# [c.append(element) for element in b if element in a and element not in c]

a = [1, 1, 66667675688, 3, 56236342, 8, 1424256263, 4242423, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 933333333333, 10, 11, 12, 13]

m=[]

def intersectie(lst1, lst2):
    
    lst3 = []

    for element in lst1:
        if element in lst2 and element not in lst3:
            lst3.append(element)


    for element in lst2:
        if element in lst1 and element not in lst3:
            lst3.append(element)       

    return lst3


print(intersectie(a,m))
intersectie(a,b)
intersectie(a,m)
