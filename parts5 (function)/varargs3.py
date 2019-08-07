#定义支持收集参数的函数
def test(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)
test(1, 2, 3, "crazy ios", "crazy android", 语文=89,数学=94)