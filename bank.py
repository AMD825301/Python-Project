class Bank:

    def __init__(self, customerName, accountNo, balance, phoneNo):
        self.customerName = customerName
        self.accountNo = accountNo
        self.balance = balance
        self.phoneNo = phoneNo

    def checkAccount(self):

        enteredAccountNo = int(input("Enter your Account No :- "))

        return enteredAccountNo == self.accountNo

    def checkBalance(self):
        if Bank.checkAccount(self):
            print("Hello {}. Available Balance = {}".format(
                self.customerName, self.balance))
        else:
            print("Account No. doesn't exists.")

    def depositMoney(self):

        if Bank.checkAccount(self):
            amount = int(input("Enter the amount to be deposited :- "))
            self.balance += amount
            print("Now Balance = ", self.balance)

        else:
            print("Please check the Account No.")

    def withdrawMoney(self):

        if Bank.checkAccount(self):
            amount = int(input("Enter the amount to be withdrawal :- "))

            if amount > self.balance:
                print("Insufficient Funds :/")
                return

            self.balance -= amount
            print("Thank you for Withdrawing! Now Balance = ", self.balance)

        else:
            print("Please check the Account No.")

    def updatePhoneNo(self):

        if Bank.checkAccount(self):
            enteredPhoneNo = int(input("Please enter your Old Phone No. "))
            if enteredPhoneNo == self.phoneNo:
                newPhoneNo = int(input("Please enter your New Phone No. "))
                self.phoneNo = newPhoneNo
                print("Your New Phone No. {} is updated successfully.".format(
                    self.phoneNo))
            else:
                print("Phone No. not exists in the record.")

        else:
            print("Please check your Account No.")


acc1 = Bank("Shubham", 1234567890, 20000, 8102366020)
