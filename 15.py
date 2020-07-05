# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?
class banking_app:
    def __init__(self,accountname,accountnumber,address,phonenumber,fathersname,mothersname,balance,interestaccured,loan):
        self.accountname=accountname
        self.accountnumber=accountnumber
        self.address=address
        self.phonenumber=phonenumber
        self.fathersname=fathersname
        self.mothersname=mothersname
        self.balance=balance
        self.interestaccured=interestaccured
        self.loan=loan
    
    def displaybalance(self):
        return self.balance
    
    def displaydetails(self):
        return self.accountname, self.accountnumber, self.address, self.phonenumber

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Your balance is %d"%(self.balance))
    
    def withdraw(self,amount):
        if int(self.balance)>amount:
            self.balance=int(self.balance)-amount
            print("You've withdrawn %d amount"%(amount))
            print("Your available balance is %d"%(self.balance))
        else:
            print("The withdraw amount is less than the available balance")


c1=banking_app('Hari Adhikari','00148914841994','Chitwan','9845012345','Shyam Adhikari','Gita Adhikari','74881','375','0')
print(c1.displaydetails())
print(c1.displaybalance())
c1.withdraw(20000)
c1.deposit(10000)