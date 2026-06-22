'''
이름, 국영수 과목을 입력 받고, 총점과 평균을 구해 주세요.
평균에 대하여 학점을 매겨 주시고, 적절한 코멘트도 작성해 주세요.
'''
name = input('이름 입력 : ')
kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
math = int(input('수학 점수 입력 : '))

total = kor + eng + math # 총점
average = total / 3.0 # 평균

if average >= 90.0:
    hakjum = 'A'
    comment = '참 잘 하셨습니다.'
elif average >= 80.0:
    hakjum = 'B'
    comment = '참 잘 하셨습니다.'
elif average >= 70.0:
    hakjum = 'C'
    comment = '조금만 더 노력하세요.'
elif average >= 60.0:
    hakjum = 'D'
    comment = '조금만 더 노력하세요.'
else:
    hakjum = 'F'
    comment = '다음 학기에 재수강하세요.'
# end if

print('%s님의 정보' % name)
print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
print('총점 : %d' % total)
print('평균 : %.2f' % average)
print('학점 : %s' % hakjum)
print('코멘트 : %s' % comment)
