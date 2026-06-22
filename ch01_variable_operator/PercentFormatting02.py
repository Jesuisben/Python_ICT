name = '김철수'
fruit = '사과'
gaesu = 8

myformat = '%s이(가) %s를 %d개 먹었습니다.'
print(myformat % (name, fruit, gaesu))

su01 = 4
su02 = 9
result = su01 * su02
print('%d 곱하기 %d는 %d입니다.' % (su01, su02, result))

a = 2.0
b = 3.0
# pow(a, b)는 a의 b제곱을 해주는 내장 함수입니다.
# 내장 함수 : 파이썬에서 미리 만들어 놓은 함수
result = pow(a, b) # a ** b
print('%f의 %f 제곱은 %f입니다.' % (a, b, result))

print('%f는 기본으로 소수점 6자리까지 보여 줍니다.')
print('%를 표현하려면 %%를 표시해야 합니다.')
rate = 0.4567
# %f의 기본값은 소수점 아래 6자리까지 보여줌 -> %.6f (c언어에 의해서)
# %라는 기호를 문자열 안에 넣을때 %%로 해서 넣음
# 역슬래쉬 넣는 느낌 \\ -> \
print('비율 : %f%%' % (100*rate))