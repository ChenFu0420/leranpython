a_list = ['crazyit', 20, -2.4, (3, 4), 'fkit']
#删除第三个元素
del a_list[2]
print(a_list)
#删除第二个到第四个（不包含）元素
del a_list[1: 3]
print(a_list)
b_list = list(range(1, 10))
#删除第3个到倒数2个（不包含）元素，间隔为2
del b_list[2: -2: 2]
print(b_list)
#删除第3个到第5个（不包含）元素，间隔为2
del b_list[2: 4]
print(b_list)
c_list = [20, 'crazyit', 30, -4, 'crazyit', 3.4]
#删除第一次找到的30
c_list.remove(30)
print(c_list)
#删除第一次找到的crazyit
c_list.remove('crazyit')
print(c_list)
c_list.clear()
print(c_list)



'''
name = 'crazyit'
print(name)
del name
print(name)
'''