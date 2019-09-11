class canvas:
    def draw_pic(self, shape):
        print('---开始绘图----')
        shape.draw(self)
class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制矩形'% canvas)
class Triangle:
    def draw(self, canvas):
        print('在%s上绘制三角形' %canvas)
class Circle:
    def draw(self, canvas):
        print('在%s上绘制圆形' %canvas)
c = canvas()
#传入Rectangle参数，绘制矩形
c.draw_pic(Rectangle())
#传入Triangle参数，绘制三角形
c.draw_pic(Triangle())
#传入Circle参数绘制圆形
c.draw_pic(Circle())