# 출력 결과
"""
큰 수를 출력하세요.
큰 수 : 8
y가 짝수이면 3 더한 값을, 홀수이면 제곱 수를 출력하세요.
결과 01 : 25
x가 y의 약수이면 'yes', 아니면 'no'를 출력하세요.
6가 12의 약수인가요? yes
"""

# 조건 변환식 사용하기
x = 8
y = 5

# result = truepart if 조건식 else falsepart
print('큰 수를 출력하세요.')
# if 오른쪽이 조건식 / 참이면 if 왼쪽 실행 / 거짓이면 else 오른쪽 실행
result = x if x > y else y
print('큰 수 : %d' % result)

print('y가 짝수이면 3 더한 값을, 홀수이면 제곱 수를 출력하세요.')
result = y+3 if y % 2 == 0 else y**2
print('결과 01 : %d' % result)

x = 6
y = 12
print('x가 y의 약수이면 \'yes\', 아니면 \'no\'를 출력하세요.')
result = 'yes' if y % x == 0 else 'no'
print('%d가 %d의 약수인가요? %s' % (x, y, result))