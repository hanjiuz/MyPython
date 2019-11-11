#try to define a class

import random


class Greeter(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)
    
    def goodbye(self):
        print("Goodbye " + self.name)
        
g = Greeter("Jessica")
g.hello()
g.goodbye()

print(type(g))

g2 = Greeter("James")
g2.hello()
g2.goodbye()


class Die(object):
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self):
        return random.randint(1, self.sides)

d = Die(10)
print(d.roll())

d = Die(100)
print(d.roll())



class Deck(object):
    def shuffle(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queue", "King"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(suit + " of " + rank)
        
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

d = Deck()
d.shuffle()
print(d.deal())
print(d.deal())
print(d.deal())

print(type(d))