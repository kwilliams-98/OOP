import random 


class Insect: 
    
    def __init__(self,w,l): #always the first method; list out the attributes of the object 
        self.wings = w 
        self.legs = l
        self.flight = 0  #need to initalize your flight variable; notice that both start off the same. the method only interacts with each attribute

    def calc_flight(self):
        self.flight = random.randint(1,10)

    
    def get_flight(self):
        return self.flight
