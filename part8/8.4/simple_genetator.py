def test(val, step):
    print("-----------函数开始执行--------------")
    cur = 0
    #遍历0~val
    for i in range(val):
        #cur 添加i * step
        cur += i * step
        print(cur, end=' ')
test(10, 2)