from user import User
from sheet import Sheet

class Kernel(User, Sheet): # 繼承User和Sheet，控制使用者的輸入是否可以執行
    def __init__(self):
        self.__read_accright = True
        self.__edit_accright = True
    
    def cheak_2(self, inputuser, sname): # 確認輸入的username與現在的username一樣才能創建sheet
        if inputuser == self._username:
            super().create_sheet_msg(inputuser, sname)
        else:
            print(f"Fail: no user named {inputuser}")
    
    def check_3(self, inputuser, sname): # 確認輸入的username/sheetname與現在的username/sheetname一樣，且Read權限有開啟
        if inputuser==self._username and sname==self._sheetname and self.__read_accright:
            super().printsheet()
        else:
            print("Fail to check a sheet.")
    
    def check_4(self, inputuser, sname): # 確認輸入的username/sheetname與現在的username/sheetname一樣，確認accessright的權限
        if inputuser==self._username and sname==self._sheetname:
            super().printsheet()
            s = input().split(" ")
            indexi = s[0]
            indexj = s[1]
            changev = s[2]
            if self.__read_accright and self.__edit_accright:
                super().changesheet(indexi, indexj, changev)
            elif self.__read_accright and self.__edit_accright==False:
                print("This sheet is not accessible.")
        else:
            print("Fail to change a value in a sheet.")
    
    def check_5(self, inputuser, sname, accright): # 確認輸入的username/sheetname與現在的username/sheetname一樣，根據使用者的輸入判斷開啟的權限
        if inputuser==self._username and sname==self._sheetname and accright=="ReadOnly":
            self.__read_accright = True
            self.__edit_accright = False
        elif inputuser==self._username and sname==self._sheetname and accright=="Read&Edit":
            self.__read_accright = True
            self.__edit_accright = True
        else:
            print("Fail to change access right.")
    
    def check_6(self, inputuser, sname, coluser): # 確認輸入的username/sheetname與現在的username/sheetname一樣才能與使用者輸入的user共用
        if inputuser==self._username and sname==self._sheetname:
            print(f"Share \"{self._username}\"'s \"{self._sheetname}\" with \"{coluser}\".")
        else:
            print("Fail to collaborate with an other user.")