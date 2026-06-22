# end=''으로 인하여 엔터키를 누르지 않는 효과입니다.
print('이름 입력 : ', end='')
name = input()

# input() 함수는 문자열을 입력 받을 때 사용합니다.
# 함수의 매개 변수를 프롬프트(prompt)라고 부릅니다.
# input() 함수의 반환 값은 문자열입니다.
# 숫자로 다룰려면 형변환이 필요합니다.
age = input('나이 입력 : ')
age = int(age) # 문자열을 숫자로 변환
height = float(input('키 입력 : ')) # 실수 타입으로 변환

print('\n% 포맷 코드 형식으로 출력')
print('이름 : %s' % name)
print('나이 : %d' % age)
print('키 : %.2f' % height)

print('\nformat() 함수를 사용한 출력')
message = '제 이름은 {}이고, 나이는 {}세 입니다.\n제 키는 {}cm입니다.'
print(message.format(name, age, height))