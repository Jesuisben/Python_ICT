# SayHello.py
# 인사말과 반복 회수 n을 이용하여 인사말을 n번 출력해주는 함수 sayHello()를 작성해 보세요.
# 반복 회수의 기본 값은 10입니다.
def sayHello(message, n = 10):
    for idx in range(n):
        print(message)
    print()
# end def

# 5번 출력하기
sayHello('안녕하세요.', 5)

# 기본 값인 10번 출력하기
sayHello('방가워요')