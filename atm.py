class Atm(object):
    
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
        self.balance=10000

    def CashWithdrawel(self):
        withdraw=int(input("Enter amount to withdraw: "))
        self.balance-=withdraw
        print( withdraw,"has been withdrawn from your account with card number ",self.cardNo)

    def balanceEnquiry(self):
        print("Amount left is ",self.balance)
    
    def deposit(self):
        deposit=int(input("Enter the amount to be deposited: "))
        self.balance+=deposit
        print(deposit,"has been deposited in your account")
        
    def callFunctions(self):
        print("Choose the option number of the task to perform!")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        choose=int(input("Choose the option: "))
        if(choose==1):
            user1.balanceEnquiry()
        elif(choose==2):
            user1.CashWithdrawel()
        elif(choose==3):
            user1.deposit()

user1=Atm(101010,100875)
user1.callFunctions()
