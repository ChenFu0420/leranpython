#同事对元组使用加法、乘法
order_endings = ('st', 'nd', 'rd')\
    +('th',) * 17 + ('st', 'nt', 'rd')\
    +('th',) * 7 + ('st',)
print(order_endings)
day = input("输入日期（1-31）：")
day_int = int(day)
print(day + order_endings[day_int - 1])