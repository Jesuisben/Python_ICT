import re
# RegExpr09.py
# 그룹화하기

print('조건에 맞는 주민 번호에 대하여 별 붙이기')
# 800925-1046555 --> 800925-1******

ssnList = ['800925-1046555', '111010-4567890', '8512-20599']

print('소괄호 기호를 사용하면, 하나의 그룹이 됩니다.')
print('그룹 번호는 1 base이고, \'\\g<숫자>\' 형식으로 사용합니다.')
regex = '(\d{6})[-](\d{1})\d{6}'
pattern = re.compile(regex)

for ssn in ssnList:
    # sub 함수는 치환할 때 사용합니다.
    print(pattern.sub('\g<1>-\g<2>******', ssn))
# end for

phones = ['010-1111-2222', '010-3333-4444', '010-5555-6666']
regex = '(\d{3})-(\d{4})-\d{4}'
pattern = re.compile(regex)

for phone in phones :
    print(pattern.sub('\g<1>-\g<2>-####', phone))
# end for