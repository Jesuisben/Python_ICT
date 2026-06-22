import re
# RegExam05.py
# 그룹화(Grouping)와 치환(Substitution) 실습

print('조건에 맞는 주민 번호에 대하여 별 붙이기')
# 800925-1046555  →  800925-1******
# 주민번호 패턴: 앞 6자리(생년월일) - 성별 1자리 이후 6자리

ssnList = ['800925-1046555', '111010-4567890', '8512-20599']

print('\n[그룹 설명]')
print('소괄호 () 를 사용하면 특정 부분을 "그룹"으로 묶습니다.')
print('그룹 번호는 1부터 시작하며, 치환 시에는 \g<번호> 로 참조합니다.\n')

# 정규식 설명:
# (\d{6})  → 그룹1 : 숫자 6개 (생년월일)
# [-]      → 하이픈 문자
# (\d{1})  → 그룹2 : 숫자 1개 (성별 코드)
# \d{6}    → 나머지 6자리
regex = r'(\d{6})-(\d{1})\d{6}'
pattern = re.compile(regex)

print('[주민번호 처리]')
for ssn in ssnList:
    # pattern.sub(치환문자, 원본)
    # \g<1> = 첫 번째 그룹(생년월일)
    # \g<2> = 두 번째 그룹(성별 코드)
    result = pattern.sub(r'\g<1>-\g<2>******', ssn)
    print(result)
# end for

print('\n===================================')
print('전화번호 가운데 자리를 마스킹하기')
phones = ['010-1111-2222', '010-3333-4444', '010-5555-6666']

# (\d{3})   → 그룹1 = 앞자리 3개
# (\d{4})   → 그룹2 = 중간 4자리
# \d{4}     → 마지막 4자리(치환 시 숨길 부분)
regex = r'(\d{3})-(\d{4})-\d{4}'
pattern = re.compile(regex)

print('[전화번호 처리]')
for phone in phones:
    result = pattern.sub(r'\g<1>-\g<2>-####', phone)
    print(result)
# end for

print('\n===================================')
print('이메일 아이디 일부 숨기기')
emails = ['hong123@gmail.com', 'kim77@naver.com', 'user999@daum.net']

# (.+) → 그룹1 : @ 앞의 모든 문자 (최소 1개)
# @ → @ 문자
# (.+) → 그룹2 : 도메인 부분
regex = r'(.{2}).+(@.+)'
pattern = re.compile(regex)

print('[이메일 처리]')
# 아이디 첫 2글자만 남기고 나머지 ***
for email in emails:
    result = pattern.sub(r'\g<1>***\g<2>', email)
    print(result)

print('\n===================================')
print('주소 앞부분 그룹화')

addrs = ['서울특별시 강남구 역삼동 123-45', '부산광역시 해운대구 좌동 45-12']

# 주소를 "시도 / 구 / 나머지"로 분리
regex = r'(.+시)\s(.+구)\s(.+)'
pattern = re.compile(regex)

print('[주소 처리]')
for addr in addrs:
    # 시도 + 구는 그대로, 나머지만 숨기기
    result = pattern.sub(r'\g<1> \g<2> ***', addr)
    print(result)


print('\n===================================')
print('제품 코드 마스킹 예시')

products = ['PRD-2024-38192', 'PRD-2025-54920']

# PRD- (문자3개)
# (\d{4}) : 그룹1 → 연도
# -(\d{5}) : 그룹2 → 일련번호
regex = r'PRD-(\d{4})-(\d{5})'
pattern = re.compile(regex)

print('[제품 코드 처리]')
for p in products:
    result = pattern.sub(r'PRD-\g<1>-#####', p)
    print(result)