class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    #定义新的函数结构
    def __del__(self):
        print("del 删除对象")
#创建一个Item对象将之赋值给im变量
im = Item("鼠标", 29.8)
#x = im
#打印im所引用的Item对象
del im
print('-----------------------')