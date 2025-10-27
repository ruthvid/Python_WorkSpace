def Details_For_Deposit():
    Deposit_Pin = int(input("Enter Pin to Deposit:-- "))
    Deposit_Amount = int(input("Enter Amount to Deposit:-- "))
    customer1.Deposit(Deposit_Pin,Deposit_Amount)


def Details_For_WithDraw():
    WithDraw_Pin = int(input("Enter Pin to WithDraw:-- "))
    WithDraw_Amount = int(input("Enter Amount to WithDraw:-- "))
    customer1.WithDraw(WithDraw_Pin,WithDraw_Amount)

def Details_For_CheckingBalance():
    Pin = int(input("Enter Pin to check Balance:-- "))
    customer1.CheckBalance(Pin)
    
def Details_For_AccountFreezing():
    Pin = int(input("Enter Pin to Freeze your Account:-- "))
    customer1.AccountFreezing(Pin)

class AxisBankAccount:
    def __init__(self,AccountHolder_Name,Current_Balance):
        self.AccountHolder_Name = AccountHolder_Name
        self.__Current_Balance = Current_Balance
        self.__Pin = 2809
        self.__HavingAtmCard = False
        self.__HavingCheckBook = False
        self.__AtmCardFreezed = False
        self.__AccountFreezed = False
        
    def __DepositProcess(self,Deposit_Amount):
        self.__Current_Balance += Deposit_Amount
        return self.__Current_Balance
    
    def __WithDrawProcess(self,WithDraw_Amount):
        self.__Current_Balance -= WithDraw_Amount
        
    def WithDraw(self,WithDraw_Pin,WithDraw_Amount):
        if WithDraw_Pin == self.__Pin:
            if WithDraw_Amount <= self.__Current_Balance:
                self.__WithDrawProcess(WithDraw_Amount)
                print(f"Amount is sucessfully Withdrawn from your Account.Your current balance is {self.__Current_Balance}")
            else:
                print("You Dont have enough Balance...")
        else:
            print("Enter cottect Pin..")
            Details_For_WithDraw()
            
    def Deposit(self,Deposit_Pin,Deposit_Amount):
        if Deposit_Pin == self.__Pin:
            self.__DepositProcess(Deposit_Amount)
            print(f"Amount is sucessfully Deposited.Your current balance is {self.__Current_Balance}")
        else:
            print("Enter cottect Pin..")
            Details_For_Deposit()
            
    def CheckBalance(self,Pin):
        if self.__Pin == Pin:
            print(f"Your current Balance is {self.__Current_Balance}")
        else:
            print("Enter correct pin..")
            Details_For_CheckingBalance()
            
    def Request_For_AtmCardApproval(self):
        self.__HavingAtmCard = True
        print("Your ATM card request is approved")
        
    def Request_For_CheckBookApproval(self):
        self.__HavingCheckBook = True
        print("Your request for CheckBook is Submitted.It will Be delivered to your address..")
        
    def Request_For_AtmCardFreezing(self):
        self.__AtmCardFreezed = True
        print("Your ATM card is Freezed..")
        
    def AccountFreezing(self,Pin):
        if self.__Pin == Pin:
            self.__AccountFreezed = False
            print("Your Account is Freezed..")
        else:
            print("Enter Correct Pin..")
            Details_For_AccountFreezing()
            

class SavingsAccount(AxisBankAccount):
    def __init__(self,AccountHolder_Name,Current_Balance):
        self.LoanLimit = 300000
        super().__init__(AccountHolder_Name,Current_Balance)
    def PersonalLoanRaise(self):
        LoanAmount = int(input("Enter required Loan amount:-- "))
        if LoanAmount > self.LoanLimit:
            print("You cannot get that much loan amount . Your loan Limit is ",self.LoanLimit )
        else:
            print("You are eligible to take that loan amount . your loan request will be processed shortly...")
            
customer1 = SavingsAccount("Ruthvi",10000)


request = input("What service do you want at the moment..(1.CheckBalance / 2.Deposit / 3.WithDraw / 4.AtmCardServices / 5.CheckBookRequest / 6.AccountFreeze 7.LoanRaising) ?  ").lower()

def Customer_Request(Request_Type):
    if Request_Type == "checkbalance" or Request_Type == "1":
        Details_For_CheckingBalance()
    elif Request_Type == "deposit" or Request_Type == "2":
        Details_For_Deposit()
    elif Request_Type == "withdraw" or Request_Type == "3":
        Details_For_WithDraw()
    elif Request_Type == "atmcardservices" or Request_Type == "4":
        def AtmService_Type():
            AtmService = input("What service do you want (1.AtmCardApproval / 2.AtmCardFreezing)? ").lower()
            if AtmService == "atmcardapproval" or AtmService == "1":
                customer1.Request_For_AtmCardApproval()
            elif AtmService == "atmfcardfreezing" or AtmService == "2":
                customer1.Request_For_AtmCardFreezing()
            else:
                print ("Enter Correct input..")
                AtmService_Type()
        AtmService_Type()
    elif Request_Type == "checkbookrequest" or Request_Type == "5":
        customer1.Request_For_CheckBookApproval()
    elif Request_Type == "accountfreezing" or Request_Type == "6":
        Details_For_AccountFreezing()
    elif Request_Type == "loanraising" or Request_Type == "7":
        customer1.PersonalLoanRaise()
    else:
        print("Enter Correct Input...")
        Correctrequest = input("What service do you want at the moment..(1.CheckBalance / 2.Deposit / 3.WithDraw / 4.AtmCardServices / 5.CheckBookRequest / 6.AccountFreeze / 7.LoanRaising) ?  ").lower()
        Customer_Request(Correctrequest)
Customer_Request(request)
    