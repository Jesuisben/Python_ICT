# 목록에 소괄호를 사용하거나, 단순 콤마만 연결하면 tuple이 됩니다.
coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')
coffee03 = '카푸치노', '마키야또'

print('자료형 타입 : ', end='')
print(type(coffee01))

mytuple = coffee01 * 3
print(mytuple)

mylist = ['바닐라라떼', '플랫화이트']
coffee04 = tuple(mylist) # list를 tuple로 변환

#  + 기호 사용시 요소 개수가 1개이더라도 반드시 콤마를 붙여 주세요.
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)

length = len(coffees)
print('요소 개수 : %d' % length)
print(type(coffees))
print(coffees)

# 불변성을 가지는 tuple 자료형의 요소에는 값을 할당할 수 없습니다.
# coffees[1] = '우유'
# TypeError: 'tuple' object does not support item assignment

# 인덱싱
print('앞에서 3번째 요소 : %s' % (coffees[3]))
print('뒤에서 2번째 요소 : %s' % (coffees[-2]))

print('1번째부터 3번째 요소들 : ', end='')
print(coffees[1:4])

print('4번째 이후의 요소들 : ', end='')
print(coffees[4:])

print('3번째 요소까지 출력 : ', end='')
print(coffees[:4])

# count() 함수를 사용하여 특정 항목이 몇 개 있는 지 확인 가능합니다.
mycount = coffees.count('아메리카노')
print('아메리카노의 개수 : %d' % (mycount))


# index() 함수를 사용하여 특정 값의 첫 번째 인덱스 번호 찾기
myindex = coffees.index('아메리카노')
print('아메리카노의 위치 색인 : %d' % (myindex))

print('튜플의 응용(swap 기법)')
x, y = 3, 4
print('before x : %d, y : %d' % (x, y))

x, y = y, x
print('after x : %d, y : %d' % (x, y))