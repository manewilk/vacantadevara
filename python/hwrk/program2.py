# nr = 1978
# inv = 0

# while(nr > 0):
#     rest = nr % 10 
#     v in= inv * 10 + rest
#     nr = nr // 10 

# print(inv - 1000)

nr = 1978
string_nr = str(nr)
l1 = [el for el in string_nr]
l1.reverse()
print(l1)
a = ""
for el in l1:
    a += el 
inv = int(a)

print(inv-1000)