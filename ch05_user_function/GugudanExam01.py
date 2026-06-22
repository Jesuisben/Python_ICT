# GugudanExam01.py
# 단수를 입력 받아서 해당 단의 구구단을 출력해주는 함수 gugudan()을 구현해 보세요.
def gugudan(dan):
    for idx in range(1, 10):
        print('%2d * %2d = %2d' % (dan, idx, dan*idx), end=' ')
    print()
# end def

su01 = 3
gugudan(su01)

# 다음 리스트를 이용하여 각각의 구구단을 출력해 보세요.
danList = [2, 4, 7]
for dan in danList:
    gugudan(dan)