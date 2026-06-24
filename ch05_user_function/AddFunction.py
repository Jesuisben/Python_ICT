# 사용자 정의 함수
def add(first, second=50) :
    return first + second

su01 = 14
su02 = 5
# positional argument : 위치 기반 매개 변수 (위치 기반 인수)
# -> 함수를 호출 할때 순서(위치)로 매개변수를 구분하는 방식
result = add(su01, su02)
print(result)
print(add(100, 200))

# positional argument + keyword argument
# 2개의 방식을 섞을때는 반드시 positional argument가 먼저 나와야 함
print(add(100, second=200))

# 다중 할당
su01, su02 = 111, 222
# keyword argument : 키워드 기반 매개 변수 (키워드 인수)
# 키워드 기반이기에 매개변수 순서가 바뀌어도 값이 같음
# 매개변수 이름을 모를때는 ()안에서 Ctrl + Space하면 보임
result = add(second=su01, first=su02)
print(result)

# TypeError: add() missing 1 required positional argument: 'second'
# 필수(required) 매개변수(argument)인 'second'가 없다는 경고문
result = add(10)
print(result)

# # AddFunction.py
# # 정수 2개를 이용하여 합을 구해주는 함수 add를 작성해 보세요.
#
# # def는 define의 줄인 말로 함수 정의시 사용합니다.
# # def는 define의 줄인 말
# # def 함수이름(매개변수01 = [기본값], 매개변수02, ...) :
# # 매개변수 : argument, parameter, 인자, 인수 등등
# def add(first, second = 50): # 함수 정의
#     return first + second
# # end def
#
# su01 = 14
# su02 = 5
#
# # positional argument : index 기반으로 매개 변수 전달 방식
# result = add(su01, su02)
# print('%d + %d = %d' % (su01, su02, result))
#
# print('%d + %d = %d' % (100, 200, add(100, 200)))
#
# su01 = 111
# su02 = 222
#
# # keyword argument : 키워드 기반으로 매개 변수 전달 방식
# result = add(second=su01, first=su02)
# print('%d + %d = %d' % (su02, su01, result))
#
# # positional 방식과 keyword 방식이 혼재
# result = add(su01, second=su02)
# print('%d + %d = %d' % (su01, su02, result))
#
# # 기본 값 사용하기
# result = add(10)
# print('%d' % (result))