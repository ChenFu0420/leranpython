SIZE = 7
array = [[0] * SIZE]
#创建一个长度为 SIZE X SIZE的二维列表
for i in range(SIZE - 1):
    array += [[0] * SIZE]
#该orient代表绕圈方向
#其中0代表向下，1代表向右，2代表向左，3代表向上
orient = 0
#将控制1~SIZE * SIZE的数值填入二维列表中
#其中j控制行索引，k控制列索引
j = 0
k = 0
for i in range(1, SIZE * SIZE + 1):
    array[j][k] = i
    #如果位于图4.2中1号转弯线上
    if j + k == SIZE -1:
        #j > k，位于左下角
        if j > k:
            orient = 1
        else:
            orient = 2
    #如果位于图4.2中2号转弯线上
    elif (k == j) and (k >= SIZE / 2):
        orient = 3
    #如果位于图4.2中的3号转外线上
    elif (j == k - 1) and (k <= SIZE /2):
        orient = 0
    #根据方向为向下绕圈
    if orient == 0:
        j += 1
    #如果方向为向右绕圈
    elif orient == 1:
        k += 1
    #如果方向为向左绕圈
    elif orient == 2:
        k -= 1
    #如果方为向向上绕圈
    elif orient == 3:
        j -= 1
#采用遍历输出上面的二维列表
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d' % array[i][j], end=' ')
    print("")