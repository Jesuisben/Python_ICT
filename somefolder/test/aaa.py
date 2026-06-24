# 방법 1: 모듈까지 import
import somefolder.mymath.MathModule

result = somefolder.mymath.MathModule.square_root(5)
print(result)

result = somefolder.mymath.MathModule.jegob(2, 3)
print(result)


# 방법 2: 함수 직접 import
# # 1) 함수 하나하나 import
# from somefolder.mymath.MathModule import square_root
# from somefolder.mymath.MathModule import jegob

# 2) 함수 한번에 import
from somefolder.mymath.MathModule import square_root, jegob

# # 3) 함수 전체 import
# from somefolder.mymath.MathModule import *

result = square_root(3)
print(result)

result = jegob(4, 5)
print(result)


# 방법 3 : 모듈을 별칭으로 import
import somefolder.mymath.MathModule as asdf

result = asdf.square_root(9)
print(result)