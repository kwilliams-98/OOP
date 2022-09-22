import CoinClass as c #case matters based on how you name your file. allows you to import the "blueprints" to create an object.
    #c is just an alias (for the file) here so you don't have to write the whole thing out

# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()' (instance of the Coin object)

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss() #don't call "Coin"; you would be calling the blueprint of an object if you did that
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
