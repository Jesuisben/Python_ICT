import re # regular expression의 줄인 말
# RegExpr01.py
# 정규 표현식을 이용하여 다음 물음에 답해 주세요.
# 다음 리스트 목록 중에서 '문자열 2개와 숫자 3개'로 구성된 항목들을 찾아 보세요.
mylist01 = ['ab123', 'cd456', 'ef789', 'abc12']

print('문자열 2개와 숫자 3개로 구성된 항목 찾기')
regex = '[a-z]{2}\d{3}' # 메타 문자를 사용한 정규 식
pattern = re.compile(regex) # 찾고자 하는 패턴

for item in mylist01:
    if pattern.match(item):
        print(f'문자열 {item}은 조건에 적합니다.')
    else:
        print(f'문자열 {item}은 조건에 부적합니다.')
    # end if
# end for

# 다음 리스트 목록 중에서 'a'와 '.txt' 사이에 숫자가 최소 3개 이상인 항목들을 찾아 보세요.
mylist02 = ['a1.txt', 'a12.txt', 'a123.txt', 'a1234.txt']

print("'a'와 '.txt' 사이에 숫자가 최소 3개 이상인 항목 찾기")
regex = 'a[0-9]{3,}.txt'
pattern = re.compile(regex)

for item in mylist02:
    if pattern.match(item):
        print(f'문자열 {item}은 조건에 적합니다.')
    else:
        print(f'문자열 {item}은 조건에 부적합니다.')
    # end if
# end for

# 다음 리스트 목록 중에서 'c'와 't' 사이에 'a'가 1번 이상인 항목들을 찾아 보세요.
mylist03 = ['at', 'cat', 'caat', 'caaat']
regex = 'ca+t' # 'ca+t' 또는 'ca*t' 또는 'ca?t'
pattern = re.compile(regex)

for item in mylist03:
    if pattern.match(item):
        print(f'문자열 {item}은 조건에 적합니다.')
    else:
        print(f'문자열 {item}은 조건에 부적합니다.')
    # end if
# end for









