# random 모듈을 사용하여 다음 물음에 답해 보세요.
import random

# randint() 함수를 적절히 사용하여 1부터 10까지의 정수 중 5개를 무작위 추출
# 후 mylist에 저장하는 코드를 작성해보세요.
# 동일한 숫자가 중복되어도 됩니다.
mylist = []
for item in range(5):
    mylist.append(random.randint(1, 10))
print(f"방법 01 리스트의 append 사용하기 : {mylist}")

# 반복하는 지역변수인 i를 굳이 사용하지 않고 반복하는 형태를 위해서 반복문을 써도 됨
mylist = [random.randint(1, 10) for i in range(5)]
print(f"방법 02 List Comprehension 사용하기 : {mylist}")

# 1부터 10까지의 정수 중에서 임의의 3개 추출하기
# 힌트) shuffle() 함수와 슬라이싱 기법 활용 또는 sample() 함수를 사용하기
# 재료
someData = [idx for idx in range(1, 11)]

# sample() 함수 사용
useSample = random.sample(someData, 3)
print(f"sample() 함수 사용하기 : {useSample}")

# shuffle() 함수와 슬라이싱 기법 활용
# shuffle() 함수는 반환를 하지 않음
random.shuffle(someData)
useSlice = someData[:3]
print(f"shuffle() 함수와 슬라이싱 : {useSlice}")


# # 랜덤 정수 생성 연습
# # 1~100 사이 랜덤 정수를 10개 리스트에 저장한 뒤 출력해 보세요.
# # 단, 동일한 숫자가 여러 번 나오면 안됩니다.
someData = [idx for idx in range(1, 101)]
mylist = random.sample(someData, 10)
print(f"랜덤 정수 10개(중복 없음): {mylist}")


# # 메뉴 랜덤 추천하기
# # 다음 메뉴 중에서 오늘 점심 메뉴를 1개 추천하세요.
menu = ['김치찌개', '제육볶음', '돈까스', '파스타', '떡볶이', '초밥', '김밥']
print(f"오늘의 점심 메뉴 추천: {random.choice(menu)}")


# # 순서 섞기(shuffle)
# # 다음 학생들의 시험 발표 순서를 무작위로 정해 보세요.
students = ['민수', '지우', '하은', '준서', '다현', '서준', '유진']
random.shuffle(students)
print(f"시험 발표 순서: {students}")


# # 무작위 표본 추출(sample)
# # 다음 회사의 직원 목록에서 랜덤하게 4명만 뽑아 프로젝트 TF팀을 만들어 보세요.
employee = ['홍길동','김철수','이영희','박민지','최현우','송다인','정윤호','백지현']
print(f"프로젝트 TF팀: {random.sample(employee, 4)}")


# # 아래 학생 리스트에서 무작위로 1명을 뽑아 오늘 발표 담당자로 선정하세요.
students = ['진우', '현아', '수민', '도윤', '예린', '현수', '수진']
print(f"오늘 발표 담당자: {random.choice(students)}")

# somedata = [idx for idx in range(1, 11)]
# mylist = list()
#
# import random
#
# for idx in range(1, 6):
#     mylist.append(random.randint(1, 10))
#
# print(mylist)
#
# print('sample() 함수 사용하기')
# result = random.sample(somedata, 3)
# print(result)
#
# print('shuffle() 함수 사용하기')
# random.shuffle(somedata)
# print(somedata[0:3])