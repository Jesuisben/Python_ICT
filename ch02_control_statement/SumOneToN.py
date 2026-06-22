number = int(input("정수 1개 입력 : "))

if number < 0:
    number = abs(number)

total = 0

for i in range(1, number + 1):
    total += i

print("1부터 %d까지의 총합은 %d입니다." % (number, total))

print("숫자 2개를 입력 받아서 사이에 있는 숫자 모두 더하기")
number01 = int(input("1번째 정수 입력 : "))
number02 = int(input("2번째 정수 입력 : "))

total = 0

for i in range(number01, number02 + 1):
    total += i

print("%d부터 %d까지의 총합은 %d입니다." % (number01, number02, total))

# su = int(input('정수 1개 입력 : '))
#
# if su < 0:
#     su = abs(su)
#
# total = 0
# for i in range(1, su + 1):
#     total += i
#
# message = '%d부터 %d까지의 총합은 %d입니다.'
# print(message % (1, su, total))
#
# print('숫자 2개를 입력 받아서 사이에 있는 숫자 모두 더하기')
# su01 = int(input('1번째 정수 입력 : '))
# su02 = int(input('2번째 정수 입력 : '))
#
# total = 0
# for i in range(su01, su02+1):
#     total += i
#
# message = '%d부터 %d까지의 총합은 %d입니다.'
# print(message % (su01, su02, total))
