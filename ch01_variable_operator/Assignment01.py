# 복합 대입/할당 연산자
x = 5
print('x = %d' % (x))

x += 3 # x = x + 3
print('x = %d' % (x))

x *= 4
print('x = %d' % (x))

x //= 7
print('x = %d' % (x))

x *= 10
print('x = %d' % (x))

x /= 3
print('x = %d' % (x))

# 1부터 10까지의 합을 복합 대입 연산자를 이용하여 풀어 보세요.
# 2개 이상의 구문을 한줄에 작성하려면 세미 콜론을 이용합니다.
total = 0
total += 1; total += 2; total += 3
total += 4; total += 5; total += 6
total += 7; total += 8; total += 9
total += 10
print('총합 = %d' % (total))