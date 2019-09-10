class User:
    def Test(self):
        print('self参数：', self)
u = User()
#以方法形式调用test（）方法
u.Test()
#将User对象的test方法复制给foo变量
foo = u.Test()
#通过foo变量（函数形式）调用test方法
foo()