import re

print('match 함수와 search 함수의 차이점에 대하여 살펴 봅니다.')
mystring = '오늘은 2025년 11월입니다.'
# \d : [0-9]와 동일한 표현식
# + : {1,}와 동일한 표현식
regEx = '\d+' # 숫자가 1개 이상이어야 되....
pattern = re.compile(regEx)

# match() : 문자열 처음부터 체크 / 반환 : match 객체
# (문자열 처음에는 없고 중간에 정규 표현식에 맞는 문자가 있으면 반환 못함)
result = pattern.match(mystring)
print('match 함수는 문자열의 처음부터 체크합니다.')
print('match 결과 : %s' % result)

# search() : 문자열 전체 체크 후 그 중 정규 표현식에 맞는 문자가 처음 나오는 부분을 체크 / 반환 : match 객체
# (문자열 처음에는 없고 중간에 정규 표현식에 맞는 문자가 있으면 그 문자를 반환함)
# But! 정규 표현식에 ^나 $가 있으면 처음이나 마지막을 강요하게 되어서 search()가 사실상 무의미?해짐
# span=(4, 8) : 인덱스 번호 4~7까지의 문자가
# match='2025' : 정규 표현식에 맞는 문자이고 그 값은 '2025'이다.
result = pattern.search(mystring)
print('search 함수는 임의의 위치에서 조건에 맞으면 출력해 줍니다.')
print('search 결과 : %s' % result)

print('\n특정 문자로 시작하는 데이터 찾기')
mylist01 = ['hello123', 'world99', 'archive']
# 정규 표현식 : h로 시작하고 h 뒤에 알파벳이 있는 항목들
regEx = 'h[a-z]*'
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

# re.Match 타입의 메소드
# start() : 매칭된 문자열의 시작 인덱스 반환
# end()   : 매칭된 문자열의 끝 인덱스 반환 (해당 끝 인덱스는 미포함)
# group() : 매칭된 문자열을 반환
# span()  : 매칭된 문자열의 (시작, 끝) 인덱스를 tuple로 반환
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
# '\d\S*' : 처음 숫자가 나온 이후 눈에 보이는 문자 모든 것 (search() 사용한다는 전제하에)
# ex) ('강원강릉시강변로410번길36'); -> 410번길36');
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