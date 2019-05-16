class Account():

    def __init__(self, owner, start_balance):
        self.owner = owner
        self.balance = start_balance

    def deposit(self, amount):
        if amount:
            self.balance += amount
            print('Deposit accepted')
        else:
            print('Invalid deposit')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Funds unavailable!')
        elif amount <= 0:
            print('Invalid withdrawal')
        else:
            self.balance -= amount
            print('Withdrawal accepted!')

    def __str__(self):
        return f'Account owner: \t{self.owner}\nAccount balance: \t${self.balance}'

acct1 = Account('Vlad', 0)
print(acct1)

print (acct1.owner)

print (acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

print(acct1)
