def test(name, message):
    print("用户名是：", name)
    print("消息是：", message)
my_list = ['孙悟空','欢迎来到疯狂软件']
test(*my_list)

def foo(name, *nums):
    print("name 参数", name)
    print("nums 参数", nums)
my_tuple = (1, 2, 3)
#使用逆向收集，将my_tuple元组的元素传个nums参数
foo('fkit', *my_tuple)

def bar(book, price, desc):
    print(book, "这本书的价格是", price)
    print('描述信息', desc)
my_dict = {'price' : 89, 'book': 'crazy ios', 'desc' : '这是一本系统全面的python学习图书'}
#按照逆向收集的方式将my_dictde多个key-value对传给bar（）函数
bar(**my_dict)