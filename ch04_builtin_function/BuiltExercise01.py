
human = ['김철수', '홍길동', '박영희']
jumsu = [50, 60, 70]

mylist = list(zip(human, jumsu))
print(mylist)

mydict = dict(mylist)
print(mydict)

result = sorted(mydict, key=mydict.get, reverse=True)
print(result)