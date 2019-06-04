books = ['疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Python讲义']
price = [76, 69, 89]
#使用zip（）函数压缩两个列表，从而实现遍历
for books, price in zip(books, price):
    print("%s的价格是: %5.2f" %(books, price))