cuvant=input("Type a word ")
cuvant=str(cuvant)
invers=cuvant[::-1]
print(invers)
if cuvant == invers:
    print("Acest cuvant este un palindrom")
else:
    print("Acest cuvant nu este un palindrom")
