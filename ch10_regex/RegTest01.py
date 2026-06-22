import re

print('\n커피 이름 2개 문자 + 숫자 3개로 구성된 항목 찾기')
coffee_list01 = ['am123', 'la456', 'mo789', 'lat12']

regEx = '^[a-z]{2}[0-9]{3}$'
pattern = re.compile(regEx)

result01 = []
for item in coffee_list01:
    if pattern.match(item):
        result01.append(item)
# end for
print('결과01 : %s' % result01)


print('\n"c"로 시작하고 ".coffee"로 끝나며 숫자가 최소 2개 이상 포함된 항목 찾기')
coffee_list02 = ['c1.coffee', 'c12.coffee', 'c345.coffee', 'c9.coffee']

regEx = '^c[0-9]{2,}\.coffee$'
pattern = re.compile(regEx)

result02 = []
for item in coffee_list02:
    if pattern.match(item):
        result02.append(item)
# end for
print('결과02 : %s' % result02)


print('\n"c"와 "e" 사이에 "a"가 1번 이상 반복되는 항목 찾기')
coffee_list03 = ['ce', 'cae', 'caae', 'caaae']

regEx = '^ca+e$'
pattern = re.compile(regEx)

result03 = []
for item in coffee_list03:
    if pattern.match(item):
        result03.append(item)
# end for
print('결과03 : %s' % result03)
