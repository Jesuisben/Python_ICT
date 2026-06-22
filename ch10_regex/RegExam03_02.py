import re
print('findall 함수를 사용하여 다음 문자열에서 숫자 2자리 형식으로 모두 추출해 보세요.')
mystring01 = '1234 abc가나다AB_555_6'
regex = '[0-9]{2}'
pattern = re.compile(regex)

mylist = pattern.findall(mystring01)
print(mylist)

print('추출된 숫자 2자리 형식 모두를 더해 보세요.')
total = 0
for idx in mylist:
    total += int(idx)
print(total)

print('finditer 함수를 사용하여 다음 문자열에서 알파벳 소문자 형식들을 모두 추출해 보세요.')
mystring02 = 'hello 123 world'

regex = '[a-z]+'
pattern = re.compile(regex)

print('발견된 문자열의 색인 위치를 이용하여 신규 list를 작성해 보세요.')
newlist = []
myiter = pattern.finditer(mystring02)
for onedata in myiter:
    print('문자열 :', onedata.group())
    start = onedata.start()
    end = onedata.end()
    newlist.append(start)
    newlist.append(end - 1)

print(newlist)