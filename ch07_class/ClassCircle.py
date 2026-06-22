class Circle:
    type = '원'
    def __init__(self, xpos, ypos, radius):
        self.xpos = xpos 
        self.ypos = ypos
        self.radius = radius

    def showinfo(self):
        print('원 중심 : {}, {}'.format(self.xpos, self.ypos))
        print('반지름 : {}'.format(self.radius))
        
        area = 3.14 * self.radius ** 2  
        print('면적 : {}'.format(area))

print('도형의 타입 : %s' % (Circle.type))
print('-' * 20)

circle1 = Circle(3, 5, 10)
circle1.showinfo()
print( '-' * 20 )
circle2 = Circle(8, 6, 20)
circle2.showinfo()