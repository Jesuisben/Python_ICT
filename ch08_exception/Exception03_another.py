class LessThan5Exception(Exception):
    def __init__(self, arg):
        super().__init__('{}는 5보다 작은 수입니다.'.format(arg))

su = input('5이상의 수를 입력하세요 : ')

try :
    su = int(su)
    if(su < 5 ):
        raise LessThan5Exception( su )
    else :
        print(f'{su}를 입력하셨군요~~잘 하셨습니다^^')

except LessThan5Exception as err :
    # 넘겨준 예외 message를 출력합니다.
    print('예외 발생 : %s' % err )

except ValueError as err :
    print('올바른 숫자 형식을 입력해 주서야 합니다')
    print(err)