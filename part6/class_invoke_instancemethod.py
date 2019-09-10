class User:
    def walk(self):
        print(self,"慢慢走")
#通过类调用实例方法
u = User()
User.walk('fkit')