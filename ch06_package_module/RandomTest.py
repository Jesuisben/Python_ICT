# RandomTest.py
import random

# 0.0 <= 값 < 1.0
print(random.random())

import sys
print('시스템 최대 정수 값 : %d' % sys.maxsize)

print('시드 값의 범위 : 0 <= 시드값 <= 시스템 최대 정수 값')
# 랜덤 함수에 시드 값을 배정하면, 항상 동일한 값을 출력합니다.
# random.seed(1234)
print(random.random())

print(random.randint(1, 10))

coffees = ['아메리카노', '카페라떼', '아이스커피', '디카페인커피', '바닐라라떼']
print(random.choice(coffees)) # 임의의 요소 1개 선택

random.shuffle(coffees) # 무작위로 섞기
print(coffees)

# 로또 번호 생성
# 임의의 숫자로 섞어서, 앞 6개는 1등, 7번째는 2등으로 처리하겠습니다.
lottoNumber = [su for su in range(1, 46)]
random.shuffle(lottoNumber)
print(lottoNumber)

lotto = sorted(lottoNumber[0:6])
secondno = lottoNumber[6:7]
print('당첨 번호 : ', lotto)
print('2등 번호 : ', secondno)

def extractLottoNo():
    random.shuffle(lottoNumber)
    lotto = sorted(lottoNumber[0:6])
    secondno = lottoNumber[6:7]
    return lotto, secondno
# end def

# 5 게임 출력하기
for idx in range(5):
    first, second = extractLottoNo()
    print('당첨 번호 : ', first)
    print('2등 번호 : ', second)
    print('-'*30)
# end for

# 다음 명단을 이용하여, 1조당 2명씩 조 배정을 해보세요.
members = ['이민정', '최현미', '강유식', '김정식', '안미주', '심현철', '오지훈', '이한나']
random.shuffle(members)
print(members)

MEMBER_SU = 2 # 조원 멤버 수

for idx in range(0, len(members), MEMBER_SU):
    print(members[idx:idx+MEMBER_SU])

# members에서 임의의 명단 n명을 추출해 보세요.
n = 3
sampling = random.sample(members, n)
print(sampling)