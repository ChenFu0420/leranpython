def get_math_func(type):
    result = 1
    #该函数用的是lambda表达式
    if type == "square":
        return lambda n : n * n
    elif type == "cube":
        return lambda n: n * n *n
    else:
        return lambda n:(1 + n) * n / 2
#调用get_math_func("cube")程序返回一个嵌套函数
math_func = get_math_func("cube") #得到cube函数
print(math_func(5))
math_func = get_math_func("square") #得到square函数
print(math_func(5))
math_func = get_math_func("other") #得到otehr函数
print(math_func(5))
