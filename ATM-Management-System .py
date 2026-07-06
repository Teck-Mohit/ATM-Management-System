Balance =100000

def chekBalance(Balance):
    print("Curent Balance : ", Balance)
    return Balance


def Deposite(Balance):
    Amoount = int(input("Enter the Deposite Amount :"))
    Balance=Balance + Amoount
    print("It ism your balance after deposit :",Balance )
    return Balance


def widrow(Balance):
    Amount = int(input("Enter the Widrow Amount : "))
    if(Balance>=Amount):
       
        print("Account has been debite")
        Balance = Balance-Amount
        print("Its blance after widrow", Balance)

    else:
        print("Insufficient Balance")
    
    return Balance

while True:
    print("==================================================")
    print("                          ATM Menu")
    print("==================================================")
    print("1.Check your Balance")
    print("2.Deposite")
    print("3.Widrow")
    print("4.Exit")

    
    choise = str(input("Enter your Choise :"))
    
    
    if(choise== "1"):
        chekBalance(Balance)
    
    elif(choise=="2"):
       Balance = Deposite(Balance)
    
    elif(choise=="3"):
        Balance = widrow(Balance)
    elif(choise=="4"):
        print("Thank You")
        break

    else:
        print("Invalid Choice")
