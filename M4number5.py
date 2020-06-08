"""
Module IV
5.Design a banking system software with options like cash withdraw, cash credit and change password. The software must
display appropriate results based on user inputs.
"""


class User:
    username = str()
    passHash = str()
    bal = int()

    def __init__(self):
        self.username = input("Name: ")
        self.passHash = input("Password: ").__hash__()
        self.bal = float(input("Balance: "))

    def info(self):
        print("Username:", self.username)
        print("Password hash:", self.passHash)
        print("Balance: $" + str(self.bal))

    def withdraw(self):
        print("Your balance is $" + str(self.bal) + ". How much would you like to withdraw?")
        while True:
            amt = float(input())
            if 0 < amt <= self.bal:
                self.bal -= amt
                print("Withdrawal successful. Your new balance is $" + str(self.bal))
                break
            else:
                print("Inadequate withdrawal amount.")

    def deposit(self):
        print("Your balance is $" + str(self.bal) + ". How much would you like to deposit?")
        amt = float(input())
        self.bal += amt
        print("Deposit successful. Your new balance is $" + str(self.bal))

    def changepass(self):
        print("Please confirm your old password.")
        while True:
            inputPass = input()
            if inputPass.__hash__() == self.passHash:
                print("Password confirmed. Input new password: ")
                newPass = input()
                self.passHash = newPass.__hash__()
                print("Password change successful.")
                break
            else:
                print("Password incorrect. Please try again.")


myUser = User()

while True:
    print("Input 'I' for account info, 'W' to withdraw, 'D' to deposit, 'C' to change password, and 'Q' to quit.")
    cmd = input()
    if cmd == "I" or 'i':
        myUser.info()
    elif cmd == "W" or "w":
        myUser.withdraw()
    elif cmd == "D" or "d":
        myUser.deposit()
    elif cmd == "C" or "c":
        myUser.changepass()
    elif cmd == "Q" or "q":
        print("Closing program.")
        break
    else:
        print("Input not recognized.")
