
"""Banking system.
The program contains a Bank class, Teller class, and a customer's class. The customer class inherits from the teller
and the teller inherits from the Bank. The Bank class consists of two dictionaries one for accounts and another for loans.
These dictionaries are where all created loan accounts and bank accounts(savings or checking) are saved with the customer's name
as key."""

#super class
class Bank(object):
    accounts = {}
    loans = {}

    def __init__(self,BankId,BankName,BankLocation):
        self.Id = BankId
        self.BanKName = BankName
        self.BankLocation = BankLocation



#teller's class, a sub class which inherits form the Bank class
class Teller(Bank):

    balance = 0

    def __init__(self,TellerID,TellerName):

         self.TellerId = TellerID
         self.Name = TellerName

    def CollectMoney(self):

        pass

# OpenAccount method creates a new customer class in form of a list and saves it in the Bank dictionary(database) for accounts
    def OpenAccount(self):

        self.AccountId = '323245'+str(self.CustomerID)

        if int(self.AccountId) <= 3232455:
            self.AccountType = 'Savings'

        else:
            self.AccountType = 'Checking'

        self.account = [self.name,'AccountNo. = '+self.AccountId,'type = '+self.AccountType,'balance = '+str(self.balance)]

        self.accounts[self.name] = self.account


#Close account method deletes an account from the Bank dictionary using the Customer's name as the key
    def CloseAccount(self):

        del self.account[self.Name]

#Creates a loanaccount for a customer depending on their bank account's status
    def LoanRequest(self,type,amount):
        self.type = type
        self.amount = amount
        self.LoanID = '0020'+str(self.CustomerID)
        if self.balance < 10000:
            print("You donot qualify for alone")

        else:
            self.loandebt = -self.amount
            self.loan = ['Loan ID = '+self.LoanID,'Account type = '+self.type,'AccountID = '+str(self.AccountId),'Customer ID = '+str(self.CustomerID),'Loan debt = '+str(self.loandebt)]

            self.loans[self.name] = self.loan

#Pays loan debt
    def Loan_Pay(self,amount):

        self.loandebt += amount

        if self.loandebt > 0:
            self.loandebt = 0
            print('Your Loan debt is now 0')
            self.balance += self.loandebt
            self.loan = ['Loan ID = '+self.LoanID,'Account type = '+self.type,'AccountID = '+str(self.AccountId),'Customer ID = '+str(self.CustomerID),'Loan debt = '+str(self.loandebt)]
            self.loans[self.name] = self.loan

        else:
            print('Your loan debt is now '+str(self.loandebt))


    def ProvideInfo(self):

        pass

    def IssueCard(self):
        pass



#Customer class inherits from the Teller class

class Customer(Teller):

    def __init__(self,name,Address,Contact,CustomerID,):
        self.name = name
        self.Address = Address
        self.CustomerID = CustomerID
        self.Contact = Contact

#Method for depositing money on the customer's created account
    def DepositMoney(self,x):
        self.x = x
        self.balance += self.x
        self.account = [self.name,'AccountNo. = '+self.AccountId,'type = '+self.AccountType,'balance = '+str(self.balance)]



#Withdraw mehod enables the customer to get some money from his or her account
    def WithdrawMoney(self,y):
        self.y = y
        self.balance -= self.y
        if self.balance < 0:
            print('You have no money on your account')

        else:
            self.account = [self.name,'AccountNo. = '+self.AccountId,'type = '+self.AccountType,'balance = '+str(self.balance)]

        pass


    def RequestCard(self):
        print('Card Request')



    def GeneralInquiry(self):

        print(self.account)


class Account(Customer):
    def details(self):
        self.OpenAccount()
        pass

class Loan(Customer):
    def about(self):
        self.ApplyForLoan()
        pass



#Instantiating objects for the created classes

Bank1 = Bank(1,"Py_Coz Bank",'Kampala')
Bank2 = Bank(2,'Yellow Bank','Cairo')

Bank1.Teller1 = Teller(1,'Teller1')
Bank1.Teller2 = Teller(2,'Teller2')
Bank1.Teller3 = Teller(3,'Teller3')

Bank2.Teller_1 = Teller(1,'Teller_1')
Bank2.Teller_2 = Teller(2,'Teller_2')
Bank2.Teller_3 = Teller(3,'Teller_3')

Bank1.Customer1 = Customer('Ben Wycliff','Makindye','+141',1)
Bank1.Customer2 = Customer('Micheal Jordan','Kikoni','+256',10)
Bank1.Customer3 = Customer('Priscilla Walaga','Makerere','+111',2)
Bank1.Customer4 = Customer('Rodric Calvin','Wandegeya','+255',9)
Bank1.Customer5 = Customer('Edwin Paul','Nankulabye','+001',3)
Bank1.Customer6 = Customer('Isaac Bumanye','Mukono','+221',8)
Bank1.Customer7 = Customer('Teddy Kats','Seeta','+001',7)
Bank1.Customer8 = Customer('Ephraim Malinga','Kampala','+991',6)
Bank1.Customer9 = Customer('Thomas Makumbi','Kikoni','+772',5)
Bank1.Customer10 = Customer('John Paul','Kabalagala','+121',4)


Bank2.Customer1 = Customer('Robert Mugabe','Lusaka','+666',1)
Bank2.Customer2 = Customer('Brian Lubega','Makindye','+171',10)
Bank2.Customer3 = Customer('Chris Tomlin','Makindye','+144',6)
Bank2.Customer4 = Customer('Angelina jolly','Makindye','+241',5)
Bank2.Customer5 = Customer('Will Smith','Makindye','+341',2)
Bank2.Customer6 = Customer('Jose Mourinho','Makindye','+451',9)
Bank2.Customer7 = Customer('Sokko Paul','Makindye','+188',7)
Bank2.Customer8 = Customer('David Degea','Makindye','+741',3)
Bank2.Customer9 = Customer('Pepe Reina','Ports mouth','+411',4)
Bank2.Customer10 = Customer('Steven Gerrad','Merseyside','+810',8)

#Demonstration of how a customer in bank1 creates and account, deposits and withdraws money
Bank1.Customer1.OpenAccount()
Bank1.Customer1.DepositMoney(10000)
print(Bank1.Customer1.account)
Bank1.Customer1.WithdrawMoney(500)
print(Bank1.Customer1.account)

#Demonstration of how a customer gets a loan and pays it
Bank1.Customer2.OpenAccount()
Bank1.Customer2.DepositMoney(222222)
print(Bank1.Customer2.account)
Bank1.Customer2.LoanRequest('student',5000000)
print(Bank1.Customer2.loan)
Bank1.Customer2.Loan_Pay(6000000)
print(Bank1.Customer2.loan)

#Demonstration that a customer whose account balance is less than 10000 can't withdraw a loan
Bank1.Customer4.OpenAccount()
Bank1.Customer4.WithdrawMoney(1000)
print(Bank1.Customer4.account)

#Demonstration of a how a customer in bank2 creates an account, deposits and withdraws money
Bank2.Customer1.OpenAccount()
Bank2.Customer1.DepositMoney(10000)
print(Bank2.Customer1.account)
Bank2.Customer1.WithdrawMoney(5000)
print(Bank2.Customer1.account)

#Demonstration of the dictionaries contain the accounts created above
print(Bank1.loans)
print(Bank1.accounts)


