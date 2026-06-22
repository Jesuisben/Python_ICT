import random

# random.randint(a, b) : a 이상 b 이하의 랜덤 정수를 생성하는 함수 (b까지 포함!)
answer = random.randint(1, 100)
print(answer)

count = 0

while True :
    su = int(input("1부터 100사이의 정수 입력 : "))

    count += 1

    # if 문 안에 아무것도 안넣으면 오류 발생하기에 임의로 넣는 것 (pass)
    # pass를 넣으면 오류는 일으키지 않음
    if answer > su :
        print("%d보다 큰 수를 입력해 주세요." % su)
    elif answer < su:
        print("%d보다 작은 수를 입력해 주세요." % su)
    else:
        print("정답입니다.")
        break

print("%d번 만에 맞추었습니다." % count)


# # 랜덤한 수를 추출하기 위한 모듈
# import random
#
# answer = random.randint(1, 100)
# print('정답 : %d' % answer) # 컴퓨터가 기억하고 있는 값
#
# count = 0 # 카운터 변수
#
# while True: # 무한 while loop 구문
#     su = int(input('1부터 100 사이의 정수 입력 : '))
#
#     count += 1
#
#     if answer > su :
#         print('%d보다 큰 수를 입력해 주세요.' % su)
#     elif answer < su :
#         print('%d보다 작은 수를 입력해 주세요.' % su)
#     else:
#         print('정답을 맞추셨군요.')
#         break # 정답이므로 게임 끝내기
#     # end if
# # end while
#
# print('%d번만에 맞추셨습니다.' % count)