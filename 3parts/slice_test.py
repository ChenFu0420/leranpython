a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
#访问从第2到第4个（不包含）的所有元素
print(a_tuple[1:3])
#访问从倒数第3到倒数第1的所有元素
print(a_tuple[-3:-1])
#访问从第2个到倒数第2个的所有元素
print(a_tuple[1:-2])
#访问从倒数第3个到第5个的所有元素
print(a_tuple[-3:4])

b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#访问从第3到第9个，间隔为2的元素
print(b_tuple[2:8:2])
#访问从第3到第9个，间隔为3的元素
print(b_tuple[2:8:3])
#访问从第3到倒数第2个，间隔为2的元素
print(b_tuple[2:-2:2])