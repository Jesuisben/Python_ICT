import re
# RegExpr07.py
# 정규 표현식 : 컴파일 옵션

print('dot 기호(.)는 줄바꿈 문자를 제외한 임의의 1글자를 의미합니다.')
mylist01 = ['a b', 'a\nb', 'acb'] # 줄바꿈 문자(\n) 포함됨
regex = 'a.b'

totalList = []
pattern = re.compile(regex)
for item in mylist01:
    if pattern.match(item):
        totalList.append(item)
# end for
print(totalList)


print('줄바꿈 문자까지 포함되도록 컴파일 옵션을 지정합니다.')
print('re.RegexFlag.DOTALL : 줄바꿈까지 포함함')
totalList = []
pattern = re.compile(regex, re.RegexFlag.DOTALL)
for item in mylist01:
    if pattern.match(item):
        totalList.append(item)
# end for
print(totalList)

print('정규 표현식은 기본 값으로 대소문자를 구분합니다.')
mylist02 = ['PYTHON', 'python']
regex = '[a-z][a-zA-Z]*' # 첫 글자는 반드시 소문자

pattern = re.compile(regex)
totalList = []
for item in mylist02:
    if pattern.match(item):
        totalList.append(item)
print(totalList)

print('re.RegexFlag.IGNORECASE : 대소문자 구분 안함')
pattern = re.compile(regex, re.RegexFlag.IGNORECASE)
totalList = []
for item in mylist02:
    if pattern.match(item):
        totalList.append(item)
print(totalList)

# dot가 3개이면 주석(comment) 또는 multiline string입니다.
print('정규 표현식은 기본 값으로 멀티 라인을 지원하지 않습니다.')
print('python으로 시작하고, 띄어 쓰기 한 칸이후 문자나 숫자가 나오는 줄 찾기')
mystring = '''python one
life is too short
python two hello python three
you need python
python four hohoho
python 5'''

# regex = 'python\s\w+'
regex = '^python\s\w+'
pattern = re.compile(regex)
result = pattern.match(mystring)
print(type(result))
print(result)

print('re.RegexFlag.MULTILINE : 멀티 라인 적용')
pattern = re.compile(regex, re.RegexFlag.MULTILINE)
result = pattern.findall(mystring)
print(type(result))
print(result)