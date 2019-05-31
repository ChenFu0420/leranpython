a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'flit', 3.33)
#计算元组相加
sum_tuple = a_tuple + b_tuple
print(sum_tuple)
print(a_tuple)#a_tuple没有改变
print(b_tuple)#b_tuplem没有改变
#两个元组相加
print(a_tuple + (-20, -30))
#下面代码报错，元组和列表不能直接相加
#print(a_tuple + [-20, -30])
a_list = [20, 30, 50, 100]
b_list = ['a', 'b', 'c']
#计算相加列表
sum_list = a_list + b_list
print(sum_list)
print(a_list + ['fkit'])