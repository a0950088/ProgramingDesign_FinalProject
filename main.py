from kernel import Kernel
   
def printMenu(): # 印出Menu
    print("---------------Menu---------------")
    print("1. Create a user.")
    print("2. Create a sheet.")
    print("3. Check a sheet.")
    print("4. Change a value in a sheet.")
    print("5. Change a sheet's access right.")
    print("6. Collaborate with an other user.")
    print("7. Quit.")
    print("----------------------------------")

if __name__ == '__main__':
    ctrl = Kernel() # 創建Kernel物件
    while True:
        printMenu()
        opt = int(input())
        if opt == 1: # 根據使用者輸入的數字執行不同功能
            uname = input()
            ctrl.create_user_msg(uname)
        elif opt == 2:
            s = input().split(" ")
            uname = s[0]
            sname = s[1]
            ctrl.cheak_2(uname, sname)
        elif opt == 3:
            s = input().split(" ")
            uname = s[0]
            sname = s[1]
            ctrl.check_3(uname, sname)
        elif opt == 4:
            s = input().split(" ")
            uname = s[0]
            sname = s[1]
            ctrl.check_4(uname, sname)
        elif opt == 5:
            s = input().split(" ")
            uname = s[0]
            sname = s[1]
            accright = s[2]
            ctrl.check_5(uname, sname, accright)
        elif opt == 6:
            s = input().split(" ")
            uname = s[0]
            sname = s[1]
            coluser = s[2]
            ctrl.check_6(uname, sname, coluser)
        elif opt == 7: # 輸入 '7' 結束程式
            break