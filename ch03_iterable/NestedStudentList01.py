# 이름, 주민번호, 국어, 영어
kim = ['김현숙', '801225-2234567', 60, 80]
lee = ['이민혁', '901111-1027890', 90, 100]
park = ['박춘섭', '000717-3123456', 40, 90]
choi = ['최영희', '100815-4123456', 70, 80]
ha = ['하수빈', '730815-2123456', 30, 70]

students = list() # 중첩 리스트(nested list)
students.append(kim)
students.append(park)
students.append(lee)
students.append(ha)
students.insert(1, choi)

# 1번째 요소안에 들어 있는 주민 번호
ssn = students[1][1]
print('1번째 요소 내의 주민 번호 : %s' % ssn)

# 2번째 요소안에 들어 있는 영어 점수
eng = students[2][3]
print('2번째 요소 내의 영어 점수 : %d' % eng)

# 0번째 요소 내의 국어 점수 변경
students[0][2] = 90

print(type(students))
print('요소 개수 : %d' % len(students))
print()
print(students)

print('\nfor 사용하기')
for bean in students:
    name = bean[0]
    ssn = bean[1]
    kor = bean[2]
    eng = bean[3]

    birth = int(ssn[0:2])
    if birth >= 50:
        birth += 1900
    else:
        birth += 2000
    # end if

    thisYear = 2024

    age = thisYear - birth

    if age >= 40.0:
        ageg = '중년'
    elif age >= 20.0:
        ageg = '청년'
    else :
        ageg = '미성년'
    # end if

    _gender = ssn[7]

    if _gender == '1' or _gender == '3':
        gender = '남자'
    else:
        gender = '여자'
    # end if

    total = kor + eng
    average = total / 2.0

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

    print(name, ssn, kor, eng, birth, age, ageg, gender, total, average, grade)
# end for