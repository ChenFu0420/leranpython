def test():
    #外层循环
    for i in range(10):
        for j in range(10):
            print("i的值是：%d，j的值是：%d" % (i, j))
            if j == 1:
                return
            print("return后面的语句")
test()