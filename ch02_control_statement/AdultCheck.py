'''
이름과 나이와 성별(숫자 1개)을 입력 받아서 출력하는 프로그램을 만들어 보세요.
성별은 숫자 1,2,3,4 중에서 1개를 입력 받습니다.
성인 판별은 나이가 19이상으로 판단합니다.
'''
name = input('이름 입력 : ')
age = int(input('나이 입력 : '))
_gender = int(input('성별 입력(숫자 1,2,3,4 중 택일) : '))

if age >= 19:
    adult = '성인'
else:
    adult = '미성년자'

if _gender == 1 or _gender == 3:
    gender = '남자'
else:
    gender = '여자'

print('이름 : %s' % name)
print('나이 : %d' % age)
print('성인 여부 : %s' % adult)
print('성별 : %s' % gender)