import time



class Admin(object):
    admin = 'Jennifer'
    passwd = 'Jennifer'

    def AdminView(self):
        print("**********************************************")
        print("*      Welcome to the banking system         *")
        print("**********************************************")

    # 菜单界面
    def FunctionView(self):
        print("******************************************************")
        print("*     （1）open an account     (2）query              *")
        print("*     （3）withdrawal          (4)deposit             *")
        print("*     （5）transfer accounts   (6)Change password     *")
        print("*     （7）lock                (8)unlock              *")
        print("*     （9）reissue a card      （0）closing an account *")
        print("*                       quit（q）                     *")
        print("******************************************************")

    def Check(self):
        inputAdmin = input("Please enter the administrator account: ")
        if self.admin != inputAdmin:
            print("Administrator account input error!")
            return -1
        inputPasswd = input("Please enter the administrator password: ")
        if self.passwd != inputPasswd:
            print("Administrator password entered wrong!")
            return -1
        print("Operation succeeded, please wait...")
        time.sleep(2)
        return 0