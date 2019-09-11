class Dog:
    __slots__ = ('wlak', 'age', 'name')
    def __init__(self, name):
        self.name = name
    def test():
        print('预先设定的test方法')
d = Dog('Snoopy')
from types import MethodType
#只允许为实例动态添加walk，age，name这三个属性或方法
d.wlak = MethodType(lambda self: print('%s正在慢慢的走' %self.name), d)
d.age = 5
d.wlak()

class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    pass
gd = GunDog('Puppy')
#完全可以为GunDog实例动态添加属性
gd.speed = 99
print(gd.speed)