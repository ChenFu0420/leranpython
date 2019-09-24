class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
#创建一个item对象将之赋值给im变量
im = item("鼠标", 29.8)
print(im)
print(im.__repr__)