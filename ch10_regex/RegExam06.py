# RegExpr08_Expanded.py
# raw string 예제 및 다양한 활용

import re

print('1. 역슬래시 2개 나온 다음 알파벳 문자열 찾기')
mystring = '\\hello how \\world \\\\python'

regex1 = '\\\\[a-z]+' # 일반 문자열 : 역슬래시 4개이지만, 2개로 이해합니다.
pattern1 = re.compile(regex1)
result1 = pattern1.findall(mystring)
print('일반 문자열 결과:', result1)  # ['\\hello', '\\world', '\\python']

regex2 = r'\\[a-z]+' # raw string : 역슬래시 2개입니다.
pattern2 = re.compile(regex2)
result2 = pattern2.findall(mystring)
print('raw string 결과  :', result2)  # ['\\hello', '\\world', '\\python']

print('\n→ raw string을 사용하면 역슬래시를 두 번 쓰지 않아도 됨')
print('예: r"\\hello" vs "\\\\hello"')

print('\n2. 문자열에서 탭(tab)과 개행(newline) 구분자 찾기')

text = "apple\tbanana\ncherry\tdate"

# 일반 문자열
regex_tab = '\\t'
regex_nl  = '\\n'

print('탭 찾기 (일반 문자열)       :', re.findall(regex_tab, text))
print('개행 찾기 (일반 문자열)     :', re.findall(regex_nl, text))

# raw string
regex_tab_r = r'\t'
regex_nl_r  = r'\n'
print('탭 찾기 (raw string)       :', re.findall(regex_tab_r, text))
print('개행 찾기 (raw string)     :', re.findall(regex_nl_r, text))

print('\n→ raw string 사용 시 \\t, \\n을 그대로 패턴으로 사용 가능')

print('\n3. 경로(path)에서 파일명 추출')

path = r"C:\Users\admin\Documents\file.txt"

# \ 문자를 패턴으로 쓸 때 raw string 사용
regex_path = r'\\([^\\]+)$'  # 마지막 \ 뒤의 파일명 추출
match = re.search(regex_path, path)
if match:
    print('파일명 추출:', match.group(1))  # file.txt

print('\n4. 원시 문자열과 일반 문자열 차이 비교')

s1 = "C:\\temp\\newfile.txt"
s2 = r"C:\temp\newfile.txt"

print('일반 문자열       :', s1)  # C:\temp\newfile.txt
print('raw 문자열        :', s2)  # C:\temp\newfile.txt

print('문자열 길이 차이  :', len(s1), 'vs', len(s2))
print('→ 일반 문자열에서는 \\t, \\n 등이 특수문자로 처리되므로 길이와 의미가 달라질 수 있음')

print('\n5. 정규식에서 특수문자 그대로 매칭')

text2 = 'price is $100, discount is 20%'

# $나 %는 정규식에서 특수 문자. raw string으로 안전하게 사용
regex_special = r'\$[0-9]+' # r'\$[0-9]+' # r'$[0-9]+' # '\$[0-9]+'  # '$[0-9]+'
print('가격 추출:', re.findall(regex_special, text2))

regex_percent = r'[0-9]+%'
print('할인 추출:', re.findall(regex_percent, text2))