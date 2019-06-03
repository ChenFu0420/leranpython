src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
a_list = [] #定义保存整除3的元素
b_list = [] #定义保存整除3余1的元素
c_list = [] #定义保存整除3余2的元素
#只有src_list还有元素就继续执行循环体
while len(src_list) > 0 :
    #弹出src——list的最后一个元素
    ele = src_list.pop()
    #如果ele % 3 不等于0
    if ele % 3 == 0 :
        a_list.append(ele)
    elif ele % 3 == 1:
        b_list.append(ele)
    else:
        c_list.append(ele)
print("整除3：", a_list)
print("初以3余1：", b_list)
print("初以3余2：", c_list)