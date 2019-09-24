class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info (self):
        pass

#创建一个Item对象，将之赋值给IM变量
im = Item("鼠标", 28.9)
print(im.__dir__())
print(dir(im))
