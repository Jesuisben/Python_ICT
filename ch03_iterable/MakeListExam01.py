coffee01 = ['아메리카노', '카페라떼', '에스프레스']
coffee02 = ['마키야또', '카페라떼']

mylist = coffee01 * 2
print(mylist)

coffees = coffee01 + coffee02
length = len(coffees)
print('요소 개수 : %d' % length)

# type() 함수는 데이터의 유형을 파악하기 위한 내장 함수입니다.
print(type(coffees))

coffees.append('바닐라라떼')
coffees.append('고구마라떼')

targetItem = '카페라떼'
idx = coffees.index(targetItem)
print('%s의 색인 위치 : %d' % (targetItem, idx))

# '카푸치노' 항목이 없으면, 2번째 요소에 추가해 보세요.
try:
    targetItem = '카푸치노'
    idx = coffees.index(targetItem)
    print('%s의 색인 위치 : %d' % (targetItem, idx))
except ValueError:
    print('리스트에 %s이(가) 없습니다.' % targetItem)
    coffees.insert(2, targetItem)

# 5번째 요소를 '콜드브루'로 변경해 보세요.
targetItem = '콜드브루'
coffees[5] = targetItem

targetItem = '카푸치노'
coffees.remove(targetItem)

idx = 3
what = coffees[idx]
print('%d 번째 요소 : %s' % (idx, what))

coffees.append('카페라떼')
coffees.append('카페라떼')
coffees.append('바닐라라떼')

targetItem = '카페라떼'
cnt = coffees.count(targetItem)
print('%s 품목의 개수 : %d' % (targetItem, cnt))

# Counter는 품목별 빈도 수가 높은 품목부터 정렬하여, 사전 형식으로 반환해 줍니다.
from collections import Counter
counter = Counter(coffees) # Counter 객체 생성
print(counter) # 빈도수 출력

print(coffees)