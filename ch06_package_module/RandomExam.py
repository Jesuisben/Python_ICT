somedata = [idx for idx in range(1, 11)]
mylist = list()

import random

for idx in range(1, 6):
    mylist.append(random.randint(1, 10))

print(mylist)

print('sample() 함수 사용하기')
result = random.sample(somedata, 3)
print(result)

print('shuffle() 함수 사용하기')
random.shuffle(somedata)
print(somedata[0:3])