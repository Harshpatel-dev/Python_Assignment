class Account(object):
     interest = 0.02
     __slots__=['balance','holder']
     def __init__(self, account_holder):
         self.balance = 50
         self.holder = account_holder

     def deposit(self, amount):
         self.balance = self.balance + amount
         print("Yes!")

     def withdraw(self,amount):
         
         if self.balance < amount :
           print("balance is insufficent:")
         else:
             self.balance=self.balance - amount
             print("now your balance is",self.balance)
           
                 
         

     def displayBalance(self, holderName):
         print("your account balance is :",self.balance)

     def transferAmount(self,amount):
           if self.balance < amount :
            print("balance is insufficent:")
           else:
             
              self.balance=self.balance - amount
              print("tranction is successful!!!! ")
              print("now your balance is",self.balance)


class SavingAccount(Account):

     def limit(self,amount):
              if amount>300000:
                  print(" your balance is higher thaN SAVING ACCOUNT ")

              else:
                  return 0
           
         
     def __str__(self):
              
              return "<<" + "Name:" + str(self.holder) + ", Current Balance:" + str(self.balance) + ">>"

    # @property
     #def AccountHolderName(self):
       #  return self.__holder

  #   @AccountHolderName.setter
    # def AccountHolderName(self,value):
      #   self.__holder= value

     def setBalance(self,value):
         if value > 0:
             self.balance=value
         else:
             self.balance=0

     def getBalance(self):
         return self.balance

        
          

         
         
