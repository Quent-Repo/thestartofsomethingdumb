import random
def ace():
    print(null)
cpu = []
you = []

deck = ["ace",2,3,4,5,6,7,8,9,10,"jak","queen","king"]
def pull_card():
    x = (deck[random.randrange(0,len(deck))])
    you.append(x)
    deck.pop()
    if (type(x) == str):
        print(you)
    else:
        print(you)
        print(deck)
pull_card()
