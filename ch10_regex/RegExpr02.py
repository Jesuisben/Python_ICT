import re
# RegExpr02.py
# match() 함수와 search() 함수를 비교해 봅니다.

mystring = '삼일절은 1919년도에 발생하였습니다.'

regex = '\d+'
pattern = re.compile(regex)

result = pattern.match(mystring)
print('match 함수는 문자열의 처음부터 체크합니다.')
print('match 결과 : %s' % result)

result = pattern.search(mystring)
print('search 함수는 임의의 위치에 부합하는 데이터가 있으면 출력해 줍니다.')
print('search 결과 : %s' % result)
print(type(result))

print('a부터 c사이의 문자열로 시작하는 데이터 찾기')
mylist01 = ['abc123', 'dab456']
regex = '[a-c]+'
pattern = re.compile(regex)

print('match 함수 결과')
for item in mylist01:
    if pattern.match(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)
# end for

print('search 함수 결과')
print('문자열에 \'abc\' 중 하나라도 포함되어 있으면 무조건 True입니다.')
for item in mylist01:
    if pattern.search(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)
# end for