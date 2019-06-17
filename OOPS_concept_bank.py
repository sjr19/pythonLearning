class Account:
    # Two attributes: owner, balance
    # Two methods: deposit, withdraw
    # Withdrawals may not exceed the available balance
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return ('Owner: {} (${})'.format(self.owner, self.balance))

    def deposit(self, money):
        self.balance += money
        print("Deposited ${}.".format(money))

    def withdraw(self, money):
        if (self.balance >= money):
            self.balance -= money
            print("Withdrawn ${}.".format(money))
        else:
            print("Insufficient funds.")

# 1. Instantiate the class
acct1 = Account('Jose', 100)    

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.deposit(50)

# 5. Make a series of deposits and Withdrawals
acct1.withdraw(75)

#6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
