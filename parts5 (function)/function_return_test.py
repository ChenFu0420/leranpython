def get_math_func(type):
    #定义一个计算平凡的局部函数
    def square(n):
        return n * n
    #定义一个计算立方的局部函数
    def cube(n):
        return n * n * n
    #定义一个计算阶乘的局部函数
    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result
    #返回局部函数
    if type == "square":
        return square
    if type == "cube":
        return cube
    else:
        return factorial
#调用get_math_func("cube")程序返回一个嵌套函数
math_func = get_math_func("cube") #得到cube函数
print(math_func(5))
math_func = get_math_func("square") #得到square函数
print(math_func(5))
math_func = get_math_func("factorial") #得到factorial函数
print(math_func(5))


