a_list = ['a', 123, 'b', 'c', 456]
#创建列表a_list
print(a_list)
start, end = int(input("start")), int(input("end"))
#用户输入start，end
b_list = a_list[start:end]
#复制start，end（不包含）区间的值到 b_list
print(b_list)