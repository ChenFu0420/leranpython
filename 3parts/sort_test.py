a_list = [3, 4, -2, -30, 14, 9.3, 3.4]
#对列表进行排序
a_list.sort()
print(a_list)
b_list = ['Pyhton', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erlang']
b_list.sort()
#对列表元素排序，默认按字符串包含的字符编码来比较大小
print(b_list)

#指定Key为len，指使用len函数对集合元素生成比较大小的键
#也就是按字符串的长度比较大小
b_list.sort(key=len)
print(b_list)
#指定反向排序
b_list.sort(key=len, reverse=True)
print(b_list)