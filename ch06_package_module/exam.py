# exam.py
def mysum(a, b) :
    return a + b

# __name__ 변수 : 파이썬에서 사용하는 해당 모듈의 이름을 의미하는 특수 형태의 내장 변수
# 프로그램(파이썬 파일)을 실행하는 주체에 따라서 __name__ 변수의 값이 달라짐
# 본인이 본인을 실행하면 (실행 주체가 본인이면) __name__ 변수의 값은 자동으로 "__main__"이 됨
# -> 여기서 실행하면 __name__의 값이 "__main__"이여서 그 조건에 맞는 동작이 실행됨
if __name__ == "__main__" :
    print(__name__)
    print("덧셈 결과 : %d" % mysum(2, 3))
else:
    print("다른 모듈이 %s 모듈을 호출함" % __name__)

print("a모듈 %s가 종료됨" % __name__)