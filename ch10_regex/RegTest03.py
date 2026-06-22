import re

print('findall 함수는 정규식과 매치되는 모든 문자열을 list 형식으로 반환해 줍니다.')
order_info = '오늘 커피가격은 아메리카노 3500원, 라테 4200원, 모카 4800원입니다.'

regex = '\d+'
pattern = re.compile(regex)
prices = pattern.findall(order_info)

print(type(prices))
print(prices)

# 날짜처럼 예시를 맞추기 위해 0000/00/00 형태로 출력하는 형식 유지
# 이번에는 가격을 "3500/4200/4800" 형태로 출력
message = prices[0] + '/' + prices[1] + '/' + prices[2]
print(message)


print('\n총 주문 수량 구하기')
order_qty = '아메리카노 2잔, 카페라테 3잔, 바닐라라테 1잔 주세요.'

regex = '\d+'
pattern = re.compile(regex)
qty_list = pattern.findall(order_qty)

total = 0
for qty in qty_list:
    total += int(qty)

print('총 주문 수량 : %d' % total)


print('\nb로 시작하는 커피 메뉴만 추출하여 정렬하기')
menu_list = '브루잉 brew 블랙 black 바닐라 vanilla 바닐라라테 latte 블루 blue'

regex = 'b[a-z]*'
pattern = re.compile(regex)
words = pattern.findall(menu_list)
words.sort()

print(words)


print('\nfinditer 함수는 결과물을 반복 가능한 객체 형식으로 반환해 줍니다.')
print('일반적으로 for 구문과 같이 사용됩니다.')

words_iter = pattern.finditer(menu_list)
for item in words_iter:
    print('객체 정보 :', item)
    print('문자열 :', item.group())
    print('색인 위치 tuple :', item.span())
    start = item.start()
    end = item.end()
    print('슬라이싱을 사용한 문자열 추출 :', menu_list[start:end])
# end for


print('\n커피 주문 수량 계산(finditer)')  
mycoffee = '에스프레소 1잔, 아메리카노 2잔, 카푸치노 3잔'

regex = '\d+'
pattern = re.compile(regex)

total = 0
orders = pattern.finditer(mycoffee)

for element in orders:
    total += int(element.group())

print('음료 총 주문 수량 : %d' % total)
