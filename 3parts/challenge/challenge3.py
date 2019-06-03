import random
length = int(input("输入列表长度"))

my_list = []
'''
for i in range(length):
    num = random.random()
    my_list.append(num)
'''
my_list = [random.random() for i in range(length)]
print(my_list)