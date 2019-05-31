str1 = input("输入一串字符")
input1, input2 = input("输入你要修改的位置和文字").split()
S = int(input1)
str2 = str1[:S] + input2 + str1[S-1:]
print(str2)