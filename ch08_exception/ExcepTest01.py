try :
    su1 = 10
    su2 = '20'

    result = su1 + su2
    print(result)

    mydict = {'hong': 10, 'kim': 20}
    findKey = 'choi'
    print(mydict[findKey])

except KeyError as err :
    print(findKey + '는 존재하지 않는 키입니다.')
    print('예외 객체 :', err)

except TypeError as err:
    print('연산시 타입 오류 발생.')
    print('예외 객체 :', err)

except Exception as err:
    print('나머지 오류 발생')
    print('예외 객체 :', err)

else :
    print('예외 없으면 실행 되요.')
    
finally:
    print('나는 무조건 실행 되요.')