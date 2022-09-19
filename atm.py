print("_________________________________________________________________________________________________")
print("WElcome to ABC Bank ATM ....!")
print("Swipe your card...")
pin=1111
balance=10000
pin=int(input("enter your pin:"))
if pin==1111:
    print("Choose your transaction:")
    print("1.Balance enqiury\n2.withdraw money\n3.Deposit\n4.Change your pin\n5.transfer money\n6.Quit")
else:
    print("invalid pin..try again..")

def balancequery():
    print(f"balance={balance}rs..")
    slip=input("Do you want slip:")
    if slip=="yes":
        print("Here is yuor slip ...\nThank you for using ABC bank ATM....!")
    else:
        print("Thank you for uisng ABC Bank ATM ...!")
def withdraw():
    amount=int(input("Enter your Amount:"))
    if amount<balance:
        print("Collect your cash..\nThank you for using ABC BAnk ATM...!")
    else:
        print("Enter valid amount...")
def deposit():
    deposit=int(input("Enter your deposit amount:"))
    if deposit>0:
        print(f"your amount has been successfully deposit  {deposit} ")
        print(f"your available balance is  {balance+deposit} ")
    else:
        print("Enter valid amount to proceed..")
def changepin():
    change_pin=int(input("Enter your New pin:"))
    if change_pin<=9999:
        print("your pin has changed succesfully...")
    else:
        print("Enter valid pin..")
def transfer():
    transfer=input("Enter your transfer id:")
    print("1.correct\n2.wrong")
    user=int(input())
    if user==1:
        print(f"Your amount will be transfer to this id  {transfer}")
    else :
        print("invalid tranfer id....")
def quit():
    quit_1=input("press yes to quit...")
    if quit_1=="yes":
        print("Quit..")
    else:
        print("choose any transaction....")
user=int(input("choose the transcation:"))

if user==1:
    balancequery()
elif user==2:
    withdraw()
elif user==3:
    deposit()
elif user==4:
    changepin()
elif user==5:
    transfer()
elif user==6:
    quit()
else:
    print("invalid process....")