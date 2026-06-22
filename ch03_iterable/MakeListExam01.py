# 리스트 생성
coffee01 = ['아메리카노', '카페라떼', '에스프레스']
coffee02 = ['마키야또', '카페라떼']

# type() : 해당 데이터의 타입을 볼 수 있는 함수
print(type(coffee01))

# 리스트를 곱하기 2하면 요소 개수가 순서대로 2배인 리스트가 됨
mylist = coffee01 * 2
print(mylist)

# 리스트끼리 더하면 요소가 합쳐진 리스트가 됨
coffee = coffee01 + coffee02
print(coffee)
length = len(coffee)
print("요소 개수 : %d" % length)

# 리스트에 요소 추가하는 법 (뒤에 추가)
coffee.append("바닐라라떼")
coffee.append("고구마라떼")
print(coffee)

# 리스트의 요소를 문자열로 추출하는 법
targetItem = "카페라떼"
idx = coffee.index(targetItem)
print("%s의 색인 위치 : %d" % (targetItem, idx))

# try / except 문 (자바의 예외처리 같은 것)
try:  # "카푸치노"가 해당 리스트에 없어서 오류가 남 (ValueError)
    targetItem = "카푸치노"
    idx = coffee.index(targetItem)
    print("%s의 색인 위치 : %d" % (targetItem, idx))
except ValueError:
    print("리스트에 %s이(가) 존재하지 않습니다." % targetItem)
    # insert(숫자, 요소) : 리스트에서 원하는 인덱스에 원하는 요소를 넣을 수 있는 함수
    coffee.insert(2, targetItem)  # 해당 숫자인 인덱스에 요소를 추가함

# 리스트의 인덱스를 이용해서 요소의 값 바꾸기
# 쓰기 기능
coffee[5] = "콜드브루"

# 리스트의 요소인 문자열을 이용해서 요소를 제거하기 (인덱스 몰라도 됨)
coffee.remove("카푸치노")

coffee.append("카페라떼")
coffee.append("카페라떼")
coffee.append("바닐라라떼")

cnt = coffee.count("카페라떼")
print("%s 품목의 갯수 : %d" % ("카페라떼", cnt))

print(coffee)

# 항목별 빈도 숫자를 구할 수 있는 Counter
# 그냥 import Counter가 아니고 from collections import Counter인 이유 :
# Counter는 독립 모듈이 아니라 collections 모듈 안에 있는 클래스여서 이렇게 import함
from collections import Counter

counter = Counter(coffee)
print(counter)

# coffee01 = ['아메리카노', '카페라떼', '에스프레스']
# coffee02 = ['마키야또', '카페라떼']
# mylist = coffee01 * 2
# print(mylist)
#
# coffees = coffee01 + coffee02
# length = len(coffees)
# print('요소 개수 : %d' % length)
#
# # type() 함수는 데이터의 유형을 파악하기 위한 내장 함수입니다.
# print(type(coffees))
#
# coffees.append('바닐라라떼')
# coffees.append('고구마라떼')
#
# targetItem = '카페라떼'
# idx = coffees.index(targetItem)
# print('%s의 색인 위치 : %d' % (targetItem, idx))
#
# # '카푸치노' 항목이 없으면, 2번째 요소에 추가해 보세요.
# try:
#     targetItem = '카푸치노'
#     idx = coffees.index(targetItem)
#     print('%s의 색인 위치 : %d' % (targetItem, idx))
# except ValueError:
#     print('리스트에 %s이(가) 없습니다.' % targetItem)
#     coffees.insert(2, targetItem)
#
# # 5번째 요소를 '콜드브루'로 변경해 보세요.
# targetItem = '콜드브루'
# coffees[5] = targetItem
#
# targetItem = '카푸치노'
# coffees.remove(targetItem)
#
# idx = 3
# what = coffees[idx]
# print('%d 번째 요소 : %s' % (idx, what))
#
# coffees.append('카페라떼')
# coffees.append('카페라떼')
# coffees.append('바닐라라떼')
#
# targetItem = '카페라떼'
# cnt = coffees.count(targetItem)
# print('%s 품목의 개수 : %d' % (targetItem, cnt))
#
# # Counter는 품목별 빈도 수가 높은 품목부터 정렬하여, 사전 형식으로 반환해 줍니다.
# from collections import Counter
# counter = Counter(coffees) # Counter 객체 생성
# print(counter) # 빈도수 출력
#
# print(coffees)
