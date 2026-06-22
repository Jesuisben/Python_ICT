# 빈 리스트 생성해두기
breads = []

# 인덱싱 및 슬라이싱을 위한 준비
# 문자열을 리스트로 만들기
breadString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
breadList = breadString.split(",")

# 인덱스 번호가 3의 배수인 항목 새로운 리스트 생성
for idx in range(len(breadList)):
    if idx % 3 == 0:
        breads.append(breadList[idx])

# 인덱스 번호가 1번째 요소만 별도로 추출하여 위에 만든 새로운 리스트에 추가
for idx in range(len(breadList)):
    if idx == 1:
        breads.append(breadList[idx])

# 출력
print(type(breads))
print("원본 데이터")
print(breadList, end="\n\n")
print("새로운 데이터")
print(breads)




















# breads = list()  # 또는 breads = []
# breadString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
# breadList = breadString.split(",")
#
# for item in breadList:
#     breads.append(item)
#
# print(type(breads))
# print(breads)