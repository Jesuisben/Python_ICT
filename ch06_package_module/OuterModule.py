# OuterModule.py
def mysum(a, b):
    return a + b


if __name__ == '__main__': # 모듈 자신이 실행한 경우
    print(__name__)
    print('덧셈 결과 : %d' % mysum(2, 3))
else: # 외부 모듈이 이 모듈을 실행 시킨 경우
    print('다른 모듈이 %s 모듈을 호출했습니다.' % __name__)
# end if


print('모듈 %s가 종료되었습니다.' % __name__)