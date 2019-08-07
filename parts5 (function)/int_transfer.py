def swap(a , b):
    #下面代码实现a,b变量值的交换
    a, b = b, a
    print("在 swap函数里，a的值是", \
        a, "b的值是", b)
a = 6
b = 9
swap(a, b)
print("交换完之后，变量a的值是", a, "b的值是：", b)