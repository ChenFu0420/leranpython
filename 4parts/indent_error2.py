#定义变量b, 并为其赋值
b = 5
if b > 4:
    #如果b大于4，则执行下面额条件执行体，只有一行代码作为代码块
    print("b 大于 4")
else:
    b -= 1
    #否则，执行下面的跳线执行体，只有一行代码作为代码块
#对于下面的代码而言，他已经不再是条件执行体的一部分，因此总会执行
print("b 不大于 4")


s_age = input("your age:")
age = int(s_age)
if age > 20:
    print("1")
     #print("2")
    #必须保证统一代码块的代码一致缩进，否则会报错！！！