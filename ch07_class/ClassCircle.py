# 1) 요구 사항
# 원의 반지름과 중심 및 면적을 구해주는 프로그램을 작성해 보세요.

class Circle:
    type = "원"

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def showinfo(self):
        print(f"원 중심 : {self.x}, {self.y}")
        print(f"반지름 : {self.r}")
        print("둘레 길이 : %.3f" % (self.r * 2 * 3.14))
        print("면적 : %.1f" % (self.r ** 2 * 3.14))


print('도형의 타입 : %s' % (Circle.type))
print('-' * 20)

circle1 = Circle(3, 5, 10)
circle1.showinfo()
print( '-' * 20 )

circle2 = Circle(8, 6, 20)
circle2.showinfo()

# class Circle:
#     type = '원'
#     def __init__(self, xpos, ypos, radius):
#         self.xpos = xpos
#         self.ypos = ypos
#         self.radius = radius
#
#     def showinfo(self):
#         print('원 중심 : {}, {}'.format(self.xpos, self.ypos))
#         print('반지름 : {}'.format(self.radius))
#
#         area = 3.14 * self.radius ** 2
#         print('면적 : {}'.format(area))
#
# print('도형의 타입 : %s' % (Circle.type))
# print('-' * 20)
#
# circle1 = Circle(3, 5, 10)
# circle1.showinfo()
# print( '-' * 20 )
# circle2 = Circle(8, 6, 20)
# circle2.showinfo()