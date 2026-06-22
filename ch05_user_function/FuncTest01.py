# FuncTest01.py
# 다음 연산을 수행하는 함수 func01()을 구현해 보세요.
# 2*su01 + 3*su02
# 3, 5 --> 21

def func01(first, second):
    return 2 * first + 3 * second
# end def

su01, su02 = 3, 5
result = func01(su01, su02)
print('su01 : %d' % (su01))
print('su02 : %d' % (su02))
print('결과 : %d' % (result))