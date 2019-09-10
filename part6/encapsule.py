class User:
    def __heien(self):
        print('示范隐藏的hide方法')
    def getname(self):
        return self.__name
    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在 3~8 之间')
        self.__name = name
    name = property(getname, setname)
    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18 ~ 70 之间')
        self.__age = age
    def getage(self):
        return self.__age
    age = property(getage, setage)
#创建User对象
u = User()
#对name属性赋值，实际上调用setname（）方法
#u.name = 'fk' #引发ValueEroor错误
u.name = 'fkit'
u.age = 25
print(u.name)
print(u.age)