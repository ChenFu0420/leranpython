#定义一个函数，声明两个形参
def my_max(x ,y):
    z = x if x > y else y
    #返回变量z的值
    return(z)
#定义一个函数，声明一个形参
def say_hi(name):
    print("======正在执行say_hi()参数=======")
    return name + "您好！"
a = 6
b = 9
#调用my_max（）函数，将函数返回值赋值给result变量
result = my_max(a, b)
print("result的值：", result)
#调用say_hi()函数，直接输出函数的返回值
print(say_hi('孙悟空'))