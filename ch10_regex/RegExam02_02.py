import re

# 다음 리스트에 대하여 search 함수를 사용하여 id와 email 정보를 추출해 보세요.
# 골뱅이(@)의 위치를 찾고, resultch 객체에 대하여 start() 메소드를 적절히 사용하면 됩니다.

mailList = ['abc@naver.com', 'aaaa@daum.net']

regex = '@'
patterntern = re.compile(regex)

for item in mailList :
    result = patterntern.search(item)
    id = item[:result.start()]
    email = item[result.start() + 1:]
    print('아이디 : %s, 메일 종류 : %s' % (id, email))
# end for

# 다음 문자열에서 'worldcup'이라는 글자를 출력해 보되,
# 반드시 search() 함수의 반환 결과인 resultch 객체를 이용하면 풀어 보세요.

mystring01 = '2002 worldcup'

regex = '[a-z]+'
pattern = re.compile(regex)
result = pattern.search(mystring01)
print(type(result))

mystart = result.start()
myend = result.end()
mygroup = result.group()
myspan = result.span()

print('문자열 시작 인덱스 :', mystart)
print('문자열 끝작 인덱스 :', myend)
print('문자열 :', mygroup)
print('tuple 색인 :', myspan)

# 아이디 : abc, 메일 종류 : naver.com
# 아이디 : aaaa, 메일 종류 : daum.net
# <class 're.resultch'>
# 문자열 시작 인덱스 : 5
# 문자열 끝작 인덱스 : 13
# 문자열 : worldcup
# tuple 색인 : (5, 13)