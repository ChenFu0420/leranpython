class  Person:
    '这是学习python定义的一个Person类'
    #下面定义了一个变量
    hari = 'black'
    def __init__(self, name = 'Charlie', age = 8):
        #下面为person对象增加的两个实例
        self.name = name
        self.age = age
        #下面定义了一个say方法
    def say(self, content):
        print(content)
p = Person()
#输出p的name、age实例变量
print(p.name, p.age)
#访问跑的name实例变量，直接为该实例变量赋值
p.name = '李刚'
#调用P的say（）方法在声明say方法时定义了连个形参
#但第一个形参（self）是自动绑定的，因此调用该方法只需要为第二个形参指定一个值
p.say('Python语言很简单，学习很容易！')
#再次输出p.name、age实例变量
print(p.name,p.age)
#为P对象增加一个skills实例变量
p.skills = ['programming', 'swimming']
print(p.skills)
#删除p对象的name实例变量
del p.name
print(p.name)