class Sheet(): # 建立Sheet
    def __init__(self):
        self._sheetname = ""
        self._sheetvalue = []

    def initialsheet(self): # 初始化sheet value
        self._sheetvalue = [[0,0,0],
                           [0,0,0],
                           [0,0,0]]
        
    def printsheet(self): # 印出sheet value內容
        for v in self._sheetvalue:
            print(v)
        
    def create_sheet_msg(self, inputuser, sname): # 讀取使用者輸入建立sheet
        self._sheetname = sname
        self.initialsheet()
        print(f"Create a sheet named \"{self._sheetname}\" for \"{inputuser}\".")
    
    def changesheet(self, indexi, indexj, changev): # 根據使用者輸入的值改變sheet value
        op1 = False
        op2 = False
        op3 = False
        op4 = False
        s1 = ''
        s2 = ''
        for v in range(len(changev)):
            if op1==False and op2==False and op3==False and op4==False:
                if changev[v] == '+':
                    op1 = True
                elif changev[v] == '-':
                    op2 = True
                elif changev[v] == '*':
                    op3 = True
                elif changev[v] == '/':
                    op4 = True
                else:
                    s1 += changev[v]
            else:
                s2 += changev[v]
                if (v+1)==len(changev) or changev[v+1]=='+' or changev[v+1]=='-' or changev[v+1]=='*' or changev[v+1]=='/':
                    if op1:
                        s1 = str(self.add(float(s1), float(s2)))
                        s2 = ''
                        op1 = False
                    elif op2:
                        s1 = str(self.sub(float(s1), float(s2)))
                        s2 = ''
                        op2 = False
                    elif op3:
                        s1 = str(self.mul(float(s1), float(s2)))
                        s2 = ''
                        op3 = False
                    elif op4:
                        s1 = str(self.div(float(s1), float(s2)))
                        s2 = ''
                        op4 = False
        self._sheetvalue[int(indexi)][int(indexj)] = float(s1) if '.' in s1 else int(s1)
        self.printsheet()
        
    def add(self, n1, n2): # 兩數相加
        return n1+n2
    
    def sub(self, n1, n2): # 兩數相減
        return n1-n2
        
    def mul(self, n1, n2): # 兩數相乘
        return n1*n2

    def div(self, n1, n2): # 兩數相除
        return n1/n2