# 초기 데이터
breads = {'바게트':100, '치아바타':200, '호밀빵':300, '베이글':400}
# 크로와상,스콘,,나쵸,식빵,스콘

# '스콘'이 존재하지 않으면 150원으로 추가하세요.
if not "스콘" in breads:
    breads["스콘"] = 150
print(breads)

# 치아바타 가격을 250원으로 수정하세요.
breads["치아바타"] = 250
print(breads)

# 단가 300원짜리가 존재하는지 체크하고, 없으면 '브리오슈'를 300원으로 추가하세요.
if 300 in breads.values():
    print("300원짜리 빵이 있습니다")
else:
    breads["브리오슈"] = 300
print(breads)

# 리스트 반복문을 사용하여 다음 항목을 추가하세요
newItems = ['통밀빵', '옥수수빵', '크랜베리빵']
for idx in range(len(newItems)):
    breads[newItems[idx]] = (idx + 5) * 100
print(breads)
print("------------------------------")

# 다음 항목에 대하여 존재하면 출력, 그렇지 않으면 예외 처리를 수행해 주세요.
targetList = ['옥수수빵', '단팥빵']
for item in targetList:
    try:
        print("품명 : %s, 가격 : %d" % (item, breads[item]))
    except KeyError:
        print("\'%s\'키가 없어서 신규 추가합니다." % item)
        breads[item] = 350
print(breads)
print("------------------------------")

# get() 사용 기본값 : '프레첼'을 조회해 보되, 없는 경우 기본 값을 200으로 출력해 보세요.
print("품명 : 프레첼, 가격 : %d" % breads.get("프레첼", 200))

# items()를 사용하여 전체 항목을 출력해 보세요.
for key, value in breads.items():
    print("항목 %s의 가격은 %d원입니다." % (key, value))
print("------------------------------")

# 조건에 따른 가격 조정 : '바게트', '치아바타'는 50원 인상, '스콘'은 50원 인하를 수행하세요.
for key, value in breads.items():
    if key == "바게트" or key == "치아바타":
        value += 50
    elif key == "스콘":
        value -= 50
    print("품명 : %s, 가격 : %d" % (key, value))