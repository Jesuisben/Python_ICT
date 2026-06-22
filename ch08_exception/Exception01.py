# Exception01.py

try:
    mylist = [1, 2, 3]
    print(mylist[5])

    x, y = 4, 0
    z = x / y
    print(z)

    print('예외가 발생하면 나는 실행이 안되요.')

except ZeroDivisionError as err:
    print('0으로 나누지 마세요.')
    print('예외 객체 정보 : %s' % err)

except IndexError as err:
    print('인덱스 접근 범위 초과.')
    print('예외 객체 정보 : %s' % err)

except Exception as err:
    print('기타 나머지 예외 발생')
    print('예외 객체 정보 : %s' % err)

else:
    print('예외가 발생하지 않으면 실행이 됩니다.')

finally:
    print('예외 발생 여부와 상관 없이 무조건 실행 됩니다.')