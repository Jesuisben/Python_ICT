import re
# RegExpr04.py

print('findall 함수는 정규식과 매치되는 모둔 문자열을 list 형식으로 반환해 줍니다.')
mystring01 = '삼일절은 1919년 3월 1일입니다.'

regex = '\d+'
pattern = re.compile(regex)
result = pattern.findall(mystring01)
print(type(result))
print(result)
message = result[0] + '/' + result[1].zfill(2) + '/' + result[2].zfill(2)
print(message)

print('총 구매 수량 구하기')
mystring02 = '사과 3개, 밤 5개, 배 4개만 주문할께요.'

regex = '\d+'
pattern = re.compile(regex)
fruits = pattern.findall(mystring02)

total = 0
for qty in fruits:
    total += int(qty)

print('총 구매 수량 : %d' % total)

print('b로 시작하는 단어들만 추출하여 정렬하기')
mystring03 = 'blow block 1234 peace blame 5678 blood'

regex = 'b[a-z]*'
pattern = re.compile(regex)
words = pattern.findall(mystring03)
words.sort()
print(words)

print('finditer 함수는 결과물을 반복이 가능한 개체 형식으로 반환해 줍니다.')
print('일반적으로 for 구문과 같이 사용됩니다.')
words = pattern.finditer(mystring03)
for item in words:
    print('객체 정보 :', item)
    print('문자열:', item.group())
    print('색인 위치 tuple :', item.span())
    start = item.start()
    end = item.end()
    print('슬라이싱을 사용한 문자열 추출 :', mystring03[start:end])
# end for

mystring04 = '아메리카노 2잔, 카페라테 4잔'
regex = '\d+'
pattern = re.compile(regex)

total = 0
coffees = pattern.finditer(mystring04)
for element in coffees:
    total += int(element.group())

print('음료 구매 수량 : %d' % total)