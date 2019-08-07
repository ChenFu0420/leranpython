#定义了支持收集参数的函数
def test(*books, num):
    print(books)
    #books被当做元组处理
    for b in books:
        print (b)
    print(num)
#调用test（）函数
test("crazy ios", "crazy android", num = 20 )