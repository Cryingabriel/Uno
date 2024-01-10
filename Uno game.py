#42
class card:
    def __init__(self,number,color):
        self.num = number
        self.color = color
cards = [card(i,"r") for i in range(10)]