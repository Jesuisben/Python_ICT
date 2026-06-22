# 튜플로 만들 재료인 문자열
breadString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"

# 문자열을 ,를 구분자로 분리해서 리스트로 생성
breadList = breadString.split(",")

# 리스트를 튜플로 타입 변경
breadList = tuple(breadList)

# 출력
print("원본 튜플:", breadList)
print("스콘 개수: %d" % breadList.count("스콘"))
print("스콘 첫 번째 인덱스: %d" % breadList.index("스콘"))

# 슬라이싱한 튜플의 요소들을 리스트로 변환해서 넣기
breads = list(breadList[:3]) + list(breadList[-3:])

# 리스트를 튜플로 변환
breads = tuple(breads)

print("새로운 튜플:", end="")
print(breads, end="\n\n")

# 리스트로 반환 후 오름차순 정렬
print("오름차순 정렬")
breads = list(breads)
breads.sort()
print(breads)

# sometuple = list()  # 또는 breads = []
# breadString = "바게트,크로와상,스콘,치아바타,나쵸,식빵,스콘,호밀빵,베이글"
# breadList = breadString.split(",")
#
# for item in breadList:
#     sometuple.append(item)
#
# breads = tuple(sometuple)
# print(type(breads))
# print(breads)