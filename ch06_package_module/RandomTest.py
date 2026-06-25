# RandomTest.py
import random

# 0.0 <= 값 < 1.0
# 0.0 이상 1.0 미만의 랜덤 실수를 반환하는 함수
print(random.random())

import sys
# sys.maxsize : sys 모듈에서 현재 시스템이 다룰 수 있는 최대 정수값을 출력하는 코드
# 자바에서 긴 타입인 Long이 64비트 시스템 기준으로 이정도의 값이 나옴
print('시스템 최대 정수 값 : %d' % sys.maxsize)

print('시드 값의 범위 : 0 <= 시드값 <= 시스템 최대 정수 값')
# 1. 시드 : 컴퓨터는 완전 랜덤 숫자를 만들 수 없어서 어떤 숫자를 기반으로 계산해서
# 랜덤처럼 보이게 만드는게 그 기반이 되는 숫자를 시드라고 함
# 시드 -> 계산 -> 랜덤처럼 보이는 값
# 2. random.seed(정수) : 시드의 숫자를 고정시킴
# 3. 랜덤 함수에 시드 값을 배정하면, 항상 동일한 값을 출력합니다.
random.seed(1234)
# 고정된 값이 나옴
print(random.random())

# 1이상 10이하의 랜덤한 정수
print(random.randint(1, 10))

# 1. random.choice() : 임의의 요소 1개 선택
# 매개변수로는 시퀀스 타입(인덱스가 있는 iterable타입)만 됨
# 문자열 타입으로 반환함
# 2. random.choices(선택할 요소 집합, 선택할 요소 갯수) : 임의의 요소 중복없이 선택
# 중복을 허용해서 선택할 수 있음 (중요!)
# List 타입으로 반환함
coffees = ['아메리카노', '카페라떼', '아이스커피', '디카페인커피', '바닐라라떼']
print(random.choice(coffees)) # 임의의 요소 1개 선택

# random.shuffle() : 리스트를 무작위로 섞어 순서를 무작위로 바꾸는 함수
# 마찬가지로 매개변수로는 시퀀스 타입만 가능
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
# random.sample(선택할 요소 집합, 선택할 요소 갯수)
# 중복을 허용하지 않음(중요!) VS random.choices() (중복 허용)
# List 타입으로 반환함
n = 3
sampling = random.sample(members, n)
print(sampling)