# with open('exercitiu_python.txt', 'a') as open_file:
    # open_file.write(t)


import sys
print(sys.argv[2])

file1 = sys.argv[2]
print(type(file1))

happy = []
prime = []
comune = []
with open('happynumbers.txt', 'r') as open_file:
    happy_text = open_file.readlines()

with open('primenumbers.txt', 'r') as open_file:
    prime_text = open_file.readlines()

for element in happy_text:
    el = int(element.rstrip())
    happy.append(el)

for element in prime_text:
    el = int(element.rstrip())
    prime.append(el)

for element in happy:
    if element in prime:
        # print(element)
        comune.append(element)


for element in comune:

    with open('comune.txt', 'a') as open_file:
        open_file.write(str(element) + '\n')
