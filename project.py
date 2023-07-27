#Bank operation Using OOP

class Bank:
    bankname="Indian National Reserve Bank"
    branch="A23,BBSR,India"

    #create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f'Hello {self.username} cong! Your Account Created Successfully')

    #deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited successfully')

    #withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully')
        else:
            print('Insufficient Fund...')

    #Ministatemnet
    def ministatement(self):
        print(f'Your Account Balance is {self.balance}')
            
        

print(f'Welcome to {Bank.bankname}, {Bank.branch}')
username=input("Enter Your Name :")
pan=input("Enter Your PAN Card Number")
address=input("Enter Your Address")


b=Bank(username,pan,address)

while True:
    print('\nPlease Select any Option : ')
    print('1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop\n')
    option=int(input(''))

    if option==1:
        amount=float(input('Enter Deposited Amount :'))
        b.deposit(amount)
        
    if option==2:
        amount=float(input('Enter withdraw Amount : '))
        b.withdraw(amount)

    if option==3:
        b.ministatement()
    
    if option==4:
        print('Thanks for using Indian National Reserve Bank...')
        break

    

        
