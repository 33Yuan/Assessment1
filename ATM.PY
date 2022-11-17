import random
class ATM(object):
    def __init__(self, allusers):
        #store information

        self.allUsers = allusers
        #User establishment
    def CreatUser(self):
        name = input("Please enter your name：")
        idCard = input("please enter your ID number：")
        phone = input("Please enter your phone number：")
        preMoney = int(input("Please enter your deposit amount："))
        if preMoney < 0:
                print("Deposit input error, account opening failed......")
                return -1
        onePasswd = input("enter your PIN：")
        if not self.checkPasswd(onePasswd):
            print("incorrect PIN entered, account opening failed......")
            return -1
            # Generate card number
        cardStr = self.creatcardStr()

        card = Card(cardStr, onePasswd, preMoney)
        user = Person(name, idCard, phone, card)
        self.allUsers[cardStr] = user
        print("Account has been opened successfully. Please remember the card number(%s)......" % cardStr)

        # balance inquiry
    def searchUserInfo(self):
        cardnum = input("Please enter your card number：")
            # Verify that the card number exists
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
            # Determine whether it is locked
        if user.card.cardlock == True:
            print("The card has been locked, please unlock it before using other operations......")
            return -1
            # code authentication
        if not self.checkPasswd(user.card.cardpasswd):
            print("Incorrect password, the card has been locked......")
            user.card.cardlock = True
            return -1
            # The query succeeds, and the result is displayed
        print("account：%s     balance：%d" % (user.card.cardStr, int(user.card.cardmoney)))

        # withdrawal
    def getMoney(self):
        cardnum = input("Please enter your card number：")
            # Verify that the card number exists
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
            # Determine whether it is locked
        if user.card.cardlock == True:
            print("The card has been locked, please unlock it before using other operations......")
            return -1
            # code authentication
        if not self.checkPasswd(user.card.cardpasswd):
            print("Incorrect password, the card has been locked......")
            user.card.cardlock = True
            return -1
        print('Your current balance is%d'% user.card.cardmoney)
        getmoney = int(input("Please enter your withdrawal amount："))
        nowmoney = int(user.card.cardmoney)
        if getmoney > nowmoney:
            print("Insufficient balance, withdrawal failure......")
            return -1
        nowmoney -= getmoney
        user.card.cardmoney = nowmoney
        print("The withdrawal is successful. Your current balance is：%d" % user.card.cardmoney)

        # deposit
    def saveMoney(self):
        cardnum = input("Please enter your card number：")
            # Verify that the card number exists
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
            # Determine whether it is locked
        if user.card.cardlock == True:
            print("The card has been locked, please unlock it before using other operations......")
            return -1
            # code authentication
        if not self.checkPasswd(user.card.cardpasswd):
            print("Incorrect PIN, the card has been locked......")
            user.card.cardlock = True
            return -1
        savemoney = int(input("Please enter your deposit amount："))
        nowmoney = int(user.card.cardmoney)
        nowmoney += savemoney
        user.card.cardmoney = nowmoney
        print("The withdrawal is successful. Your current balance is：%d" % user.card.cardmoney)

        # transfer accounts
    def transferMoney(self):
        cardnum = input("Please enter your card number：")
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
        if user.card.cardlock == True:
            print("The card has been locked, please unlock it before using other operations......")
            return -1
        if not self.checkPasswd(user.card.cardpasswd):
            print("Incorrect password, the card has been locked......")
            user.card.cardlock = True
            return -1
        print("account：%s     balance：%d" % (user.card.cardStr, int(user.card.cardmoney)))
        tocardStr = input("Please enter the account you wish to transfer the money to：")
        usertoid = self.allUsers.get(tocardStr)
        if not usertoid:
            print("The card number does not exist, and the query fails......")
            return -1
        tomoney = int(input("Please enter the amount you wish to transfer："))
        nowmoney = int(user.card.cardmoney)
        tonowmoney = int(usertoid.card.cardmoney)
        if tomoney > nowmoney:
            print("The balance is insufficient, the transfer failed......")
            return -1
        nowmoney -= tomoney
        tonowmoney += tomoney
        user.card.cardmoney = nowmoney
        usertoid.card.cardmoney = tonowmoney
        print("The transfer is successful. Your current balance is：%d" % user.card.cardmoney)

        # change PIN
    def changePasswd(self):
        cardnum = input("Please enter your card number：")
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
        if user.card.cardlock == True:
            print("The card has been locked, please unlock it before using other operations......")
            return -1
        if not self.checkPasswd(user.card.cardpasswd):
            print("Incorrect password, the card has been locked......")
            user.card.cardlock = True
            return -1
        newpasswd = input("please enter new PIN：")
        newpasswd2 = input("Please confirm the new PIN:")
        if newpasswd != newpasswd2:
            print("Failed to change the password because the two passwords are inconsistent. Procedure")
            return -1
        user.card.cardpasswd = newpasswd
        print("PIN changed successfully......")

        # 锁定
    def lockUser(self):
        cardnum = input("Please enter your card number：")
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
        if user.card.cardlock:
            print("The card has been locked, please use other functions after the end")
            return -1
        if not self.checkPasswd(user.card.cardpasswd):
            print("PIN ERROR......")
            return -1
            # lock
        user.card.cardlock = True
        print("Locked successfully......")

        # unlock
    def unlockUser(self):
        cardnum = input("Please enter your card number：")
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, unlocking failed......")
            return -1
        if not user.card.cardlock:
            print("The card is unlocked and does not need to be unlocked......")
            return -1
        if not self.checkPasswd(user.card.cardpasswd):
            print("Password error, unlocking failed......")
            return -1
        temid = input("please enter your ID number：")
        if temid != user.idCard:
            print("ID number entered wrong, unlocking failed......")
            return -1
            # unlock
        user.card.cardlock = False
        print("Successfully unlocked......")

        # Refill card
    def newCard(self):
        cardnum = input("Please enter your card number：")
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
        if not self.checkPasswd(user.card.cardpasswd):
            print("PIN error......")
            return -1
            # Regenerate the card number
        newcard = self.creatcardStr()
        user.card.cardStr = newcard
        print("The replacement card has been successfully processed. Here is your new card number：%s" % user.card.cardStr)

        # closing an account
    def killUser(self):
        cardnum = input("Please enter your card number：")
        user = self.allUsers.get(cardnum)
        if not user:
            print("The card number does not exist, the query failed......")
            return -1
        if not self.checkPasswd(user.card.cardpasswd):
            print("Password error, registration failure......")
            return -1
        self.allUsers.pop(cardnum)
        print("The account has since been closed......")

        # Verify password, loop three times without correct output error
    def checkPasswd(self, realPasswd):
        for i in range(3):
            temPasswd = input("Please confirm PIN：")
            if temPasswd == realPasswd:
                return True
        return False

        # The card number is generated randomly
    def creatcardStr(self):
            # Verify that the PIN is the same
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
                # Determine whether it is repeated
            if not self.allUsers.get(str):
                return str
class Person(object):
    def __init__(self,name,idCard,phone,card):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.card = card
class Card(object):
    def __init__(self,cardStr,cardpasswd,cardmoney):
        self.cardStr = cardStr
        self.cardpasswd = cardpasswd
        self.cardmoney = cardmoney
        self.cardlock = False
