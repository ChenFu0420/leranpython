#定义仓库
repository = dict()
#定义购物清单对象
shop_list= []

#定义一个函数来初始化商品
def init_repository():
    #初始化很多商品，每个元组代表一个商品
    goods1 = ("1000001", "疯狂Ruby讲义", 88.0)
    goods2 = ("1000002", "疯狂Swift讲义", 69.0)
    goods3 = ("1000003", "疯狂Kotlin讲义", 59.0)
    goods4 = ("1000004", "疯狂JAVA讲义", 109.0)
    goods5 = ("1000005", "疯狂Android讲义", 108.0)
    goods6 = ("1000006", "疯狂IOS讲义", 77.0)
    #把商品放入库中
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6
#显示超时的商品清单，就是遍历代表仓库的dict字典
def show_goods():
    print("欢迎光临 疯狂超市")
    print("疯狂超市的商品清单")
    print("%13s%40s%10s"%("条码", "商品名称", "单价"))
    #遍历repository中所有value来显示商品清单
    for goods in repository.values():
        print("%15s%40s%12s" % goods)
#显示购物清单，就是遍历代表购物清单的list的列表
def show_list():
    print('=' * 100)
    #如果清单不为空，则输出清单内容
    if not shop_list:
        print("还未购买商品")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
                ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 100)
        #记录总计的价钱
        sum = 0
        #遍历代表购物清单的list列表
        for i, item in enumerate(shop_list):
            #转换id为索引加1
            id = i + 1
            #获取该购物明细的第1个元素：商品条码
            code = item[0]
            #获取商品条码读取商品，再获取商品名称
            name = repository[code][1]
            #获取商品条码读取商品，再获取商品单价
            price = repository[code][2]
            #获取该购物明细项的第二个元素：商品数量
            number = item[1]
            #小计
            amount = price * number
            #计算总计
            sum = sum + amount
            line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
                   (id, code, name, price, number, amount)
            print(line)
        print("-" * 100)
        print("                           总计：", sum)
    print("=" * 100)
#添加购买的商品，就是想代表用户购物清单的list列表中添加一项
def add():
    #等待输入条码
    code = input("请输入商品条码:\n" )
    #如果没有找到条码，条码错误
    if code not in repository:
        print("条码错误，请重新输入")
        return
    #根据条码找商品
    goods = repository[code]
    #等待输入数量
    number = input("输入你要购买的数量：\n")
    #把商品和购买的数量封装成list后加入购物车清单中
    shop_list.append([code,int(number)])
#修改购买商品的数量，就是修改代表用户购物清单的list列表元素
def edit():
    id = input("请输入要修改的购物明细项目的ID：\n")
    #id减1得到购物明细项目的索引
    index = int(id) - 1
    #根据索引获取某个购物明细项
    item = shop_list[index]
    #提示输入新的购买数量
    number = input("请输入重新购买的数量：\n")
    #修改item里的number
    item[1] = int(number)
#删除以后买的商品明细项，就是删除代表用户购物清单的list列表的元素
def delete():
    id = input("请输入要删除的购物明细项的ID：")
    index= int(id) - 1
    #直接根据所从清单里面删除购物明细项
    del shop_list[index]
def payment():
    show_list()
    print('\n' * 3)
    print("欢迎下次光临")
    #退出程序
    import os
    os._exit(0)
cmd_dict = {'a': add, 'e': edit, 'd': delete, 'p': payment, 's':show_list}
#显示命令提示
def show_command():
    #等待命令
    cmd = input("请输入指令：\n" +
                "添加（a） 修改（e） 删除（d） 结算（p） 超市商品（s） \n")
    #如果用户输入的字符串没有对应的命令
    if cmd not in cmd_dict:
        print("不要玩!")
    else:
        cmd_dict[cmd]()
init_repository()
show_goods()
#显示清单和操作命令提示
while True:
    show_list()
    show_command()