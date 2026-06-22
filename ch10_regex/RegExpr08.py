import re
# RegExpr08.py
# raw string : 특수 문자(이스케이스 시퀀스 문자)를 해석하지 않고, 곧이 곧대로 해석하겠습니다.

print('역슬래시 2개 나온 다음 나오는 모든 알파벳 문자열 찾기')
mystring = '\\hello how \\world'

regex = '\\\\[a-z]+'
pattern = re.compile(regex)
result = pattern.findall(mystring)
print(result)

print('정규식 앞에 r을 붙이면 raw string으로 인식합니다.')
regex = r'\\[a-z]+'
pattern = re.compile(regex)
result = pattern.findall(mystring)
print(result)