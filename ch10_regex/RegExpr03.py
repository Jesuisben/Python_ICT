import re
# RegExpr03.py

print('match 함수의 반환 결과는 Match 객체입니다.')
print('Match 객체에는 색인의 위치나 문자열 정보를 위한 여러 메소드들이 제공됩니다.')

mystring = 'python'

regex = '[a-z]+' # 알파벳이 1번 이상 출현
pattern = re.compile(regex)

result = pattern.match(mystring)
print(type(result))
print(result)
print('문자열 시작 인덱스 : [%d]' % result.start())
print('문자열 끝 인덱스 : [%s]' % result.end())
print('문자열 위치 tuple 정보 : ', result.span())
print('매치된 문자열 정보 : [%s]' % result.group())

# 다음 예시는 숫자부터 시작하므로 search 함수를 적용해야 합니다.
mystring = '2002 python'
regex = '[a-z]+'
pattern = re.compile(regex)

result = pattern.search(mystring)
print(type(result))
print(result)
print('문자열 시작 인덱스 : [%d]' % result.start())
print('문자열 끝 인덱스 : [%s]' % result.end())
print('문자열 위치 tuple 정보 : ', result.span())
print('매치된 문자열 정보 : [%s]' % result.group())