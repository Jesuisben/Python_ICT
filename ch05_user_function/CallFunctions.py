def square(x):
    result = x ** 2
    print('%d의 제곱 값은 %d입니다.' % (x, result))
    return result

def jegob(su1, su2):
    result = square(su1) + square(su2)
    return result

def max(su1, su2):
    result = 0
    if su1 >= su2 :
        result = su1
    else:
        result = su2
    print('%d와(과) %d 중에서 큰 수는 %d입니다.' % (su1, su2, result))
    return result

def sub(su1, su2):
    result = su1 - su2
    print('%d와(과) %d의 뺄셈을 연산합니다.' % (su1, su2))
    print('결과 :', result)

su01, su02 = 5, 7
newsu1 = jegob(su01, su02)
newsu2 = max(su01, su02)
sub(newsu1, newsu2)