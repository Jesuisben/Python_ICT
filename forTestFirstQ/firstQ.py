"""
선택한 자료형 : list

- 시험 문제
주어진 중첩 list를 사용하여 다음 조건에 맞는 list를 생성하시오

- 기초 데이터
students = [["신강철", 90, 80, 60], ["강 산", 70, 20, 30], ["김수호", 50, 80, 70]]

- 요구 사항
1. 학생들의 이름 (list comprehension 사용)
2. 학생들의 개인 점수 총합 (학생 개인의 각 과목의 점수를 합산한 결과들)
3. 과목별 평균 점수 (한 개의 과목별로 학생들의 점수의 합산해서 학생 수로 나누기)
(학생 리스트의 요소들은 순서대로 이름, 국어점수, 수학점수, 과학점수이다. )

- 실행 결과
학생들 : ['신강철', '강 산', '김수호']
학생들의 개인 점수 총합 : [210, 240, 180]
과목별 평균 점수 : [70.0, 80.0, 60.0]

- 출제 의도
기본적인 list를 넘어 list 타입의 응용인 list comprehension과 중첩 list를 사용하게 하여
list 자체에 대한 개념을 탄탄하게 가지고 있는지 평가하기 위해 출제하였다.
"""

# 답지
# 기초 데이터
students = [["신강철", 90, 80, 60], ["강 산", 70, 80, 50], ["김수호", 50, 80, 70]]

# 1. 학생들의 이름 (list comprehension 사용)
name = [student[0] for student in students]
print(f"학생들 : {name}")


kor = 0
math = 0
science = 0

total = []
average = []

# 2. 학생들의 개인 점수 총합 (학생 개인의 각 과목의 점수를 합산한 결과들)
for student in students:
    kor += student[1]
    math += student[2]
    science += student[3]

total.append(kor)
total.append(math)
total.append(science)
print(f"학생들의 개인 점수 총합 : {total}")

# 3. 과목별 평균 점수 (한 개의 과목별로 학생들의 점수의 합산해서 학생 수로 나누기)
average.append(kor / len(students))
average.append(math / len(students))
average.append(science / len(students))
print(f"과목별 평균 점수 : {average}")