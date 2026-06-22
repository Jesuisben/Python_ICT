total = 0

for i in range(1, 3):
    for k in range(5, 8):
        total += i + k

print('총합 01 : %d' % total)

total = 0
for i in range(1, 4, 2):
    for k in range(2, 6, 3):
        total += 2 * i + k

print('총합 02 : %d' % total)
