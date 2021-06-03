class Atm(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
        self.balance=10000

    def CashWithdrawel(self):
        withdraw=int(input("Enter amt: "))
        self.balance-=withdraw
        print( withdraw,"has been withdrawn from your account with card number ",self.cardNo)

    def balanceEnquiry(self):
        print("Amount left is ",self.balance)
    
user1=Atm(101010,100875)
user2=Atm(202020,3010)
user1.CashWithdrawel()
user1.balanceEnquiry()
