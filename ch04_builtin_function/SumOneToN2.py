# 1) 요구 사항
# 정수 2개를 입력 받아서 두 수를 포함하고 사이의 모든 수를 덧셈하는 프로그램을 만들어 보세요.
# 앞 자리 수가 뒷자리 수보다 값이 큰 경우 swap 기법을 사용하여 두 변수의 값을 서로 바꾸어 주세요.
# swap 힌트) a, b = b, a
# 단, 음수가 입력이 되는 경우는 절대값으로 변경하여 풀어 보도록 합니다
#
# 2) 출력 결과
# 1번째 정수 입력 : 3
# 2번째 정수 입력 : 5
# 3부터 5까지의 총합은 12입니다.

num1 = int(input("1번째 정수 입력 : "))
num2 = int(input("2번째 정수 입력 : "))

if num1 < 0 :
    num1 = abs(num1)
if num2 < 0 :
    num2 = abs(num2)
if num2 < num1 :
    # swap 이용하기
    num1, num2 = num2, num1

total = 0
for i in range(num1, num2 + 1):
    total += i

print(f"{num1}부터 {num2}까지의 총합은 {total}입니다.")