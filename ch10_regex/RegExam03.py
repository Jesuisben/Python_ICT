import re

print('findall 함수는 정규식과 매치되는 모든 문자열을 list 형식으로 반환해 줍니다.')
mystring01 = '삼일절은 1919년 3월 1일입니다.'
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.findall(mystring01)
print(result)
message = '삼일절 : %s년 %s월 %s일' % (result[0], result[1].zfill(2), result[2].zfill(2))
print(message)

print('\n총 구매 수량 구하기')
mystring02 = '사과 5개, 밤 3개, 배 4개만 주문할께요'
regEx = '\d+'
pattern = re.compile(regEx)
quantity = pattern.findall(mystring02)

total = 0
for qty in quantity:
    total += int(qty)

print(f'총 구매 수량 : {total}개')

print('\nb로 시작하는 단어들만 추출하기')
mystring03 = 'blow block 1234 peace blame 5678 blood'
regEx = 'b[a-z]*'
pattern = re.compile(regEx)
words = pattern.findall(mystring03)
words.sort()
print(words)

print('\nfinditer 함수는 결과물을 반복이 가능한 개체 형식으로 반환해 줍니다.')
print('일반적으로 for 구문과 같이 사용합니다.')
words = pattern.finditer(mystring03)
for item in words:
    print('객체 정보 :', item)
    print('문자열 정보 :', item.group())
    print('색인 위치 tuple :', item.span())
    start, end = item.start(), item.end()
    print('슬라이싱을 사용한 문자열 추출 :', mystring03[start:end])
    print()
# end for

mystring04 = '아메리카노 2잔, 카페라떼 4잔'
regEx = '\d+'
pattern = re.compile(regEx)
coffees = pattern.finditer(mystring04)

total = 0
for element in coffees:
    total += int(element.group())
print(f'음료 구매 수량 : {total}')