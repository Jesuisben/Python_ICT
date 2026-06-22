import math

def deviation( list1 )  :
    length = len( list1 )
    total = 0.0
    for item in list1 :
        total = item + total
    # end for
    print('총합 : %d' % total)

    average = total / length
    print('평균 : %.2f' % average)

    imsi = 0.0
    for item in list1 :
        imsi += (average - item ) ** 2
    # end for
    print('차이 제곱의 총합 : %.2f' % imsi)

    imsi = imsi / length
    print('분산 : %.2f' % imsi)

    return math.sqrt(imsi)
# end def


mylist = [10, 30, 40, 80]
result = deviation(mylist)

# 출력 결과 : 25.495097568
print('표준 편차 : %.8f' % result)