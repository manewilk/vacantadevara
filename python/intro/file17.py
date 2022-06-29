a = int(input("Write a number "))
print(a)
c = [1, 1]


x = 1
y = 1
m = 0
n = 0

while x+y<a:
        
    m = x
    n = y
    x = n
    y = m + n

    c.append(y)
    if y >= a:
        break





print(c)


#1 1 2 3 5 8 13 ...