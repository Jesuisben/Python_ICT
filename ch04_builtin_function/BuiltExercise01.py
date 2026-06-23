human = ['김철수', '홍길동', '박영희']
jumsu = [50, 60, 70]

# zip() 함수를 사용하여, 다음과 같은 데이터 mylist를 만드세요.
mylist = []
for item in zip (human, jumsu):
    mylist.append(item)
print(mylist)

# mylist를 사전 mydict으로 변경해 보세요.(dict() 함수 적절히 사용)
mydict = dict(mylist)
print(mydict)

# mydict를 이용하여 점수가 높은 사람 순부터 '이름'을 출력해 보세요.(sorted() 함수)
result = sorted(mydict, key=mydict.get, reverse=True)
print(result)
























# human = ['김철수', '홍길동', '박영희']
# jumsu = [50, 60, 70]
#
# mylist = list(zip(human, jumsu))
# print(mylist)
#
# mydict = dict(mylist)
# print(mydict)
#
# result = sorted(mydict, key=mydict.get, reverse=True)
# print(result)