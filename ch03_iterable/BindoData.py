# list, dict, comprehension 기능을 이용한 빈도 수 추출하기
import random
mydict = {}

for idx in range(1, 101):
    data = random.randint(1, 10)
    if data in mydict :
        mydict[data] += 1
    else :
        mydict[data] = 1

mylist = [key for key in mydict.keys()]
mylist.sort()

for key in mylist:
    print('숫자 %2d은(는) %2d번 추출되었습니다.' % ( key, mydict[key] ))