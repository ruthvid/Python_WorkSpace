class BankAccount:
    def __init__(self,name,bal,acc_no):
        self.name = name
        self.bal = bal
        self._acc_no = acc_no
        self.__pin = 1234
    def show_details(self):
        print(f"{self.name} is having a bank acc with accountno {self.acc_no} with minimum balance of {self.bal}")
    def BankDeposit(self,d_acc_num,d_amount):
        if d_acc_num == self.acc_no:
            self.bal += d_amount
            print(f"You have added {d_amount} and your total balance id {self.bal}")
        else:
            print(f"You entered wrong account number ",d_acc_num)
    def BankWithdraw(self,w_acc_no,w_amount):
        if w_acc_no == self.acc_no:
            if w_amount <= self.bal :
                self.final_bal = self.bal - w_amount
                print(f"You are withdrawing {w_amount}")
                print(f"Your final balance is {self.final_bal}")
            else:
                print(f"Your current balance is {self.bal} . You are exceeding the withdraw Limit..!")
        else:
            print("Incorrect Account Number ..!")
    def Check_bal(self,acc_no_for_Bal,Pin_for_bal):
        if acc_no_for_Bal == self.acc_no:
            if Pin_for_bal == self.__pin:
                print(f"Your current balance is {self.final_bal}")
            else:
                print(f"You entered wrong pin {Pin_for_bal}")
        else:
            print(f"You entered wrong acc number {acc_no_for_Bal}")
    def Change_pin(self,old_pin):
        if self.__pin == old_pin:
            new_pin = int(input("Enter New Pin:-- "))
            self.__pin = new_pin
            print(f"Your new pin is {self.__pin}")
        else:
            print(f"You entered wrong pin {old_pin}..")
    def Total_details(self):
        print(f"Here is The Final Summary about Your account..")
        print(f"{self.name} is having an account with account number {self.acc_no} with an updated pin number of {self.__pin} and his final balance is {self.final_bal} ")          
    
acc1=BankAccount("Ruthvi",5000,"6345227788")
# acc1.show_details()
# acc_number= input("Enter Bank account number :-- ")
# Deposit_amount = int(input("Enter amount for deposit:-- "))
# acc1.BankDeposit(acc_number,Deposit_amount)
# Withdraw_amount = int(input("Enter the amount you want to withdraw:-- "))
# acc1.BankWithdraw(acc_number,Withdraw_amount)
# pin_num = int(input("Enter Pin for checking Balance:-- "))
# acc1.Check_bal(acc_number,pin_num)
# old_pin = int(input("Enter Old pin for Changing pin:-- "))
# acc1.Change_pin(old_pin)
# acc1.Total_details()
print(acc1._acc_no)
print(acc1._BankAccount__pin)