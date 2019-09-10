class Address:
    detail = '广州'
    post_coed = '510660'
    def info(self):
        #尝试直接访问变量
#       print(detail) #报错
        #通过类来访问变量
        print(Address.detail)
        print(Address.post_coed)
#通过类来访问Address类的变量
print(Address.detail)
addr = Address()
addr.info()
#修改Address类的变量
Address.detail = '佛山'
Address.post_coed = '460110'
addr.info()