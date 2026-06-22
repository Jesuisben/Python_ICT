# RandomSuGenerate.py
# a이상 b이하의 랜덤한 정수 n개를 list로 만들어 주는 함수 randomGen() 함수를 구현해보세요.
import random

def randomGen(a, b, n):
    mylist = []

    # a : 하한값, b : 상한값, n : 추출 개수
    for idx in range(n):
        mylist.append(random.randint(a, b))
    # end for

    return mylist
# end def


a, b, n = 5, 8, 3
result = randomGen(a, b, n)
print(result)