propozitie = "Lorem ipsum sin dolor"
new_propozitie = ""
for lit in propozitie:
    if lit in ["a","e", "i", "o", "u"]:
        new_propozitie += "X"
    else:
        new_propozitie += lit
        

print("\n", new_propozitie)
print("\n", propozitie) 