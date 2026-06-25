# ZfillTest01.py
mystring = 'hello'

max_length = 10 # 전체 길이
fill_string = '~' # 채워 넣을 글자

result = mystring.ljust(max_length, fill_string)
print(result)

result = mystring.rjust(max_length, fill_string)
print(result)

# 빈 자리만큼 숫자 0을 채워 주는 함수입니다.
# 공부 한번하기
result = mystring.zfill(max_length)
print(result)

# 금일은 03월 04일입니다.
month = 3
day = 4
strMonth = str(month).zfill(2)
strDay = str(day).zfill(2)

message = '금일은 %s월 %s일입니다.' % (strMonth, strDay)
print(message)