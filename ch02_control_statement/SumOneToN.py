su = int(input('정수 1개 입력 : '))

if su < 0:
    su = abs(su)

total = 0
for i in range(1, su + 1):
    total += i

message = '%d부터 %d까지의 총합은 %d입니다.'
print(message % (1, su, total))

print('숫자 2개를 입력 받아서 사이에 있는 숫자 모두 더하기')
su01 = int(input('1번째 정수 입력 : '))
su02 = int(input('2번째 정수 입력 : '))

total = 0
for i in range(su01, su02+1):
    total += i

message = '%d부터 %d까지의 총합은 %d입니다.'
print(message % (su01, su02, total))