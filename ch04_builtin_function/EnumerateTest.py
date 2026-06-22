# EnumerateTest.py
fruits = ['사과', '감', '오렌지', '한라봉', '바나나']

# enumerate 함수는 iterable 객체의 색인 번호와 값을 튜플 형식으로 반환해 줍니다.
# 일반적으로 현재 요소의 인덱스를 사용하고자 할 때 주로 사용합니다.
for idx, value in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (idx, value)
    print(message)
print('-'*30)

for idx, value in enumerate(fruits, start=1):
    message = '품목 \'%s\'의 인덱스 : %d' % (value, idx)
    print(message)
print('-'*30)

for item in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (item[0], item[1])
    print(message)
print('-'*30)

print('*은 가변 매개 변수로 인식되며, tuple으로 취급됩니다.')
for item in enumerate(fruits):
    message = '{}번째 값 : {}'.format(*item)
    print(message)
print('-'*30)

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




