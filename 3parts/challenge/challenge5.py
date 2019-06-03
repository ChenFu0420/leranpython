import random
length = int(input("输入列表长度"))
my_list = []
for i in range(length):
    num = random.randint(65, 65 + 25)
#随机大写字母
    my_list.append(chr(num))
#添加到my_list列表
print(my_list)
my_list = [chr(random.randint(65, 65 + 25)) for i in range(length)]
print(my_list)