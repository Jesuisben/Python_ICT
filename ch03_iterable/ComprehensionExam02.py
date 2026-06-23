# list comprehension을 활용한 문제
# 평균 이상 점수를 받은 학생 수 출력하기
scores = [55, 80, 92, 45, 68, 88] # 평균 이상이면 '우수'

# 1. 평균 구하기
total = 0
for item in scores:
    total += item
average = total / len(scores)

# 2. comprehension
resultScores = [idx for idx in scores if idx >= average]

# 3. 출력
print(f"원본 데이터 : {scores}")
print(f"결과 데이터 : {resultScores}")
print(f"평균 이상 학생 수: {len(resultScores)}명")
print("")

# 나이가 18세 이상인 사람만 추출하여 몇 명인지 출력
ages = [12, 17, 18, 20, 35, 15]

# 1. comprehension
agesOver = [idx for idx in ages if idx >= 18]

# 2. 출력
print(f"원본 데이터 : {ages}")
print(f"결과 데이터 : {agesOver}")
print(f"성인 인원: {len(agesOver)}명")
print("")

# 양수만 골라서 개수 출력하기
numbers = [-5, 3, 0, 7, -2, 10, -8]

# 1. comprehension
posNumber = [idx for idx in numbers if idx >0]

# 2. 출력
print(f"원본 데이터 : {numbers}")
print(f"결과 데이터 : {posNumber}")
print(f"양수 개수: {len(posNumber)}개")
print("")


# 짝수만 골라서 출력 및 개수 표시
data = [1, 4, 7, 10, 13, 16]

# 1. comprehension
oddData = [idx for idx in data if idx % 2 == 0]

# 2. 출력
print(f"원본 데이터 : {data}")
print(f"결과 데이터 : {oddData}")
print(f"짝수 개수: {len(oddData)}개")
print("")

# 이름 리스트에서 3글자 이상인 이름만 추출
names = ["유나", "철수", "민지", "Tom", "Ann", "Jennifer"]

# 1. comprehension
threeNames = [idx for idx in names if len(idx) >= 3]

# 2. 출력
print(f"원본 데이터 : {names}")
print(f"결과 데이터 : {threeNames}")
print(f"3글자 이상 이름 수: {len(threeNames)}개")

