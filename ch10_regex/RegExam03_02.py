import re

# findall 함수를 사용하여 다음 문자열에서 숫자 2자리 형식으로 모두 추출해 보세요.
mystring01 = '1234 abc가나다AB_555_6'

regex = "[0-9]{2}"
pattern = re.compile(regex)

# findall() : 정규 표현식과 매칭되는 것을 리스트 형식으로 반환함
result = pattern.findall(mystring01)
print("findall 함수를 사용하여 다음 문자열에서 숫자 2자리 형식으로 모두 추출해 보세요.")
print(result)

print("추출된 숫자 2자리 형식 모두를 더해 보세요.")

total = 0
for item in result:
    total += int(item)

print(total)


# finditer 함수를 사용하여 다음 문자열에서 알파벳 소문자 형식들을 모두 추출해 보세요.
# finditer() : 정규 표현식과 매칭되는 것을 iterable 타입으로 반환함
mystring02 = 'hello 123 world'
print("finditer 함수를 사용하여 다음 문자열에서 알파벳 소문자 형식들을 모두 추출해 보세요.")
print("발견된 문자열의 색인 위치를 이용하여 신규 list를 작성해 보세요.")

regex = "[a-z]+"
pattern = re.compile(regex)
result = pattern.finditer(mystring02)

# 발견된 문자열의 색인 위치를 이용하여 신규 list를 작성해 보세요.
mylist = []

for item in result:
    print(f"문자열 : {item.group()}")
    mylist.append(item.start())
    mylist.append(item.end()-1)

print(mylist)


# import re
# print('findall 함수를 사용하여 다음 문자열에서 숫자 2자리 형식으로 모두 추출해 보세요.')
# mystring01 = '1234 abc가나다AB_555_6'
# regex = '[0-9]{2}'
# pattern = re.compile(regex)
#
# mylist = pattern.findall(mystring01)
# print(mylist)
#
# print('추출된 숫자 2자리 형식 모두를 더해 보세요.')
# total = 0
# for idx in mylist:
#     total += int(idx)
# print(total)
#
# print('finditer 함수를 사용하여 다음 문자열에서 알파벳 소문자 형식들을 모두 추출해 보세요.')
# mystring02 = 'hello 123 world'
#
# regex = '[a-z]+'
# pattern = re.compile(regex)
#
# print('발견된 문자열의 색인 위치를 이용하여 신규 list를 작성해 보세요.')
# newlist = []
# myiter = pattern.finditer(mystring02)
# for onedata in myiter:
#     print('문자열 :', onedata.group())
#     start = onedata.start()
#     end = onedata.end()
#     newlist.append(start)
#     newlist.append(end - 1)
#
# print(newlist)