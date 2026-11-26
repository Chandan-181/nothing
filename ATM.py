class ATM:
    def __init__(self,balance):
        self__balance=balance
    def check_balance(self):
        print(self.__balance)
    def withdraw(self,balance):
        if amount>self__balance:
            print("insufficient amount")
        else:
            self__balance-=amount
            print("withdrawal successful")
while True:
    print("welcome to the ATM")
    print("1.check balance")
    print("2.withdraw")
    choice=int(input("enter your choice:"))
    if choice==1:
        atm=ATM(10000)
        atm.check_balance()
    elif choice==2:
        atm=ATM(10000)
        amount=int(input("enter the amount to withdraw:"))
        atm.withdraw(10000)
    print("thank you for using the ATM")
    if input("do you want to continue? (yes/no)")=="no":
        break