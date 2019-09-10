class Inconstructor:
    def __init__(self):
        #在构造方法中定义一个foo变量
        foo = 0
        #使用self代表该构造方法正在初始化的对象
        #下面的代码将会吧改构造方法争在初始化的对象的foo实例变成6
        self.foo = 6
#所有使用Inconstructor创建的对象的foo 实例变量将被设为6
print(Inconstructor().foo)