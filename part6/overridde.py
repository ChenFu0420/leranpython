class Bird:
    #Bird类的fly（）方法
    def fly(self):
        print("我在天空自由飞翔")
class Ostrich(Bird):
    #重写Brid类的fly（）方法
    def fly(self):
        print("我只能在地上奔跑")

#创建Ostrich对象
os = Ostrich()
#执行Ostrich对象的fly（）方法，将输“出我只能在地上奔跑”
os.fly()