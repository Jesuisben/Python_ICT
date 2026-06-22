import re
# RegExpr06.py

print('다음 목록 중에서 올바른 우편 번호 형식을 찾아 주세요.')
zipcodes = ['12345', 'a12345', '12345b', 'a12345b']

regex = '^\d{5}$' # '\d{5}' 또는 '^\d{5}' 또는 '\d{5}$' 또는 '^\d{5}$'
pattern = re.compile(regex)

for item in zipcodes:
    if pattern.search(item):
        print('%s : True' % item)
    else:
        print('%s : False' % item)
# end for

print('다음 목록 중에서 올바른 전화 번호 형식만 별도로 list 데이터로 만들어 보세요.')
print('기호 하이폰은 필수 입력 사항입니다.')
handphones = ['010-1111-2222', 'hello010-1111-2222', '011-123-4567', '01011112222']

regex = '^\d{3}-\d{3,4}-\d{4}$'
pattern = re.compile(regex)

phoneList = list()

for phone in handphones:
    if pattern.search(phone):
        phoneList.append(phone)
# end for

print(phoneList)