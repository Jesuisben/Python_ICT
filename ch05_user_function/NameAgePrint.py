# NameAgePrint.py
# 이름과 나이를 입력 받아서 신상 정보를 출력해 주는 함수 namePrint()를 구현해 보세요.

def namePrint(name, age):
    message = '\'{}\'님의 나이는 {}세입니다.'.format(name, age)
    print(message)
# end def

name = '이재욱'
age = 30
result = namePrint(name, age)
print(type(result))
print(result)

if result == None:
    print('값을 반환하지 않음')# negative
else:
    print('값을 반환함') # positive