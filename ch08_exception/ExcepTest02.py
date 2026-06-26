students = ['철수', '영희', '민수', '지영']
checkList = ['철수', '훈식']

def checkStudent(people):
    if not person in students:
        raise ValueError(f"'학생 {person}'은(는) 명단에 없습니다!")
    print(f"학생 {person}은(는) 출석했습니다.")


for person in checkList:
    try:
        checkStudent(person)
    except ValueError as err:
        print(err)


# # 다음 학생 명단을 사용하여, 출석 체크 함수 checkStudent 함수를 구현해 보세요.
# students = ['철수', '영희', '민수', '지영']
#
# # 출석하지 않으면 예외를 발생시키도록 합니다.
# # 학생 아무개는 출석했습니다.
# # 학생 아무개는 명단에 없습니다!
#
# # 출석 체크할 학생 명단
# checkList = ['철수', '훈식']
