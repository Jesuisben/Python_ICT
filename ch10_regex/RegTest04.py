import re

# -----------------------------------------------------
# 1) split 함수로 문자열을 분리하여 사전 만들기
# -----------------------------------------------------
print('1) split 함수를 사용하여 데이터를 사전으로 변환하기')
mystring01 = '사과:10/오렌지:20/감:30/밤:40'

# ':' 또는 '/'를 구분자로 사용
regex = '[:/]'
pattern = re.compile(regex)
result = pattern.split(mystring01)

# 리스트를 2개씩 묶어 사전으로 변환
fruitDict = {result[i]: result[i+1] for i in range(0, len(result), 2)}

print(fruitDict)
# 출력 예: {'사과': '10', '오렌지': '20', '감': '30', '밤': '40'}


# -----------------------------------------------------
# 2) sub 함수를 사용하여 '-'를 '/'로 변경
# -----------------------------------------------------
print('\n2) sub 함수를 사용하여 -를 /로 변경하기')
mylist = ['광복절 : 1945-08-15', '삼일절 : 1919-03-01']

# 하이픈(-)을 슬래시(/)로 변경
regex = '-'
pattern = re.compile(regex)

for sentence in mylist:
    result = pattern.sub('/', sentence)
    print(result)
# 출력 예:
# 광복절 : 1945/08/15
# 삼일절 : 1919/03/01
