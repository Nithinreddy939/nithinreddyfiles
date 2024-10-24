class Account:
    def __init__(self,accName,accNo,accType,accBal):
        self.__accName=accName
        self.__accNo = accNo
        self.__accType = accType
        self.__accBal = accBal
    def setDetails(self):
        self.__accName=input("Enter your Name as per Gov Id:")
        self.__accNo=int(input("Enter your Account Number:"))
        self.__accType=input("Enter the Type of the Account you Like:")
        self.__accBal=int(input("Enter the Minimum Balance to Deposit:"))
        return
    def getaccName(self):
        return self.__accName

    def getaccNo(self):
        return self.__accNo

    def getaccType(self):
        return self.__accType

    def getaccBal(self):
        return  self.__accBal

    def withdraw(self):
        amount=int(input("enter the amount to be withdraw:"))
        if amount>self.__accBal-500:
            print(f"Insuficiant funds in your account")
            return
        self.__accBal -= amount
        print("successfully withdraw your amount....")
        print(f"Current Balance:{self.__accBal}")
    def deposit(self):
        amount=int(input("enter the amount to be deposit:"))
        self.__accBal += amount
        print("successfully deposit your amount...")
        print(f"Available Balance:{self.__accBal}")

    def display(self):
        print("Your Account Details:")
        print("______________________")
        print(f"Account holder name:{self.__accName}")
        print(f"Account number:{self.__accNo}")
        print(f"Account type:{self.__accType}")
        print(f"Account Balance:{self.__accBal}")
    def invalidno(self):
        return f"Get out from My Mother Land...."


    def exit(self):
        return f"congratulation completed your transaction..."
