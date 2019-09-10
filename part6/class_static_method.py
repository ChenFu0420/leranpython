class Bird:
    # @使用classmethod 修饰的方法是类方法
    @classmethod
    def fly (cls):
        print('类方法 fly', cls)
    # 使用@staitcmethod 修饰 的方法是静态方法
    @staticmethod
    def info (p):
        print('静态方法info：', p)
#调用类方法，Brid类会自动绑定到第一个参数
Bird.fly()
#调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
Bird.info('crazyit')
#创建Brid对象
b = Bird
#使用此对象调用fly()类方法，其实依然还是使用类的调用的
#因此第一个参数依然被自动绑定到Brid类
b.fly()
#使用对象调用info()静态方法，其实依然还是使用类的调用的
#因此程序必须为第一个参数执行绑定
b.info('fkit')