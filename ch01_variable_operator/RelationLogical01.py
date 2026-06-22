# 관계 논리 연산자
print('관계 연산자')
a, b = 10, 20
print('a = %d, b = %d' % (a, b))
print('a >= b : %s' % (a >= b))
print('a <= b : %s' % (a <= b))
print('a > b : %s' % (a > b))
print('a < b : %s' % (a < b))
print('a == b : %s' % (a == b))
print('a != b : %s' % (a != b))

print('논리 연산자')
logical01 = a >= b
logical02 = a != b
logical03 = a == b
print('logical01 : %s' % logical01)
print('logical02 : %s' % logical02)
print('logical03 : %s' % logical03)

# python(java) : and(&&), or(||), not(!)
print('logical01 and logical02 : %s' % (logical01 and logical02))
print('logical01 or logical02 : %s' % (logical01 or logical02))
print('not logical01 : %s' % (not logical01)) # 진위값 부호 반전하기

# 연산자 우선 순위 : not > and > or
#                  3번째(or)    2번째(and) 1번째(not)
result = logical01 or logical02 and not logical03
print('result : %s' % result)

# '거짓'은 정수 값 0으로, '참'은 1로 변환이 됩니다.
su01, su02 = int(True), int(False)
print('su01 : %d, su02 : %d' % (su01, su02))

mylist = [logical01, logical02, logical03]
print(mylist)

total = sum(mylist) # sum 함수는 총합을 구해 주는 내장 함수
print('참 갯수 : %d' % total)

# len 함수는 요소의 개수를 반환해주는 내장 함수
average = total / len(mylist)
print('평균 : %.3f' % average)

print('문자열 비교')
print('\'hello\' > \'world\' : %s' % ('hello' > 'world'))