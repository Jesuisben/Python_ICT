# SungjukTest.py
# 이름과 국영수 정보를 입력 받아서, 합격 여부를 출력해주는 함수 sungjukInfo()를 구현해 보세요.
# 합격은 평균이 70점 이상이어야 합니다.
# 영어/수학 각 과목의 미응시자에 대하여 기본 점수를 부여하도록 합니다.
# 기본 점수 : 영어(50), 수학(60)

'''
TypeError: sungjukInfo() missing 2 required positional arguments: 'eng' and 'math'
sungjukInfo() 함수에서 필수 매개 변수 2개('eng'와'math')가 누락 되었네요.
required positional arguments:
'''

def sungjukInfo(name, kor, eng = 50, math = 60):
    # name과 kor는 기본 값이 없으므로, 필수 입력 사항입니다.
    # 반면에 eng와 math는 기본 값이 있으므로, 옵션 입력 사항입니다.
    total = kor + eng + math
    average = total / 3.0

    if average >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'
    # end if

    print('%s 학생의 정보' % name)
    print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
    print('총점 : %d, 평균 : %.2f, 합격 여부 : %s' % (total, average, passOrFail))
    print()
# end def

# positional argument
name, kor, eng, math = '김철수', 50, 60, 70
sungjukInfo(name, kor, eng, math)
sungjukInfo('박영희', 80)

# keyword argument
sungjukInfo(math = 30, eng = 90, name = '심현철', kor = 100)

# 혼합 형태  : positional, keyword argument
sungjukInfo('권유정', 80, math = 90)

# keyword argument는 positional argument 앞에 놓을 수 없습니다.
# sungjukInfo(math = 40, 80, 60 )