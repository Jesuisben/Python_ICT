# 랜덤한 수를 추출하기 위한 모듈
import random

answer = random.randint(1, 100)
print('정답 : %d' % answer) # 컴퓨터가 기억하고 있는 값

count = 0 # 카운터 변수

while True: # 무한 while loop 구문
    su = int(input('1부터 100 사이의 정수 입력 : '))

    count += 1

    if answer > su :
        print('%d보다 큰 수를 입력해 주세요.' % su)
    elif answer < su :
        print('%d보다 작은 수를 입력해 주세요.' % su)
    else:
        print('정답을 맞추셨군요.')
        break # 정답이므로 게임 끝내기
    # end if
# end while

print('%d번만에 맞추셨습니다.' % count)