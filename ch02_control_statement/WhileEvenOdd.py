# odd : 홀수 / even : 짝수
odd = 0
even = 0

i = 1

while i < 11 :
    if i % 2 != 0 :
        odd += i
    else:
        even += i
    i += 1

print("홀수의 총합 : %d" % odd)
print("짝수의 총합 : %d" % even)

# odd, even = 0, 0
#
# i = 1
# while i < 11:
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
#     i += 1
#
# print("홀수의 총합 : %d" % odd)
# print("짝수의 총합 : %d" % even)
