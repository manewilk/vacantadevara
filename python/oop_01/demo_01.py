

class Player:

    def __init__(self, name):
        self.name = name

    def score(self):
        return 1

    def draw(self):
        #print("---- X----")
        return "X"


p1 = Player("Marius")

print(p1.score())
print(p1.name)
print(p1.draw())