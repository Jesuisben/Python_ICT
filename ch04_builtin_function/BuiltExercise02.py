human = ['김철수', '홍길동', '박영희', '심수련', '유재민']

mylist = []
for idx, value in enumerate(human):
    if idx % 2 == 0:
        mylist.append(value)
print(mylist)

newhuman = list(item + '님' for item in human)
print(newhuman)