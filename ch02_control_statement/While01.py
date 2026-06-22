# 1부터 10까지의 총합 구하기
total = 0
i = 1
while i < 11:
    total += i
    i += 1

print('총합01 : %d' % total)

# 1 + 4 + 7 + ... + 100 = 1717
total = 0
i = 1
while i < 101:
    total += i
    i += 3

print('총합02 : %d' % total)

# 1*1 + 6*6 + 11*11 + ... + 96*96 = 63670
total = 0
i = 1
while i < 96+1:
    total += i**2
    i += 5

print('총합03 : %d' % total)

# 1*2 + 2*3 + 3*4 + 4*5 + 5*6 = 70
total = 0
i = 1
while i < 5+1:
    total += i*(i+1)
    i += 1

print('총합04 : %d' % total)