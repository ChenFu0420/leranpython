class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
im = Item("鼠标", 28.9)
print(im.__dict__)
#通过dict访问name属性
print(im.__dict__['name'])
#通过dict访问price属性
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 30
print(im.name)
print(im.price)