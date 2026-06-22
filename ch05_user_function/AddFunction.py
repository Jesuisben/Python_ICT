# AddFunction.py
# 정수 2개를 이용하여 합을 구해주는 함수 add를 작성해 보세요.

# def는 define의 줄인 말로 함수 정의시 사용합니다.
# def는 define의 줄인 말
# def 함수이름(매개변수01 = [기본값], 매개변수02, ...) :
# 매개변수 : argument, parameter, 인자, 인수 등등
def add(first, second = 50): # 함수 정의
    return first + second
# end def

su01 = 14
su02 = 5

# positional argument : index 기반으로 매개 변수 전달 방식
result = add(su01, su02)
print('%d + %d = %d' % (su01, su02, result))

print('%d + %d = %d' % (100, 200, add(100, 200)))

su01 = 111
su02 = 222

# keyword argument : 키워드 기반으로 매개 변수 전달 방식
result = add(second=su01, first=su02)
print('%d + %d = %d' % (su02, su01, result))

# positional 방식과 keyword 방식이 혼재
result = add(su01, second=su02)
print('%d + %d = %d' % (su01, su02, result))

# 기본 값 사용하기
result = add(10)
print('%d' % (result))