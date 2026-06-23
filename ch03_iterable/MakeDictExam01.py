# 사전 생성
coffees = dict() # {}

# "에스프레소"라는 키로 1000이라는 값을 coffees 사전에 집어 넣는다
coffees["에스프레소"] = 1000 # insert
coffees["에스프레소"] = 1500 # overwrite (키는 중복X여서 덮어쓰기가 됨)

coffees["카페라떼"] = 2000
coffees["카푸치노"] = 3000
coffees["마키야또"] = 4000

targetItem = "카페라떼"

# 해당 키가 coffees 사전에 존재하는지 알아보는 함수 in
bool_value = targetItem in coffees

if bool_value:
    print("%s 키가 있습니다." % targetItem)
else:
    print("%s 키가 없습니다." % targetItem)

targetItem = "핫초코"
bool_value = targetItem in coffees

# 자바에서는 논리 데이터를 부정하려면 "!"를 사용했는데
# 파이썬에서는 not을 사용함 (논리 데이터 앞에)
# 참고로 and(&&), or(||)
if not bool_value:
    coffees[targetItem] = 5000

# 키만 가져오기
print(coffees.keys())
# 값만 가져오기
print(coffees.values())

price = 6000
bool_value = price in coffees.values()

if bool_value:
    print("%d짜리 품목이 존재합니다." % price)
else:
    print("%d짜리 품목이 없어서 추가할께요." % price)
    coffees["아이스커피"] = price

# 리스트의 요소를 꺼내서 사전에 키로 넣고 그에 맞는 값을 설정해서 넣기 (반복문 사용)
listCoffee = ["바닐라라떼", "라벤더", "딸기라떼", "콜드브루"]
for idx in range(len(listCoffee)):
    coffees[listCoffee[idx]] = (idx + 7) * 1000

targetItem = "핫초코"
print("%s의 가격은 %d원입니다" % (targetItem, coffees[targetItem]))

targetList = ["라벤더", "우유커피"]

for key in targetList:
    try:
        price = coffees[key]
        message = "품명 : %s, 가격 : %d" % (key, price)
        print(message)
    except KeyError:
        print("%s 키가 존재하지 않아서, 신규 추가합니다." % key)
        coffees[key] = 5000

targetItem = "둥글레차"

# 자바의 map 컬렉션의 get() 함수와 같은 느낌
# get() : 사전에 있는 키로 값을 가져오는 함수
# get(key) : 해당 키가 없으면 None을 반환
# get(key, defaultValue) : 해당 키가 없으면 기본값을 반환함
# 해당 키가 없으면 기본값을 반환할뿐 사전에 그 키와 값이 들어가지는 않음
# (오류 안나게 하는 안전한 함수)
price = coffees.get(targetItem, 300)
message = "품명 : %s, 가격 : %d" % (targetItem, price)
print(message)

print(coffees)

# items() : 키와 값을 콤마를 구분자로 해서 반환함
# 지역 변수를 1개만 쓰면 그 변수에 튜플의 형태로 키와 값이 한쌍으로 묶여서 들어감
for (key, value) in coffees.items():
    message = "항목 %s의 단가는 %d원입니다." % (key, value)
    print(message)

# clear() : 사전의 내용을 비울때 사용하는 함수
coffees.clear()

print("요소 개수 : %d" % len(coffees))

# coffees = dict() # {}
#
# # 존재하지 않는 key는 신규 추가됩니다.
# coffees['에스프레소'] = 1000
#
# # 해당 키가 이미 존재하면 overwrite됩니다.
# coffees['에스프레소'] = 1500
#
# coffees['카페라떼'] = 2000
# coffees['카푸치노'] = 3000
# coffees['마키야또'] = 4000
#
# targetItem = '카페라떼'
#
# # in 연산자를 사용한 키 찾기
# bool = targetItem in coffees
#
# if bool:
#     print('%s키가 있습니다.' % targetItem)
# else:
#     print('%s키가 없습니다.' % targetItem)
#
# # '핫초코'가 있는지 확인하고, 없으면 5000원으로 추가해 보세요.
# targetItem = '핫초코'
# bool = targetItem in coffees
#
# # 힌트) 값을 부정하고자 할 때는 not 키워드를 사용하시면 됩니다.
# if not bool:
#     coffees[targetItem] = 5000
#
# print(coffees.keys())
#
# print(coffees.values())
#
# # 가격이 6000인 품목이 존재하는지 체크 하시고,
# # 존재하지 않으면, '아이스커피'를 6000원으로 추가하세요.
# price = 6000
# bool = price in coffees.values()
# if bool:
#     print('%d짜리 품목이 존재합니다.' % price)
# else:
#     print('품목이 존재하지 않아서 추가합니다.')
#     coffees['아이스커피'] = price
#
# listCoffee = ['바닐라라떼', '라벤더', '딸기라떼', '콜드브루']
#
# # 반복문을 사용하여 다음 항목을 추가합니다.
# for idx in range(len(listCoffee)):
#     coffees[listCoffee[idx]] = (idx + 7) * 1000
#
# targetItem = '핫초코'
# print('%s의 가격은 %d원입니다.' % (targetItem, coffees[targetItem]))
#
# # 다음 항목들을 반복하여, 해당 품목이 존재하면 가격 정보를 출력해주세요.
# # 존재하지 않으면 상품을 단가 5000원으로 추가해 보세요.
# targetList = ['라벤더', '우유커피']
#
# for key in targetList:
#     try:
#         price = coffees[key]
#         message = '품명 : %s, 가격 : %d' % (key, price)
#         print(message)
#     except KeyError:
#         print('\'%s\' 키가 존재하지 않아서, 신규 추가하겠습니다.' % key)
#         coffees[key] = 5000
#     # end try
# # end for
#
# # 해당 key가 존재하지 않으면, 기본 값으로 3000원을 출력해 보세요.
# targetItem = '둥글레차'
# price = coffees.get(targetItem, 3000)
# print('품명 : %s, 가격 : %d' % (targetItem, price))
#
# # 특정 요소를 제거하기
# targetItem = '아이스커피'
# popItem = coffees.pop(targetItem)
# print('제거된 \'%s\'의 이전 가격은 \'%s\'이었습니다.' % (targetItem, popItem))
#
# del coffees['에스프레소']
#
# for (key, value) in coffees.items():
#     message = '항목 %s의 단가는 %d원입니다.' % (key, value)
#     print(message)
# # end for
#
# # 전체 목록을 출력하되, 특정 품목별은 단가를 변경하여 출력해 보세요.
# # 500원 인상 : '카페라떼', '카푸치노'
# # 500원 인하 : '핫초코'
#
# print('전체 출력')
# for key in coffees.keys():
#     if key == '카페라떼' or key == '카푸치노':
#         coffees[key] += 500
#     elif key == '핫초코':
#         coffees[key] -= 500
#     else:
#         pass
#
#     message = '품명 : %s, 가격 : %d' % (key, coffees[key])
#     print(message)
# # end for
#
# coffees.clear()
#
# if len(coffees) == 0:
#     print('my dict is empty')
# else:
#     print('my dict is not empty')
# # end if
#
# print(type(coffees))
# print('요소 개수 : %d' % len(coffees))
# print(coffees)