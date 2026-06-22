# 출력 결과
"""
이름 입력 : 김현수
학년 입력 : 3
반 입력 : 6
국어 입력 : 85.3
영어 입력 : 64.2
수학 입력 : 79.7
이름 : 김현수
3학년 6반
국어 : 85.30
영어 : 64.20
수학 : 79.70
총점 : 229.20
평균 : 76.40
"""


# 이름과 국어, 영어, 수학 점수를 입력 받아서 총점과 평균을 구해보세요.
name = input('이름 입력 : ')
grade = input('학년 입력 : ')
myclass = input('반 입력 : ')

kor = float(input('국어 입력 : '))
eng = float(input('영어 입력 : '))
math = float(input('수학 입력 : '))

total = kor + eng + math
average = total/3.0

print('이름 : %s' % (name))
print("%s학년 %s반" % (grade, myclass))
print('국어 : %.2f' % (kor))
print('영어 : %.2f' % (eng))
print('수학 : %.2f' % (math))
print('총점 : %.2f' % (total))
print('평균 : %.2f' % (average))