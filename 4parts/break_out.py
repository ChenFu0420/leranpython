exit_falg = False
#外层循环
for i in range(0, 5):
    #内存循环
    for j in range(0, 3):
        print("i的值是：%d j的值是：%d" %(i, j))
        if j == 1:
            exit_falg = True
            #调出外层循环
            break
    #如果exit_flag为True，跳出外层循环
    if exit_falg:
        break