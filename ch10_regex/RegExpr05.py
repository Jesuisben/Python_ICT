import re
# RegExpr05.py
print('split 함수는 명시된 정규식으로 데이터를 분리해주는 함수입니다.')
mystring01 = '사과 오렌지:감,밤'
regex = '[:, ]' # 대괄호 내의 모든 문자를 구분자로 사용해 주세요.
pattern = re.compile(regex)
result = pattern.split(mystring01)
print(type(result))
print(result)

print('sub 함수는 주어진 패턴과 일치하는 문자열을 변경해 줍니다.')
print('\'-\' 문자을 \'/\'으로 변경합니다.')
mystring02 = '광복절 : 1945-08-15'
regex = '-'
pattern = re.compile(regex)
result = pattern.sub('/', mystring02)
print(result)

print('subn 함수는 주어진 패턴과 일치하는 문자열을 n개만 변경해 줍니다.')
print('반환 타입은 tuple입니다.')
print('subn 함수의 n은 정수를 의미합니다.')
mystring03 = '01-02-03-04-05'
regex = '-'
pattern = re.compile(regex)

for idx in range(1, 5):
    result = pattern.subn('/', mystring03, count=idx)
    # print(type(result)) # tuple
    print(result)
# end for
