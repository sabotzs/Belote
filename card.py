class Card:
    number = ""
    color = ""
    to nqma kakvi da sa default-nite ppc 
    def __init__(self,number,color):
        self.number = number
        self.color = color

    def __eq__(self,other):
        return self.number == other.number and self.color == other.color

    def __gt__(self,other):
        list_of_number = ["7","8","9","10","J","Q","K","A"]
        for i in range(0,len(list_of_number)):
            if self.number == list_of_number[i]:
                self_index = i
            if other.number == list_of_number[i]:
                other_index = i
        return self_index > other_index



