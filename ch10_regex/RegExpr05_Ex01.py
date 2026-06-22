import re

print('다음 데이터를 정규 표현식 split 함수를 사용하여 사전으로 만들어 보세요.')
mystring01 = '사과:10/오렌지:20/감:30/밤:40'

regex = '[:/]'
pattern = re.compile(regex)
result = pattern.split(mystring01)

fruitDict = dict()
for idx in range(0, len(result), 2):
    fruitDict[result[idx]] = result[idx+1]
# end for

print(fruitDict)

print('다음 데이터를 sub 함수를 사용하여 - 기호를 / 기호로 변경해 보세요.')
mylist = ['광복절 : 1945-08-15', '삼일절 : 1919-03-01']
for sentence in mylist:
    result = pattern.sub('/', sentence)
    print(result)
# end for