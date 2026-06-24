def starPrint(n=10) :
    for idx in range(1, n + 1):
        if idx % 5 == 0 :
            print("*")
        else:
            print("*", end="")

starPrint(24)
print("\n")
starPrint()


# # 파일 이름 : PrintStar.py
# # 카운터 수 n을 입력 받아서 별을 n번 출력하는 함수 starPrint()를 작성해 보세요.
# # 한줄에 별을 5개씩 출력해야 합니다.
# # 별의 개수가 입력이 되지 않으면, 기본 값으로 10번이 출력되어야 합니다.
# def starPrint(n=10):
#     for idx in range(1, n + 1):
#         print('*', end=' ')
#         if idx % 5 == 0:
#             print()
#     print()
#
#
# # end def
#
# starPrint(24)
# print()
# starPrint()
