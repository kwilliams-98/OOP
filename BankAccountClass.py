# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal #this class has one attribute. 
        #put 2 underscores in front of the attribute to hide it (prevents tampering). MUST use underscores everywhere!

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount):
        self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
        if self.__balance >= abs(amount):
            self.__balance -= abs(amount)
        else:
            print('Error: Insufficient funds')

      # The get_balance method returns the
      # account balance.

    def get_balance(self):
        return self.__balance



    def __str__(self): 
      return 'The balance is $' + format(self.__balance, ',.2f')

#it's important to test because you can't think of every scenario!