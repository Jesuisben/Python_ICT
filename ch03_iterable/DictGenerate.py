mydict = {"이름":"홍길동", "국어":60, "영어":80}

defaultJumsu = 80 # 미응시시 기본 점수

subject = ['국어', '영어', '수학']
for item in subject:
    try:
        imsi = mydict[item]
    except KeyError: # 해당 과목 없으면 추가함
        mydict[item] = defaultJumsu
# end for

total = 0 # 모든 과목의 총점
for item in subject:
    total += mydict[item]

mydict['총점'] = total
average = total/3.0
mydict['평균'] = '%.2f' % average # 소수점 2자리까지 표시

if average >= 90.0:
    grade = 'A'
elif average >= 80.0:
    grade = 'B'
elif average >= 70.0:
    grade = 'C'
elif average >= 60.0:
    grade = 'D'
else:
    grade = 'F'
# end if

mydict['학점'] = grade
print(mydict)