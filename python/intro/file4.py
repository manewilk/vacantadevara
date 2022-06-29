a = [5, 10, 15, 20, 25]
b = []
b.append(a[0])
b.append(a[-1])
# print("Lista mea este: ", b)


def list_ends(a_list):
    print("Hopa lume")
    return [a_list[0], a_list[len(a_list)-1]]


print(list_ends(["mere", "pere", "portocale"]))