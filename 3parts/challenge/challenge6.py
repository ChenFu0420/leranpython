import random
length = int(input("输入列表长度"))
#输入列表长度
my_list = []
for i in range(length):
    my_list.append(input("请输入字符串"))
#输入用户输入列表长度的内容
print(my_list)
new_list = []
[new_list.append(i) for i in my_list if not i in new_list]
#添加没重复的字符串到new_list列表
print(new_list)

new_list = list({}.fromkeys(my_list).keys())
print(new_list)