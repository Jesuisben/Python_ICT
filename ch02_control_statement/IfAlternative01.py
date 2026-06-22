# 단순 if 구문, 양자 택일 if 구문
# 홀수이면 출력하고, 짝수이면 무시하세요.
su = 5
if su % 2 == 1:
    print('%d는(은) 홀수입니다.' % su)

if su % 2 == 0:
    print('%d is even number' % su)
else:
    print('%d is odd number' % su)

print('이 구문은 무조건 실행됩니다.')