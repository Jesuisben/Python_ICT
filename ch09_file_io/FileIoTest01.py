coffees = ['아메리카노', '카페라떼', '카푸치노', '바닐라라떼', '모카']

dataIn = "../dataIn/"

myfile01 = open(file= dataIn + "coffee_menu.txt", mode="w", encoding="UTF-8")

# 'coffee_menu.txt' 파일에 위의 커피 메뉴 리스트를 다음과 같이 저장해보세요.
# 저장 형식은 '오늘 추천 커피는 아메리카노입니다.'
for idx in range(len(coffees)):
    myfile01.write(f"오늘 추천 커피는 {coffees[idx]}입니다.\n")
    # 기존 파일에 커피별 특성을 다음과 같이 추가합니다.
    if idx % 2 == 0: # 짝수이면
        # 1번째 커피 xxx 풍미가 깊어요.
        myfile01.write(f"\t{idx + 1}번째 커피 {coffees[idx]} 풍미가 깊어요.\n")
    else: # 홀수이면
        # 2번째 커피 yyy 부드럽게 즐기세요.
        myfile01.write(f"\t{idx + 1}번째 커피 {coffees[idx]} 부드럽게 즐기세요.\n")
myfile01.close()

# 반복문과 with 구문을 사용하여 커피 관련 파일 여러개 만들어 봅니다.
# 파일 이름 : coffee01.txt ~ coffee05.txt
for i in range(1, 6):
    filename = "coffee" + str(i).zfill(2)
    with open(file= dataIn + filename, mode="w", encoding="UTF-8") as myfile02:
        # 각 파일의 내용
        # 나는 "{filename}" 파일입니다. 커피 정보를 담습니다.
        myfile02.write(f"나는 '{filename}' 파일입니다. 커피 정보를 담습니다.")

# 변수 coffees에 담겨 있는 각 커피 이름으로 별도의 txt 파일 생성
for item in coffees:
    with open(file= dataIn + item, mode="w", encoding="UTF-8") as myfile03:
        myfile03.write(f"{item} 정보를 위한 텍스트 파일입니다.")