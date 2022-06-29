a = 5 
print(f"ID ul lui a este {id(a)}, iar valoarea este {a}") 



def f(x):
    a = 6
    print(f"ID ul lui a este {id(a)}, iar valoarea este {a}") 
    def g():
        a = 77
        print(f"ID ul lui a este {id(a)}, iar valoarea este {a}")
    g()



def g():
    a = 7
    print(f"ID ul lui a este {id(a)}, iar valoarea este {a}") 

f(22)
g()
print(f"ID ul lui a este {id(a)}, iar valoarea este {a}") 