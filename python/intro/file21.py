
class A:

    def presentm(self):
        print("I am from class A")

class B:
    # pass
    def presentm(self):
        print("I am from class B")

class C(B, A):
    pass
    # def presentm(self):
    #     print("I am from class C")
        

# a = A()
# a.presentm()

# b = B()
# b.presentm()

c = C()
c.presentm()
print(c.mro())