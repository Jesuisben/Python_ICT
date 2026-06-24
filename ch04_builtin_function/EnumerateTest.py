# EnumerateTest.py
fruits = ['사과', '감', '오렌지', '한라봉', '바나나']

# enumerate() : 매개변수의 요소의 색인 번호와 값을 나열(열거)하는 함수
# 자바의 enum(열거형 타입)과 비슷한 맥락임
for xx in enumerate(fruits):
    print(xx)
print("*"*30)

# enumerate 함수는 iterable 객체의 색인 번호와 값을 튜플 형식으로 반환해 줍니다.
# 일반적으로 현재 요소의 인덱스를 사용하고자 할 때 주로 사용합니다.
for idx, value in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (idx, value)
    print(message)
print('-'*30)

# start : 색인 번호를 나열할때의 기본값(시작점) 설정 (기본값은 0)
# 타입 - idx : int / value : string
for idx, value in enumerate(fruits, start=1):
    message = '품목 \'%s\'의 인덱스 : %d' % (value, idx)
    print(message)
print('-'*30)

# 타입 - item : tuple
for item in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (item[0], item[1])
    print(message)
print('-'*30)

print('*은 가변 매개 변수로 인식되며, tuple으로 취급됩니다.')
for item in enumerate(fruits):
    # string의 함수 format()을 이용해서 매개변수를 문자열 안에 넣기
    message = '{}번째 값 : {}'.format(*item)
    print(message)
print('-'*30)

# enumerate() 함수는 iterable이면 다 사용가능하지만
# 키와 값을 짝지어 모두 반환하는 items() 함수는 키와 값을 가진 사전만 사용 가능함
# 공통점 : tuple 타입으로 반환
# 차이점 : enumerate() - 인덱스, 값 반환 / items() - 키, 값 반환
# 사전의 items()라는 함수는 key, value를 tuple 형식으로 반환해 줍니다.
coffees = {'아메리카노':5000, '카페라떼':6000, '카푸치노':5500}

for name, price in coffees.items():
    message = '\'%s\'의 단가는 %d원입니다.' % (name, price)
    print(message)
print()

for item in coffees.items():
    message = '\'%s\'의 단가는 %d원입니다.' % (item[0], item[1])
    print(message)
print()

for item in coffees.items():
    message = '품목 \'{}\'의 단가 : {}원'.format(*item)
    print(message)
print()