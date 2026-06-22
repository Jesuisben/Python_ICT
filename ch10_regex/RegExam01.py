import re

print('\n알파벳 3개 + 숫자 2개로 구성된 항목 찾기')
mylist01 = ['abc12', 'abcd12', 'xy345', 'pq678', 'abcd1']

# ^와 $를 명시하면 "전체 완전 일치", 명시하지 않으면 "부분 일치"
regEx = '^[a-zA-Z]{3}[0-9]{2}$' # 정규 표현식
pattern = re.compile(regEx)
# print(type(pattern)) # <class 're.Pattern'>

result01 = [] # 결과를 저장할 리스트

for item in mylist01:
    if pattern.match(item): # 조건에 충족하면
        result01.append(item)
    # end if
# end for
print('결과01 : %s' % result01)

print('\nfile + 영문자 최소 2개 이상 + .png')
print('주의 : 점은 임의의 한문자(줄바꿈 제외), 역슬래시 점은 점 기호를 의미')
mylist02 = ['filea.png', 'fileab.png', 'fileabc.png', 'file.png', 'file99.png', 'filexyzXpng']
regEx = '^file[a-zA-Z]{2,}\.png$'
pattern = re.compile(regEx)

result02 = []

for item in mylist02:
    if pattern.match(item):
        result02.append(item)
    # end if
# end for
print('결과02 : %s' % result02)

def extract_by_regex(data, regExpr):
    # 정규식 regExpr를 사용하여 data에서 조건에 맞는 항목만 리스트로 반환해 줍니다.
    pattern = re.compile(regExpr)
    result = []

    for bean in data:
        if pattern.match(bean):
            result.append(bean)
        # end if
    # end for

    return result
# end def

print('\nb로 시작하고, g로 끝나는 데 둘 사이에 e가 2번 이상 반복')
mylist03 = ['beg', 'beeg', 'beeeg', 'bg']
regEx = '^be{2,}g$'
result03 = extract_by_regex(mylist03, regEx)
print('결과03 : %s' % result03)

print('\n숫자로 시작(0제외)하고, 이후에 알파벳이 1개 이상인 항목 찾기')
mylist04 = ['1a', '2abc', '9xyz', '0ab']
regEx = '^[1-9][a-zA-Z]+$' # + 기호는 최소 1번 이상
result04 = extract_by_regex(mylist04, regEx)
print('결과04 : %s' % result04)

print('\nhello 또는 hi로 시작하는 항목들 찾기')
mylist05 = ['hello123', 'hi999', 'hey77', 'hello']
regEx = '^(hello|hi).*$' # .* 은 임의의 문자 0번 이상 반복을 의미
result05 = extract_by_regex(mylist05, regEx)
print('결과05 : %s' % result05)