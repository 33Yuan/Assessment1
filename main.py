import os
import pickle
import time

from ATM import ATM
from Admin import Admin

def main():
    # interface object
    admin = Admin()

    # Starting an Administrator
    admin.AdminView()
    if admin.Check():
        return -1

    # Whether the file that stores the information exists
    if os.path.exists("userinfo.txt"):
        filepath = "userinfo.txt"
    else:
        open("userinfo.txt", "wb")
        filepath = "userinfo.txt"

    if os.path.getsize(filepath):
        f = open(filepath, "rb")
        allusers = pickle.load(f)
    else:
        allusers = "Opening the function menu"
        allusers = {}
    print((allusers))
    atm = ATM(allusers)

    while True:
        admin.FunctionView()
        option = input("Please enter your operation：")
        if option == '1':
            # open an account
            atm.CreatUser()
        elif option == '2':
            # query
            atm.searchUserInfo()
        elif option == '3':
            # withdrawal
            atm.getMoney()
        elif option == '4':
            # deposit
            atm.saveMoney()
        elif option == '5':
            # transfer accounts
            atm.transferMoney()
        elif option == '6':
            # change PIN
            atm.changePasswd()
        elif option == '7':
            # lock
            atm.lockUser()
        elif option == '8':
            # unlock
            atm.unlockUser()
        elif option == '9':
            # reissue a card
            atm.newCard()
        elif option == '0':
            # closing an account
            atm.killUser()
        elif option == 'q':
            # quit
            if not admin.Check():
                # Save the user information in the current system to a file
                f = open(filepath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1

        time.sleep(2)


if __name__ == "__main__":
    main()

