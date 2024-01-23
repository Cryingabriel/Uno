#42
class card:
    def __init__(self,number,color):
        self.num = number
        self.color = color
    def printInfo(self):
        print("Number:", self.num)
        print("Color:", self.color)
def gimmeCards() -> list[card]:
    cards = []
    colors = ("r","y","g","b")
    for a in range(2): #In uno there's a second of each card
        for c in colors:
            cards.extend(card(i,c) for i in range(10))
            cards.extend(card(i,c) for i in range(-3,0))#For special cards :D
            #number -1 is reverse
            #number -2 is skip
            #number -3 is +2
    for o in range(4):
        cards.append(card(0,"w"))#W for wild
        cards.append(card(4,"w"))#4 for +4
        #cards.append(card(9,"w"))#Blank card (Ignore me for now)
    return cards