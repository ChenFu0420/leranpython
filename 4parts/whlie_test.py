#循环的初始化条件
count_i = 0
#当count_i小于10时，执行循环体
while count_i < 10:
    print('count:', count_i)
    #迭代语句
    count_i += 1
print("循环结束")

#下面是一个死循环
count_i = 0
while count_i < 10:
    print('count:', count_i)
    count_i -= 1
print('结束循环')