class AtmMachine:
    def __init__(self,AccountHolder,Amount):
        self.name = AccountHolder
        self.amount = Amount
        self.__pin = 1234
    def __PinCheck_For_Deposit(self,D_Pin):
        if self.__pin == D_Pin:
            return True
        else:
            print("Wrong Pin Entered..")
    def __PinCheck_For_WithDraw(self,W_Pin):
        if self.__pin == W_Pin:
            return True
        else:
            print("Wrong Pin Entered..")
    def deposit(self,Dep_Pin,Dep_amount):
        if self.__PinCheck_For_Deposit(Dep_Pin):
            self.amount += Dep_amount
            print(f"You have added {Dep_amount} and your current balance is {self.amount}")
    def WithDraw(self,WitDra_Pin,WitDra_amount):
        if self.__PinCheck_For_WithDraw(WitDra_Pin):
            if WitDra_amount <= self.amount:
                self.amount -= WitDra_amount
                print(f"{WitDra_amount} is debited.Your current balance is {self.amount}")
            else:
                print(f"Insufficient Balance . Your Balance id {self.amount}")

atm = AtmMachine("Ruthvi",5000)
Input_Pin = int(input("Enter Pin to Deposit/Withdraw:-- "))
depositAmount = int(input("Enter amount to deposit:-- "))
atm.deposit(Input_Pin,depositAmount)
WithDraw_amount = int(input("Enter amount to Withdraw:-- "))
atm.WithDraw(Input_Pin,WithDraw_amount)