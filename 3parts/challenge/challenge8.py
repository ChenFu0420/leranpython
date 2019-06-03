a = input("随机输入多个大写英文字母").split()
s_dict = {}.fromkeys(a)
print(a)
for i in s_dict.keys():
    s_dict[i] = a.count(i)
print(s_dict)