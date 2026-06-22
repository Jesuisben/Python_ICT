# ComplexData01.py
# 다음 데이터를 이용하여 사전을 만들어 보세요.
fruits = [('바나나', 10), ('수박', 20), ('오렌지', 15)]

fruitDict01 = {} # fruitDict = dict()
for item in fruits:
    fruitDict01[item[0]] = item[1]
# end for
print(fruitDict01)

fruitDict02 = dict()
for (name, qty) in fruits:
    fruitDict02[name] = qty
# end for
print(fruitDict02)

# 다음 데이터를 이용하여 각 과일의 총 구매 수량을 사전으로 만들어 보세요.
fruits = [('바나나', 10), ('수박', 20), ('사과', 30), ('수박', 30), ('사과', 50), ('오렌지', 15)]

fruitDict03 = dict()
for (name, qty) in fruits:
    if name in fruitDict03:
        fruitDict03[name] = fruitDict03[name] + qty
    else:
        fruitDict03[name] = qty
    # end if
# end for
print(fruitDict03)

# 중간 고사와 기말 고사 시험 점수를 저장하고 있는 리스트
# 학생별로 총점을 구해 보세요.
# 중간 고사와 기말 고사의 각각의 총점을 구해보세요.
examdata = [('김철수', 50, 70), ('강유신', 60, 75), ('이종환', 55, 80)]

print('학생별 총점 구하기')
for item in examdata:
    name = item[0]
    total = item[1] + item[2]
    message = '%s님의 총점은 %d점입니다.'
    print(message % (name, total))
# end for

print('각 고사별 총점 구하기')
midtotal = finaltotal = 0
for (name, midexam, finalexam) in examdata:
    midtotal += midexam
    finaltotal += finalexam
print('중간 고사 총점 : %d, 기말 고사 총점 : %d' % (midtotal, finaltotal))

print('range() 함수를 사용하여 각 고사별 총점 구하기')
midtotal = finaltotal = 0
for idx in range(len(examdata)):
    midtotal += examdata[idx][1]
    finaltotal += examdata[idx][2]
print('중간 고사 총점 : %d, 기말 고사 총점 : %d' % (midtotal, finaltotal))