class User(): # 建立User
    def __init__(self):
        self._username = ""
    
    def create_user_msg(self, uname): # 讀取使用者的輸入建立User
        self._username = uname
        print(f"Create a user named \"{self._username}\".")