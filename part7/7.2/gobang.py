inputStr = input("请输入你下棋的坐标，应以X，Y的格式：\n")
while inputStr != None:
    try:
        #将用户输入的字符串以逗号作为分隔符，分割成两个字符串
        x_str, y_str = inputStr.split(sep=',')
        #如果要下棋的点不为空
        if board[int(y_str) - 1][int(x_str) - 1] != "┼":
            inputStr = input("您输入的坐标点已有棋子了，请重新输入 \n")
            continue
        #把对应的列表元素赋为”●“
        board = [int(y_str) - 1][int(x_str)-1] = "●"
    except Exception:
        inputStr = input("您输入的作弊不合法，其请重新输入，下棋坐标应以X,Y的格式\n")
        continue
