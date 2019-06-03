import random
length = int(input("输入列表长度"))
#用户输入列表长度
my_list = []
#定义my_list空列表
for i in range(length):
    num = random.randint(0, 200)
#定义num随机整数范围为0-200
    if num %2 == 0:
#如果能被2整除+1添加到my_list列表，如不能直接添加到my_list表
        my_list.append(num + 1)
    else:
        my_list.append(num)
print(my_list)
my_list = [random.randint(0, 100) * 2 + 1 for i in range(length)]
print(my_list)