class Comment:
    def __init__(self, detail, view_time):
        self.detail = detail
        self.view_time = view_time
        def info():
            print("一条简单的评论，内容是%s" %self.detail)

c = Comment('疯狂python讲义很不错', 20)
#判断是佛包含指定的属性或方法
print(hasattr(c, 'detail'))
print(hasattr(c, 'view_time'))
print(hasattr(c, 'info'))
#获取指定属性的属性值
print(getattr(c, 'detail'))
print(getattr(c, 'view_time'))
#由于info是方法下面代码会提示name ‘info’ is not defined
#print(getattr(c, info, '默认值'))

#未指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_time', 32)

#输出重新设置后的属性值

print(c.detail)
print(c.view_time)