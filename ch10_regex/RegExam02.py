import re

print('match 함수와 search 함수의 차이점에 대하여 살펴 봅니다.')
mystring = '오늘은 2025년 11월입니다.'
regEx = '\d+' # 숫자가 1개 이상이어야 되....
pattern = re.compile(regEx)

result = pattern.match(mystring)
print('match 함수는 문자열의 처음부터 체크합니다.')
print('match 결과 : %s' % result)

result = pattern.search(mystring)
print('search 함수는 임의의 위치에서 조건에 맞으면 출력해 줍니다.')
print('search 결과 : %s' % result)

print('\n특정 문자로 시작하는 데이터 찾기')
mylist01 = ['hello123', 'world99']
regEx = '^h[a-z]*' # h로 시작하는 항목들
pattern = re.compile(regEx)

print('match 함수 실행 결과')
for item in mylist01:
    if pattern.match(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)

print('search 함수 실행 결과')
for item in mylist01:
    if pattern.search(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)

print('match 함수와 search 함수의 실행 결과는 동일합니다.')

print('\nmatch 함수의 반환 결과는 Match 객체입니다.')
print('Match 객체는 색인의 위치나 문자열 정보를 위한 여러 개의 메소드가 존재합니다.')
mystring = 'python1234'
regEx = '[a-z]+' # 알파벳 소문자가 1번 이상 나오기
pattern = re.compile(regEx)
result = pattern.match(mystring)
print(type(result))

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {mystring[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')

print('\nsearch 함수의 반환 결과 역시 Match 객체입니다.')
yourstring = '2026 worldcup'
regEx = '[a-z]+' # 알파벳 소문자가 1번 이상 나오기
pattern = re.compile(regEx)
result = pattern.search(yourstring)
print(type(result))

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {yourstring[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')

addressList = ["('강원원주시웅비2길8');",
          "('강원도철원군서면와수로181번길7-16');",
          "('강원평창군봉평면태기로68');",
          "('강원강릉시강변로410번길36');"]

print('방법01')
regEx = '\d\S*' # 숫자로 시작한 이후에 white character 문자가 아닌것 들...
pattern = re.compile(regEx)
for address in addressList:
    mymatch = pattern.search(address)
    print(mymatch.group().replace("');", ""))
# end for

print('\n방법02')
regEx = "\d\S*\'" # 숫자로 시작한 이후에 외따옴표까지 ...
pattern = re.compile(regEx)
for address in addressList:
    mymatch = pattern.search(address)
    print(mymatch.group().rstrip("\'")) # 우측 외따옴표 지우기
# end for


