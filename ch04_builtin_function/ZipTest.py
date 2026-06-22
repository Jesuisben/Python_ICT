# ZipTest.py
# zip() 함수는 iterable 객체에서 순서대로 요소 1개씩을 묶어서 tuple 형태로 만들어 주는 함수입니다.
# 요소의 갯수가 다른 경우, 가장 짧은 요소를 기준으로 쌍(pair)을 만들어 줍니다.

name = ['바나나', '사과', '오렌지']
qty = [10, 30, 20]

for item in zip(name, qty):
    # print(type(item))
    print(item)
print()

name = ['바나나', '사과', '오렌지']
qty = [10, 30]

for item in zip(name, qty):
    # print(type(item))
    print(item)

print('문자열은 글자 1개씩 쌍(pair)을 만들어 줍니다.')
str01 = 'abc'
str02 = 'def'
for munja in zip(str01, str02):
    print(munja)
print()

data01 = ['이현식', '김유정', '강희숙']
data02 = [40, 30, 50]
data03 = ['마포', '용산', '구로']

# 이름: 이현식님, 나이 : 40세, 주소 : 마포
for (name, age, address) in zip(data01, data02, data03):
    message = '이름: %s님, 나이 : %d세, 주소 : %s'
    print(message % (name, age, address))
print()