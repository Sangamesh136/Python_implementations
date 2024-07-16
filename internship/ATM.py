option =0
mainBalance = 10000
def checkBalance():
    print("Your balance is: ", mainBalance)
    return

def withdraw():
    wd=int(input("Enter the amount you want to withdraw:"))
    mainBalance=mainBalance-wd
    print("Withdrawal in progress...")
    print("Withdrawal successfull..!")
    print("Your total withdrawal is: ",wd)
    print("Your current balance: ", mainBalance)
    
    reciept = int(input("Do you what to have a receipt? \n 1)Yes \n 2) No"))
    if(reciept==1):
        print("Generating Your reciept... \n\n")
        print("TOTAL WITHDRAWL: ",wd)
        print("\n Main Balance: ", mainBalance)
        print("\n ")
        return
    else:
        print("Transaction Successfull!")
        print("THANK YOU!")
        return
    

def deposite():
    depo=int(input("Enter the amount you want to deposite"))
    mainBalance=mainBalance+depo
    print("Your main balance after Deposite is: ", mainBalance)
    return

def Exit():
    print("Thank You \n Come again.")
    return


while(True):
    print("1) Check the balance")
    print("2) Withdraw")
    print("3) Deposite")
    print("4) Exit")
    option = int(input("Enter Your option"))
    if(option==1):
        checkBalance()
    
    if(option==2):
        withdraw()
    
    if(option==3):
        deposite()
        
    if(option==4):
        break