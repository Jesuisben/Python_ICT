# 사각형의 둘레와 넓이 및 대각선 길이 구하기
import math # 수학과 관련된 모듈

width = 10.0
height = 5.0
area = width * height
perimeter = 2.0 * (width + height)

# ** 기호는 거듭 제곱 연산자입니다.
diagonal = math.sqrt(width*width + height ** 2)

print('너비 : ' + str(width))
print('높이 : ' + str(height))
print('사각형의 넓이 : ' + str(area))
print('사각형의 둘레 : ' + str(perimeter))
print('대각선 길이 : ' + str(diagonal))
