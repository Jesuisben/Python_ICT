# List와 tuple의 차이
# List는 요소 편집이 가능하지만 tuple은 불가능

# tuple의 3가지 다른 모양
# 1) 가장 무난한 모양
coffee01 = ("아메리카노", "카페라떼")  # tuple의 소괄호
# 2) 매개변수가 한개인 함수인 tuple이여서 tuple에 속하는 tuple 덩어리를 한개로 만들어서 넣어야 함
# 마치 타입을 변환하는 함수 느낌 ex) str(123) -> "123"
coffee02 = tuple(("콜드브루", "아이스커피"))  # tuple 함수의 소괄호 # 위 아래 둘다 사실상 똑같음
# 3) 굳이 소괄호를 안쓰고 그냥 콤마로 연결해도 tuple이 됨
coffee03 = "카푸치노", "마키야또"

print(type(coffee01))

# tuple 끼리는 합쳐지지만 타입이 안맞는 List와는 합쳐지지 않아서 tuple로 타입을 변환함
mylist = ["바닐라라떼", "플랫화이트"]
coffee04 = tuple(mylist)

# 문자열을 직접 넣어 tuple에 추가하는 방식은 불가함 -> 타입이 맞지 않아서 + 연산자 사용 불가
# 따라서 (,)안에 넣음 (콤마 앞에 tuple에 넣을 문자열 넣기)
# 만약 그냥 ("문자열")하면 str로 인식해서 차별점을 두어서 tuple로 인식하기 위해서 콤마를 넣음
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ("에스프레소",)
length = len(coffees)
print("요소 개수 : %d" % length)
print(type(coffees))

# tuple은 List와 다르게 불변(immutable) 자료형이기 때문에 요소를 추가, 삭제 또는 변경하는 것이 불가능
# # TypeError: 'tuple' object does not support item assignment
# coffees[1] = "우유"

# 인덱싱과 슬라이싱 (순서를 따지는 집합은 인덱싱과 슬라이싱이 가능함)
# 인덱싱
print("앞에서 3번째 요소 : %s" % coffees[3])
print("뒤에서 2번째 요소 : %s" % coffees[-2])

# 슬라이싱
print("1번째부터 3번째 요소까지 출력", end="")
print(coffees[1:4])

print("4번째 이후의 요소들 : ", end="")
print(coffees[4:])

print("3번째 요소까지 출력 : ", end="")
print(coffees[:4])

# 문자열을 이용해서 tuple의 해당 문자열의 개수 알아내기
mycount = coffees.count("아메리카노")
print("아메리카노의 개수 : %d" % mycount)

# 문자열을 이용해서 tuple의 해당 문자열의 인덱스 알아내기
myindex = coffees.index("아메리카노")
print("아메리카노의 색인 번호 : %d" % myindex)

print()
print(coffees)

# 한번에 변수 정의함 (Java에 없는 문법)
# 원래는 x = 3, y = 4
# Python의 다중 할당
x, y = 3, 4
print("before x : %d, y : %d" % (x, y))

# 정의된 변수의 값을 서로 맞바꿈 (java에 없는 문법)
# Python의 Swap
x, y = y, x
print("after x : %d, y : %d" % (x, y))

# # 목록에 소괄호를 사용하거나, 단순 콤마만 연결하면 tuple이 됩니다.
# coffee01 = ('아메리카노', '카페라떼')
# coffee02 = ('콜드브루', '아이스커피')
# coffee03 = '카푸치노', '마키야또'
#
# print('자료형 타입 : ', end='')
# print(type(coffee01))
#
# mytuple = coffee01 * 3
# print(mytuple)
#
# mylist = ['바닐라라떼', '플랫화이트']
# coffee04 = tuple(mylist) # list를 tuple로 변환
#
# #  + 기호 사용시 요소 개수가 1개이더라도 반드시 콤마를 붙여 주세요.
# coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
#
# length = len(coffees)
# print('요소 개수 : %d' % length)
# print(type(coffees))
# print(coffees)
#
# # 불변성을 가지는 tuple 자료형의 요소에는 값을 할당할 수 없습니다.
# # coffees[1] = '우유'
# # TypeError: 'tuple' object does not support item assignment
#
# # 인덱싱
# print('앞에서 3번째 요소 : %s' % (coffees[3]))
# print('뒤에서 2번째 요소 : %s' % (coffees[-2]))
#
# print('1번째부터 3번째 요소들 : ', end='')
# print(coffees[1:4])
#
# print('4번째 이후의 요소들 : ', end='')
# print(coffees[4:])
#
# print('3번째 요소까지 출력 : ', end='')
# print(coffees[:4])
#
# # count() 함수를 사용하여 특정 항목이 몇 개 있는 지 확인 가능합니다.
# mycount = coffees.count('아메리카노')
# print('아메리카노의 개수 : %d' % (mycount))
#
#
# # index() 함수를 사용하여 특정 값의 첫 번째 인덱스 번호 찾기
# myindex = coffees.index('아메리카노')
# print('아메리카노의 위치 색인 : %d' % (myindex))
#
# print('튜플의 응용(swap 기법)')
# x, y = 3, 4
# print('before x : %d, y : %d' % (x, y))
#
# x, y = y, x
# print('after x : %d, y : %d' % (x, y))
