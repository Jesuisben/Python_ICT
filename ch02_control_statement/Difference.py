sumA, sumB = 0, 0

for i in range(1, 51):
    if i % 3 == 0:
        sumB += i
    else:
        sumA += i
# end for

print('3의 배수의 총합 : %d' % sumA)
print('3의 배수가 아닌 정수의 총합 : %d' % sumB)
print('차이 : %d' % (sumA - sumB))