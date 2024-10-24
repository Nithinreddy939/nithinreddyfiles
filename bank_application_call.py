from application.bank_application import Account
acc1=Account("Nithin",12343,"saving",5000)
appli=input("Do You have Account In Our Bank?[Yes|No]:")
if appli.lower()=="yes":
    accnumber=int(input("Enter the account Number:"))
    pin=int(input("Enter the ATM pin:"))
    print()
    if accnumber==acc1.getaccNo():
        print("checking Details.......")
        acc1.display()
        print()
    else:
        print("You Don't have account")
        print("Creating to Open your New Bank Account:")
        details = acc1.setDetails()

else:
    print("Creating to Open your New Bank Account:")
    details=acc1.setDetails()
def repeat():
    print("Perform the operation on your account:")
    print("_______________________________________")
    print("press 1 for Account name")
    print("press 2 for Account number")
    print("press 3 for Account type")
    print("press 4 for Account balance")
    print("press 5 for Account withdraw")
    print("press 6 for Account deposit")
    print("press 7 for Account displayDetails")
    print("print 8 for Exit")
    print()
    user=int(input("Enter the number and get your Details:"))
    while True:
        if user==0:
            print()
            print(acc1.invalidno())
            print()
            break
        if user==1:
            print(acc1.getaccName())
        elif user==2:
            print(acc1.getaccNo())
        elif user==3:
            print(acc1.getaccType())
        elif user==4:
            print(acc1.getaccBal())
        elif user==5:
            acc1.withdraw()
        elif user==6:
            acc1.deposit()
        elif user==7:
            acc1.display()
        elif user==8:
            print(acc1.exit())
            return

        else:
            print("Your Entered Invalid number,Enter the number between 0 to 8")
            repeat()
        break
    user2=input("Are you want to repeat the Transaction:[Yes|No] ")
    if user2.lower()=="yes":
        repeat()
    elif user2.lower()=="no":
        print("OOP's,Transaction Declined....\nThank you please again visit our Bank...")
        return
    else:
        print("Transaction successfully completed....\nThank you please again visit our Bank...")

repeat()

