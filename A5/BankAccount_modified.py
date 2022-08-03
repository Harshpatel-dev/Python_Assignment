class Account(object):
    
    __slotes__ = ['balance' , 'holder']

    def __init__(self , account_holder):
        self.holder = account_holder
        self.balance = 0.00
        self.interest = 0.00
        
    def deposite(self , amount):
        self.balance = self.balance + amount;
        print("Your A/C 01010xxxx credited for ",amount)
    
    def withdraw(self , amount):
        if(self.balance < amount - 2000):
            print("Balance is insufficient");
        else:
            self.balance = self.balance - amount
            print("Your curret Balance is ",self.balance)
    

    def displayBalance(self):
        print("Your current Balance is :",self.balance)

    def transferAmount(self , amount , accountID):
        if(self.balance < amount - 2000):
            print("Balance is insufficient");
        else:
            self.balance = self.balance - amount
            accountID.balance = accountID.balance + amount
            print("Transaction is suceessfull")
            print("Your curret Balance is ",self.balance)


class SavingAccount(Account):

    # interest = 0.00
    
    __slotes__ = ['interest']

    def __init__(self , holder):
        Account.__init__(self , holder)
        SavingAccount.interest = 1.00
    
    def modifyInterest(self , newInterest):
        if(newInterest >= 0.00):
            SavingAccount.interest = newInterest
        else:
            print("Interest can/'t be negative.......")


    def getInterest(self):
        return SavingAccount.interest

    def calculateMonthlyInterest(self):
        return (self.balance*SavingAccount.interest)/100
    
    def __str__(self):
         return "* " + "Name:" + str(self.holder) + ", Current Balance:" + str(self.balance + self.calculateMonthlyInterest())


first_account = SavingAccount("Harsh Patel")
first_account.deposite(10000)

secound_account = SavingAccount("Bipin Mishra")
secound_account.deposite(20000)

first_account.transferAmount(5000 , secound_account)
secound_account.displayBalance()

print(first_account)
print(secound_account)

first_account.modifyInterest(2)

print(first_account)
print(secound_account)


# // error ->class SavingAccount has no attribute 'xyz'
print(first_account.xyz)







    