# format() 함수 다뤄보기
# 문자열(string)에는 format()이라는 함수가 있음

coffee = 3 # 판매가 가능한 커피 잔수
price = 2000 # 단가

# {}안에 들어가는 내용은 치환될 어떠한 것
# format() 함수의 매개변수가 출력될때 {}안에 들어가게 됨
message = '우리 매장에서는 커피 {}잔이 판매 가능합니다.'
print(message)
print(message.format(coffee))

message = '커피 1잔의 가격은 {}입니다.'
print(message.format(price))

# {} 기호에는 암시적으로 숫자 0번부터 매겨 집니다.
# format 함수의 매개변수의 순서에 따라서 {}안에 들어가서 치환되는 것도 순서대로임
message = '커피 {}잔, 단가 : {}'
print(message.format(coffee, price))

# 순서대로 넣지 말고 직접 format 함수의 매개변수의 순서(숫자)를 이용해서 치환에 써보기
# {}안에 숫자를 넣으면 format 함수의 매개변수의 순서에 맞는 숫자가 들어가게 됨
message = '커피 {0}잔, 단가 : {1}'
print(message.format(coffee, price)) # 0번은 coffee, 1번은 price

# 응용
message = '커피 {1}잔, 단가 : {0}'
print(message.format(price, coffee))

money = 5000 # 입금액
print('{}원을 입금하였습니다.'.format(money))

change = money - price # 잔돈
message = '거스름돈 : {}, 판매 : {}잔'
print(message.format(change, 1))

coffee = coffee - 1 # 남은 잔
message = '남은 커피는 {}잔입니다.'
print(message.format(coffee))