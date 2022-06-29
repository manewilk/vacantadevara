nr = int(input("Please insert a number: "))
divizori = []

# for element in range(1, nr+1):
#     if nr%element==0:
#         divizori.append(element)

jumate = int(nr/2)
# print(jumate)


# element = 1
# while element < nr:
#     if nr%element==0:
#         if element >= jumate:
#             break
#         divizori.append(element)

#     element += 1

[divizori.append(element) for element in range(1, nr+1) if nr%element==0 and element < jumate]

print(divizori)

