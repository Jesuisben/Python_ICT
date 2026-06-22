# SumTest.py
from OuterModule import mysum
su01, su02 = 3, 5

result = mysum(su01, su02)
print('더하기 : %d' % result)

print('모듈 %s가 종료되었습니다.' % __name__)