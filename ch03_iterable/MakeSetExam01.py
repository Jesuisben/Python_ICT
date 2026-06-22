coffees = set()

print('자료형 타입 : ', end='')
print(type(coffees))

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노')

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

newItems = ['콜드브루', '고구마라떼', '디카페인커피']
coffees.update(newItems)

# 집합은 순서가 없으므로, 인덱싱/슬라이싱이 불가능합니다.
# print(coffees[3])
# TypeError: 'set' object is not subscriptable

findItem = '카푸치노'

bool = findItem in coffees
print(f'{findItem} 존재 여부 : {bool}')

# '마키야또'가 존재하는 지 확인하고, 없으면 추가해 보세요.
findItem = "마키아또"
if not findItem in coffees:
    coffees.add(findItem)
# end if 

findItem = '믹스커피'
coffees.remove(findItem)

# '바닐라라떼'를 삭제하되, 항목이 없으면 예외처리 하세요.
try:
    findItem = '바닐라라떼'
    coffees.remove(findItem)
except KeyError:
    print(f'\'{findItem}\'는 목록에 존재하지 않습니다.')
# end try

print(type(coffees))
print('요소 개수 : %d' % len(coffees))
print(coffees)

print('반복문을 사용한 출력')
for element in coffees:
    print(element)
# end for

# 집합 연산
store01 = set(['고구마라떼', '에스프레소', '아메리카노', '마키아또'])
store02 = set(['아메리카노', '마키아또', '카페라떼', '디카페인커피'])

print('2 매장에서 판매 가능한 품목')
union_set = store01.union(store02)
print('합집합01 : %s' % union_set)

union_set = store01 | store02 # | 기호 사용
print('합집합02 : %s' % union_set)

print('2 매장에서 공통적으로 판매 가능한 품목')
intersection_set = store01.intersection(store02)
# & 기호도 사용 가능합니다.
print('교집합 : %s' % intersection_set)

print('1번째 매장에서만 판매 가능한 품목')
difference_set_01 = store01.difference(store02)
# - 기호도 사용 가능합니다.
print('차집합 A-B : %s' % difference_set_01)

difference_set_02 = store02.difference(store01)
print('차집합 B-A : %s' % difference_set_02)

symmetric_difference_set = store01.symmetric_difference(store02)
print('차집합들의 합집합 : %s' % symmetric_difference_set)

super_set = set(['고구마라떼', '에스프레소', '아메리카노', '마키아또'])
sub_set_01 = set(['아메리카노', '마키아또'])
sub_set_02 = set(['바닐라라떼', '마키아또'])

bool = sub_set_01.issubset(super_set)
if bool:
    print('집합01은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합01은 슈퍼 집합의 부분 집합이 아닙니다.')

bool = sub_set_02.issubset(super_set)
if bool:
    print('집합02은 슈퍼 집합의 부분 집합입니다.')
else:
    print('집합02은 슈퍼 집합의 부분 집합이 아닙니다.')

bool = super_set.issuperset(sub_set_01)
if bool:
    print('super_set은 sub_set_01의 상위 집합입니다.')
else:
    print('super_set은 sub_set_01의 상위 집합이 아닙니다.')