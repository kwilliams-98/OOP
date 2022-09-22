import InsectClass as i 

#create 2 separate instances of the object 
housefly = i.Insect(2,4) #you MUST have values here that correspond to the values passed through init 
mosquito = i.Insect(4,8) #values of the attributes assigned based on the things that you are creating. This allows you to recieve values from 
#the user instead of hardcoding things into the program!

#call the method for each instance
housefly.calc_flight()
mosquito.calc_flight()
    
print("The housefly can fly up to", housefly.get_flight())
print("The mosquito can fly up to", mosquito.get_flight())