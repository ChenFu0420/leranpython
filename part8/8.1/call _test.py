class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def validLogin(self):
        print('验证%s的登录' % self.name)
u = User('crazyit', 'leegang')
#判断u.name是否包含__call__方法，及判断是否可以调用
print(hasattr(u.name,'__call__'))
#判断u.password是否包含__call__方法，及判断他是否可以调用
print(hasattr(u.password,'__call__'))
#判断u.vaildlong是否包含__call__方法，及判断是否可以调用
print(hasattr(u.validLogin, '__call__'))

#定义role类
class Role:
    def __init__(self, name):
        self.name = name
    #定义__call__方法
    def __call__(self):
        print("执行Role对象")
r = Role('管理员')
#直接调用Role对象，就是调用该对想的__call__方法
r()