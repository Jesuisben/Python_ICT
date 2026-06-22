# 1부터 10까지의 총합 구하기
# range(from, to, step) : from부터 (to-1)까지 step씩 증가하면서 연속된 숫자를 발생 시켜 주는 함수
# from은 0을 step은 1을 기본 값으로 가지고 있습니다.

total = 0
for i in range(1, 11): # 1부터 11직전까지
    total += i

print('총합01 : %d' % total)

# 1 + 4 + 7 + ... + 100 = 1717
total = 0
for i in range(1, 101, 3):
    total += i

print('총합02 : %d' % total)

# 97 + 92 + 87 + ... + 7  + 2 = 990
total = 0
for i in range(97, 1, -5):
    total += i

print('총합03 : %d' % total)

# 1*1 + 6*6 + 11*11 + ... + 96*96 = 63670
total = 0
for i in range(1, 96+1, 5):
    total += i**2

print('총합04 : %d' % total)

# 1*2 + 2*3 + 3*4 + 4*5 + 5*6 = 70
total = 0
for i in range(1, 5+1):
    total += i*(i+1)

print('총합05 : %d' % total)