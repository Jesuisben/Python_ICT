# 1. re(regular expression) 모듈 import 하기
import re

print("알파벳 3개, 숫자 2개로 구성")
mylist01 = ["abc12", "abcd12", "xy345", "xy34", "pq678", "abcd1"]

# 2. 정규 표현식 만들기
# 메타문자로 구성됨
reg_expr = "[a-zA-Z]{3}[0-9]{2}" # 정규 표현식

# 3. 정규식을 가지고 compile 하기
# compile() : 아직 문자열인 정규 표현식을 패턴 객체로 변환시켜주는 함수
pattern = re.compile(reg_expr)

# 4. match() 함수로 매치가 되는지 확인하기
for item in mylist01:
    if pattern.match(item):
        print(item)